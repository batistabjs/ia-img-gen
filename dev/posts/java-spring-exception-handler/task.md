---
title: "Tratamento Global de Exceções"
description: "Implementar handler global de exceções com @ControllerAdvice para tratamento consistente de erros"
stack: "Java 17 + Spring Boot 3"
category: "java-spring"
difficulty: "intermediario"
tags: ["exception-handling", "controller-advice", "java"]
---

# Task: Tratamento Global de Exceções

## Objetivo
Criar um mecanismo centralizado de tratamento de exceções usando @ControllerAdvice, garantindo responses consistentes em toda a API.

## Código de Exemplo

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(fieldError ->
            errors.put(fieldError.getField(), fieldError.getDefaultMessage())
        );

        ErrorResponse error = new ErrorResponse(
            HttpStatus.BAD_REQUEST.value(),
            "Dados inválidos",
            LocalDateTime.now(),
            errors
        );
        return ResponseEntity.badRequest().body(error);
    }

    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<ErrorResponse> handleDataIntegrity(DataIntegrityViolationException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.CONFLICT.value(),
            "Violação de integridade dos dados",
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneral(Exception ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            "Erro interno do servidor",
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

## Conceitos Demonstrados
- @ControllerAdvice para tratamento global
- Exceções específicas do domínio
- Validação de campos com BindingResult
- Response padronizada com ErrorResponse

## Uso na Imagem
Título: "Exception Handling Global" com destaque para a anotação @RestControllerAdvice.
