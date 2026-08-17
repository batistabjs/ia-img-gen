---
title: "Validação de Dados com Bean Validation"
description: "Implementar validação robusta de dados usando anotações Bean Validation no Spring Boot"
stack: "Java 17 + Spring Boot 3 + Hibernate Validator"
category: "java-spring"
difficulty: "basico"
tags: ["bean-validation", "hibernate-validator", "java"]
---

# Task: Validação de Dados com Bean Validation

## Objetivo
Demonstrar como usar as anotações de validação do Bean Validation (JSR 380) para validar dados de entrada em uma aplicação Spring Boot.

## Código de Exemplo

```java
public record CreateUserRequest(

    @NotBlank(message = "Nome é obrigatório")
    @Size(min = 2, max = 100, message = "Nome deve ter entre 2 e 100 caracteres")
    String name,

    @NotBlank(message = "Email é obrigatório")
    @Email(message = "Email deve ser válido")
    String email,

    @NotBlank(message = "Senha é obrigatória")
    @Size(min = 8, message = "Senha deve ter no mínimo 8 caracteres")
    @Pattern(regexp = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).*$",
             message = "Senha deve conter maiúscula, minúscula e número")
    String password,

    @NotNull(message = "Data de nascimento é obrigatória")
    @Past(message = "Data de nascimento deve ser no passado")
    LocalDate birthDate,

    @Valid
    AddressRequest address
) {}

// Custom validator
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = CpfValidator.class)
public @interface Cpf {
    String message() default "CPF inválido";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}
```

## Conceitos Demonstrados
- Anotações @NotBlank, @Email, @Size, @Pattern
- Validação de data com @Past
- Validação em cascata com @Valid
- Validador customizado para CPF

## Uso na Imagem
Título: "Bean Validation no Spring Boot" com destaque para as anotações de validação.
