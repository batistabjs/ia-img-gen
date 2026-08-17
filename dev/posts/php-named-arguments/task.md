---
title: "PHP 8 - Named Arguments"
description: "Usar Named Arguments para chamadas de função mais legíveis e flexíveis"
stack: "PHP 8.2+"
category: "php"
difficulty: "basico"
tags: ["php8", "named-arguments", "funcionalidade"]
---

# Task: PHP 8 - Named Arguments

## Objetivo
Demonstrar como Named Arguments no PHP 8 tornam as chamadas de função mais legíveis, permitindo pular parâmetros opcionais e tornar o código mais expressivo.

## Código de Exemplo

```php
<?php

// Função com múltiplos parâmetros opcionais
function createUser(
    string $name,
    string $email,
    string $role = 'user',
    bool $active = true,
    ?string $avatar = null
): array {
    return compact('name', 'email', 'role', 'active', 'avatar');
}

// ❌ Antes do PHP 8 - difícil de ler
$user1 = createUser('João', 'joao@email.com', 'admin', true, null);

// ✅ PHP 8 - Named Arguments - claro e flexível
$user2 = createUser(
    name: 'Maria',
    email: 'maria@email.com',
    role: 'moderator',
    avatar: 'https://example.com/avatar.jpg'
);

// Pular parâmetros opcionais
$user3 = createUser(
    name: 'Pedro',
    email: 'pedro@email.com',
    avatar: 'https://example.com/pedro.jpg'
);

// Útil com funções de biblioteca
$html = str_replace(
    search: ['foo', 'bar'],
    replace: ['baz', 'qux'],
    subject: 'foo and bar'
);

// Com arrays
$config = [
    'host' => 'localhost',
    'port' => 5432,
    'dbname' => 'myapp',
];

$conn = pg_connect(
    host: $config['host'],
    port: $config['port'],
    dbname: $config['dbname']
);
```

## Conceitos Demonstrados
- Sintaxe de Named Arguments (nome: valor)
- Pular parâmetros opcionais
- Legibilidade em chamadas de função
- Uso com funções built-in do PHP

## Uso na Imagem
Título: "PHP 8 Named Arguments" com destaque para a sintaxe `nome: valor`.
