---
id: "dantas-cap02-q06"
titulo: "Distribuicao Exponencial: FDP e Probabilidades"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade"]
referencia: "Dantas, Cap. 2, Q. 6"
---

## Enunciado
Seja $X$ uma variável aleatória contínua cuja função densidade de probabilidade é dada por: $f(x) = \lambda e^{-\lambda x}$ para $x > 0$ e zero no complementar. 
(a) Verifique que $\int_{-\infty}^{\infty} f(x)dx = 1$. 
(b) Calcule $P(X > 6)$. 
(c) Esboce o gráfico de $f(x)$.

## Solução

A função de densidade apresentada corresponde à clássica Distribuição Exponencial com parâmetro $\lambda > 0$.

- **(a) Verifique que a integral é igual a 1:**
$$ \int_{-\infty}^{\infty} f(x) \, dx = \int_{0}^{\infty} \lambda e^{-\lambda x} \, dx $$
A integral de $e^{-\lambda x}$ é $-\frac{1}{\lambda} e^{-\lambda x}$. Aplicando isso:
$$ \int_{0}^{\infty} \lambda e^{-\lambda x} \, dx = \lambda \left[ -\frac{1}{\lambda} e^{-\lambda x} \right]_0^\infty = \left[ -e^{-\lambda x} \right]_0^\infty $$
Avaliando os limites de integração:
$$ \lim_{x \to \infty} (-e^{-\lambda x}) - (-e^0) = 0 - (-1) = 1 $$
A propriedade está verificada.

- **(b) Calcule $P(X > 6)$:**
Podemos integrar a função densidade de 6 a $\infty$:
$$ P(X > 6) = \int_{6}^{\infty} \lambda e^{-\lambda x} \, dx = \left[ -e^{-\lambda x} \right]_6^\infty $$
$$ P(X > 6) = 0 - (-e^{-6\lambda}) = e^{-6\lambda} $$

- **(c) Esboço do gráfico de $f(x)$:**
A curva da função $f(x) = \lambda e^{-\lambda x}$ descreve um decaimento exponencial restrito ao primeiro quadrante ($x \ge 0$). 
- Quando $x = 0$, $f(0) = \lambda$. Esse é o ponto de intercepto no eixo Y (o valor máximo da densidade).
- Conforme $x$ cresce ($x \to \infty$), o valor de $e^{-\lambda x}$ tende assintoticamente a zero, então a curva decresce rapidamente aproximando-se do eixo X, sem nunca o cruzar.
- Para $x < 0$, a função é 0 (uma linha reta coincidente com o eixo negativo).
