import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import urllib.request
import json
import base64

load_dotenv()

# 1. Configuração de argumentos
parser = argparse.ArgumentParser(description="Gerador de imagens via OpenRouter API")
parser.add_argument(
    "-p", "--prompt",
    type=str,
    default="prompt-sys-pe.md",
    help="Arquivo de prompt (default: prompt-sys-pe.md)"
)
parser.add_argument(
    "-n", "--prefix",
    type=str,
    default="capoeira",
    help="Prefixo do nome da imagem e diretório (default: capoeira)"
)
parser.add_argument(
    "--aspect-ratio",
    type=str,
    default="9:16",
    help="Proporção da imagem (default: 9:16)"
)
parser.add_argument(
    "--quality",
    type=str,
    default="medium",
    choices=["low", "medium", "high"],
    help="Qualidade da imagem (default: medium)"
)
args = parser.parse_args()

# 2. Configurações da API
API_KEY = os.environ.get("OPENROUTER_KEY", "SUA_API_KEY_AQUI")
BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# 3. Lê o prompt do arquivo
prompt_path = Path(args.prompt)
if not prompt_path.exists():
    raise FileNotFoundError(f"Arquivo de prompt não encontrado: {prompt_path}")
prompt_text = prompt_path.read_text(encoding="utf-8")

# 4. Configurações de geração de imagem
API_MODEL = os.environ.get("OPENROUTER_IMAGE_MODEL", "openai/gpt-image-2")
print(f"Modelo de geração de imagem: {API_MODEL}")
print(f"Prompt: {prompt_path.name}")
print(f"Prefixo: {args.prefix}")

# 5. Diretórios baseados no prefixo
prefix = args.prefix
output_dir = Path(f"imgs/{prefix}/geradas")
output_dir.mkdir(parents=True, exist_ok=True)
matriz_dir = Path(f"imgs/{prefix}/matriz")

# 6. Carrega imagens de referência do diretório matriz
input_references = []

if matriz_dir.exists():
    print(f"Carregando imagens de referência de: {matriz_dir}")
    
    for img_file in matriz_dir.glob("*"):
        if img_file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            print(f"  - Carregando: {img_file.name}")
            
            with open(img_file, "rb") as f:
                img_data = f.read()
                img_b64 = base64.b64encode(img_data).decode("utf-8")
            
            media_type_map = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".webp": "image/webp"
            }
            media_type = media_type_map.get(img_file.suffix.lower(), "image/png")
            
            input_references.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{media_type};base64,{img_b64}"
                }
            })
    
    print(f"Total de imagens de referência: {len(input_references)}")
else:
    print(f"Diretório de matriz não encontrado: {matriz_dir}")
    print("Gerando sem referências.")

# 7. Prepara a requisição para a API de imagens do OpenRouter
url = f"{BASE_URL}/images"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": API_MODEL,
    "prompt": prompt_text,
    "n": 1,
    "quality": args.quality,
    "aspect_ratio": args.aspect_ratio
}

if input_references:
    payload["input_references"] = input_references

print(f"\nSolicitando geração de imagem...")
print(f"Prompt: {prompt_text[:100]}...")

try:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    with urllib.request.urlopen(req, timeout=180) as response:
        result = json.loads(response.read().decode("utf-8"))
    
    # 8. Salva a imagem
    if "data" in result and len(result["data"]) > 0:
        image_data = result["data"][0]
        
        if "b64_json" in image_data:
            image_bytes = base64.b64decode(image_data["b64_json"])
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_filename = f"{prefix}_{timestamp}.png"
            image_path = output_dir / image_filename
            
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            
            print(f"\nImagem salva em: {image_path}")
            
            if "usage" in result:
                usage = result["usage"]
                print(f"\n=== Consumo ===")
                print(f"  Custo: ${usage.get('cost', 0):.4f}")
                print(f"  Tokens de entrada: {usage.get('prompt_tokens', 0)}")
                print(f"  Tokens de saída: {usage.get('completion_tokens', 0)}")
        else:
            print("Formato de resposta inesperado:", result)
    else:
        print("Nenhuma imagem foi gerada:", result)
        
except urllib.error.HTTPError as e:
    error_body = e.read().decode("utf-8")
    print(f"Erro HTTP {e.code}: {error_body}")
except Exception as e:
    print(f"Erro ao gerar imagem: {e}")
    raise
