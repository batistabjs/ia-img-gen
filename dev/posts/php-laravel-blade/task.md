---
title: "Laravel - Blade Templates"
description: "Criar views dinâmicas com Blade, o motor de templates do Laravel"
stack: "PHP 8.2+ + Laravel 11 + Blade"
category: "php"
difficulty: "basico"
tags: ["laravel", "blade", "templates", "php"]
---

# Task: Laravel - Blade Templates

## Objetivo
Demonstrar como usar Blade para criar templates reutilizáveis com layouts, componentes e diretivas condicionais.

## Código de Exemplo

```php
{{-- resources/views/layouts/app.blade.php --}}
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{{ $title ?? 'Meu App' }}</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    @include('partials.navbar')

    <main class="container">
        @yield('content')
    </main>

    @include('partials.footer')
</body>
</html>

{{-- resources/views/posts/index.blade.php --}}
@extends('layouts.app')

@section('content')
    <h1>Posts</h1>

    @if($posts->isEmpty())
        <p class="text-muted">Nenhum post encontrado.</p>
    @else
        <div class="grid">
            @foreach($posts as $post)
                <x-post-card :post="$post" />
            @endforeach
        </div>
    @endif

    {{ $posts->links() }}
@endsection

{{-- Componente Blade --}}
{{-- resources/views/components/post-card.blade.php --}}
@props(['post'])

<article class="card">
    <h2>{{ $post->title }}</h2>
    <p>{{ Str::limit($post->content, 100) }}</p>
    <span class="badge">{{ $post->category }}</span>

    @auth
        <a href="{{ route('posts.edit', $post) }}">Editar</a>
    @endauth
</article>

{{-- Uso do componente --}}
<x-post-card :post="$post" />
```

## Conceitos Demonstrados
- Layouts com @extends e @yield
- Seções com @section e @show
- Diretivas @if, @foreach
- Componentes Blade
- Slots e props

## Uso na Imagem
Título: "Laravel Blade Templates" com ícone de template/layout.
