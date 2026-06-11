---
id: "07-desigualdades-concentracao"
titulo: "Desigualdades de Concentração"
ordem: 7.1
ementa_ref: "Conteúdo extra — Dantas, Cap. 7"
tags: ["markov", "tchebyschev", "chernoff", "limitantes"]
---

# Desigualdades de Concentração

> **Nota:** este é um tópico extra. O conteúdo do Capítulo 7 do Dantas não está no guarda-chuva da ementa de Probabilidade B, mas é apresentado aqui como complemento por sua importância teórica e prática.

## Teoria Aprofundada

As desigualdades de concentração fornecem **limitantes superiores** para a probabilidade de uma variável aleatória se afastar de um valor de referência (em geral, sua média). Elas são valiosas porque exigem pouquíssima informação sobre a distribuição: muitas vezes basta conhecer $E(X)$, ou $E(X)$ e $Var(X)$.

### Desigualdade de Markov

Se $X \ge 0$ é uma variável aleatória não negativa e $a > 0$, então:

$$P(X \ge a) \le \frac{E(X)}{a}$$

A demonstração parte de $E(X) = \int_0^{\infty} x f(x)\, dx \ge \int_a^{\infty} x f(x)\, dx \ge a \int_a^{\infty} f(x)\, dx = a\, P(X \ge a)$.

É a desigualdade mais fraca da família, pois usa apenas a média, mas é a base para todas as outras: aplicá-la a funções crescentes de $X$ gera limitantes mais finos.

### Desigualdade de Tchebyschev

Se $X$ tem média $\mu$ e variância $\sigma^2$ finitas, então para todo $k > 0$:

$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

Equivalentemente, para todo $\varepsilon > 0$:

$$P(|X - \mu| \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$$

A demonstração é uma aplicação direta da desigualdade de Markov à variável não negativa $(X - \mu)^2$ com $a = k^2\sigma^2$.

A interpretação é poderosa: **qualquer** distribuição com variância finita concentra pelo menos $1 - 1/k^2$ de sua massa no intervalo $[\mu - k\sigma,\ \mu + k\sigma]$. Por exemplo, ao menos $75\%$ da massa está a 2 desvios padrão da média, e ao menos $88{,}9\%$ a 3 desvios — sem qualquer hipótese sobre a forma da distribuição.

### Desigualdade de Chernoff

Se $X$ tem função geradora de momentos $\phi_X(t) = E[e^{tX}]$, então para todo $t > 0$:

$$P(X \ge x_0) \le \frac{\phi_X(t)}{e^{t x_0}}$$

A demonstração aplica Markov à variável não negativa $e^{tX}$: o evento $\{X \ge x_0\}$ coincide com $\{e^{tX} \ge e^{t x_0}\}$ quando $t > 0$.

Como a desigualdade vale para todo $t > 0$, o melhor limitante é obtido **minimizando** o lado direito em $t$:

$$P(X \ge x_0) \le \min_{t > 0} \frac{\phi_X(t)}{e^{t x_0}}$$

O limitante de Chernoff costuma ser muito mais justo que Markov e Tchebyschev, pois explora toda a informação contida na FGM (todos os momentos), decaindo exponencialmente na cauda.

## Comparação entre os limitantes

| Desigualdade | Informação exigida | Qualidade do limitante |
|---|---|---|
| Markov | $E(X)$ | Fraco (decaimento em $1/a$) |
| Tchebyschev | $E(X)$ e $Var(X)$ | Moderado (decaimento em $1/\varepsilon^2$) |
| Chernoff | FGM $\phi_X(t)$ | Forte (decaimento exponencial) |

## Usabilidade e Aplicações

- **Controle de qualidade e produção:** com apenas a média e a variância da produção diária, Tchebyschev fornece garantias do tipo "a produção fica entre $a$ e $b$ unidades com probabilidade de pelo menos $p$".
- **Limitantes para a Poisson:** aplicar Chernoff a $X \sim \text{Poisson}(\lambda)$ produz limitantes exponenciais para $P(X \ge x_0)$, muito mais informativos que Markov.
- **Fundamentação teórica:** a desigualdade de Tchebyschev é o ingrediente central da demonstração da Lei Fraca dos Grandes Números (ver o tópico de Convergência e TLC).
- **Interpretação dos limitantes:** essas desigualdades não calculam probabilidades exatas; elas garantem cotas válidas para qualquer distribuição compatível com a informação disponível. Quando a distribuição é conhecida, o valor exato pode ser muito menor que a cota.
