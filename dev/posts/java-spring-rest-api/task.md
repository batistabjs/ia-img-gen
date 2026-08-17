---
title: "Criando uma REST API com Spring Boot"
description: "Construir uma API REST completa usando Spring Boot com endpoints CRUD para gerenciamento de usuários"
stack: "Java 17 + Spring Boot 3 + Spring Data JPA + H2"
category: "java-spring"
difficulty: "intermediario"
tags: ["spring-boot", "rest-api", "crud", "java"]
---

# Task: Criando uma REST API com Spring Boot

## Objetivo
Criar uma API RESTful completa com operações CRUD utilizando Spring Boot, demonstrando a estrutura padrão de uma aplicação backend em Java.

## Código de Exemplo

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public ResponseEntity<List<UserResponse>> findAll() {
        return ResponseEntity.ok(userService.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<UserResponse> findById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.findById(id));
    }

    @PostMapping
    public ResponseEntity<UserResponse> create(@Valid @RequestBody CreateUserRequest request) {
        UserResponse user = userService.create(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }

    @PutMapping("/{id}")
    public ResponseEntity<UserResponse> update(@PathVariable Long id,
                                                @Valid @RequestBody UpdateUserRequest request) {
        return ResponseEntity.ok(userService.update(id, request));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        userService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
```

## Conceitos Demonstrados
- Anotações REST (@RestController, @RequestMapping)
- Injeção de dependência via construtor
- ResponseEntity para responses HTTP
- Validação com @Valid
- Endpoints CRUD completos

## Uso na Imagem
O código acima deve ser exibido com syntax highlighting em tema escuro, com destaque para as anotações Spring em cor diferente. O título da imagem deve ser "REST API com Spring Boot".
