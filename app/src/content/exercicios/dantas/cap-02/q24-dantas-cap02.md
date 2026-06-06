---
id: "q24-dantas-cap02"
titulo: "Questão 24"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Se a função de distribuição F da variável aleatória X fosse definida de uma das formas abaixo, descreva como as condições (a), (b) e (c) do lema 2.4.1 deveriam ser modificadas em cada caso: 
i) $F(x) = P(X < x)$ 
ii) $F(x) = P(X > x)$ 
iii) $F(x) = P(X \ge x)$

## Solução

O Lema 2.4.1 define as três propriedades clássicas de uma Função de Distribuição Acumulada "padrão", definida como $F(x) = P(X \le x)$:
- (a) Limites assintóticos: $\lim_{x \to -\infty} F(x) = 0$ e $\lim_{x \to \infty} F(x) = 1$.
- (b) Monotonicidade: $F(x)$ é não decrescente.
- (c) Continuidade: $F(x)$ é contínua à direita.

Vamos analisar como essas propriedades precisariam ser ajustadas para cada uma das definições não-padrão de acumulação.

**i) $F(x) = P(X < x)$ (Acumulada estrita à esquerda)**
- (a) Os limites permanecem idênticos: a probabilidade de ser menor que $-\infty$ é $0$, e de ser menor que $\infty$ é $1$.
- (b) A função continua sendo **não decrescente**, pois a área de acúmulo da probabilidade da esquerda para a direita só aumenta.
- (c) Ao invés de contínua à direita, a função passaria a ser **contínua à esquerda** ($\lim_{\delta \to 0^+} F(x - \delta) = F(x)$), porque eventuais descontinuidades de probabilidade concentrada (saltos discretos em $X=x$) não estão incluídas no limite.

**ii) $F(x) = P(X > x)$ (Sobrevivência estrita à direita)**
- (a) Os limites invertem: $\lim_{x \to -\infty} F(x) = 1$ (toda a probabilidade está à direita de $-\infty$) e $\lim_{x \to \infty} F(x) = 0$ (não há nada à direita de $\infty$).
- (b) Como a probabilidade acúmula à direita de um limite $x$ que varre o espaço de números, quanto maior for o limiar de "sobrevivência" $x$, menor é a área. Portanto, a função seria **não crescente**.
- (c) A função é complementar à acumulada clássica $P(X \le x)$. Como $P(X \le x)$ é contínua à direita, $1 - P(X \le x)$ também será. Assim, a propriedade de ser **contínua à direita** se mantém.

**iii) $F(x) = P(X \ge x)$ (Sobrevivência ou Complementar não-estrita)**
- (a) Os limites invertem como no caso anterior: no $-\infty$ a função vale 1, e no $\infty$ a função vale 0.
- (b) Assim como no caso (ii), a área à direita do limite $x$ torna a função **não crescente**.
- (c) Por analogia complementar com o caso (i), uma vez que eventuais massas discretas de probabilidade no ponto $x$ são englobadas pela função $P(X \ge x)$, a função se ajustaria a ser **contínua à esquerda**.
