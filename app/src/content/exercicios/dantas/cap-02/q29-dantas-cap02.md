---
id: "dantas-cap02-q29"
titulo: "Roleta: Estrategia de Aposta e Esperanca"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "probabilidade"]
referencia: "Dantas, Cap. 2, Q. 29"
---

## Enunciado
Um livro para apostadores recomenda a seguinte estratégia que afirma ser vencedora para o jogo de roleta. Aposte R$ 1,00 nas vermelhas. Se o resultado do giro da roleta for vermelha (cuja probabilidade é $18/38$), então retire seu benefício de R$ 1,00 e saia do jogo. Se perder a aposta (cuja probabilidade é $20/38$), faça uma aposta adicional de R$ 1,00 em vermelha em cada um dos próximos dois giros da roleta, e então saia. Seja X o seu ganho ao deixar o jogo de roleta. 
(a) Determine $P(X > 0)$. 
(b) Você acha que, de fato, esta é uma estratégia vencedora? Justifique. 
(c) Calcule E(X).

## Solução

Considerando as apostas na roleta: probabilidade de ganhar em 1 giro é $p = \frac{18}{38}$ e de perder é $q = \frac{20}{38}$.

A estratégia dita os seguintes cenários e ganhos líquidos $X$:
1. **Ganha no 1º giro:** Probabilidade $p = \frac{18}{38}$. Lucro $X = +1$.
2. **Perde no 1º giro:** (Probabilidade $q = \frac{20}{38}$). Ele continua e aposta mais 1 nos dois giros seguintes. A partir daqui, são 3 desdobramentos de lucro independentes para os dois últimos jogos:
   - *Ganha os 2 giros extras:* Ganho parcial $+2$. Somado à perda de $-1$ do começo, o lucro total é $X = +1$. Isso ocorre com probabilidade $q \times p^2$.
   - *Ganha 1 e Perde 1 dos giros extras:* Ganho parcial é $0$. Com a perda inicial de $-1$, lucro total $X = -1$. Probabilidade: $q \times (2pq)$.
   - *Perde os 2 giros extras:* Ganho parcial $-2$. Lucro total $X = -3$. Probabilidade: $q \times q^2 = q^3$.

Resumo da distribuição de probabilidade da variável X (Ganho):
- $P(X=1) = p + q p^2$
- $P(X=-1) = 2 p q^2$
- $P(X=-3) = q^3$

- **(a) Determine $P(X > 0)$:**
A probabilidade do ganho ser estritamente maior que zero é ser $X=1$.
$$ P(X > 0) = P(X=1) = p + q p^2 = \frac{18}{38} + \left(\frac{20}{38}\right)\left(\frac{18}{38}\right)^2 $$
Simplificando com frações irredutíveis ($p=\frac{9}{19}, q=\frac{10}{19}$):
$$ P(X > 0) = \frac{9}{19} + \frac{10}{19} \cdot \frac{81}{361} = \frac{3249}{6859} + \frac{810}{6859} = \frac{4059}{6859} \approx 0,5917 \text{ ou } 59,17\% $$

- **(b) Esta é uma estratégia vencedora?**
Apesar de ter **cerca de 59% de chances de sair lucrando ($X=1$)**, esta **não é** uma estratégia vencedora do ponto de vista matemático. Na roleta americana, cada aposta tem valor esperado negativo. Uma manipulação na quantia ou ordem das apostas pode aumentar a probabilidade de um pequeno ganho, mas condensa o risco em perdas maiores quando elas ocorrem (neste caso, a perda de $-3$). A longo prazo, a lei dos grandes números garante que o balanço geral da estratégia vai corroer o capital devido à expectativa inerente do jogo ser negativa.

- **(c) Calcule E(X):**
Pela definição de esperança matemática $\sum x_i P(X=x_i)$:
$$ E(X) = 1 \cdot P(X=1) + (-1) \cdot P(X=-1) + (-3) \cdot P(X=-3) $$
$$ E(X) = 1 \left( \frac{4059}{6859} \right) - 1 \left( 2 \cdot \frac{9}{19} \cdot \frac{100}{361} \right) - 3 \left( \frac{1000}{6859} \right) $$
$$ E(X) = \frac{4059}{6859} - \frac{1800}{6859} - \frac{3000}{6859} = \frac{4059 - 4800}{6859} $$
$$ E(X) = -\frac{741}{6859} \approx -0,108 $$
O lucro esperado é negativo em 10,8 centavos para cada ciclo da estratégia, corroborando a resposta do item b.
