---
title: "WebSockets com Spring"
description: "Implementar comunicação em tempo real usando WebSockets com Spring Boot"
stack: "Java 17 + Spring Boot 3 + WebSocket + STOMP"
category: "java-spring"
difficulty: "avancado"
tags: ["websocket", "stomp", "real-time", "java"]
---

# Task: WebSockets com Spring

## Objetivo
Configurar WebSocket com protocolo STOMP para comunicação em tempo real entre cliente e servidor.

## Código de Exemplo

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOriginPatterns("*")
                .withSockJS();
    }
}

@Controller
public class ChatController {

    @MessageMapping("/chat.sendMessage")
    @SendTo("/topic/public")
    public ChatMessage sendMessage(@Payload ChatMessage chatMessage) {
        chatMessage.setTimestamp(LocalDateTime.now());
        return chatMessage;
    }

    @MessageMapping("/chat.addUser")
    @SendTo("/topic/public")
    public ChatMessage addUser(@Payload ChatMessage chatMessage,
                               SimpMessageHeaderAccessor headerAccessor) {
        headerAccessor.getSessionAttributes().put("username", chatMessage.getSender());
        chatMessage.setType(MessageType.JOIN);
        return chatMessage;
    }
}

// Cliente JavaScript
// const socket = new SockJS('/ws');
// const stompClient = Stomp.over(socket);
// stompClient.subscribe('/topic/public', (message) => {
//     const chatMessage = JSON.parse(message.body);
//     displayMessage(chatMessage);
// });
```

## Conceitos Demonstrados
- Configuração WebSocket com STOMP
- Message Broker em memória
- Endpoints de mensagem
// - Headers de sessão
// - Cliente JavaScript SockJS

## Uso na Imagem
Título: "WebSockets com Spring Boot" com ícone de comunicação bidirecional.
