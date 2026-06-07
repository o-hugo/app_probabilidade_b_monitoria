---
id: "dantas-cap02-q33"
titulo: "FDP da Distancia em Triangulo Aleatorio"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida"]
referencia: "Dantas, Cap. 2, Q. 33"
---

## Enunciado
Considere um ponto escolhido uniformemente no interior de um triângulo de base B e altura H. Seja X a distância da base ao ponto escolhido, obtenha a função densidade de probabilidade de X.

## Solução

A probabilidade do ponto escolhido cair dentro de qualquer sub-região do triângulo depende apenas da proporção de área que essa sub-região representa em relação à área total do triângulo. (As posições horizontais são independentes da altura se analisadas pela proporção de base remanescente).

Seja $X$ a distância da base até o ponto (isto é, a "altura" vertical da posição do ponto, $0 \le X \le H$).

Para encontrar $P(X > x)$, precisamos calcular a probabilidade de o ponto estar posicionado a uma altura superior a $x$. Essa região forma um triângulo menor, na porção superior do triângulo maior.
Por semelhança de triângulos, o triângulo superior tem altura $H - x$.
A razão entre a área desse triângulo menor e a do triângulo original de altura $H$ é dada pelo quadrado da razão de semelhança (que no caso é a razão das alturas):
$$ \frac{\text{Área}_{X > x}}{\text{Área}_{\text{Total}}} = \left(\frac{H - x}{H}\right)^2 = \left(1 - \frac{x}{H}\right)^2 $$

Então, a função de probabilidade complementar (função de sobrevivência) é:
$$ P(X > x) = \left(1 - \frac{x}{H}\right)^2 $$

A Função de Distribuição Acumulada $F_X(x)$ será:
$$ F_X(x) = P(X \le x) = 1 - P(X > x) = 1 - \left(1 - \frac{x}{H}\right)^2 $$
Válida no intervalo de posições $0 \le x \le H$.

Para obtermos a **função densidade de probabilidade**, $f_X(x)$, basta derivarmos a Função de Distribuição em relação a $x$:
$$ f_X(x) = \frac{d}{dx} \left[ 1 - \left(1 - \frac{x}{H}\right)^2 \right] $$
Aplicando a regra da cadeia:
$$ f_X(x) = -2 \left(1 - \frac{x}{H}\right) \cdot \frac{d}{dx}\left(1 - \frac{x}{H}\right) = -2 \left(1 - \frac{x}{H}\right) \cdot \left(-\frac{1}{H}\right) $$
$$ f_X(x) = \frac{2}{H} \left(1 - \frac{x}{H}\right) $$

Esta densidade vale para $0 \le x \le H$. Ela indica que é mais provável o ponto estar perto da base ($x \to 0$, $f(x)$ máximo em $2/H$) e sua probabilidade diminui linearmente até $0$ ao se aproximar do topo ($x \to H$).
