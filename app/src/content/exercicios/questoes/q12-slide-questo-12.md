---
id: "questoes-q12-slide-questo-12"
titulo: "Questão 12"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
tags: ["metodo-jacobiano"]
---

## Enunciado

Suponha que a variável aleatória contínua X tenha fdp $f(x)=e^{-x}$, para $x>0$. Ache a fdp das seguintes variáveis aleatórias: 

 (a) $Y=X^{3}$ 

 (b) $Z=\frac{3}{(X+1)^{2}}$

## Solução

## Parte (a): fdp de $Y=X^{3}$


## Passo 1: Definir a Transformação e sua Inversa

A transformação é $y = g(x) = x^3$. Como o domínio de X é $x>0$, essa função é estritamente crescente. Podemos usar o método da transformação.

A função inversa é $x = g^{-1}(y) = y^{1/3}$.

Resumo: Identificamos a transformação e sua inversa. A monotonicidade permite usar o método direto.



## Passo 2: Calcular a Derivada da Inversa

Calculamos a derivada de $x$ em relação a $y$:

$$\frac{dx}{dy} = \frac{d}{dy}(y^{1/3}) = \frac{1}{3}y^{-2/3}$$

O valor absoluto $|rac{dx}{dy}|$ é o mesmo, pois o resultado já é positivo para $y>0$.

Resumo: Encontramos o Jacobiano da transformação, que é a derivada da função inversa.



## Passo 3: Aplicar a Fórmula da Transformação

A fórmula é $f_Y(y) = f_X(g^{-1}(y)) \cdot |\frac{dx}{dy}|$.

$$f_Y(y) = (e^{-y^{1/3}}) \cdot (\frac{1}{3}y^{-2/3}) = \frac{1}{3}y^{-2/3}e^{-y^{1/3}}$$

O domínio de Y é $y>0$, pois se $x>0$, então $y=x^3>0$.

Resumo: Substituímos a função inversa e sua derivada na fórmula da transformação para obter a nova fdp.


## Parte (b): fdp de $Z=\frac{3}{(X+1)^{2}}$


## Passo 1: Definir a Transformação e sua Inversa

A transformação é $z = g(x) = \frac{3}{(x+1)^2}$. Para $x>0$, essa função é estritamente decrescente.

Inversa: $z(x+1)^2 = 3 \implies (x+1)^2 = \frac{3}{z} \implies x+1 = \sqrt{\frac{3}{z}} \implies x = g^{-1}(z) = \sqrt{\frac{3}{z}} - 1$.

Resumo: Encontramos a função inversa da transformação. A monotonicidade garante que a inversa é única.



## Passo 2: Calcular a Derivada da Inversa

$$\frac{dx}{dz} = \frac{d}{dz}(\sqrt{3}z^{-1/2} - 1) = \sqrt{3} \cdot (-\frac{1}{2}z^{-3/2}) = -\frac{\sqrt{3}}{2}z^{-3/2}$$

O valor absoluto é $|\frac{dx}{dz}| = \frac{\sqrt{3}}{2}z^{-3/2}$.

Resumo: Calculamos a derivada da inversa para obter o Jacobiano.



## Passo 3: Aplicar a Fórmula e Definir o Domínio

$$f_Z(z) = f_X(g^{-1}(z)) \cdot |\frac{dx}{dz}| = e^{-(\sqrt{3/z}-1)} \cdot \frac{\sqrt{3}}{2}z^{-3/2}$$

Para o domínio: quando $x \to 0$, $z \to 3$. Quando $x \to \infty$, $z \to 0$. Portanto, o domínio de Z é $0 < z < 3$.

Resumo: Substituímos na fórmula da transformação e mapeamos o domínio de X para o novo domínio de Z.
