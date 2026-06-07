---
id: "questoes-q17-slide-questo-17"
titulo: "Questão 17"
topicos: ["funcao-de-variavel-aleatoria", "modelos-continuos"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
tags: ["metodo-fda"]
---

## Enunciado

Seja X uma variável aleatória contínua com fdp dada por $f(x)=\lambda e^{-\lambda x}$, $x>0$, $\lambda>0$. Determine a densidade de $Y=1/X.$

## Solução

## Passo 1: Definir a Transformação e sua Inversa

A variável X segue uma distribuição Exponencial com parâmetro $\lambda$.

A transformação é $Y = g(X) = 1/X$. Para $X>0$, esta função é estritamente decrescente.

A inversa é $X = g^{-1}(Y) = 1/Y$.

Resumo: Identificamos a transformação e sua inversa.



## Passo 2: Calcular a Derivada da Inversa

$$\frac{dX}{dY} = \frac{d}{dY}(Y^{-1}) = -1 \cdot Y^{-2} = -\frac{1}{Y^2}$$

O valor absoluto é $|\frac{dX}{dY}| = \frac{1}{Y^2}$.

Resumo: Calculamos o Jacobiano da transformação.



## Passo 3: Aplicar a Fórmula e Definir o Domínio

$$f_Y(y) = f_X(g^{-1}(y)) \cdot |\frac{dX}{dY}| = f_X(1/y) \cdot \frac{1}{y^2}$$

Substituindo na fdp exponencial:

$$f_Y(y) = (\lambda e^{-\lambda(1/y)}) \cdot \frac{1}{y^2} = \frac{\lambda}{y^2}e^{-\lambda/y}$$

O domínio de X é $x>0$. Como $y=1/x$, o domínio de Y também é $y>0$.

Esta distribuição é conhecida como **distribuição Inversa-Gama** (em um caso particular).

Resumo: Aplicamos a fórmula da transformação para encontrar a fdp de Y, que é o inverso de uma variável exponencial.
