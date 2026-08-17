---
title: "Spring Boot Profiles"
description: "Configurar múltiplos ambientes usando Profiles no Spring Boot"
stack: "Java 17 + Spring Boot 3"
category: "java-spring"
difficulty: "basico"
tags: ["profiles", "configuration", "java"]
---

# Task: Spring Boot Profiles

## Objetivo
Demonstrar como usar Profiles para gerenciar configurações diferentes para cada ambiente (dev, test, prod) em uma aplicação Spring Boot.

## Código de Exemplo

```java
// application.yml (default)
spring:
  application:
    name: my-api
  profiles:
    active: dev

---
# application-dev.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
  jpa:
    show-sql: true
    hibernate:
      ddl-auto: create-drop

logging:
  level:
    com.app: DEBUG

---
# application-prod.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USER}
    password: ${DB_PASS}
  jpa:
    show-sql: false
    hibernate:
      ddl-auto: validate

logging:
  level:
    root: WARN
    com.app: INFO

---
// Configuração condicional
@Configuration
@Profile("prod")
public class ProductionConfig {

    @Bean
    public CacheManager cacheManager() {
        return new ConcurrentMapCacheManager("users", "products");
    }
}
```

## Conceitos Demonstrados
- Arquivos de configuração por profile
- Separação dev/test/prod
- @Profile para beans condicionais
- Variáveis de ambiente em produção

## Uso na Imagem
Título: "Spring Boot Profiles - Multi-ambiente" com ícones de configuração.
