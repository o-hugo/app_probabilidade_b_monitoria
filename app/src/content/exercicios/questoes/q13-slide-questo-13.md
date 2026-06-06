---
id: "questoes-q13-slide-questo-13"
titulo: "Questão 13"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
---

## Enunciado

A energia radiante $(em~Btu/hora/pe^{2})$ é dada pela seguinte função da temperatura T (em escala Fahrenheit): $E=0,173(\frac{T}{100})^{4}.$ Suponha que a temperatura T seja considerada uma variável aleatória contínua com fdp $f(t)=200t^{-2}$ , $40\le t\le50$. Estabeleça a fdp da energia radiante E.

## Solução

## Passo 1: Definir a Transformação e sua Inversa

A transformação é $E = g(T) = 0.173(\frac{T}{100})^4$. Esta função é estritamente crescente para $T>0$.

Inversa: $\frac{E}{0.173} = (\frac{T}{100})^4 \implies \frac{T}{100} = (\frac{E}{0.173})^{1/4} \implies T = g^{-1}(E) = 100(\frac{E}{0.173})^{1/4}$.

Resumo: Identificamos a transformação da temperatura (T) para energia (E) e calculamos sua inversa.



## Passo 2: Calcular a Derivada da Inversa

$$T = \frac{100}{(0.173)^{1/4}} E^{1/4}$$

$$\frac{dT}{dE} = \frac{100}{(0.173)^{1/4}} \cdot \frac{1}{4} E^{-3/4} = \frac{25}{(0.173)^{1/4}} E^{-3/4}$$

Resumo: Calculamos a derivada da temperatura em relação à energia.



## Passo 3: Aplicar a Fórmula da Transformação

$$f_E(e) = f_T(g^{-1}(e)) \cdot |\frac{dT}{dE}|$$

Substituindo $g^{-1}(e)$ em $f_T(t) = 200t^{-2}$:

$$f_T(g^{-1}(e)) = 200 \cdot [100(\frac{e}{0.173})^{1/4}]^{-2} = 200 \cdot 100^{-2} \cdot (\frac{e}{0.173})^{-1/2} = 0.02 \cdot (\frac{0.173}{e})^{1/2}$$

Agora multiplicamos pela derivada:

$$f_E(e) = [0.02 \frac{\sqrt{0.173}}{\sqrt{e}}] \cdot [\frac{25}{(0.173)^{1/4}} e^{-3/4}] = \frac{0.5 \cdot (0.173)^{1/2}}{(0.173)^{1/4}} e^{-1/2}e^{-3/4} = 0.5 \cdot (0.173)^{1/4} e^{-5/4}$$

Resumo: Realizamos as substituições na fórmula da transformação e simplificamos a álgebra para obter a fdp de E.



## Passo 4: Determinar o Domínio de E

O domínio de T é $[40, 50]$. Aplicamos a transformação para encontrar o novo domínio:

Limite inferior: $E_{min} = 0.173(\frac{40}{100})^4 = 0.173(0.0256) \approx 0.00443$.

Limite superior: $E_{max} = 0.173(\frac{50}{100})^4 = 0.173(0.0625) \approx 0.01081$.

O domínio da fdp de E é aproximadamente $[0.00443, 0.01081]$.

Resumo: Transformamos os limites do domínio original para encontrar os limites do domínio da nova variável.
