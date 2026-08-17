---
title: "PostgreSQL - Window Functions"
description: "Usar Window Functions para análises complexas sem agrupar resultados"
stack: "PostgreSQL 16"
category: "database"
difficulty: "avancado"
tags: ["postgresql", "window-functions", "analytics", "sql"]
---

# Task: PostgreSQL - Window Functions

## Objetivo
Demonstrar Window Functions do PostgreSQL para realizar cálculos analíticos complexos sem colapsar linhas como GROUP BY.

## Código de Exemplo

```sql
-- Ranking de vendas por funcionário dentro de cada departamento
SELECT
    employee_name,
    department,
    sales_amount,
    RANK() OVER (
        PARTITION BY department
        ORDER BY sales_amount DESC
    ) as rank_in_dept,
    RANK() OVER (
        ORDER BY sales_amount DESC
    ) as global_rank
FROM sales;

-- Média móvel de 7 dias
SELECT
    date,
    revenue,
    AVG(revenue) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as moving_avg_7d
FROM daily_revenue;

-- Cálculo de percentual do total
SELECT
    product_name,
    category,
    sales,
    ROUND(
        sales * 100.0 / SUM(sales) OVER (PARTITION BY category),
        2
    ) as pct_in_category,
    SUM(sales) OVER (
        PARTITION BY category
        ORDER BY sales DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_total
FROM product_sales;

-- Lag e Lead para comparação com período anterior
SELECT
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) as prev_month,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) as growth,
    LEAD(revenue, 1) OVER (ORDER BY month) as next_month
FROM monthly_revenue;

-- NTILE para divisão em quartis
SELECT
    customer_id,
    total_spent,
    NTILE(4) OVER (ORDER BY total_spent DESC) as spending_quartile
FROM customer_totals;
```

## Conceitos Demonstrados
- RANK, DENSE_RANK, ROW_NUMBER
- PARTITION BY para segmentação
- Funções de janela (ROWS/RANGE)
- LAG e LEAD
- NTILE para bucketing

## Uso na Imagem
Título: "PostgreSQL Window Functions" com gráfico de análise.
