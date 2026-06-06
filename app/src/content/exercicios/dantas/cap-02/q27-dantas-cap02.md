---
id: "q27-dantas-cap02"
titulo: "Questão 27"
topicos: []
dificuldade: "dificil"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
De um conjunto de N elementos, um subconjunto não-vazio é escolhido aleatoriamente (considere que todos os subconjuntos não-vazios têm a mesma probabilidade de serem escolhidos). Seja X o número de elementos contidos no subconjunto escolhido, determine a função de distribuição de X, bem como E(X) e Var(X). Verifique que $\lim_{N \to \infty} \frac{E(X)}{N} = \frac{1}{2}$ e $\lim_{N \to \infty} \frac{\text{Var}(X)}{N} = \frac{1}{4}$.

## Solução

Um conjunto de $N$ elementos possui $2^N$ subconjuntos (incluindo o conjunto vazio). Como a escolha recai sobre subconjuntos **não-vazios**, o nosso espaço amostral contém $2^N - 1$ subconjuntos equiprováveis.

- **Função de Distribuição de X:**
A probabilidade pontual de escolher um subconjunto de tamanho exato $k$ é a razão entre o número de subconjuntos desse tamanho e o total não-vazio:
$$ P(X = k) = \frac{\binom{N}{k}}{2^N - 1}, \quad \text{para } k = 1, 2, \dots, N $$
A função de distribuição acumulada é $F_X(x) = \sum_{k=1}^{\lfloor x \rfloor} \frac{\binom{N}{k}}{2^N - 1}$.

- **Esperança $E(X)$:**
$$ E(X) = \sum_{k=1}^{N} k P(X=k) = \frac{1}{2^N - 1} \sum_{k=1}^{N} k \binom{N}{k} $$
Uma identidade clássica do Binômio de Newton nos diz que $\sum_{k=1}^{N} k \binom{N}{k} = N 2^{N-1}$. Logo:
$$ E(X) = \frac{N 2^{N-1}}{2^N - 1} $$

- **Variância $\text{Var}(X)$:**
Calcularemos $E[X(X-1)]$, a esperança do momento fatorial, pois é mais fácil manipular os termos binomiais:
$$ E[X(X-1)] = \sum_{k=1}^{N} k(k-1) \frac{\binom{N}{k}}{2^N - 1} $$
A identidade binomial para essa soma é $N(N-1)2^{N-2}$. Assim:
$$ E[X(X-1)] = \frac{N(N-1)2^{N-2}}{2^N - 1} $$
Para obter o segundo momento, usamos $E(X^2) = E[X(X-1)] + E(X)$:
$$ E(X^2) = \frac{N(N-1)2^{N-2} + N 2^{N-1}}{2^N - 1} = \frac{N(N+1)2^{N-2}}{2^N - 1} $$
Finalmente, $\text{Var}(X) = E(X^2) - (E(X))^2$:
$$ \text{Var}(X) = \frac{N(N+1)2^{N-2}}{2^N - 1} - \left( \frac{N 2^{N-1}}{2^N - 1} \right)^2 $$

- **Verificação dos Limites ($N \to \infty$):**
Quando $N \to \infty$, a constante $-1$ no denominador torna-se insignificante perante o imenso crescimento de $2^N$, ou seja, $2^N - 1 \approx 2^N$.
Para $E(X)/N$:
$$ \lim_{N \to \infty} \frac{E(X)}{N} = \lim_{N \to \infty} \frac{\frac{N 2^{N-1}}{2^N}}{N} = \lim_{N \to \infty} \frac{2^{N-1}}{2^N} = \frac{1}{2} $$
Para $\text{Var}(X)/N$:
Simplificando as frações por $2^N - 1 \approx 2^N$:
$E(X^2) \approx \frac{N(N+1)2^{N-2}}{2^N} = \frac{N^2+N}{4}$.
$E(X) \approx \frac{N 2^{N-1}}{2^N} = \frac{N}{2} \implies (E(X))^2 \approx \frac{N^2}{4}$.
Substituindo na variância:
$$ \text{Var}(X) \approx \frac{N^2+N}{4} - \frac{N^2}{4} = \frac{N}{4} $$
Dividindo por $N$ e tomando o limite:
$$ \lim_{N \to \infty} \frac{\text{Var}(X)}{N} = \lim_{N \to \infty} \frac{N/4}{N} = \frac{1}{4} $$
As igualdades propostas pelo exercício estão demonstradas.
