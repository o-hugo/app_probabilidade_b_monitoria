---
id: "questoes-q09-lista-questo-9"
titulo: "Questão 9"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
tags: ["probabilidade"]
---

## Enunciado

Arqueólogos estudaram uma certa região e estabeleceram um modelo téorico para C, comprimento de fósseis da região (em cm). Suponha que C é uma variável aleatória contínua com a seguinte fdp $f(c)=\begin{cases}\frac{1}{40}(\frac{c}{10}+1),&se&0\le c\le20;\\ 0,&caso~contrario.\end{cases}$ Qual a probabilidade de um fossil, escolhido ao acaso, apresentar comprimento inferior a 8 cm?

## Solução

## Passo 1: Montar a Integral

A probabilidade de o comprimento C ser inferior a 8 cm é $P(C < 8)$. Para encontrá-la, integramos a fdp desde o limite inferior do domínio (0) até 8.

$$P(C < 8) = \int_{0}^{8} f(c) \,dc = \int_{0}^{8} \frac{1}{40}(\frac{c}{10}+1) \,dc$$

Resumo: Formulamos a pergunta como uma integral da fdp sobre o intervalo de interesse.



## Passo 2: Resolver a Integral

$$P(C < 8) = \frac{1}{40} \int_{0}^{8} (\frac{c}{10}+1) \,dc = \frac{1}{40} [\frac{c^2}{2 \cdot 10} + c]_{0}^{8}$$

$$= \frac{1}{40} [\frac{c^2}{20} + c]_{0}^{8} = \frac{1}{40} [(\frac{8^2}{20} + 8) - (0)]$$

$$= \frac{1}{40} [\frac{64}{20} + 8] = \frac{1}{40} [3.2 + 8] = \frac{11.2}{40}$$

$$= \frac{112}{400} = \frac{7}{25} = 0.28$$

A probabilidade é de **28%**.

Resumo: Calculamos a integral definida para encontrar o valor numérico da probabilidade.
