---
id: "dantas-cap03-q21"
titulo: "Melhor estimador linear de Y dado X por mínimos quadrados"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "b = Cov(X,Y)/Var(X); a = E[Y] - b*E[X]"
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 3, Q. 21"
---

# Exercício 21

Determine os coeficientes $a$ e $b$ que minimizam

$$Q(a,b) = E\!\left[(\hat{Y}(X) - Y)^2\right], \quad \text{onde } \hat{Y}(X) = a + bX.$$

---

## Passo 1: Desenvolvimento de $Q(a,b)$

**Resumo:** Expande-se o quadrado e aplica-se a linearidade da esperança.

$$Q(a,b) = E[(a + bX - Y)^2].$$

Denotando $\mu_X = E[X]$, $\mu_Y = E[Y]$, $\sigma_X^2 = \text{Var}(X)$, $\sigma_Y^2 = \text{Var}(Y)$, $\sigma_{XY} = \text{Cov}(X,Y)$:

$$Q(a,b) = E[a^2 + b^2X^2 + Y^2 + 2abX - 2aY - 2bXY]$$

$$= a^2 + b^2 E[X^2] + E[Y^2] + 2ab\mu_X - 2a\mu_Y - 2b E[XY].$$

---

## Passo 2: Condições de primeira ordem

**Resumo:** Derivam-se as equações $\partial Q/\partial a = 0$ e $\partial Q/\partial b = 0$.

$$\frac{\partial Q}{\partial a} = 2a + 2b\mu_X - 2\mu_Y = 0 \implies a = \mu_Y - b\mu_X. \tag{1}$$

$$\frac{\partial Q}{\partial b} = 2b E[X^2] + 2a\mu_X - 2E[XY] = 0. \tag{2}$$

---

## Passo 3: Resolução para $b$

**Resumo:** Substitui-se (1) em (2) e simplifica.

Substituindo $a = \mu_Y - b\mu_X$ em (2):

$$2b E[X^2] + 2(\mu_Y - b\mu_X)\mu_X - 2E[XY] = 0$$

$$b(E[X^2] - \mu_X^2) = E[XY] - \mu_X\mu_Y$$

$$b = \frac{E[XY] - \mu_X\mu_Y}{E[X^2] - \mu_X^2} = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}.$$

---

## Passo 4: Resultado final

**Resumo:** Os coeficientes ótimos expressam-se em termos dos momentos de primeira e segunda ordem.

$$\boxed{b = \frac{\text{Cov}(X,Y)}{\text{Var}(X)} = \rho \frac{\sigma_Y}{\sigma_X}, \qquad a = \mu_Y - b\,\mu_X = E[Y] - \frac{\text{Cov}(X,Y)}{\text{Var}(X)} E[X].}$$

O preditor linear ótimo é:

$$\hat{Y}(X) = E[Y] + \frac{\text{Cov}(X,Y)}{\text{Var}(X)}(X - E[X]).$$

O erro quadrático mínimo é:

$$Q_{\min} = \text{Var}(Y)(1 - \rho^2),$$

onde $\rho = \text{Corr}(X,Y)$.
