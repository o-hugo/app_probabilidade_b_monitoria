---
id: "questoes-q16-slide-questo-16"
titulo: "Questão 16"
topicos: ["funcao-de-variavel-aleatoria", "modelos-continuos"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
tags: ["metodo-jacobiano"]
---

## Enunciado

A velocidade de uma molécula em um gás uniforme em equilíbrio é uma variável aleatória V com fdp dada por $f(v)=av^{2}e^{-bv^{2}}$, $v>0$, onde $b=m/2kT$. T, m e k denotam, respectivamente, a constante de Boltzman, a temperatura absoluta e a massa da molécula. Determine a distribuição da variável aleatória a $W=mV^{2}/2$, qual representa a energia cinética da molécula.

## Solução

## Passo 1: Definir a Transformação e sua Inversa

A transformação é a energia cinética $W = g(V) = \frac{1}{2}mV^2$. Para $V > 0$, é estritamente crescente.

A inversa é: $V^2 = \frac{2W}{m} \implies V = g^{-1}(W) = \sqrt{\frac{2W}{m}}$.

Resumo: Definimos a relação entre energia cinética e velocidade e encontramos a função inversa.



## Passo 2: Calcular a Derivada da Inversa

$$V = \sqrt{\frac{2}{m}} W^{1/2}$$

$$\frac{dV}{dW} = \sqrt{\frac{2}{m}} \cdot \frac{1}{2} W^{-1/2} = \frac{1}{\sqrt{2mW}}$$

Resumo: Calculamos o Jacobiano da transformação.



## Passo 3: Aplicar a Fórmula da Transformação

$$f_W(w) = f_V(g^{-1}(w)) \cdot |\frac{dV}{dW}|$$

Primeiro, avaliamos $f_V$ na inversa:

$$f_V(\sqrt{2w/m}) = a(\sqrt{2w/m})^2 e^{-b(\sqrt{2w/m})^2} = a(\frac{2w}{m})e^{-b(\frac{2w}{m})}$$

Agora, multiplicamos pelo Jacobiano:

$$f_W(w) = [a(\frac{2w}{m})e^{-b(\frac{2w}{m})}] \cdot [\frac{1}{\sqrt{2mW}}] = \frac{2aw}{m\sqrt{2mW}} e^{-\frac{2bw}{m}}$$

$$= \frac{2a w^{1/2}}{m \sqrt{2m}} e^{-\frac{2bw}{m}} = \frac{\sqrt{2}a}{m^{3/2}} w^{1/2} e^{-\frac{2bw}{m}}$$

Resumo: Substituímos as funções na fórmula da transformação e simplificamos a expressão resultante.



## Passo 4: Simplificar o Expoente e Reconhecer a Distribuição

Substituímos o valor de $b=m/2kT$ no expoente:

$$-\frac{2bw}{m} = -\frac{2(m/2kT)w}{m} = -\frac{w}{kT}$$

A fdp de W é: $f_W(w) = C \cdot w^{1/2} e^{-w/kT}$, onde $C = \frac{\sqrt{2}a}{m^{3/2}}$ é uma constante.

Esta é a forma de uma **distribuição Gama**, com parâmetro de forma $\alpha = 3/2$ e parâmetro de escala $\theta = kT$.

Resumo: Simplificamos o resultado e identificamos a forma final como pertencente a uma família conhecida de distribuições (Gama).
