---
title: "Flyway - Migração de Banco de Dados"
description: "Gerenciar versão do schema do banco usando Flyway no Spring Boot"
stack: "Java 17 + Spring Boot 3 + Flyway + PostgreSQL"
category: "java-spring"
difficulty: "intermediario"
tags: ["flyway", "migration", "database", "java"]
---

# Task: Flyway - Migração de Banco de Dados

## Objetivo
Implementar migrações de banco de dados versionadas e reproduzíveis usando Flyway, garantindo integridade do schema em todos os ambientes.

## Código de Exemplo

```sql
-- V1__create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_active ON users(active);

-- V2__create_posts_table.sql
CREATE TABLE posts (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    user_id BIGINT NOT NULL,
    published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_posts_user FOREIGN KEY (user_id) REFERENCES users(id)
);

-- V3__add_user_avatar.sql
ALTER TABLE users ADD COLUMN avatar_url VARCHAR(500);
ALTER TABLE users ADD COLUMN bio TEXT;
```

```yaml
# application.yml
spring:
  flyway:
    enabled: true
    locations: classpath:db/migration
    baseline-on-migrate: true
    validate-on-migrate: true
```

```java
// Verificação em runtime
@Component
public class FlywayHealthCheck implements HealthIndicator {

    private final Flyway flyway;

    @Override
    public Health health() {
        try {
            FlywayStatus status = flyway.info().getLatest().getType();
            if (status == FlywayStatus.SUCCESS) {
                return Health.up().withDetail("migration", "current").build();
            }
            return Health.down().withDetail("migration", status).build();
        } catch (Exception e) {
            return Health.down().withException(e).build();
        }
    }
}
```

## Conceitos Demonstrados
- Migrations SQL versionadas (V1__, V2__)
- Índices e constraints
- Configuração Spring Boot
- Validação de migrations
- Health check do Flyway

## Uso na Imagem
Título: "Flyway Database Migrations" com ícone de database e setas de versão.
