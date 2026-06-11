---
id: "dantas-cap03-q06"
titulo: "Aplicação de P(X>x,Y>y) ao problema da urna"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "P(X≥1, Y≥1) = 90/220"
tags: ["probabilidade", "fda"]
referencia: "Dantas, Cap. 3, Q. 6"
---

# Exercício 6

Usando o resultado do Exercício 5, aplicado ao Exercício 1 (urna com 3 vermelhas, 4 brancas, 5 azuis; 3 bolas retiradas sem reposição), determine $P(\text{pelo menos 1 vermelha e pelo menos 1 branca})$, ou seja, $P(X \geq 1,\, Y \geq 1)$.

---

## Solução

Do Exercício 5, temos a identidade:

$$P(X > x,\, Y > y) = 1 - F_X(x) - F_Y(y) + F(x,y),$$

onde $F$, $F_X$, $F_Y$ são, respectivamente, as f.d.a.'s conjunta, marginal de $X$ e marginal de $Y$.

Queremos $P(X \geq 1,\, Y \geq 1) = P(X > 0,\, Y > 0)$, então aplicamos com $x = 0$ e $y = 0$:

$$P(X > 0,\, Y > 0) = 1 - F_X(0) - F_Y(0) + F(0,0).$$

Da tabela do Exercício 1:

$$F_X(0) = P(X \leq 0) = p_X(0) = \frac{84}{220},$$

$$F_Y(0) = P(Y \leq 0) = p_Y(0) = \frac{56}{220},$$

$$F(0,0) = P(X \leq 0,\, Y \leq 0) = p(0,0) = \frac{10}{220}.$$

Logo:

$$P(X \geq 1,\, Y \geq 1) = 1 - \frac{84}{220} - \frac{56}{220} + \frac{10}{220} = \frac{220 - 84 - 56 + 10}{220} = \frac{90}{220} = \frac{9}{22}.$$

**Verificação direta:** Os pares $(x,y)$ com $x \geq 1$ e $y \geq 1$ são $(1,1)$, $(1,2)$, $(2,1)$:

$$\frac{60 + 18 + 12}{220} = \frac{90}{220} = \frac{9}{22}. \checkmark$$

$$\boxed{P(X \geq 1,\, Y \geq 1) = \frac{9}{22} \approx 0{,}409}$$
