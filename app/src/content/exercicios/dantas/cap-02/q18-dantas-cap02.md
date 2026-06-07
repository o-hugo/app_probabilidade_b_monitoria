---
id: "dantas-cap02-q18"
titulo: "FGM de Variaveis Aleatorias Discretas"
topicos: ["02-funcao-geradora-momentos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fgm"]
referencia: "Dantas, Cap. 2, Q. 18"
---

## Enunciado
Calcule a função geradora de momentos da variável aleatória X (discreta) quando: 
(a) $f(x) = 1/6$, se $x = 1$ ou $x = -1$, e $f(x) = 4/6$, se $x = 0$. 
(b) $f(x) = (1/2)^x$, $x = 1, 2, 3, \ldots$ 
(c) $f(x) = (1-p)^{x-1}p$, $x = 1, 2, \ldots$

## Solução

A Função Geradora de Momentos (FGM) de uma variável discreta é dada pela esperança $M_X(t) = E[e^{tX}] = \sum e^{tx} P(X=x)$.

- **(a) Variável discreta finita:**
O espaço amostral é $x \in \{-1, 0, 1\}$.
$$ M_X(t) = \sum_{x \in \{-1,0,1\}} e^{tx} f(x) $$
$$ M_X(t) = e^{t(-1)}\left(\frac{1}{6}\right) + e^{t(0)}\left(\frac{4}{6}\right) + e^{t(1)}\left(\frac{1}{6}\right) $$
$$ M_X(t) = \frac{e^{-t}}{6} + \frac{4}{6} + \frac{e^t}{6} $$
Agrupando os termos:
$$ M_X(t) = \frac{e^t + e^{-t}}{6} + \frac{2}{3} $$
*(Opcionalmente, pode-se escrever usando o cosseno hiperbólico: $M_X(t) = \frac{1}{3}\cosh(t) + \frac{2}{3}$).*

- **(b) $f(x) = \left(\frac{1}{2}\right)^x$ para $x = 1, 2, \ldots$:**
$$ M_X(t) = \sum_{x=1}^{\infty} e^{tx} \left(\frac{1}{2}\right)^x $$
Podemos juntar os expoentes $x$:
$$ M_X(t) = \sum_{x=1}^{\infty} \left(\frac{e^t}{2}\right)^x $$
Isto é uma progressão geométrica infinita com primeiro termo $a_1 = \frac{e^t}{2}$ e razão $q = \frac{e^t}{2}$. Converge se $q < 1 \implies e^t < 2 \implies t < \ln 2$.
A soma da P.G. é:
$$ M_X(t) = \frac{a_1}{1 - q} = \frac{\frac{e^t}{2}}{1 - \frac{e^t}{2}} $$
Multiplicando em cima e embaixo por 2:
$$ M_X(t) = \frac{e^t}{2 - e^t} $$

- **(c) $f(x) = (1-p)^{x-1}p$ para $x = 1, 2, \ldots$:**
Esta é a distribuição Geométrica clássica.
$$ M_X(t) = \sum_{x=1}^{\infty} e^{tx} (1-p)^{x-1} p $$
Para igualar as potências, multiplicamos e dividimos por $(1-p)$:
$$ M_X(t) = \frac{p}{1-p} \sum_{x=1}^{\infty} e^{tx} (1-p)^x = \frac{p}{1-p} \sum_{x=1}^{\infty} \left[ e^t(1-p) \right]^x $$
Novamente, P.G. infinita convergente se $e^t(1-p) < 1$:
$$ M_X(t) = \frac{p}{1-p} \cdot \frac{e^t(1-p)}{1 - e^t(1-p)} $$
Cancelando o $(1-p)$:
$$ M_X(t) = \frac{pe^t}{1 - (1-p)e^t} $$
