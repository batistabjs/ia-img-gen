---
title: "PostgreSQL - Full Text Search"
description: "Implementar busca textual completa nativa no PostgreSQL"
stack: "PostgreSQL 16"
category: "database"
difficulty: "intermediario"
tags: ["postgresql", "full-text-search", "tsvector", "sql"]
---

# Task: PostgreSQL - Full Text Search

## Objetivo
Demonstrar o sistema de Full Text Search nativo do PostgreSQL para buscas de texto eficientes com ranking e stemming.

## Código de Exemplo

```sql
-- Criar tabela com coluna para FTS
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    body TEXT NOT NULL,
    search_vector TSVECTOR
);

-- Criar índice GIN para FTS
CREATE INDEX idx_articles_search ON articles USING GIN (search_vector);

-- Atualizar search_vector automaticamente com trigger
CREATE OR REPLACE FUNCTION update_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector :=
        setweight(to_tsvector('portuguese', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('portuguese', COALESCE(NEW.body, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_articles_search
    BEFORE INSERT OR UPDATE ON articles
    FOR EACH ROW
    EXECUTE FUNCTION update_search_vector();

-- Busca textual simples
SELECT title, body
FROM articles
WHERE search_vector @@ to_tsquery('portuguese', 'spring & boot');

-- Busca com ranking (ts_rank)
SELECT
    title,
    ts_rank(search_vector, query) as rank,
    ts_headline('portuguese', body, query,
        'StartSel=<b>, StopSel=</b>, MaxWords=50'
    ) as highlighted
FROM articles, to_tsquery('portuguese', 'spring & boot') query
WHERE search_vector @@ query
ORDER BY rank DESC;

-- Busca com fuzzy matching (tratar erros de digitação)
SELECT title
FROM articles
WHERE search_vector @@ to_tsquery('portuguese', 'spring & bot');
-- Não encontraria nada, mas usando pg_trgm:

-- Habilitar extensão para fuzzy search
CREATE EXTENSION IF NOT EXISTS pg_trgm;

SELECT title
FROM articles
WHERE title % 'spring bot'  -- % é o operador de similaridade
ORDER BY similarity(title, 'spring bot') DESC;

-- Autocomplete
SELECT DISTINCT title
FROM articles
WHERE title ILIKE 'spring%'
LIMIT 10;
```

## Conceitos Demonstrados
- Tipo TSVECTOR e TSQUERY
- Índice GIN para FTS
- Pesos (A, B, C, D) para relevância
- ts_rank para ranking
- ts_headline para highlighting
- Fuzzy search com pg_trgm

## Uso na Imagem
Título: "PostgreSQL Full Text Search" com ícone de lupa/busca.
