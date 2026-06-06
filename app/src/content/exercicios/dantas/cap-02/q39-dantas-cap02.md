---
id: "q39-dantas-cap02"
titulo: "Questão 39"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Um homem possui em seu chaveiro $n$ chaves e deseja abrir a porta de sua casa experimentando as chaves ao acaso e independentemente. Determine a média e a variância do número de tentativas se 
(a) As chaves incorretas são descartadas e, consequentemente, não mais selecionadas. 
(b) As chaves incorretas não são separadas, podendo ser escolhidas novamente. 
Admita que apenas uma chave consegue abrir a porta.

## Solução

Seja $X$ a variável aleatória que representa o número da tentativa na qual ele finalmente acerta a chave.

- **(a) Chaves incorretas são descartadas (Sem reposição):**
Quando as chaves testadas são descartadas, ele testará sucessivamente do universo que resta. A chave certa pode ser, de forma perfeitamente equiprovável, a primeira, a segunda, ..., ou a enésima chave testada. Nenhuma posição na fila de testes é favorecida em relação à outra.
Portanto, $X$ segue uma **Distribuição Uniforme Discreta** no intervalo de inteiros $\{1, 2, \dots, n\}$.
Para esta distribuição Uniforme, $P(X=k) = \frac{1}{n}$.
Usando as fórmulas clássicas da Uniforme Discreta:
**Média:**
$$ E(X) = \frac{1+n}{2} $$
**Variância:**
$$ \text{Var}(X) = \frac{n^2 - 1}{12} $$

- **(b) Chaves incorretas não são separadas (Com reposição):**
Quando ele não descarta as chaves, cada teste se torna um ensaio independente de Bernoulli. A probabilidade de encontrar a chave certa é sempre $p = \frac{1}{n}$, e a de errar é $q = 1 - \frac{1}{n}$.
Neste caso, $X$ conta o número de testes necessários até a ocorrência do primeiro "sucesso". Esta é a clássica **Distribuição Geométrica**.
A função de probabilidade é $P(X=k) = q^{k-1} p$.
Usando as propriedades da distribuição Geométrica:
**Média:**
$$ E(X) = \frac{1}{p} = \frac{1}{\frac{1}{n}} = n $$
**Variância:**
$$ \text{Var}(X) = \frac{1-p}{p^2} = \frac{1 - \frac{1}{n}}{\left(\frac{1}{n}\right)^2} = n^2 \left(\frac{n-1}{n}\right) = n(n-1) = n^2 - n $$

**Comentário comparativo:** Descartar as chaves erradas, como dita o senso comum, reduz enormemente o número de tentativas esperadas (de $n$ para aproximadamente a metade $n/2$) e estreita muito a variância, indicando maior precisão e menor sorte/azar.
