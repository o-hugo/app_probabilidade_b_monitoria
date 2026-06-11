---
id: "questoes-q19-livro-exemplo-231"
titulo: "Exemplo 2.3.1"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "fda"]
referencia: "Dantas, Ex. 2.3.1"
---

## Enunciado

Seja a fdp $f(x)=x$ para $0\le x\le1$, $f(x)=2-x$ para $1\le x\le2$ e zero no complementar. Calcule as probabilidades $P[0\le X\le0,8]$ e $P[0,3\le X\le1,5]$.

## Solução

## Passo 1: Entender a fdp (Distribuição Triangular)

A função de densidade é definida por partes, formando um triângulo com base no intervalo $[0, 2]$ e altura 1 no ponto $x=1$. A área total do triângulo é $\frac{base \times altura}{2} = \frac{2 \times 1}{2} = 1$, confirmando que é uma fdp válida.



## Passo 2: Calcular $P[0\le X\le0,8]$

Como o intervalo $[0, 0.8]$ está inteiramente dentro da primeira parte da definição ($0 \le x \le 1$), usamos $f(x)=x$.

$$P[0\le X\le0,8]=\int_{0}^{0,8}x\,dx=\frac{1}{2}x^{2}|_{0}^{0,8}=\frac{1}{2}(0,8)^{2} - 0 = 0.32$$

Resumo: Integramos a primeira parte da fdp no intervalo especificado.



## Passo 3: Calcular $P[0,3\le X\le1,5]$

Este intervalo abrange as duas partes da definição da fdp. Portanto, precisamos dividir a integral em duas partes: uma de 0.3 a 1 (onde $f(x)=x$) e outra de 1 a 1.5 (onde $f(x)=2-x$).

$$P[0,3\le X\le1,5]=\int_{0,3}^{1}x\,dx+\int_{1}^{1,5}(2-x)dx$$

$$= [\frac{1}{2}x^{2}]_{0,3}^{1} + [2x - \frac{1}{2}x^2]_{1}^{1,5}$$

$$= (\frac{1^2}{2} - \frac{0.3^2}{2}) + ((2(1.5) - \frac{1.5^2}{2}) - (2(1) - \frac{1^2}{2}))$$

$$= (0.5 - 0.045) + ((3 - 1.125) - (2 - 0.5))$$

$$= 0.455 + (1.875 - 1.5) = 0.455 + 0.375 = 0.83$$

Resumo: Dividimos a integral no ponto $x=1$ onde a definição da fdp muda, calculamos cada parte e somamos os resultados.
