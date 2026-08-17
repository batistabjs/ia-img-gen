---
title: "Laravel - Rotas e Middleware"
description: "Configurar rotas RESTful e middleware para autenticação e autorização"
stack: "PHP 8.2+ + Laravel 11"
category: "php"
difficulty: "intermediario"
tags: ["laravel", "routes", "middleware", "php"]
---

# Task: Laravel - Rotas e Middleware

## Objetivo
Demonstrar como definir rotas organizadas e middleware para proteger endpoints e processar requisições no Laravel.

## Código de Exemplo

```php
<?php

// routes/web.php e routes/api.php
use App\Http\Controllers\UserController;
use App\Http\Controllers\PostController;

// Rotas simples
Route::get('/', [HomeController::class, 'index']);
Route::get('/about', fn() => view('about'));

// Rotas de recurso (CRUD)
Route::resource('users', UserController::class);
Route::resource('posts', PostController::class)->only([
    'index', 'show', 'store', 'update', 'destroy'
]);

// Grupo com middleware
Route::middleware(['auth'])->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index']);
    Route::resource('posts', PostController::class)->except(['index', 'show']);
});

// Grupo com prefix e middleware
Route::prefix('admin')->middleware(['auth', 'admin'])->group(function () {
    Route::get('/users', [AdminUserController::class, 'index']);
    Route::delete('/users/{user}', [AdminUserController::class, 'destroy']);
});

// Middleware customizado
class EnsureUserIsActive
{
    public function handle(Request $request, Closure $next)
    {
        if (!$request->user()->active) {
            return redirect('/inactive');
        }
        return $next($request);
    }
}

// Rate limiting
Route::middleware('throttle:5,1')->group(function () {
    Route::post('/login', [AuthController::class, 'login']);
});
```

## Conceitos Demonstrados
- Rotas básicas e resource
- Grupos de rotas
- Middleware de autenticação
- Middleware customizado
- Rate limiting

## Uso na Imagem
Título: "Laravel Routes & Middleware" com ícone de camadas/rotas.
