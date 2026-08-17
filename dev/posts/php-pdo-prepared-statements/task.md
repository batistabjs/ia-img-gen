---
title: "PHP - PDO e Prepared Statements"
description: "Acessar banco de dados de forma segura usando PDO com Prepared Statements"
stack: "PHP 8.2+ + PDO"
category: "php"
difficulty: "basico"
tags: ["pdo", "prepared-statements", "database", "php"]
---

# Task: PHP - PDO e Prepared Statements

## Objetivo
Demonstrar como usar PDO para acessar bancos de dados de forma segura, prevenindo SQL Injection com Prepared Statements.

## Código de Exemplo

```php
<?php

// Conexão PDO segura
$dsn = 'mysql:host=localhost;dbname=myapp;charset=utf8mb4';
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
];

try {
    $pdo = new PDO($dsn, 'user', 'password', $options);
} catch (PDOException $e) {
    throw new RuntimeException("Database error: " . $e->getMessage());
}

// ❌ PERIGOSO - SQL Injection
$email = $_GET['email'];
$pdo->query("SELECT * FROM users WHERE email = '$email'");

// ✅ SEGURO - Prepared Statement
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email AND active = :active");
$stmt->execute([
    ':email' => $email,
    ':active' => true
]);
$user = $stmt->fetch();

// Insert com prepared statement
$stmt = $pdo->prepare("
    INSERT INTO posts (title, content, user_id, created_at)
    VALUES (:title, :content, :user_id, NOW())
");
$stmt->execute([
    ':title' => $title,
    ':content' => $content,
    ':user_id' => $userId
]);
$newId = $pdo->lastInsertId();

// Transaction
$pdo->beginTransaction();
try {
    $stmt1 = $pdo->prepare("UPDATE accounts SET balance = balance - :amount WHERE id = :id");
    $stmt1->execute([':amount' => 100, ':id' => 1]);

    $stmt2 = $pdo->prepare("UPDATE accounts SET balance = balance + :amount WHERE id = :id");
    $stmt2->execute([':amount' => 100, ':id' => 2]);

    $pdo->commit();
} catch (Exception $e) {
    $pdo->rollBack();
    throw $e;
}

// Fetch com loop
$stmt = $pdo->query("SELECT * FROM users");
while ($row = $stmt->fetch()) {
    echo $row['name'];
}
```

## Conceitos Demonstrados
- Conexão PDO segura
- Prepared Statements (named params)
- Prevenção de SQL Injection
- Transactions
- Fetch modes

## Uso na Imagem
Título: "PDO & Prepared Statements" com ícone de escudo/segurança.
