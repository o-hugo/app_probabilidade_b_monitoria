---
id: "q11-dantas-cap02"
titulo: "Questão 11"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Mostre, para toda variável aleatória $X$ contínua, que:
(a) Se existe uma constante $\alpha$ tal que $P(X \ge \alpha) = 1$, então $E(X) \ge \alpha$.
(b) Se existe uma constante $\beta$ tal que $P(X \le \beta) = 1$, então $E(X) \le \beta$.
(c) Se $X \ge Y$ (isto é, $X(\omega) \ge Y(\omega)$, $\forall \omega \in \Omega$), então $E(X) \ge E(Y)$, onde $Y$ é uma variável aleatória contínua.
*(Verifique se os resultados em (a), (b) e (c) continuam válidos se $X$ e $Y$ são discretas.)*

## Solução

As propriedades seguem da monotonicidade da integral (e do somatório).

- **(a) Mostre que se $P(X \ge \alpha) = 1$, então $E(X) \ge \alpha$:**
Se a probabilidade de $X$ ser maior ou igual a $\alpha$ é 1, a função densidade $f(x)$ é zero para todo $x < \alpha$.
A esperança de $X$ é dada por:
$$ E(X) = \int_{-\infty}^{\infty} x f(x) \, dx = \int_{\alpha}^{\infty} x f(x) \, dx $$
Como no intervalo de integração temos $x \ge \alpha$ e a densidade é não-negativa ($f(x) \ge 0$):
$$ \int_{\alpha}^{\infty} x f(x) \, dx \ge \int_{\alpha}^{\infty} \alpha f(x) \, dx = \alpha \int_{\alpha}^{\infty} f(x) \, dx $$
Como a integral de $f(x)$ em todo o seu domínio é igual a 1 (e esse domínio é exatamente de $\alpha$ até $\infty$ já que $P(X \ge \alpha)=1$):
$$ E(X) \ge \alpha \times 1 = \alpha $$

- **(b) Mostre que se $P(X \le \beta) = 1$, então $E(X) \le \beta$:**
De forma análoga, $f(x)$ é zero para $x > \beta$.
$$ E(X) = \int_{-\infty}^{\beta} x f(x) \, dx $$
Neste intervalo, $x \le \beta$, logo:
$$ \int_{-\infty}^{\beta} x f(x) \, dx \le \int_{-\infty}^{\beta} \beta f(x) \, dx = \beta \int_{-\infty}^{\beta} f(x) \, dx = \beta $$
Portanto, $E(X) \le \beta$.

- **(c) Mostre que se $X \ge Y$, então $E(X) \ge E(Y)$:**
Se $X(\omega) \ge Y(\omega)$ para todo $\omega$, podemos definir uma nova variável $Z = X - Y$.
Como $X \ge Y$, temos que $Z \ge 0$ e, consequentemente, $P(Z \ge 0) = 1$.
Pelo item (a), se $P(Z \ge 0) = 1$, temos que $E(Z) \ge 0$.
Pela linearidade da esperança, $E(Z) = E(X - Y) = E(X) - E(Y)$.
Logo:
$$ E(X) - E(Y) \ge 0 \implies E(X) \ge E(Y) $$

*Se as variáveis fossem discretas, as integrais seriam substituídas por somatórios sobre o conjunto de valores possíveis, e as desigualdades de cada termo nos somatórios se manteriam de maneira idêntica. A demonstração é válida também para variáveis discretas.*
