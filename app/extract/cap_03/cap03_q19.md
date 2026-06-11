---
id: "dantas-cap03-q19"
titulo: "X - ρY e Y são não-correlacionados quando Corr(X,Y)=ρ"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(X - ρY, Y) = 0"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 19"
---

# Exercício 19

Sejam $X$ e $Y$ variáveis aleatórias com $E[X] = E[Y] = 0$, $\text{Var}(X) = \text{Var}(Y) = 1$ e $\text{Corr}(X,Y) = \rho$. Verifique que $X - \rho Y$ e $Y$ são não-correlacionados.

---

## Solução

Como $\text{Var}(X) = \text{Var}(Y) = 1$, temos $\text{Cov}(X,Y) = \rho \cdot 1 \cdot 1 = \rho$.

Calculamos $\text{Cov}(X - \rho Y,\; Y)$ usando bilinearidade:

$$\text{Cov}(X - \rho Y,\; Y) = \text{Cov}(X, Y) - \rho\,\text{Cov}(Y, Y)$$

$$= \text{Cov}(X,Y) - \rho\,\text{Var}(Y) = \rho - \rho \cdot 1 = 0. \quad \square$$

Portanto, $X - \rho Y$ e $Y$ são **não-correlacionados**.

> **Interpretação:** A transformação $X \mapsto X - \rho Y$ remove a componente de $X$ que é linearmente associada a $Y$. O resultado $X - \rho Y$ é o "resíduo" de $X$ após projeção linear sobre $Y$, e é ortogonal (no sentido de covariância zero) a $Y$. Esta é a base da **regressão linear simples**.

> **Observação:** Não-correlação não implica independência em geral. Mas se $(X,Y)$ for bivariada normal, então $X - \rho Y$ e $Y$ são de fato independentes.
