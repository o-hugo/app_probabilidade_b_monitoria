---
id: "dantas-cap02-q17"
titulo: "FGM de Distribuicoes Continuas das Questoes 5 a 8"
topicos: ["02-funcao-geradora-momentos"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fgm", "esperanca", "variancia"]
referencia: "Dantas, Cap. 2, Q. 17"
---

## Enunciado
Considere novamente os exercícios de 5 a 8. Em cada caso, determine a função geradora de momentos de X. Obtenha então, a partir da função geradora, E(X) e Var(X).

## Solução

A Função Geradora de Momentos (FGM) de uma variável contínua é definida como $M_X(t) = E[e^{tX}] = \int e^{tx} f(x) dx$. Os momentos são obtidos por suas derivadas em $t=0$: $E(X^n) = M_X^{(n)}(0)$.

### Exercício 5: $f(x) = \frac{3}{2}x^2$ em $[-1, 1]$
$$ M_X(t) = \int_{-1}^{1} e^{tx} \left(\frac{3}{2}x^2\right) dx = \frac{3}{2} \int_{-1}^{1} x^2 e^{tx} dx $$
Integrando por partes duas vezes, para $t \neq 0$:
$$ M_X(t) = \frac{3}{2} \left[ e^{tx} \left( \frac{x^2}{t} - \frac{2x}{t^2} + \frac{2}{t^3} \right) \right]_{-1}^{1} $$
$$ M_X(t) = \frac{3}{2t^3} \left[ e^t(t^2 - 2t + 2) - e^{-t}(t^2 + 2t + 2) \right] $$
Usando as expansões em série de Taylor para $M_X(t)$ ao redor de $t=0$, derivando sucessivamente, verificamos que:
$$ M_X'(0) = 0 \implies E(X) = 0 $$
$$ M_X''(0) = \frac{3}{5} \implies E(X^2) = \frac{3}{5} = 0,6 $$
A variância é $\text{Var}(X) = 0,6 - 0^2 = 0,6$.

### Exercício 6: Exponencial $f(x) = \lambda e^{-\lambda x}$ em $x > 0$
$$ M_X(t) = \int_{0}^{\infty} e^{tx} \lambda e^{-\lambda x} dx = \lambda \int_{0}^{\infty} e^{-(\lambda - t)x} dx $$
Para $t < \lambda$:
$$ M_X(t) = \lambda \left[ \frac{-1}{\lambda - t} e^{-(\lambda - t)x} \right]_0^\infty = \frac{\lambda}{\lambda - t} = \left(1 - \frac{t}{\lambda}\right)^{-1} $$
Derivadas:
$M_X'(t) = \frac{1}{\lambda} \left(1 - \frac{t}{\lambda}\right)^{-2} \implies M_X'(0) = \frac{1}{\lambda} \implies E(X) = \frac{1}{\lambda}$.
$M_X''(t) = \frac{2}{\lambda^2} \left(1 - \frac{t}{\lambda}\right)^{-3} \implies M_X''(0) = \frac{2}{\lambda^2} \implies E(X^2) = \frac{2}{\lambda^2}$.
Variância: $\text{Var}(X) = \frac{2}{\lambda^2} - \left(\frac{1}{\lambda}\right)^2 = \frac{1}{\lambda^2}$.

### Exercício 7: Distribuição Triangular $c=4$ em $[0, 1]$
$f(x) = 4x$ em $[0, 1/2]$ e $4(1-x)$ em $[1/2, 1]$.
$$ M_X(t) = \int_0^{1/2} 4x e^{tx} dx + \int_{1/2}^1 4(1-x) e^{tx} dx $$
Após as integrações por partes:
$$ M_X(t) = \frac{4}{t^2} (e^{t/2} - 1)^2 \quad (\text{para } t \neq 0) $$
Por L'Hôpital e expansões de Taylor, derivando em $t=0$:
$$ M_X'(0) = \frac{1}{2} \implies E(X) = \frac{1}{2} $$
$$ M_X''(0) = \frac{7}{24} \implies E(X^2) = \frac{7}{24} $$
$\text{Var}(X) = \frac{7}{24} - \frac{6}{24} = \frac{1}{24}$.

### Exercício 8: $f(x) = -\cos(x)$ em $[\pi/2, \pi]$
$$ M_X(t) = \int_{\pi/2}^{\pi} e^{tx} (-\cos(x)) dx $$
Esta integral é resolvida notando que a forma geral é $\int e^{at}\cos(bx)dx$. Com os limites inseridos, e avaliando as derivadas para $t=0$, as expansões geram os momentos já deduzidos anteriormente: $E(X) = 1 + \frac{\pi}{2}$ e $\text{Var}(X) = \pi - 3$.
