---
id: "dantas-cap02-q32"
titulo: "FDA do Quadrado da Distancia em Disco"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 2, Q. 32"
---

## Enunciado
Considere um ponto escolhido aleatoriamente no interior de um disco de raio R no plano. Seja X o quadrado da distância do centro do disco ao ponto escolhido, obtenha a função de distribuição de X.

## Solução

Seja a variável aleatória $D$ a distância euclidiana do centro do disco ao ponto escolhido. Sabemos que o ponto deve estar em algum lugar dentro do disco principal de raio $R$, o que delimita o alcance $0 \le D \le R$. A probabilidade obedece a uma métrica de áreas (Distribuição Geométrica Bidimensional Uniforme).

A probabilidade do ponto ter uma distância ao centro menor ou igual a uma constante $d$ é a razão entre a área do círculo que tem raio $d$ e a área do disco inteiro (raio $R$):
$$ P(D \le d) = \frac{\text{Área do círculo de raio } d}{\text{Área do disco de raio } R} = \frac{\pi d^2}{\pi R^2} = \frac{d^2}{R^2} $$

O enunciado define $X$ como o quadrado dessa distância, isto é, $X = D^2$. O intervalo de valores possíveis para $X$ vai de $0^2$ a $R^2$, logo $x \in [0, R^2]$.
Queremos encontrar a Função de Distribuição Acumulada $F_X(x) = P(X \le x)$. Substituindo $X$:
$$ P(X \le x) = P(D^2 \le x) $$
Como as distâncias são positivas, podemos extrair a raiz quadrada sem nos preocuparmos com sinais negativos:
$$ P(D^2 \le x) = P(D \le \sqrt{x}) $$
Agora, basta substituirmos o valor $\sqrt{x}$ na nossa equação das áreas:
$$ F_X(x) = P(D \le \sqrt{x}) = \frac{(\sqrt{x})^2}{R^2} = \frac{x}{R^2} $$

Portanto, a Função de Distribuição de $X$ (para $0 \le x \le R^2$) é:
$$ F_X(x) = \frac{x}{R^2} $$

*Nota: Derivando esta F.D.A. em relação a $x$, chegamos na constante $\frac{1}{R^2}$. Isso significa que a variável $X$ (o quadrado da distância) segue uma distribuição **Uniforme** em $[0, R^2]$.*
