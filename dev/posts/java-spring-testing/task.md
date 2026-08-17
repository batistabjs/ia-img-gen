---
title: "Testes com Spring Boot"
description: "Escrever testes unitários e de integração usando JUnit 5 e MockMvc"
stack: "Java 17 + Spring Boot 3 + JUnit 5 + Mockito + MockMvc"
category: "java-spring"
difficulty: "intermediario"
tags: ["testing", "junit5", "mockito", "java"]
---

# Task: Testes com Spring Boot

## Objetivo
Demonstrar como escrever testes unitários e de integração robustos usando JUnit 5, Mockito e MockMvc no Spring Boot.

## Código de Exemplo

```java
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldReturnUser_whenFindById() throws Exception {
        UserResponse user = new UserResponse(1L, "João", "joao@email.com");

        when(userService.findById(1L)).thenReturn(user);

        mockMvc.perform(get("/api/users/1"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("João"))
               .andExpect(jsonPath("$.email").value("joao@email.com"));
    }

    @Test
    void shouldReturn404_whenUserNotFound() throws Exception {
        when(userService.findById(99L))
            .thenThrow(new ResourceNotFoundException("User not found"));

        mockMvc.perform(get("/api/users/99"))
               .andExpect(status().isNotFound());
    }

    @Test
    void shouldCreateUser_whenValidData() throws Exception {
        CreateUserRequest request = new CreateUserRequest("Maria", "maria@email.com", "12345678");
        UserResponse response = new UserResponse(1L, "Maria", "maria@email.com");

        when(userService.create(any(CreateUserRequest.class))).thenReturn(response);

        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)))
               .andExpect(status().isCreated())
               .andExpect(jsonPath("$.name").value("Maria"));
    }
}

// Teste de integração
@DataJpaTest
class UserRepositoryTest {

    @Autowired
    private TestEntityManager entityManager;

    @Autowired
    private UserRepository userRepository;

    @Test
    void shouldFindUserByEmail() {
        User user = new User("Test", "test@email.com");
        entityManager.persistAndFlush(user);

        Optional<User> found = userRepository.findByEmail("test@email.com");

        assertThat(found).isPresent();
        assertThat(found.get().getName()).isEqualTo("Test");
    }
}
```

## Conceitos Demonstrados
- @WebMvcTest para testes de controller
- MockBean para isolar dependências
- MockMvc para simular requisições HTTP
- @DataJpaTest para testes de repositório
- AssertJ para assertions fluentes

## Uso na Imagem
Título: "Testes em Spring Boot" com ícone de check/teste.
