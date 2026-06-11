---
id: "dantas-cap05-q19"
titulo: "Taxa de Falha da Distribuição Gama"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["taxa-de-falha", "confiabilidade"]
referencia: "Dantas, Cap. 5, Q. 19"
---

## Enunciado

Determine a função taxa de falha de $X \sim \text{Gama}(t, \lambda)$ com densidade $f(x) = \frac{\lambda e^{-\lambda x}(\lambda x)^{t-1}}{\Gamma(t)},\; x>0$.

## Solução

A taxa de falha é $h(x) = f(x)/R(x)$ onde $R(x) = P(X > x) = 1 - F(x)$.

$$h(x) = \frac{f(x)}{1 - F(x)} = \frac{\dfrac{\lambda e^{-\lambda x}(\lambda x)^{t-1}}{\Gamma(t)}}{1 - F_{\text{Gama}(t,\lambda)}(x)}.$$

Para a distribuição Gama, $R(x) = 1 - F(x) = \frac{\Gamma(t, \lambda x)}{\Gamma(t)}$ onde $\Gamma(t, u) = \int_u^\infty s^{t-1}e^{-s}ds$ é a função Gama incompleta superior. Portanto:

$$h(x) = \frac{\lambda e^{-\lambda x}(\lambda x)^{t-1}}{\Gamma(t, \lambda x)}.$$

**Caso especial $t=1$:** $X \sim \text{Exp}(\lambda)$, $h(x) = \lambda$ (taxa constante — falta de memória).

**Para $t > 1$:** $h(x)$ é crescente em $x$ (desgaste). **Para $0 < t < 1$:** $h(x)$ é decrescente (taxa de falha decrescente).
