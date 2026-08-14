import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import urllib.request
import json
import base64

load_dotenv()

# 1. Configurações da API
API_KEY = os.environ.get("OPENROUTER_KEY", "SUA_API_KEY_AQUI")
BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# 2. Lê o prompt do arquivo
prompt_text = Path("prompt-sys-pe.md").read_text(encoding="utf-8")

# 3. Configurações de geração de imagem
# Modelo openai/gpt-image-2 suporta até 16 imagens de referência
API_MODEL = os.environ.get("OPENROUTER_IMAGE_MODEL", "openai/gpt-image-2")
print(f"Modelo de geração de imagem: {API_MODEL}")

# 4. Diretório de saída e matriz
output_dir = Path("imgs/geradas")
output_dir.mkdir(parents=True, exist_ok=True)
matriz_dir = Path("imgs/matriz")

# 5. Carrega imagens de referência do diretório matriz
input_references = []

if matriz_dir.exists():
    print(f"Carregando imagens de referência de: {matriz_dir}")
    
    # Carrega todas as imagens do diretório matriz
    for img_file in matriz_dir.glob("*"):
        if img_file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            print(f"  - Carregando: {img_file.name}")
            
            # Lê a imagem e converte para base64
            with open(img_file, "rb") as f:
                img_data = f.read()
                img_b64 = base64.b64encode(img_data).decode("utf-8")
            
            # Determina o media type
            media_type_map = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".webp": "image/webp"
            }
            media_type = media_type_map.get(img_file.suffix.lower(), "image/png")
            
            # Adiciona à lista de referências
            input_references.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{media_type};base64,{img_b64}"
                }
            })
    
    print(f"Total de imagens de referência: {len(input_references)}")
else:
    print("Diretório de matriz não encontrado. Gerando sem referências.")

# 6. Prepara a requisição para a API de imagens do OpenRouter
url = f"{BASE_URL}/images"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": API_MODEL,
    "prompt": prompt_text,
    "n": 1,
    "quality": "medium",
    "aspect_ratio": "9:16"
}

# Adiciona referências se houver
if input_references:
    payload["input_references"] = input_references

print("\nSolicitando geração de imagem ao modelo via OpenRouter...")
print(f"Prompt: {prompt_text[:100]}...")

try:
    # Converte o payload para JSON
    data = json.dumps(payload).encode("utf-8")
    
    # Cria a requisição HTTP
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    # Envia a requisição
    with urllib.request.urlopen(req, timeout=180) as response:
        result = json.loads(response.read().decode("utf-8"))
    
    # 7. Salva a imagem
    if "data" in result and len(result["data"]) > 0:
        image_data = result["data"][0]
        
        # Verifica se tem b64_json
        if "b64_json" in image_data:
            image_bytes = base64.b64decode(image_data["b64_json"])
            
            # Gera nome do arquivo com timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_filename = f"capoeira_selfie_{timestamp}.png"
            image_path = output_dir / image_filename
            
            # Salva a imagem
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            
            print(f"\nImagem salva em: {image_path}")
            
            # Exibe informações de uso
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