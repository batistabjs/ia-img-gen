---
title: "MySQL - Transactions e Isolation Levels"
description: "Gerenciar concorrência com transactions e níveis de isolamento"
stack: "MySQL 8.0"
category: "database"
difficulty: "avancado"
tags: ["mysql", "transactions", "isolation", "sql"]
---

# Task: MySQL - Transactions e Isolation Levels

## Objetivo
Demonstrar como usar transações e níveis de isolamento para garantir consistência em operações concorrentes no MySQL.

## Código de Exemplo

```sql
-- Transaction básica
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Verificar se as duas operações foram bem sucedidas
SELECT balance FROM accounts WHERE id IN (1, 2);

COMMIT;  -- ou ROLLBACK se algo falhou

-- Níveis de Isolation Level
-- Verificar nível atual
SELECT @@transaction_isolation;
-- Possíveis valores: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE

-- Definir nível de isolamento
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- ============================================
-- PROBLEMAS DE CONCORRÊNCIA
-- ============================================

-- Dirty Read (só acontece em READ UNCOMMITTED)
-- Sessão 1: START TRANSACTION; UPDATE accounts SET balance = 0 WHERE id = 1;
-- Sessão 2: SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
--           SELECT balance FROM accounts WHERE id = 1;  -- Vê 0 (não commitado)

-- Non-Repeatable Read (READ COMMITTED)
-- Sessão 1: START TRANSACTION; SELECT balance FROM accounts WHERE id = 1;  -- 100
-- Sessão 2: UPDATE accounts SET balance = 200 WHERE id = 1; COMMIT;
-- Sessão 1: SELECT balance FROM accounts WHERE id = 1;  -- Agora vê 200!

-- Phantom Read (REPEATABLE READ)
-- Sessão 1: START TRANSACTION; SELECT COUNT(*) FROM accounts WHERE balance > 0;  -- 5
-- Sessão 2: INSERT INTO accounts (balance) VALUES (500); COMMIT;
-- Sessão 1: SELECT COUNT(*) FROM accounts WHERE balance > 0;  -- Agora vê 6!

-- ============================================
-- LOCKS
-- ============================================

--悲观锁 (Pessimistic Lock)
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;  -- Bloqueia a linha
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- 乐观锁 (Optimistic Lock) - usando version column
-- UPDATE accounts SET balance = balance - 100, version = version + 1
-- WHERE id = 1 AND version = 5;  -- Se version mudou, falha
```

## Conceitos Demonstrados
- START TRANSACTION, COMMIT, ROLLBACK
- Isolation Levels (4 níveis)
- Dirty Read, Non-Repeatable Read, Phantom Read
-悲观锁 (FOR UPDATE)
- 乐观锁 (version column)

## Uso na Imagem
Título: "MySQL Transactions & Isolation" com diagrama de concorrência.
