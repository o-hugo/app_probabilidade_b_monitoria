---
id: "dantas-cap05-q29"
titulo: "Mediana da Uniforme, Normal e Exponencial"
topicos: ["03-modelos-continuos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "(a)(a+b)/2 (b)μ (c)ln2/λ"
tags: ["mediana"]
referencia: "Dantas, Cap. 5, Q. 29"
---

## Enunciado

Determine a mediana $m$ tal que $F(m) = 1/2$ para: (a) $X \sim U(a,b)$; (b) $X \sim N(\mu, \sigma^2)$; (c) $X \sim \text{Exp}(\lambda)$.

## Solução

**(a)** $F(m) = (m-a)/(b-a) = 1/2 \implies m = (a+b)/2$.

**(b)** $F(m) = \Phi((m-\mu)/\sigma) = 1/2 \implies (m-\mu)/\sigma = 0 \implies m = \mu$.

**(c)** $F(m) = 1 - e^{-\lambda m} = 1/2 \implies e^{-\lambda m} = 1/2 \implies m = \ln 2 / \lambda$.
