---
id: "questoes-q20-livro-exemplo-243"
titulo: "Exemplo 2.4.3"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Consideremos a variável aleatória X com densidade de probabilidade dada no exemplo 2.3.1 (distribuição triangular). Determine sua função de distribuição e calcule $P[0,7\le X\le1,8]$.

## Solução

## Passo 1: Calcular a FDA para $0 \le x < 1$

A FDA, $F(x)$, é a integral da fdp de $-\infty$ até $x$. Para este intervalo, $f(y)=y$.

$$F(x) = \int_0^x y\,dy = [\frac{1}{2}y^2]_0^x = \frac{1}{2}x^2$$

Resumo: Integramos a primeira parte da fdp para encontrar a primeira parte da FDA.



## Passo 2: Calcular a FDA para $1 \le x < 2$

Para este intervalo, a FDA é a área acumulada até $x=1$ mais a integral da segunda parte da fdp de 1 até $x$.

$$F(x) = F(1) + \int_1^x (2-y)\,dy$$

Sabemos que $F(1) = \frac{1}{2}(1)^2 = \frac{1}{2}$.

$$F(x) = \frac{1}{2} + [2y - \frac{y^2}{2}]_1^x = \frac{1}{2} + (2x - \frac{x^2}{2}) - (2(1) - \frac{1^2}{2})$$

$$= \frac{1}{2} + 2x - \frac{x^2}{2} - (2 - \frac{1}{2}) = \frac{1}{2} + 2x - \frac{x^2}{2} - \frac{3}{2} = -\frac{1}{2}x^2 + 2x - 1$$

Resumo: Calculamos a área da segunda parte e somamos com a área já acumulada da primeira parte.



## Passo 3: Montar a FDA completa

Juntando todas as partes:

$$ F(x) = \begin{cases} 0, & x < 0 \\ \frac{1}{2}x^2, & 0 \le x < 1 \\ -\frac{1}{2}x^2 + 2x - 1, & 1 \le x < 2 \\ 1, & x \ge 2 \end{cases} $$



## Passo 4: Calcular $P[0,7\le X\le1,8]$

Usamos a propriedade $P[a < X \le b] = F(b) - F(a)$.

$$P[0,7\le X\le1,8] = F(1.8) - F(0.7)$$

$F(1.8) = -\frac{1}{2}(1.8)^2 + 2(1.8) - 1 = -1.62 + 3.6 - 1 = 0.98$

$F(0.7) = \frac{1}{2}(0.7)^2 = 0.245$

$$P[0,7\le X\le1,8] = 0.98 - 0.245 = 0.735$$

Resumo: Aplicamos a propriedade da FDA para calcular a probabilidade no intervalo, usando as expressões corretas para cada ponto.
