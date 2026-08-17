---
title: "Spring Data JPA - Repository Pattern"
description: "Implementar o padrão Repository usando Spring Data JPA para acesso a dados"
stack: "Java 17 + Spring Boot 3 + Spring Data JPA + PostgreSQL"
category: "java-spring"
difficulty: "intermediario"
tags: ["spring-data", "jpa", "repository", "java"]
---

# Task: Spring Data JPA - Repository Pattern

## Objetivo
Demonstrar como usar o Spring Data JPA para criar repositórios com queries derivadas e customizadas, eliminando boilerplate de acesso a dados.

## Código de Exemplo

```java
public interface UserRepository extends JpaRepository<User, Long> {

    // Query derivada pelo nome do método
    Optional<User> findByEmail(String email);

    List<User> findByActiveTrueOrderByCreatedAtDesc();

    // Query com JPQL
    @Query("SELECT u FROM User u WHERE u.name LIKE %:name% AND u.active = true")
    List<User> findActiveByName(@Param("name") String name);

    // Query nativa
    @Query(value = "SELECT * FROM users WHERE created_at > :date",
           nativeQuery = true)
    List<User> findRecentUsers(@Param("date") LocalDateTime date);

    // Projeção customizada
    @Query("SELECT new com.app.dto.UserSummary(u.name, u.email) FROM User u")
    List<UserSummary> findAllSummaries();
}
```

## Conceitos Demonstrados
- Herança de JpaRepository
- Queries derivadas automática
- JPQL com @Query
- Queries nativas
- Projeção com construtores

## Uso na Imagem
O código deve destacar a interface Repository com syntax highlighting, mostrando a elegância do Spring Data. Título: "Spring Data JPA Repository".
