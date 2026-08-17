---
title: "Laravel - Eloquent ORM"
description: "Dominar o Eloquent ORM para consultas elegantes e relacionamentos no Laravel"
stack: "PHP 8.2+ + Laravel 11 + Eloquent"
category: "php"
difficulty: "intermediario"
tags: ["laravel", "eloquent", "orm", "php"]
---

# Task: Laravel - Eloquent ORM

## Objetivo
Demonstrar o poder do Eloquent ORM para mapear tabelas do banco em objetos PHP, incluindo relacionamentos, scopes e accessor/mutators.

## Código de Exemplo

```php
<?php

// Model com relacionamentos
class User extends Model
{
    protected $fillable = ['name', 'email', 'password'];
    protected $hidden = ['password', 'remember_token'];

    // Relacionamento: User hasMany Posts
    public function posts()
    {
        return $this->hasMany(Post::class);
    }

    // Relacionamento: User belongsToMany Roles
    public function roles()
    {
        return $this->belongsToMany(Role::class);
    }

    // Scope customizado
    public function scopeActive(Builder $query): Builder
    {
        return $query->where('active', true);
    }

    public function scopeRecent(Builder $query, int $days = 7): Builder
    {
        return $query->where('created_at', '>=', now()->subDays($days));
    }

    // Accessor
    public function getNameAttribute(string $value): string
    {
        return ucfirst($value);
    }

    // Mutator
    public function setPasswordAttribute(string $value): void
    {
        $this->attributes['password'] = Hash::make($value);
    }
}

// Consultas elegantes
$users = User::active()
    ->recent(30)
    ->with(['posts', 'roles'])
    ->get();

// Lazy Loading
foreach ($user->posts as $post) {
    echo $post->title;
}

// Eager Loading (evita N+1)
$posts = Post::with('author')->get();

// Consulta com.aggregate
$stats = User::selectRaw('role, COUNT(*) as total')
    ->groupBy('role')
    ->havingRaw('COUNT(*) > 5')
    ->get();
```

## Conceitos Demonstrados
- Definição de Model
- Relacionamentos hasMany, belongsToMany
- Scopes locais
- Accessors e Mutators
- Eager Loading com with()

## Uso na Imagem
Título: "Eloquent ORM no Laravel" com ícone de banco de dados e objetos.
