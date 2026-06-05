---
id: "questoes-q07-lista-questo-7"
titulo: "Questão 7"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

O diâmetro X de um cabo elétrico supõe-se ser uma variável aleatória contínua X, com função densidade de probabilidade $f(x)=6x(1-x)$, $0\le x\le1$.

(a) Verifique que essa expressão é uma função densidade de probabilidade e esboce o seu gráfico.

(b) Obtenha uma expressão para a função de distribuição de X e esboce o seu gráfico.

(c) Determine um número b tal que $P(X<b)=2P(X>b)$.

(d) Calcule $P(X\le\frac{1}{2}|\frac{1}{3}<X<\frac{2}{3})$.

## Solução

## Parte (a): Verificação da fdp


**1. Não-negatividade:** No intervalo $[0, 1]$, o termo $x$ é $\ge 0$ e o termo $(1-x)$ também é $\ge 0$. Portanto, $f(x)=6x(1-x) \ge 0$ para todo $x$ no domínio.

**2. Integral igual a 1:**

$$\int_0^1 6x(1-x) \,dx = \int_0^1 (6x-6x^2) \,dx = [3x^2 - 2x^3]_0^1$$

$$= (3(1)^2 - 2(1)^3) - (0) = 3 - 2 = 1$$

Ambas as condições são satisfeitas. É uma fdp válida.


## Parte (b): Expressão para a FDA


$$F(x) = \int_0^x f(t)\,dt = \int_0^x (6t-6t^2)\,dt = [3t^2 - 2t^3]_0^x = 3x^2 - 2x^3$$


## Parte (c): Determinar b


## Passo 1: Formular a equação

A condição $P(X<b)=2P(X>b)$ pode ser reescrita usando a FDA como $F(b) = 2(1 - F(b))$.

$$F(b) = 2 - 2F(b) \implies 3F(b) = 2 \implies F(b) = \frac{2}{3}$$

Substituindo a expressão da FDA: $3b^2 - 2b^3 = \frac{2}{3}$.

Multiplicando por 3, obtemos a equação cúbica: $9b^2 - 6b^3 = 2 \implies 6b^3 - 9b^2 + 2 = 0$.

Resumo: Convertemos o problema de probabilidade em uma equação algébrica envolvendo a FDA.



## Passo 2: Resolver a equação cúbica

Resolver equações cúbicas analiticamente pode ser complexo. No entanto, podemos testar valores ou usar um método numérico (como Newton-Raphson) para encontrar a raiz no intervalo $[0,1]$. A solução é $b \approx 0.618$.

Resumo: Encontramos a solução da equação cúbica que pertence ao domínio da variável aleatória.


## Parte (d): Probabilidade Condicional


## Passo 1: Montar a fórmula

$$P(X\le\frac{1}{2}|\frac{1}{3}<X<\frac{2}{3}) = \frac{P((X \le \frac{1}{2}) \cap (\frac{1}{3} < X < \frac{2}{3}))}{P(\frac{1}{3} < X < \frac{2}{3})}$$

A interseção é o intervalo $\frac{1}{3} < X \le \frac{1}{2}$. Portanto:

$$P = \frac{P(\frac{1}{3} < X \le \frac{1}{2})}{P(\frac{1}{3} < X < \frac{2}{3})} = \frac{F(\frac{1}{2}) - F(\frac{1}{3})}{F(\frac{2}{3}) - F(\frac{1}{3})}$$



## Passo 2: Calcular os valores da FDA e resolver

$F(\frac{1}{2}) = 3(\frac{1}{2})^2 - 2(\frac{1}{2})^3 = \frac{3}{4} - \frac{2}{8} = \frac{1}{2}$

$F(\frac{1}{3}) = 3(\frac{1}{3})^2 - 2(\frac{1}{3})^3 = \frac{3}{9} - \frac{2}{27} = \frac{7}{27}$

$F(\frac{2}{3}) = 3(\frac{2}{3})^2 - 2(\frac{2}{3})^3 = \frac{12}{9} - \frac{16}{27} = \frac{20}{27}$

$$P = \frac{\frac{1}{2} - \frac{7}{27}}{\frac{20}{27} - \frac{7}{27}} = \frac{\frac{27-14}{54}}{\frac{13}{27}} = \frac{\frac{13}{54}}{\frac{13}{27}} = \frac{13}{54} \cdot \frac{27}{13} = \frac{27}{54} = \frac{1}{2}$$

A probabilidade é **0.5**.
