---
id: "lista02-q21-taxa-de-mortalidade"
titulo: "Taxa de Mortalidade"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

O que significa dizer que a taxa de mortalidade de fumantes é o dobro da de não-fumantes, i.e., $\lambda_F(t) = 2\lambda_{NF}(t)$?

## Solução

A probabilidade de sobreviver até o tempo T é a função de confiabilidade $R(T) = e^{-\int_0^T \lambda(t) dt}$.<br>Para não-fumantes: $R_{NF}(T) = e^{-\int_0^T \lambda_{NF}(t) dt}$.<br>Para fumantes: $R_F(T) = e^{-\int_0^T \lambda_F(t) dt} = e^{-\int_0^T 2\lambda_{NF}(t) dt} = e^{-2\int_0^T \lambda_{NF}(t) dt}$.<br>Substituindo a expressão de $R_{NF}$:<br>$ R_F(T) = (e^{-\int_0^T \lambda_{NF}(t) dt})^2 = (R_{NF}(T))^2 $.<br>Isso significa que a probabilidade de um fumante sobreviver é o **quadrado** da probabilidade de um não-fumante, uma redução muito mais drástica do que simplesmente a metade.
