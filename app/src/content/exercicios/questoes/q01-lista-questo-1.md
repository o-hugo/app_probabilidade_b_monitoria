---
id: "questoes-q01-lista-questo-1"
titulo: "Questão 1"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

A variável aleatória contínua X tem fdp $f(x)=3x^{2}$, para $-1 \le x \le 0$. Se $b$ for um número que satisfaça a $-1 < b < 0$, calcule $P(X>b|X<\frac{b}{2})$.

## Solução

## Passo 1: Entender a Fórmula da Probabilidade Condicional

A probabilidade condicional de um evento A ocorrer, dado que um evento B já ocorreu, é calculada pela fórmula:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Neste problema, nossos eventos são:

- $A: X > b$
- $B: X < \frac{b}{2}$


Resumo: Identificamos que o problema exige a fórmula da probabilidade condicional e definimos os eventos A e B.



## Passo 2: Determinar a Região de Interseção ($A \cap B$)

A interseção ($A \cap B$) representa a condição em que ambos os eventos ocorrem simultaneamente, ou seja, $X > b$ E $X < \frac{b}{2}$. Como $b$ é um número negativo (ex: -0.5), $\frac{b}{2}$ é maior que $b$ (ex: -0.25). Portanto, a região de interseção é o intervalo $b < X < \frac{b}{2}$.

Resumo: A interseção dos eventos A e B corresponde ao intervalo de valores de X entre $b$ e $b/2$.



## Passo 3: Calcular a Probabilidade do Denominador, $P(B)$

Para encontrar $P(B) = P(X < \frac{b}{2})$, integramos a fdp desde o limite inferior do domínio (-1) até $\frac{b}{2}$:

$$P(X < \frac{b}{2}) = \int_{-1}^{b/2} f(x) \,dx = \int_{-1}^{b/2} 3x^{2} \,dx$$

$$= [x^{3}]_{-1}^{b/2} = (\frac{b}{2})^{3} - (-1)^{3} = \frac{b^{3}}{8} + 1$$

Resumo: Calculamos a probabilidade do evento B integrando a fdp no intervalo correspondente.



## Passo 4: Calcular a Probabilidade do Numerador, $P(A \cap B)$

Para encontrar $P(A \cap B) = P(b < X < \frac{b}{2})$, integramos a fdp no intervalo da interseção:

$$P(b < X < \frac{b}{2}) = \int_{b}^{b/2} 3x^{2} \,dx = [x^{3}]_{b}^{b/2}$$

$$= (\frac{b}{2})^{3} - b^{3} = \frac{b^{3}}{8} - b^{3} = \frac{b^{3} - 8b^{3}}{8} = -\frac{7b^{3}}{8}$$

Resumo: Calculamos a probabilidade da interseção A e B integrando a fdp no intervalo correspondente.



## Passo 5: Montar a Fração Final e Simplificar

Agora, substituímos os resultados dos passos 3 e 4 na fórmula da probabilidade condicional:

$$P(X>b|X<\frac{b}{2}) = \frac{P(A \cap B)}{P(B)} = \frac{-\frac{7b^{3}}{8}}{1 + \frac{b^{3}}{8}}$$

Para simplificar, multiplicamos o numerador e o denominador por 8:

$$= \frac{-7b^{3}}{8(1 + \frac{b^{3}}{8})} = \frac{-7b^{3}}{8 + b^{3}}$$

Resumo: Substituímos as probabilidades calculadas na fórmula original e simplificamos a expressão para obter a resposta final.


## Calculadora Interativa

<label for="b-slider-q1" class="block font-medium">Ajuste o valor de $b$ (entre -1 e 0):</label>
<input type="range" id="b-slider-q1" min="-0.99" max="-0.01" step="0.01" value="-0.5" class="w-full"><span id="b-value-q1" class="font-mono text-lg">-0.50</span>

Resultado: $P(X>b|X<b/2) = <span id="result-q1"></span>$
