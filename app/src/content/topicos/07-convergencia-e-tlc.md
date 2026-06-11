---
id: "07-convergencia-e-tlc"
titulo: "Convergência de Variáveis Aleatórias e TLC"
ordem: 7.2
ementa_ref: "Conteúdo extra — Dantas, Cap. 7"
tags: ["lei-grandes-numeros", "convergencia", "tlc", "aproximacao"]
---

# Convergência de Variáveis Aleatórias e Teorema do Limite Central

> **Nota:** este é um tópico extra. O conteúdo do Capítulo 7 do Dantas não está no guarda-chuva da ementa de Probabilidade B, mas é apresentado aqui como complemento por sua importância teórica e prática.

## Teoria Aprofundada

Este tópico estuda o comportamento de **sequências de variáveis aleatórias** $X_1, X_2, \dots$ quando $n \to \infty$. Os dois resultados centrais — a Lei dos Grandes Números e o Teorema do Limite Central — explicam por que médias amostrais estabilizam e por que a distribuição Normal aparece em toda parte.

### Convergência em probabilidade

A sequência $X_n$ **converge em probabilidade** para $X$, denotado $X_n \xrightarrow{P} X$, se para todo $\varepsilon > 0$:

$$\lim_{n \to \infty} P(|X_n - X| \ge \varepsilon) = 0$$

Intuitivamente, a probabilidade de $X_n$ se afastar de $X$ por qualquer margem fixa torna-se desprezível para $n$ grande.

### Convergência em distribuição

A sequência $X_n$ **converge em distribuição** para $X$, denotado $X_n \xrightarrow{D} X$, se:

$$\lim_{n \to \infty} F_{X_n}(x) = F_X(x)$$

em todo ponto $x$ de continuidade de $F_X$. Aqui não se exige proximidade entre as variáveis, apenas entre suas funções de distribuição.

### Relação entre os dois tipos

- Convergência em probabilidade **implica** convergência em distribuição: $X_n \xrightarrow{P} X \implies X_n \xrightarrow{D} X$.
- A recíproca é falsa em geral. Contraexemplo clássico: se $X \sim N(0,1)$ e $X_n = -X$ para todo $n$, então $X_n \xrightarrow{D} X$ (mesma distribuição), mas $|X_n - X| = 2|X|$ não se aproxima de zero, logo não há convergência em probabilidade.
- Caso especial: quando o limite é uma **constante** $c$, os dois conceitos coincidem: $X_n \xrightarrow{D} c \iff X_n \xrightarrow{P} c$.

### Lei Fraca dos Grandes Números

Sejam $X_1, X_2, \dots$ independentes e identicamente distribuídas com média $\mu$ e variância $\sigma^2$ finitas, e seja $\bar{X}_n = \frac{1}{n}\sum_{i=1}^{n} X_i$. Então:

$$\bar{X}_n \xrightarrow{P} \mu$$

A demonstração usa a desigualdade de Tchebyschev: como $E(\bar{X}_n) = \mu$ e $Var(\bar{X}_n) = \sigma^2/n$,

$$P(|\bar{X}_n - \mu| \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2} \xrightarrow{n \to \infty} 0$$

É o resultado que justifica estimar a média populacional pela média amostral e interpretar probabilidade como frequência relativa de longo prazo.

### Sequências clássicas de convergência

- **Máximo de uniformes:** se $X_i \sim U(0, \theta)$ i.i.d. e $M_n = \max(X_1, \dots, X_n)$, então $M_n \xrightarrow{P} \theta$; além disso, $n(\theta - M_n)$ converge em distribuição para uma Exponencial.
- **Mínimo de uniformes:** $m_n = \min(X_1, \dots, X_n) \xrightarrow{P} 0$, e $n\, m_n$ converge em distribuição para uma Exponencial.
- **Geométrica escalada:** se $X_n \sim \text{Geométrica}(p_n)$ com $n p_n \to \lambda$, então $X_n / n \xrightarrow{D} \text{Exponencial}(\lambda)$.
- **Somas de Poisson:** se $S_n \sim \text{Poisson}(n\lambda)$, então $(S_n - n\lambda)/\sqrt{n\lambda} \xrightarrow{D} N(0,1)$ — caso particular do TLC.

### Teorema do Limite Central

Sejam $X_1, X_2, \dots$ i.i.d. com média $\mu$ e variância $\sigma^2 \in (0, \infty)$, e $S_n = X_1 + \dots + X_n$. Então:

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{D} N(0, 1)$$

Equivalentemente, $\bar{X}_n$ é aproximadamente $N\!\left(\mu, \sigma^2/n\right)$ para $n$ grande. O resultado vale **qualquer que seja** a distribuição comum dos $X_i$, desde que a variância seja finita — esta universalidade explica a onipresença da Normal.

A demonstração usual usa funções geradoras de momentos: mostra-se que $M_{Z_n}(t) \to e^{t^2/2}$, a FGM da $N(0,1)$, e invoca-se a propriedade de unicidade da FGM.

## Usabilidade e Aplicações

- **Aproximação Normal da Binomial:** se $X \sim \text{Binomial}(n, p)$ com $n$ grande, $X \approx N(np,\ np(1-p))$, com correção de continuidade quando necessário.
- **Aproximação Normal da Poisson e da Gama:** $\text{Poisson}(\lambda)$ com $\lambda$ grande e $\text{Gama}(n, \beta)$ com $n$ grande são aproximadamente Normais, pois ambas são somas de parcelas i.i.d.
- **Determinação de tamanho amostral:** o TLC permite responder "qual o menor $n$ tal que $P(|\bar{X}_n - \mu| \le \varepsilon) \ge 0{,}95$?", convertendo a exigência em quantis da Normal padrão.
- **Aproximação de Stirling:** o TLC aplicado a somas de Poisson fornece uma derivação probabilística da fórmula de Stirling, $n! \approx \sqrt{2\pi n}\, n^n e^{-n}$.
