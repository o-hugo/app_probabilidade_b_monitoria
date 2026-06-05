# Glossario de Notacao

Este glossario define a notacao padrao usada em todo o aplicativo. Todas as formulas, resolucoes e visualizadores seguem esta convencao. A consistencia notacional reduz a carga cognitiva e evita confusao entre fontes diferentes (risco R2 do plan.md).

---

## Variaveis Aleatorias

| Notacao | Significado |
|---|---|
| $X, Y, Z$ | Variaveis aleatorias (maiusculas) |
| $x, y, z$ | Valores observados / realizacoes (minusculas) |

## Funcoes Fundamentais

| Notacao | Significado |
|---|---|
| $f(x)$ ou $f_X(x)$ | Funcao Densidade de Probabilidade (FDP) |
| $F(x)$ ou $F_X(x)$ | Funcao de Distribuicao Acumulada (FDA) |
| $R(t) = 1 - F(t)$ | Funcao de Confiabilidade (sobrevivencia) |
| $\lambda(t) = f(t)/R(t)$ | Funcao taxa de falha |
| $M_X(t) = E[e^{tX}]$ | Funcao Geradora de Momentos (FGM) |

## Momentos e Medidas

| Notacao | Significado |
|---|---|
| $E[X]$ ou $\mu$ | Esperanca (media) |
| $E[X^k]$ | k-esimo momento em relacao a origem |
| $Var(X)$ ou $\sigma^2$ | Variancia |
| $\sigma$ | Desvio padrao |
| $Cov(X,Y)$ | Covariancia |
| $\rho_{XY}$ | Coeficiente de correlacao |

## Distribuicoes

| Notacao | Distribuicao |
|---|---|
| $X \sim U(a, b)$ | Uniforme continua em $[a, b]$ |
| $X \sim Exp(\lambda)$ | Exponencial com taxa $\lambda$ |
| $X \sim Gama(\alpha, \beta)$ | Gama com forma $\alpha$ e escala $\beta$ |
| $X \sim Beta(\alpha, \beta)$ | Beta com parametros $\alpha, \beta$ |
| $X \sim N(\mu, \sigma^2)$ | Normal com media $\mu$ e variancia $\sigma^2$ |
| $X \sim Pareto(\alpha, \beta)$ | Pareto com forma $\alpha$ e escala $\beta$ |
| $X \sim Weibull(\alpha, \beta)$ | Weibull com escala $\alpha$ e forma $\beta$ |
| $X \sim Laplace(\mu, b)$ | Laplace com locacao $\mu$ e escala $b$ |
| $X \sim Lognormal(\mu, \sigma^2)$ | Lognormal cujo logaritmo e $N(\mu, \sigma^2)$ |
| $X \sim \chi^2(k)$ | Qui-quadrado com $k$ graus de liberdade |
| $X \sim B(n, p)$ | Binomial com $n$ ensaios e prob. de sucesso $p$ |

## Normal Padrao

| Notacao | Significado |
|---|---|
| $Z$ | Variavel normal padrao, $Z \sim N(0, 1)$ |
| $\Phi(z)$ | FDA da normal padrao: $\Phi(z) = P(Z \le z)$ |
| $\phi(z)$ | FDP da normal padrao |

## Transformacoes

| Notacao | Significado |
|---|---|
| $Y = g(X)$ | Transformacao de variavel aleatoria |
| $g^{-1}(y) = h(y)$ | Funcao inversa da transformacao |
| $\|dh(y)/dy\|$ | Valor absoluto do Jacobiano |
| $F^{-1}(u)$ | Inversa da FDA (quantil) |

## Distribuicoes Bivariadas

| Notacao | Significado |
|---|---|
| $f(x, y)$ ou $f_{X,Y}(x, y)$ | FDP conjunta |
| $f_X(x)$, $f_Y(y)$ | FDPs marginais |
| $f_{Y|X}(y|x)$ | FDP condicional de $Y$ dado $X = x$ |
| $E[Y|X=x]$ | Esperanca condicional |
| $Var(Y|X=x)$ | Variancia condicional |

## Funcoes Especiais

| Notacao | Significado |
|---|---|
| $\Gamma(\alpha) = \int_0^\infty t^{\alpha-1}e^{-t}dt$ | Funcao Gama |
| $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$ | Funcao Beta |
| $\Gamma(n) = (n-1)!$ para $n$ inteiro | Relacao com fatorial |

## Convencoes de Parametrizacao

**Nota importante:** Diferentes livros-texto usam parametrizacoes diferentes para a mesma distribuicao. Neste aplicativo, adotamos as seguintes convencoes:

- **Exponencial:** $f(x) = \lambda e^{-\lambda x}$, onde $\lambda$ e a taxa (inverso da media). Media = $1/\lambda$.
- **Gama:** $f(x) = \frac{1}{\Gamma(\alpha)\beta^\alpha} x^{\alpha-1}e^{-x/\beta}$, onde $\alpha$ e a forma e $\beta$ e a escala. Media = $\alpha\beta$.
- **Pareto:** $f(x) = \frac{\alpha\beta^\alpha}{x^{\alpha+1}}$ para $x \ge \beta$, onde $\alpha$ e a forma e $\beta$ e a escala (minimo).
- **Weibull:** $f(x) = \frac{\beta}{\alpha}(\frac{x}{\alpha})^{\beta-1}e^{-(x/\alpha)^\beta}$, onde $\alpha$ e a escala e $\beta$ e a forma.

Quando um exercicio usar parametrizacao diferente, isso sera indicado explicitamente no enunciado.
