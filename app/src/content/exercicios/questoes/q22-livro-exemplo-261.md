---
id: "questoes-q22-livro-exemplo-261"
titulo: "Exemplo 2.6.1"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Calcular a esperança da variável aleatória X cuja densidade de probabilidade é dada por: $f(x)=\begin{cases}2x,&para~0\le x\le0,5,\\ -\frac{2}{3}x+\frac{4}{3},&para~0,5\le x\le2\\ 0,&no~complementar\end{cases}$

## Solução

## Passo 1: Montar a Integral para a Esperança

A esperança $E(X)$ é calculada por $\int_{-\infty}^{\infty} x f(x) \,dx$. Como a fdp é definida por partes, a integral também deve ser dividida.

$$E(X)=\int_{0}^{0,5}x(2x)dx+\int_{0,5}^{2}x(-\frac{2}{3}x+\frac{4}{3})dx$$

Resumo: Dividimos a integral da esperança em duas partes, correspondendo a cada trecho da fdp.



## Passo 2: Calcular a Primeira Integral

$$\int_{0}^{0,5} 2x^2 \,dx = [\frac{2x^3}{3}]_0^{0.5} = \frac{2(0.5)^3}{3} - 0 = \frac{2(0.125)}{3} = \frac{0.25}{3} = \frac{1}{12}$$

Resumo: Resolvemos a integral para o primeiro intervalo da fdp.



## Passo 3: Calcular a Segunda Integral

$$\int_{0,5}^{2} (-\frac{2}{3}x^2+\frac{4}{3}x) \,dx = [-\frac{2x^3}{9} + \frac{4x^2}{6}]_{0.5}^2 = [-\frac{2x^3}{9} + \frac{2x^2}{3}]_{0.5}^2$$

Avaliando nos limites:

Em $x=2$: $(-\frac{2(2)^3}{9} + \frac{2(2)^2}{3}) = -\frac{16}{9} + \frac{8}{3} = \frac{-16+24}{9} = \frac{8}{9}$

Em $x=0.5$: $(-\frac{2(0.5)^3}{9} + \frac{2(0.5)^2}{3}) = -\frac{2(0.125)}{9} + \frac{2(0.25)}{3} = -\frac{0.25}{9} + \frac{0.5}{3} = \frac{-0.25+1.5}{9} = \frac{1.25}{9} = \frac{5/4}{9} = \frac{5}{36}$

A integral é: $\frac{8}{9} - \frac{5}{36} = \frac{32-5}{36} = \frac{27}{36} = \frac{3}{4}$

Resumo: Resolvemos a integral para o segundo intervalo da fdp.



## Passo 4: Somar os Resultados

$$E(X) = \frac{1}{12} + \frac{3}{4} = \frac{1}{12} + \frac{9}{12} = \frac{10}{12} = \frac{5}{6}$$

O valor da esperança é $\frac{5}{6} \approx 0.8333$.

Resumo: Somamos os resultados das duas integrais para obter a esperança total.
