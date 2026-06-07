---
id: "dantas-cap02-q12"
titulo: "Propriedades da Variancia e Transformacoes Lineares"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["variancia"]
referencia: "Dantas, Cap. 2, Q. 12"
---

## Enunciado
Seja $X$ uma variável aleatória com $E(X^2) < \infty$ e sejam $\alpha$ e $\beta$ constantes reais. 
(a) Mostre que $\text{Var}(\alpha X + \beta) = \alpha^2 \text{Var}(X)$. 
(b) Calcule $E[(\beta X + 4)^2]$ se $E(X) = 10$ e $\text{Var}(X) = 3$.

## Solução

- **(a) Mostre que $\text{Var}(\alpha X + \beta) = \alpha^2 \text{Var}(X)$:**
A variância de uma variável aleatória é definida como a esperança do quadrado do desvio em relação à sua média:
$$ \text{Var}(Y) = E\left[(Y - E[Y])^2\right] $$
Seja $Y = \alpha X + \beta$. Sabemos que $E[\alpha X + \beta] = \alpha E[X] + \beta$.
Substituindo na definição de variância:
$$ \text{Var}(\alpha X + \beta) = E\left[ \left( (\alpha X + \beta) - (\alpha E[X] + \beta) \right)^2 \right] $$
As constantes $\beta$ se anulam:
$$ \text{Var}(\alpha X + \beta) = E\left[ \left( \alpha X - \alpha E[X] \right)^2 \right] $$
Fatorando $\alpha$:
$$ \text{Var}(\alpha X + \beta) = E\left[ \left( \alpha (X - E[X]) \right)^2 \right] $$
$$ \text{Var}(\alpha X + \beta) = E\left[ \alpha^2 (X - E[X])^2 \right] $$
Como $\alpha^2$ é uma constante, pode sair do operador de esperança:
$$ \text{Var}(\alpha X + \beta) = \alpha^2 E\left[ (X - E[X])^2 \right] = \alpha^2 \text{Var}(X) $$

- **(b) Calcule $E[(\beta X + 4)^2]$ se $E(X) = 10$ e $\text{Var}(X) = 3$:**
Primeiro, vamos calcular $E[X^2]$. Sabemos que:
$$ \text{Var}(X) = E[X^2] - (E[X])^2 $$
$$ 3 = E[X^2] - (10)^2 \implies E[X^2] = 3 + 100 = 103 $$
Expandindo o quadrado do binômio procurado:
$$ (\beta X + 4)^2 = \beta^2 X^2 + 8\beta X + 16 $$
Aplicando a esperança pela linearidade:
$$ E\left[ \beta^2 X^2 + 8\beta X + 16 \right] = \beta^2 E[X^2] + 8\beta E[X] + 16 $$
Substituindo $E[X] = 10$ e $E[X^2] = 103$:
$$ E\left[ (\beta X + 4)^2 \right] = \beta^2 (103) + 8\beta (10) + 16 $$
$$ E\left[ (\beta X + 4)^2 \right] = 103\beta^2 + 80\beta + 16 $$
