---
title: "PHP 8.1 - Enums e Type Declarations"
description: "Usar Enums, Fiber e tipos avançados no PHP 8.1+"
stack: "PHP 8.1+"
category: "php"
difficulty: "intermediario"
tags: ["php81", "enums", "types", "php"]
---

# Task: PHP 8.1 - Enums e Type Declarations

## Objetivo
Demonstrar as funcionalidades modernas de tipos do PHP 8.1+, incluindo Enums, readonly properties e intersection types.

## Código de Exemplo

```php
<?php

// Enum básico
enum Status: string
{
    case Pending = 'pending';
    case Active = 'active';
    case Inactive = 'inactive';
    case Banned = 'banned';
}

// Enum com método
enum Color: string
{
    case Red = 'red';
    case Green = 'green';
    case Blue = 'blue';

    public function label(): string
    {
        return match($this) {
            self::Red => 'Vermelho',
            self::Green => 'Verde',
            self::Blue => 'Azul',
        };
    }

    public static function fromValue(string $value): self
    {
        return self::tryFrom($value) ?? self::Red;
    }
}

// Uso em model
class User extends Model
{
    protected $casts = [
        'status' => Status::class,
    ];
}

// Readonly properties (PHP 8.1)
class Coordinate
{
    public function __construct(
        public readonly float $latitude,
        public readonly float $longitude,
    ) {}
}

// Intersection types
interface HasName { public function getName(): string; }
interface HasEmail { public function getEmail(): string; }

function notifyUser(HasName&HasEmail $user): void
{
    echo "Notificando {$user->getName()} ({$user->getEmail()})";
}

// First-class callable syntax
$trim = trim(...);
$result = $trim('  hello  ');

// Fibers (PHP 8.1)
$fiber = new Fiber(function (): void {
    echo "Fiber started\n";
    $value = Fiber::suspend('from fiber');
    echo "Fiber resumed with: $value\n";
});

$result = $fiber->start();
$fiber->resume('hello from main');
```

## Conceitos Demonstrados
- Backed Enums (string/int)
- Métodos em Enums
- Readonly properties
- Intersection types
- Fibers

## Uso na Imagem
Título: "PHP 8.1+ Modern Features" com destaque para Enum e tipos.
