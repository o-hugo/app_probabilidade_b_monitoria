---
id: "06-distribuicoes-bivariadas"
titulo: "Distribuições Bivariadas"
ordem: 6
ementa_ref: "Distribuições bivariadas"
tags: ["bivariada", "conjunta", "marginal", "condicional", "covariancia", "independencia"]
---

# Distribuições Bivariadas

Distribuições bivariadas estendem os conceitos de probabilidade para analisar o comportamento simultâneo de duas variáveis aleatórias continuas associadas, denotadas como o par $(X, Y)$.

## FDP Conjunta

A probabilidade conjunta de que os valores de $(X, Y)$ caiam em uma região particular bidimensional $A$ do plano $xy$ é obtida integrando a **Função de Densidade de Probabilidade Conjunta (FDP Conjunta)** sobre a referida região:

$$P((X,Y) \in A) = \iint_A f_{X,Y}(x,y) dx dy$$

A função $f_{X,Y}(x,y)$ deve satisfazer $f(x,y) \ge 0$ e a integral dupla sobre todo o plano deve ser igual a 1.

## FDPs Marginais

Dada a FDP conjunta de $(X, Y)$, podemos encontrar o comportamento individual de apenas uma das variáveis (distribuição marginal) ao "integrar para fora" a variável não desejada.

$$f_X(x) = \int_{-\infty}^{\infty} f(x,y) dy$$
$$f_Y(y) = \int_{-\infty}^{\infty} f(x,y) dx$$

## Independência

Duas variáveis aleatórias contínuas são independentes se a FDP conjunta for o produto exato das FDPs marginais para qualquer par de valores de x e y:

$$f(x,y) = f_X(x) f_Y(y) \quad \text{para todo } (x,y)$$

## FDP Condicional

A **distribuição condicional** reflete o comportamento probabilístico de uma variável quando a outra está fixada em um valor observável conhecido. A densidade condicional de $Y$ dado que $X=x$ (para $f_X(x)>0$) é:

$$f_{Y|X}(y|x) = \frac{f(x,y)}{f_X(x)}$$

## Medidas de Associação: Covariância e Correlação

Para medir a dependência e relação linear entre $X$ e $Y$, utilizamos a covariância e o coeficiente de correlação de Pearson.

**Covariância:**
$$Cov(X,Y) = E[(X-\mu_X)(Y-\mu_Y)] = E[XY] - E[X]E[Y]$$

**Correlação:**
$$\rho = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$

Onde $\rho$ está sempre restrito entre -1 e +1. Valores próximos aos extremos refletem forte correlação linear.

> "A high correlation does not necessarily imply a causal relation."
> -- Johnson & Bhattacharyya (2010). Statistics. p. 98.

## Usabilidade e Aplicações

Relações entre variáveis são centrais na aplicação estatística e em todas as ciências, visando modelar previsibilidade e risco:
- Em **finanças**, a correlação conjunta entre as flutuações e retornos diários de diferentes ativos baseia a teoria matemática moderna de diversificação de portfólio.
- Em **estudos epidemiológicos**, entre variáveis de exposição e tempo de sobrevivência ou tempo de resposta a vacinas ou dosagens.
- Na **meteorologia**, para analisar o comportamento multivariado de variáveis de tempestade (precipitação, velocidade dos ventos).
- As distribuições condicionais e a predição fundamentam a modelagem de **Machine Learning** de inferência condicional probabilística.
