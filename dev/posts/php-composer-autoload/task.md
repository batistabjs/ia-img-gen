---
title: "Composer e Autoload no PHP"
description: "Gerenciar dependências e carregamento automático de classes com Composer"
stack: "PHP 8.2+ + Composer 2"
category: "php"
difficulty: "basico"
tags: ["composer", "autoload", "psr4", "php"]
---

# Task: Composer e Autoload no PHP

## Objetivo
Entender como o Composer gerencia dependências e fornece autoload de classes usando PSR-4, eliminando a necessidade de require manual.

## Código de Exemplo

```json
// composer.json
{
    "name": "vendor/my-app",
    "description": "Aplicação PHP moderna",
    "type": "project",
    "require": {
        "php": "^8.2",
        "guzzlehttp/guzzle": "^7.8",
        "monolog/monolog": "^3.5",
        "vlucas/phpdotenv": "^5.6"
    },
    "require-dev": {
        "phpunit/phpunit": "^10.3",
        "squizlabs/php_codesniffer": "^3.7"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\": "database/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    }
}
```

```php
<?php
// Sem Composer - require manual e frágil
require_once 'vendor/autoload.php';
require_once 'lib/Database.php';
require_once 'lib/Router.php';

// Com Composer - autoload automático via PSR-4
use App\Models\User;
use App\Controllers\AuthController;
use GuzzleHttp\Client;
use Monolog\Logger;

// Classes carregadas automaticamente pelo Composer
$user = new User();
$client = new Client();
$logger = new Logger('app');

// Scripts de namespace
// composer dump-autoload  → regera o arquivo de autoload
// composer install         → instala dependências
// composer update          → atualiza dependências
// composer require pkg     → adiciona nova dependência
// composer remove pkg      → remove dependência
```

## Conceitos Demonstrados
- Estrutura do composer.json
- Autoload PSR-4
- Dependências require vs require-dev
- Scripts úteis do Composer
- Namespace organization

## Uso na Imagem
Título: "Composer - PHP Package Manager" com ícone de pacote/dependência.
