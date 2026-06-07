---
id: "questoes-q15-slide-questo-15"
titulo: "Questão 15"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
tags: ["metodo-fda"]
---

## Enunciado

Para medir velocidades do ar, utiliza-se um tubo (conhecido como tubo estático de Pitot), o qual permite que se meça a pressão diferencial. Esta pressão diferencial é dada por $P=(1/2)dV^{2},$ onde d é a densidade do ar e V é a velocidade do vento (mph). Achar a fdp de P, quando V for uma variável aleatória uniformemente distribuída sobre o intervalo (10,20), isto é, a fdp de V é dada por $f(v)=1/10$, para $10\le v\le20$.

## Solução

## Passo 1: Definir a Transformação, a Inversa e a fdp Original

A fdp original é $f_V(v) = \frac{1}{10}$ para $10 \le v \le 20$.

A transformação é $P = g(V) = \frac{1}{2}dV^2$. Para $V > 0$, é estritamente crescente.

A inversa é: $V^2 = \frac{2P}{d} \implies V = g^{-1}(P) = \sqrt{\frac{2P}{d}}$.

Resumo: Coletamos todas as funções necessárias para aplicar o método da transformação.



## Passo 2: Calcular a Derivada da Inversa

$$V = \sqrt{\frac{2}{d}} P^{1/2}$$

$$\frac{dV}{dP} = \sqrt{\frac{2}{d}} \cdot \frac{1}{2} P^{-1/2} = \frac{1}{\sqrt{2d}} P^{-1/2} = \frac{1}{\sqrt{2dP}}$$

Resumo: Encontramos o Jacobiano da transformação.



## Passo 3: Aplicar a Fórmula da Transformação

$$f_P(p) = f_V(g^{-1}(p)) \cdot |\frac{dV}{dP}|$$

Como $f_V(v)$ é constante e igual a $1/10$ no domínio relevante, temos:

$$f_P(p) = \frac{1}{10} \cdot \frac{1}{\sqrt{2dP}}$$

Resumo: Substituímos a fdp original e o jacobiano na fórmula para encontrar a nova fdp.



## Passo 4: Determinar o Domínio de P

Mapeamos o domínio de V, $[10, 20]$, para o domínio de P:

Limite inferior: $P_{min} = \frac{1}{2}d(10)^2 = 50d$.

Limite superior: $P_{max} = \frac{1}{2}d(20)^2 = 200d$.

Portanto, a fdp de P é $f_P(p) = \frac{1}{10\sqrt{2dp}}$ para $50d \le p \le 200d$.

Resumo: Encontramos os limites do domínio da pressão P com base nos limites da velocidade V.
