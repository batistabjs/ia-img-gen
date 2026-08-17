---
title: "Spring Security com JWT"
description: "Implementar autenticação stateless usando JWT com Spring Security"
stack: "Java 17 + Spring Boot 3 + Spring Security + JWT"
category: "java-spring"
difficulty: "avancado"
tags: ["spring-security", "jwt", "autenticacao", "java"]
---

# Task: Spring Security com JWT

## Objetivo
Configurar autenticação baseada em tokens JWT para uma API REST, incluindo geração, validação e refresh de tokens.

## Código de Exemplo

```java
@Component
public class JwtTokenProvider {

    @Value("${jwt.secret}")
    private String jwtSecret;

    @Value("${jwt.expiration}")
    private long jwtExpiration;

    public String generateToken(Authentication authentication) {
        UserPrincipal userPrincipal = (UserPrincipal) authentication.getPrincipal();

        Date now = new Date();
        Date expiryDate = new Date(now.getTime() + jwtExpiration);

        return Jwts.builder()
                .setSubject(Long.toString(userPrincipal.getId()))
                .claim("email", userPrincipal.getEmail())
                .setIssuedAt(now)
                .setExpiration(expiryDate)
                .signWith(SignatureAlgorithm.HS512, jwtSecret)
                .compact();
    }

    public Long getUserIdFromToken(String token) {
        Claims claims = Jwts.parser()
                .setSigningKey(jwtSecret)
                .parseClaimsJws(token)
                .getBody();

        return Long.parseLong(claims.getSubject());
    }

    public boolean validateToken(String authToken) {
        try {
            Jwts.parser().setSigningKey(jwtSecret).parseClaimsJws(authToken);
            return true;
        } catch (JwtException | IllegalArgumentException e) {
            return false;
        }
    }
}
```

## Conceitos Demonstrados
- Geração de tokens JWT
- Extração de claims
- Validação de tokens
- Configuração de expiração
- Algoritmo de assinatura HS512

## Uso na Imagem
Código com destaque para as operações JWT. Título: "JWT Authentication com Spring Security".
