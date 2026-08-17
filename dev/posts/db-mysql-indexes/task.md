---
title: "MySQL - Indexes e Performance"
description: "Otimizar consultas com estratégias de indexação em MySQL"
stack: "MySQL 8.0"
category: "database"
difficulty: "intermediario"
tags: ["mysql", "indexes", "performance", "sql"]
---

# Task: MySQL - Indexes e Performance

## Objetivo
Demonstrar como criar e usar índices eficientes no MySQL para melhorar drasticamente a performance de consultas.

## Código de Exemplo

```sql
-- Índice simples em coluna única
CREATE INDEX idx_users_email ON users(email);

-- Índice composto (coluna da esquerda é obrigatória)
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- ✅ Usa o índice composto corretamente
SELECT * FROM orders
WHERE user_id = 123 AND created_at > '2024-01-01';

-- ❌ Não usa eficientemente (pula user_id)
SELECT * FROM orders WHERE created_at > '2024-01-01';

-- Índice coberto (covering index) - evita acesso à tabela
CREATE INDEX idx_posts_covering ON posts(user_id, status, created_at);

-- Query otimizada com covering index
SELECT created_at FROM posts
WHERE user_id = 456 AND status = 'published';

-- Índice parcial (MySQL 8.0+)
CREATE INDEX idx_active_users ON users(email)
WHERE active = true;

-- Análise de performance com EXPLAIN
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) as order_count
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE u.active = true
GROUP BY u.id
HAVING order_count > 5;

-- Verificar índices não utilizados
SELECT * FROM sys.schema_unused_indexes;

-- Monitorar queries lentas
SHOW VARIABLES LIKE 'slow_query_log';
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;
```

## Conceitos Demonstrados
- Índices simples e compostos
- Covering indexes
- Índices parciais
- EXPLAIN ANALYZE
- Identificação de queries lentas

## Uso na Imagem
Título: "MySQL Indexes & Performance" com gráfico de velocidade.
