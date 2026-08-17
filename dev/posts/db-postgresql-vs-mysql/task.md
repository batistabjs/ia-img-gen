---
title: "PostgreSQL vs MySQL - Comparação"
description: "Entender as diferenças, vantagens e caso de uso de cada banco de dados"
stack: "PostgreSQL 16 / MySQL 8.0"
category: "database"
difficulty: "intermediario"
tags: ["postgresql", "mysql", "comparison", "database"]
---

# Task: PostgreSQL vs MySQL - Comparação

## Objetivo
Comparar PostgreSQL e MySQL em termos de funcionalidades, performance e caso de uso ideal para cada cenário.

## Código de Exemplo

```sql
-- ============================================
-- DIFERENÇAS DE SINTAXE
-- ============================================

-- SERIAL vs AUTO_INCREMENT
-- PostgreSQL:
CREATE TABLE users_pg (
    id SERIAL PRIMARY KEY,  -- ou GENERATED ALWAYS AS IDENTITY
    name VARCHAR(100) NOT NULL
);

-- MySQL:
CREATE TABLE users_mysql (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- UPSERT (INSERT or UPDATE)
-- PostgreSQL:
INSERT INTO users (email, name) VALUES ('a@a.com', 'João')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- MySQL:
INSERT INTO users (email, name) VALUES ('a@a.com', 'João')
ON DUPLICATE KEY UPDATE name = VALUES(name);

-- JSON queries
-- PostgreSQL (nativo):
SELECT data->>'name' FROM users WHERE data @> '{"active": true}';

-- MySQL (JSON functions):
SELECT JSON_EXTRACT(data, '$.name') FROM users
WHERE JSON_CONTAINS(data, '{"active": true}');

-- CTEs recursivos
-- PostgreSQL: WITH RECURSIVE (suporte completo)
-- MySQL 8.0+: WITH RECURSIVE (suporte desde 8.0)

-- Full Text Search
-- PostgreSQL: tsvector, tsquery, GIN indexes
-- MySQL: FULLTEXT indexes, MATCH AGAINST

-- ============================================
-- QUANDO USAR CADA UM
-- ============================================

-- ✅ PostgreSQL quando:
-- - Precisa de JSONB nativo
-- - Dados geográficos (PostGIS)
-- - Custom types e enums complexos
-- - Transactions ACID completas
-- - Extensibilidade (extensões)

-- ✅ MySQL quando:
-- - Aplicações web simples (WordPress, Laravel)
-- - Read-heavy workloads
-- - Replicação master-slave simples
-- - Ecossistema mais maduro para CMS
-- - Host compartilhado disponível
```

## Conceitos Demonstrados
- Diferenças de sintaxe
- UPSERT em cada banco
- JSON nativo vs JSON functions
- Casos de uso ideais
- Trade-offs de cada opção

## Uso na Imagem
Título: "PostgreSQL vs MySQL - Which to Choose?" com diagrama comparativo.
