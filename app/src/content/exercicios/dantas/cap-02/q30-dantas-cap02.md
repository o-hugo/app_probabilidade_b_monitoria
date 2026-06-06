---
id: "q30-dantas-cap02"
titulo: "Questão 30"
topicos: ["03-modelos-continuos","05-funcao-de-variavel-aleatoria"]
dificuldade: "dificil"
origem: "livro"
solucao_verificada: false
---

## Enunciado
A variável aleatória Y tem distribuição de probabilidade dada por
$$P(Y = k) = \frac{1}{k!} \int_0^\infty f(t) t^k e^{-t} dt, \quad k = 0, 1, 2, \dots$$
onde $f(t)$ é a função densidade de probabilidade de uma variável aleatória com média $\mu$ e variância $\sigma^2$. Calcule $E(Y)$ e $\text{Var}(Y)$.

## Solução

A variável $Y$ é o resultado de uma mistura de distribuições. Condicionalmente a uma variável contínua auxiliar $T$, sabemos que a expressão dada remete à distribuição Poisson. Ou seja, $Y|T=t \sim \text{Poisson}(t)$, e $T$ segue uma distribuição cuja densidade de probabilidade marginal é $f(t)$.
Numa distribuição de Poisson regular de parâmetro $\lambda$, sabemos que $E[\text{Poisson}(\lambda)] = \lambda$ e $\text{Var}[\text{Poisson}(\lambda)] = \lambda$.
Isso significa que, dada a variável $T$, os momentos condicionais são:
$$ E(Y | T) = T $$
$$ \text{Var}(Y | T) = T $$

Para extrair os momentos marginais de $Y$ a partir da distribuição condicional, faremos uso dos teoremas da Esperança Total e Variância Total (Teorema de Eve).

- **Cálculo da Esperança $E(Y)$:**
Pela Lei da Esperança Total:
$$ E(Y) = E_T\left[ E(Y|T) \right] $$
Substituindo o primeiro momento condicional $E(Y|T) = T$:
$$ E(Y) = E_T[T] $$
A esperança de $T$ é fornecida pelo enunciado como sendo $\mu$. Logo:
$$ E(Y) = \mu $$

- **Cálculo da Variância $\text{Var}(Y)$:**
A Lei da Variância Total nos garante que a variância de uma variável pode ser decomposta na esperança da variância condicional mais a variância da esperança condicional:
$$ \text{Var}(Y) = E_T\left[ \text{Var}(Y|T) \right] + \text{Var}_T\left[ E(Y|T) \right] $$
Substituindo os dois momentos condicionais obtidos da Poisson ($T$ em ambos os casos):
$$ \text{Var}(Y) = E_T[T] + \text{Var}_T[T] $$
Sabemos pelo enunciado que $E_T[T]$ corresponde à média $\mu$ e que a variância natural da variável $T$, $\text{Var}_T[T]$, equivale a $\sigma^2$. Assim:
$$ \text{Var}(Y) = \mu + \sigma^2 $$

*Nota Analítica: É perfeitamente possível chegar a estes valores aplicando as definições padrões de somatório sobre a série de Taylor e permutando com a integral. O termo $k/k!$ será manipulado dentro do somatório gerando $t \cdot e^t$ que será cortado com $e^{-t}$, resultando analiticamente nas expressões $\int t \cdot f(t)dt$ para o primeiro e momentos em T.*
