---
title: "Cache com Spring Cache"
description: "Implementar cache em memória usando Spring Cache e Redis"
stack: "Java 17 + Spring Boot 3 + Spring Cache + Redis"
category: "java-spring"
difficulty: "intermediario"
tags: ["cache", "redis", "performance", "java"]
---

# Task: Cache com Spring Cache

## Objetivo
Demonstrar como usar a abstração de cache do Spring para melhorar performance de consultas frequentes, suportando Redis como provedor.

## Código de Exemplo

```java
@Service
@CacheConfig(cacheNames = "users")
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Cacheable(key = "#id", unless = "#result == null")
    public UserResponse findById(Long id) {
        simulateSlowQuery();
        return userRepository.findById(id)
            .map(UserMapper::toResponse)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }

    @Cacheable(key = "#email")
    public UserResponse findByEmail(String email) {
        return userRepository.findByEmail(email)
            .map(UserMapper::toResponse)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }

    @CachePut(key = "#result.id")
    public UserResponse update(Long id, UpdateUserRequest request) {
        User user = userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        user.setName(request.name());
        return UserMapper.toResponse(userRepository.save(user));
    }

    @CacheEvict(key = "#id")
    public void delete(Long id) {
        userRepository.deleteById(id);
    }

    @CacheEvict(allEntries = true)
    public void clearCache() {
        // Cache cleared
    }

    private void simulateSlowQuery() {
        try { Thread.sleep(1000); } catch (InterruptedException e) {}
    }
}
```

## Conceitos Demonstrados
- @Cacheable para leitura com cache
- @CachePut para atualização
- @CacheEvict para invalidação
- Cache key customizada
- Condição 'unless' para null

## Uso na Imagem
Título: "Spring Cache + Redis" com ícone de cache/lightning.
