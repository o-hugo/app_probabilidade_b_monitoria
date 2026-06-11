---
id: "dantas-cap03-q05"
titulo: "Expressão de P(X>x, Y>y) em termos da f.d.a. conjunta"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "P(X>x, Y>y) = 1 - F_X(x) - F_Y(y) + F(x,y)"
tags: ["fda", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 5"
---

# Expressão de P(X>x, Y>y) em termos da f.d.a. conjunta

## Enunciado

Sejam $X$ e $Y$ variáveis aleatórias com f.d.a. conjunta $F(x, y) = P(X \leq x, Y \leq y)$. Denote por $F_X(x) = P(X \leq x)$ e $F_Y(y) = P(Y \leq y)$ as distribuições marginais. Mostre que:

$$P(X > x,\ Y > y) = 1 - F_X(x) - F_Y(y) + F(x, y).$$

---

## Solução

Utilizamos o princípio da inclusão-exclusão junto com a lei da probabilidade total.

**Passo 1:** Escreva o complementar do evento $\{X > x, Y > y\}$:

$$\{X > x, Y > y\}^c = \{X \leq x\} \cup \{Y \leq y\}.$$

**Passo 2:** Pela lei da probabilidade:

$$P(X > x, Y > y) = 1 - P(\{X \leq x\} \cup \{Y \leq y\}).$$

**Passo 3:** Pela fórmula de inclusão-exclusão:

$$P(\{X \leq x\} \cup \{Y \leq y\}) = P(X \leq x) + P(Y \leq y) - P(X \leq x, Y \leq y).$$

**Passo 4:** Substituindo:

$$P(X > x, Y > y) = 1 - P(X \leq x) - P(Y \leq y) + P(X \leq x, Y \leq y)$$

$$= 1 - F_X(x) - F_Y(y) + F(x, y). \qquad \blacksquare$$
