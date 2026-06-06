---
id: "q40-dantas-cap02"
titulo: "Questão 40"
topicos: []
dificuldade: "dificil"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Um produto de venda sazonal traz um lucro de B reais por unidade vendida e um prejuízo de L reais por cada unidade estocada e não vendida. O número de unidades deste produto vendidas em um certo supermercado (X) é uma variável aleatória com distribuição de probabilidade $p(i) = P(X=i)$, $i \ge 0$. Supondo que o estoque é feito no início da estação, que não pode haver reposição do produto durante a mesma e que não há devolução das unidades estocadas, determine o nível de estoque que maximiza o lucro esperado do supermercado.

## Solução

Seja $k$ a variável de decisão determinística: o número de unidades encomendadas para o estoque inicial.
A demanda $X$ é uma variável aleatória.
O lucro total da operação é uma função $G(k, X)$, definida como a receita dos itens efetivamente vendidos subtraída do custo/prejuízo dos itens não vendidos (encalhados).
- Quantidade vendida: Nunca é maior do que a demanda $X$ nem maior do que o estoque $k$. Ou seja, $\min(X, k)$.
- Quantidade encalhada: É a parte do estoque $k$ que superou a demanda $X$. Ou seja, $\max(0, k - X)$.
$$ G(k, X) = B \cdot \min(X, k) - L \cdot \max(0, k - X) $$

Buscamos maximizar a Esperança desse lucro, $E[G(k)]$. O jeito mais inteligente de achar o máximo em uma função discreta é usar as **diferenças marginais**, verificando o que acontece ao acrescentar 1 unidade extra no estoque. Analisamos a diferença entre ter $k+1$ unidades e $k$ unidades no estoque:
$$ \Delta G(k) = G(k+1, X) - G(k, X) $$

Existem dois cenários excludentes:
1. **A demanda é maior que o estoque atual ($X > k$):** A unidade extra comprada será com certeza vendida. O lucro aumenta em $B$. Probabilidade desse evento: $P(X > k)$.
2. **A demanda é menor ou igual ao estoque ($X \le k$):** A demanda já foi plenamente saciada. A unidade extra sobrará integralmente, causando um prejuízo $L$. Probabilidade desse evento: $P(X \le k)$.

Portanto, o ganho esperado ao adicionar a unidade de número $(k+1)$ é:
$$ E[\Delta G(k)] = B \cdot P(X > k) - L \cdot P(X \le k) $$
Sabendo que probabilidade total é $1$, $P(X > k) = 1 - P(X \le k)$. Substituindo:
$$ E[\Delta G(k)] = B(1 - P(X \le k)) - L \cdot P(X \le k) $$
$$ E[\Delta G(k)] = B - (B + L) P(X \le k) $$

Para que valha a pena adquirir essa $(k+1)$-ésima unidade, o ganho marginal esperado deve ser positivo (ou nulo na margem):
$$ E[\Delta G(k)] \ge 0 \implies B - (B + L) P(X \le k) \ge 0 $$
$$ B \ge (B + L) P(X \le k) \implies P(X \le k) \le \frac{B}{B+L} $$

O lucro crescerá se aumentarmos $k$ até o momento em que adicionar a próxima unidade crie uma expectativa negativa. 
A inversão matemática de sinal acontece no menor limite onde não se satisfaz a equação, então, o nível de estoque ideal (ótimo) $k^*$ é o **menor valor inteiro que satisfaça a condição reversa**:
$$ P(X \le k^*) \ge \frac{B}{B+L} $$

*(Este é um modelo clássico de pesquisa operacional chamado de **Modelo de Estoque do Jornaleiro / Newsvendor Model**)*.
