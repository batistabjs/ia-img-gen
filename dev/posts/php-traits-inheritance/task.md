---
title: "PHP - Traits e Herança"
description: "Reutilizar código com Traits e entender herança no PHP moderno"
stack: "PHP 8.2+"
category: "php"
difficulty: "intermediario"
tags: ["traits", "heranca", "reutilizacao", "php"]
---

# Task: PHP - Traits e Herança

## Objetivo
Demonstrar como Traits permitem reutilizar código em múltiplas classes, resolvendo a limitação de herança múltipla do PHP.

## Código de Exemplo

```php
<?php

// Trait para timestamps
trait HasTimestamps
{
    public function createdAt(): string
    {
        return $this->created_at->format('d/m/Y H:i');
    }

    public function timeAgo(): string
    {
        return $this->created_at->diffForHumans();
    }
}

// Trait para soft delete
trait SoftDeletes
{
    public function softDelete(): void
    {
        $this->deleted_at = now();
        $this->save();
    }

    public function restore(): void
    {
        $this->deleted_at = null;
        $this->save();
    }
}

// Trait com conflito resolvido
trait Cacheable
{
    public function cacheKey(): string
    {
        return strtolower(class_basename($this)) . '_' . $this->id;
    }
}

// Uso em models
class User extends Model
{
    use HasTimestamps, SoftDeletes;

    protected $fillable = ['name', 'email'];
}

class Post extends Model
{
    use HasTimestamps, SoftDeletes, Cacheable;

    protected $fillable = ['title', 'content', 'user_id'];
}

// Herança tradicional
abstract class BaseModel
{
    protected string $table;

    public function getTable(): string
    {
        return $this->table;
    }
}

class Product extends BaseModel
{
    protected string $table = 'products';
}

// Interface + Trait
interface Auditable
{
    public function getAuditLog(): array;
}

trait AuditTrait
{
    public function getAuditLog(): array
    {
        return $this->audits()->toArray();
    }
}

class Order extends Model implements Auditable
{
    use AuditTrait;
}
```

## Conceitos Demonstrados
- Definição de Traits
- Múltiplos Traits
- Conflito de Traits (precedence)
- Traits com interfaces
- Herança abstrata

## Uso na Imagem
Título: "PHP Traits - Code Reuse" com diagrama de herança/mixins.
