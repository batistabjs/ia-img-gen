---
title: "MySQL - Replication Setup"
description: "Configurar replicação master-slave para alta disponibilidade e balanceamento"
stack: "MySQL 8.0"
category: "database"
difficulty: "avancado"
tags: ["mysql", "replication", "high-availability", "sql"]
---

# Task: MySQL - Replication Setup

## Objetivo
Configurar replicação entre servidores MySQL para alta disponibilidade, backup e balanceamento de leitura.

## Código de Exemplo

```sql
-- ============================================
-- CONFIGURAÇÃO NO SERVIDOR MASTER
-- ============================================

-- Habilitar binlog no my.cnf
-- [mysqld]
-- server-id = 1
-- log-bin = mysql-bin
-- binlog-format = ROW

-- Criar usuário de replicação
CREATE USER 'repl_user'@'%' IDENTIFIED BY 'strong_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl_user'@'%';
FLUSH PRIVILEGES;

-- Verificar status do binlog
SHOW MASTER STATUS;
-- +------------------+----------+--------------+------------------+-------------------------------------------+
-- | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set                         |
-- +------------------+----------+--------------+------------------+-------------------------------------------+
-- | mysql-bin.000003 |      785 |              |                  | a1b2c3d4-e5f6-7890-abcd-ef1234567890:1-5 |
-- +------------------+----------+--------------+------------------+-------------------------------------------+

-- ============================================
-- CONFIGURAÇÃO NO SERVIDOR SLAVE
-- ============================================

-- [mysqld]
-- server-id = 2
-- relay-log = relay-bin
-- read-only = 1

-- Configurar replicação
CHANGE MASTER TO
    MASTER_HOST = '192.168.1.100',
    MASTER_USER = 'repl_user',
    MASTER_PASSWORD = 'strong_password',
    MASTER_LOG_FILE = 'mysql-bin.000003',
    MASTER_LOG_POS = 785;

-- Iniciar replicação
START SLAVE;

-- Verificar status da replicação
SHOW SLAVE STATUS\G
-- Verificar:
-- Slave_IO_Running: Yes
-- Slave_SQL_Running: Yes
-- Seconds_Behind_Master: 0

-- Verificar erros
SHOW SLAVE STATUS\G | grep -E 'Running|Error|Behind'
```

## Conceitos Demonstrados
- Configuração de binlog
- Usuário de replicação
- CHANGE MASTER TO
- Monitoramento de replicação
- Detecção de erros

## Uso na Imagem
Título: "MySQL Replication - Master/Slave" com diagrama de réplicas.
