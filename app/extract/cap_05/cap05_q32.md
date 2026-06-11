---
id: "dantas-cap05-q32"
titulo: "Transformação Linear de Uniforme para U(0,1)"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Y = (X-a)/(b-a)"
tags: ["metodo-fda"]
referencia: "Dantas, Cap. 5, Q. 32"
---

## Enunciado

$X \sim U(a,b)$. Determine $\alpha, \beta \in \mathbb{R}$ tais que $Y = \alpha X + \beta \sim U(0,1)$.

## Solução

Queremos $Y = \alpha X + \beta$ com $P(0 \le Y \le 1) = 1$. Isso exige:
- $\alpha a + \beta = 0$ e $\alpha b + \beta = 1$.

Subtraindo: $\alpha(b-a) = 1 \implies \alpha = 1/(b-a)$.

Substituindo: $\beta = -a/(b-a)$.

Portanto:

$$Y = \frac{X - a}{b - a} \sim U(0,1).$$

Verificação: $F_Y(y) = P(Y \le y) = P(X \le a + y(b-a)) = y$ para $y \in [0,1]$. $\checkmark$
