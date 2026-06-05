---
id: "questoes-q18-slide-questo-18"
titulo: "Questão 18"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
---

## Enunciado

Todo ano, um determinado rio transborda. Suponha que o marcador de limite mínimo de água esteja definido em 1 e que o marcador de limite máximo de água Y tenha a seguinte função de distribuição acumulada (fda): $F_{Y}(y)=1-\frac{1}{y^{2}}$, para $y\ge1$.

(a) Verifique se $F_{Y}(y)$ é uma função de distribuição acumulada (fda).

(b) Encontre $f_{Y}(y)$, a função densidade de probabilidade (fdp) de Y.

(c) Se o marcador de limite mínimo de água for redefinido para 0 e utilizarmos uma unidade de medida que seja $1/10$ da que foi dada anteriormente, o marcador de limite máximo passa a ser $Z=10(Y-1)$. Encontre $F_{Z}(z)$, a fda de Z.

## Solução

## Parte (a): Verificação da fda


Para ser uma fda válida, a função deve atender a três propriedades:

1. **Limite no infinito negativo:** $\lim_{y \to -\infty} F_Y(y) = 0$. Como a função é definida para $y \ge 1$, consideramos $F_Y(y)=0$ para $y<1$. O limite é 0. (OK)

2. **Limite no infinito positivo:** $\lim_{y \to \infty} F_Y(y) = \lim_{y \to \infty} (1 - \frac{1}{y^2}) = 1 - 0 = 1$. (OK)

3. **Não-decrescente:** A função deve ser não-decrescente. Podemos verificar sua derivada: $F_Y'(y) = \frac{d}{dy}(1-y^{-2}) = -(-2y^{-3}) = \frac{2}{y^3}$. Para $y \ge 1$, a derivada é positiva, logo a função é crescente. (OK)

A função **é uma fda válida**.


## Parte (b): Encontrar a fdp


A fdp é a derivada da fda. Como calculado no passo anterior:

$$f_Y(y) = \frac{d}{dy}F_Y(y) = \frac{2}{y^3}, \text{ para } y \ge 1$$


## Parte (c): Encontrar a fda de Z


## Passo 1: Usar a Definição de fda

$$F_Z(z) = P(Z \le z)$$

Substituímos a definição de Z na inequação:

$$F_Z(z) = P(10(Y-1) \le z) = P(Y-1 \le \frac{z}{10}) = P(Y \le 1 + \frac{z}{10})$$

Resumo: Expressamos a fda de Z em termos de uma probabilidade envolvendo Y.



## Passo 2: Usar a fda de Y

A expressão $P(Y \le a)$ é, por definição, $F_Y(a)$. Portanto:

$$P(Y \le 1 + \frac{z}{10}) = F_Y(1 + \frac{z}{10})$$

Agora, substituímos $y = 1 + \frac{z}{10}$ na fórmula de $F_Y(y)$: 

$$F_Z(z) = 1 - \frac{1}{(1 + \frac{z}{10})^2}$$

Para o domínio de Z: Se $y \ge 1$, então $Y-1 \ge 0$, o que implica $Z = 10(Y-1) \ge 0$.

Resumo: Aplicamos a fda conhecida de Y para obter a fda da variável transformada Z.
