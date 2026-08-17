---
title: "Laravel - API Resources"
description: "Transformar models em JSON usando API Resources para responses consistentes"
stack: "PHP 8.2+ + Laravel 11"
category: "php"
difficulty: "intermediario"
tags: ["laravel", "api-resources", "json", "php"]
---

# Task: Laravel - API Resources

## Objetivo
Criar API Resources para transformar models em JSON estruturado, incluindo wrapping, meta data e relacionamentos.

## Código de Exemplo

```php
<?php

// App/Http/Resources/UserResource.php
class UserResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'status' => $this->status->value,
            'avatar' => $this->avatar_url,
            'posts_count' => $this->whenCounted('posts'),
            'roles' => RoleResource::collection($this->whenLoaded('roles')),
            'created_at' => $this->created_at->toISOString(),
        ];
    }
}

// Resource com wrapping
class PostResource extends JsonResource
{
    public static $wrap = 'data';

    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'title' => $this->title,
            'content' => $this->content,
            'author' => new UserResource($this->whenLoaded('author')),
            'tags' => $this->tags->pluck('name'),
        ];
    }
}

// Controller usando Resources
class UserController extends Controller
{
    public function index()
    {
        $users = User::with('roles')->paginate(15);

        return UserResource::collection($users)
            ->additional([
                'meta' => [
                    'total' => $users->total(),
                    'per_page' => $users->perPage(),
                ]
            ]);
    }

    public function show(User $user)
    {
        $user->load(['posts', 'roles']);

        return new UserResource($user);
    }

    public function store(StoreUserRequest $request)
    {
        $user = User::create($request->validated());

        return new UserResource($user)
            ->response()
            ->setStatusCode(201);
    }
}

// Response format
{
    "data": {
        "id": 1,
        "name": "João",
        "email": "joao@email.com",
        "status": "active",
        "posts_count": 5,
        "roles": [
            {"id": 1, "name": "admin"}
        ]
    },
    "meta": {
        "total": 100,
        "per_page": 15
    }
}
```

## Conceitos Demonstrados
- Definição de API Resource
- Condiçãoais com when/whenCounted/whenLoaded
- Wrapping de responses
- Meta data e pagination
- Status codes customizados

## Uso na Imagem
Título: "Laravel API Resources" com ícone de API/json.
