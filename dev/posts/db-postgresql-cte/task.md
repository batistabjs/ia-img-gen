---
title: "PostgreSQL - CTEs (Common Table Expressions)"
description: "Simplificar queries complexas com CTEs recursivas e não-recursivas"
stack: "PostgreSQL 16"
category: "database"
difficulty: "intermediario"
tags: ["postgresql", "cte", "recursive", "sql"]
---

# Task: PostgreSQL - CTEs (Common Table Expressions)

## Objetivo
Demonstrar como CTEs tornam queries complexas mais legíveis e manuteníveis, incluindo CTEs recursivas para dados hierárquicos.

## Código de Exemplo

```sql
-- CTE básica para tornar query mais legível
WITH active_users AS (
    SELECT id, name, email
    FROM users
    WHERE active = true
    AND created_at > NOW() - INTERVAL '30 days'
),
user_stats AS (
    SELECT
        u.id,
        u.name,
        COUNT(o.id) as order_count,
        SUM(o.total) as total_spent
    FROM active_users u
    LEFT JOIN orders o ON o.user_id = u.id
    GROUP BY u.id, u.name
)
SELECT
    name,
    order_count,
    total_spent,
    CASE
        WHEN total_spent > 1000 THEN 'VIP'
        WHEN total_spent > 500 THEN 'Premium'
        ELSE 'Regular'
    END as tier
FROM user_stats
WHERE order_count > 0
ORDER BY total_spent DESC;

-- CTE recursiva - Árvore de categorias
WITH RECURSIVE category_tree AS (
    -- Caso base: categorias raiz
    SELECT id, name, parent_id, 0 as level, name as path
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    -- Caso recursivo: subcategorias
    SELECT c.id, c.name, c.parent_id, ct.level + 1,
           ct.path || ' > ' || c.name
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT
    REPEAT('  ', level) || name as display_name,
    path,
    level
FROM category_tree
ORDER BY path;

-- CTE para paginação com cursor
WITH cursor_page AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY id) as rn
    FROM products
    WHERE id > :last_seen_id
)
SELECT * FROM cursor_page
WHERE rn <= 20;
```

## Conceitos Demonstrados
- CTEs não-recursivas
- CTEs recursivas com UNION ALL
- Hierarquias com recursão
- Legibilidade de queries complexas
- Paginação com cursor

## Uso na Imagem
Título: "PostgreSQL CTEs - Common Table Expressions" com diagrama de recursão.
