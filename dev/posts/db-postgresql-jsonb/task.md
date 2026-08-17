---
title: "PostgreSQL - JSONB Queries"
description: "Armazenar e consultar dados JSON nativamente com o tipo JSONB"
stack: "PostgreSQL 16"
category: "database"
difficulty: "avancado"
tags: ["postgresql", "jsonb", "nosql", "sql"]
---

# Task: PostgreSQL - JSONB Queries

## Objetivo
Demonstrar o poder do tipo JSONB do PostgreSQL para armazenar e consultar dados semiestruturados com performance nativa.

## Código de Exemplo

```sql
-- Criar tabela com coluna JSONB
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Inserir dados com JSONB
INSERT INTO events (name, metadata) VALUES
('page_view', '{"page": "/home", "user_id": 42, "browser": "Chrome"}'),
('purchase', '{"product_id": 100, "amount": 99.90, "currency": "BRL"}'),
('signup', '{"method": "email", "referrer": "google.com"}');

-- Consultar com operador ->
SELECT name, metadata->>'page' as page
FROM events
WHERE metadata->>'page' IS NOT NULL;

-- Consultar com ->
SELECT * FROM events
WHERE metadata->'amount' > 50;

-- Contém (contains)
SELECT * FROM events
WHERE metadata @> '{"browser": "Chrome"}';

-- Chaves existentes
SELECT * FROM events
WHERE metadata ? 'user_id';

-- Busca em array JSONB
SELECT * FROM events
WHERE metadata->'tags' ? 'premium';

-- Criar índice GIN para buscas JSONB
CREATE INDEX idx_events_metadata ON events USING GIN (metadata);

-- Agregar dados JSONB
SELECT
    metadata->>'currency' as currency,
    COUNT(*) as count,
    SUM((metadata->>'amount')::numeric) as total
FROM events
WHERE name = 'purchase'
GROUP BY currency;

-- Atualizar JSONB
UPDATE events
SET metadata = metadata || '{"converted": true}'::jsonb
WHERE id = 1;

-- Remover chave
UPDATE events
SET metadata = metadata - 'referrer';
```

## Conceitos Demonstrados
- Tipo JSONB vs JSON
- Operadores ->, ->>, @>, ?
- Índice GIN para buscas
- Atualização e remoção de chaves
- Agregação de dados JSONB

## Uso na Imagem
Título: "PostgreSQL JSONB - NoSQL no SQL" com ícone de JSON/banco.
