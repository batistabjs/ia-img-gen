---
title: "MySQL - Stored Procedures"
description: "Criar e gerenciar procedures e functions para lógica de negócio no banco"
stack: "MySQL 8.0"
category: "database"
difficulty: "intermediario"
tags: ["mysql", "stored-procedures", "functions", "sql"]
---

# Task: MySQL - Stored Procedures

## Objetivo
Demonstrar como criar e usar Stored Procedures e Functions no MySQL para encapsular lógica de negócio no banco de dados.

## Código de Exemplo

```sql
-- Stored Procedure para transferência bancária
DELIMITER //

CREATE PROCEDURE transfer_funds(
    IN p_from_account INT,
    IN p_to_account INT,
    IN p_amount DECIMAL(10,2),
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE v_balance DECIMAL(10,2);

    -- Verificar saldo
    SELECT balance INTO v_balance
    FROM accounts WHERE id = p_from_account
    FOR UPDATE;

    IF v_balance >= p_amount THEN
        -- Debitar
        UPDATE accounts
        SET balance = balance - p_amount
        WHERE id = p_from_account;

        -- Creditar
        UPDATE accounts
        SET balance = balance + p_amount
        WHERE id = p_to_account;

        -- Registrar transação
        INSERT INTO transactions (from_account, to_account, amount)
        VALUES (p_from_account, p_to_account, p_amount);

        SET p_success = TRUE;
    ELSE
        SET p_success = FALSE;
    END IF;
END //

DELIMITER ;

-- Chamar a procedure
CALL transfer_funds(1, 2, 100.00, @success);
SELECT @success;

-- Function para calcular idade
DELIMITER //

CREATE FUNCTION calculate_age(p_birth_date DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, p_birth_date, CURDATE());
END //

DELIMITER ;

-- Usar a function
SELECT name, calculate_age(birth_date) as age
FROM users;
```

## Conceitos Demonstrados
- Procedures com parâmetros IN/OUT
- Variáveis locais
- Controle de fluxo (IF/ELSE)
- Transactions dentro de procedures
- Functions determinísticas

## Uso na Imagem
Título: "MySQL Stored Procedures" com ícone de procedure/processo.
