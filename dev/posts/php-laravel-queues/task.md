---
title: "Laravel - Queues e Jobs"
description: "Processar tarefas assíncronas usando Queues e Jobs no Laravel"
stack: "PHP 8.2+ + Laravel 11 + Redis/Database"
category: "php"
difficulty: "avancado"
tags: ["laravel", "queues", "jobs", "async", "php"]
---

# Task: Laravel - Queues e Jobs

## Objetivo
Demonstrar como usar Queues para processar tarefas pesadas de forma assíncrona, melhorando a performance e experiência do usuário.

## Código de Exemplo

```php
<?php

// Job para envio de email
class SendWelcomeEmail implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries = 3;
    public int $timeout = 60;

    public function __construct(
        public User $user
    ) {}

    public function handle(Mailer $mailer): void
    {
        $mailer->to($this->user->email)
            ->send(new WelcomeMail($this->user));
    }

    public function failed(Throwable $exception): void
    {
        Log::error("Email failed for user {$this->user->id}", [
            'exception' => $exception
        ]);
    }
}

// Job com cadeia (chain)
class ProcessOrder implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public function handle(): void
    {
        // Processar pagamento
        $this->payment->charge();

        // Enviar email de confirmação
        $this->order->sendConfirmation();

        // Atualizar estoque
        $this->order->updateStock();
    }
}

// Dispatch de jobs
SendWelcomeEmail::dispatch($user);

// Com delay
SendWelcomeEmail::dispatch($user)->delay(now()->addMinutes(5));

// Cadeia de jobs
Bus::chain([
    new ProcessPayment($order),
    new SendConfirmationEmail($order),
    new UpdateInventory($order),
])->onConnection('redis')->onQueue('orders')->dispatch();

// Filtrar jobs com middleware
class RateLimited implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public function middleware(): array
    {
        return [new WithoutOverlapping(5)];
    }
}
```

## Conceitos Demonstrados
- Implementação de ShouldQueue
- Configuração de tries e timeout
- Tratamento de falhas
- Dispatch com delay
- Cadeia de jobs (Bus::chain)
- Middleware de queue

## Uso na Imagem
Título: "Laravel Queues & Jobs" com ícone de fila/async.
