---
title: "PostgreSQL - Table Partitioning"
description: "Dividir tabelas grandes em partições para melhor performance e manutenção"
stack: "PostgreSQL 16"
category: "database"
difficulty: "avancado"
tags: ["postgresql", "partitioning", "performance", "sql"]
---

# Task: PostgreSQL - Table Partitioning

## Objetivo
Demonstrar como particionar tabelas grandes no PostgreSQL para melhorar performance de consultas e facilitar manutenção.

## Código de Exemplo

```sql
-- ============================================
-- PARTITIONING POR RANGE (temporal)
-- ============================================

CREATE TABLE orders (
    id BIGSERIAL,
    user_id BIGINT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
) PARTITION BY RANGE (created_at);

-- Criar partições por mês
CREATE TABLE orders_2024_01 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE orders_2024_02 PARTITION OF orders
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

CREATE TABLE orders_2024_03 PARTITION OF orders
    FOR VALUES FROM ('2024-03-01') TO ('2024-04-01');

-- ============================================
-- PARTITIONING POR LIST
-- ============================================

CREATE TABLE products (
    id BIGSERIAL,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
) PARTITION BY LIST (category);

CREATE TABLE products_electronics PARTITION OF products
    FOR VALUES IN ('electronics', 'computers', 'phones');

CREATE TABLE products_clothing PARTITION OF products
    FOR VALUES IN ('clothing', 'shoes', 'accessories');

-- ============================================
-- PARTITIONING POR HASH
-- ============================================

CREATE TABLE sessions (
    id UUID NOT NULL,
    user_id BIGINT NOT NULL,
    data JSONB NOT NULL
) PARTITION BY HASH (user_id);

CREATE TABLE sessions_p0 PARTITION OF sessions
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE sessions_p1 PARTITION OF sessions
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE sessions_p2 PARTITION OF sessions
    FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE sessions_p3 PARTITION OF sessions
    FOR VALUES WITH (MODULUS 4, REMAINDER 3);

-- ============================================
-- MANUTENÇÃO DE PARTIÇÕES
-- ============================================

-- Criar nova.partição automaticamente
CREATE TABLE orders_2024_04 PARTITION OF orders
    FOR VALUES FROM ('2024-04-01') TO ('2024-05-01');

-- Remover.partição antiga (drop cascade)
DROP TABLE orders_2023_01;

-- Verificar particionamento
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
WHERE tablename LIKE 'orders_%'
ORDER BY tablename;
```

## Conceitos Demonstrados
- Partitioning por RANGE, LIST, HASH
- Criar e gerenciar partições
- Manutenção e monitoramento
- Performance com partition pruning

## Uso na Imagem
Título: "PostgreSQL Partitioning" com diagrama de partições.
