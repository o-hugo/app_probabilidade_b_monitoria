---
id: "questoes-q05-lista-questo-5"
titulo: "Questão 5"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

A demanda diária de arroz num supermercado, em centenas de quilos, é uma v.a. com f.d.p. $f(x)=\begin{cases}\frac{2x}{3},&0\le x<1,\\ -\frac{x}{3}+1,&1\le x<3,\\ 0,&x<0~ou~x>3.\end{cases}$

(a) Qual a probabilidade de se vender mais do que 150 kg, num dia escolhido ao acaso?

(b) Em 30 dias, quanto o gerente do supermercado espera vender?

(c) Qual a quantidade de arroz que deve ser deixada à disposição dos clientes diariamente para que não falte arroz em 95% dos dias?

## Solução

## Parte (a): Vender mais de 150 kg


## Passo 1: Converter a Pergunta em Probabilidade

A variável X é dada em "centenas de quilos". Portanto, 150 kg correspondem a $X = 1.5$. A pergunta é: qual a probabilidade de $X > 1.5$?

Para $X=1.5$, estamos no segundo intervalo da fdp ($1 \le x < 3$), onde $f(x) = -x/3+1$.

$$P(X > 1.5) = \int_{1.5}^{3} (-\frac{x}{3}+1) \,dx$$

Resumo: Traduzimos a pergunta para uma integral definida da fdp no intervalo relevante.



## Passo 2: Resolver a Integral

$$P(X > 1.5) = [-\frac{x^2}{6} + x]_{1.5}^{3}$$

$$= (-\frac{3^2}{6} + 3) - (-\frac{1.5^2}{6} + 1.5) = (-\frac{9}{6} + 3) - (-\frac{2.25}{6} + 1.5)$$

$$= (-1.5 + 3) - (-0.375 + 1.5) = 1.5 - 1.125 = 0.375$$

A probabilidade de vender mais de 150 kg é de **37.5%**.

Resumo: Calculamos a integral e encontramos a probabilidade desejada.


## Parte (b): Venda esperada em 30 dias


## Passo 1: Calcular a Esperança Diária $E(X)$

Como a fdp é definida por partes, a integral para a esperança também será dividida:

$$E(X) = \int_{0}^{1} x(\frac{2x}{3}) \,dx + \int_{1}^{3} x(-\frac{x}{3}+1) \,dx$$

$$= \int_{0}^{1} \frac{2x^2}{3} \,dx + \int_{1}^{3} (-\frac{x^2}{3}+x) \,dx$$

$$= [\frac{2x^3}{9}]_{0}^{1} + [-\frac{x^3}{9}+\frac{x^2}{2}]_{1}^{3}$$

$$= (\frac{2}{9}) + [(-\frac{27}{9}+\frac{9}{2}) - (-\frac{1}{9}+\frac{1}{2})] = \frac{2}{9} + [(-3+4.5) - (\frac{7}{18})] = \frac{2}{9} + [1.5 - \frac{7}{18}]$$

$$= \frac{4}{18} + \frac{27}{18} - \frac{7}{18} = \frac{24}{18} = \frac{4}{3} \approx 1.333$$

A venda diária esperada é de 133.3 kg.

Resumo: Calculamos a venda média diária integrando $x \cdot f(x)$ em todas as partes do domínio.



## Passo 2: Calcular a Venda Esperada em 30 dias

Venda Total = $30 \times E(X) = 30 \times \frac{4}{3} = 40$ centenas de quilos.

O gerente espera vender **4000 kg** de arroz em 30 dias.

Resumo: Multiplicamos a média diária pelo número de dias.


## Parte (c): Estoque para 95% dos dias


## Passo 1: Formular a Equação

Queremos encontrar uma quantidade de estoque $q$ tal que a demanda seja menor ou igual a $q$ em 95% das vezes. Matematicamente: $P(X \le q) = 0.95$.

Primeiro, vemos a probabilidade acumulada até $X=1$: $P(X \le 1) = \int_0^1 \frac{2x}{3}dx = [\frac{x^2}{3}]_0^1 = \frac{1}{3} \approx 0.333$.

Como $0.333 < 0.95$, sabemos que o valor de $q$ está no segundo intervalo ($1 \le q < 3$).

A equação é: $P(X \le q) = P(X \le 1) + P(1 < X \le q) = 0.95$

$$\frac{1}{3} + \int_{1}^{q} (-\frac{x}{3}+1) \,dx = 0.95$$

Resumo: Montamos uma equação para o 95º percentil da distribuição, descobrindo em qual intervalo da fdp ele se encontra.



## Passo 2: Resolver a Equação para q

$$\int_{1}^{q} (-\frac{x}{3}+1) \,dx = 0.95 - \frac{1}{3} = \frac{19}{20} - \frac{1}{3} = \frac{57-20}{60} = \frac{37}{60}$$

$$[-\frac{x^2}{6} + x]_{1}^{q} = \frac{37}{60}$$

$$(-\frac{q^2}{6} + q) - (-\frac{1}{6} + 1) = \frac{37}{60} \implies -\frac{q^2}{6} + q - \frac{5}{6} = \frac{37}{60}$$

Multiplicando por 60 para eliminar os denominadores: $-10q^2 + 60q - 50 = 37 \implies 10q^2 - 60q + 87 = 0$.

Resumo: Resolvemos a parte integral da equação, resultando em uma equação quadrática para q.



## Passo 3: Solucionar a Equação Quadrática

Usamos a fórmula de Bhaskara para $10q^2 - 60q + 87 = 0$:

$$q = \frac{-(-60) \pm \sqrt{(-60)^2 - 4(10)(87)}}{2(10)} = \frac{60 \pm \sqrt{3600 - 3480}}{20}$$

$$q = \frac{60 \pm \sqrt{120}}{20} \approx \frac{60 \pm 10.954}{20}$$

Isso nos dá duas soluções: $q_1 \approx \frac{70.954}{20} \approx 3.55$ e $q_2 \approx \frac{49.046}{20} \approx 2.45$.

Como estabelecemos que $q$ deve estar no intervalo $[1, 3]$, a única solução válida é $q \approx 2.45$.

A quantidade de arroz a ser estocada é de **245 kg**.

Resumo: Resolvemos a equação quadrática e selecionamos a raiz que se encaixa no domínio do problema.

<h5 class="text-center font-semibold mt-6">Gráfico da fdp: $f(x)$</h5>
