---
id: "lista02-q22-frmula-alternativa-para-ex"
titulo: "Fórmula Alternativa para E[X]"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Mostre que para uma v.a. não-negativa e contínua X, $E(X)=\int_{0}^{\infty}P(X>t)dt$.

## Solução

Usamos integração por partes na integral $\int_{0}^{\infty} P(X>t) dt$.<br>Sabemos que $P(X>t) = 1-F(t)$.<br>Seja $u = 1-F(t)$ e $dv = dt$. Então $du = -f(t)dt$ e $v = t$.<br>A fórmula de integração por partes é $\int u dv = uv - \int v du$.<br>$$ \int_{0}^{\infty} (1-F(t)) dt = [t(1-F(t))]_{0}^{\infty} - \int_{0}^{\infty} t(-f(t))dt $$

Avaliando o primeiro termo: $\lim_{t \to \infty} t(1-F(t)) - 0$. Se $E[X]$ é finito, este limite é 0.<br>$$ = 0 + \int_{0}^{\infty} tf(t)dt = E[X] $$
