---
id: "questoes-q04-lista-questo-4"
titulo: "Questão 4"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

Certa liga é formada pela mistura fundida de dois metais. A liga resultante contém certa porcentagem de chumbo, X, que pode ser considerada uma v.a. com f.d.p. $f(x)=\frac{3}{5}\cdot10^{-5}x(100-x)$ , $0\le x\le100$. Suponha que L, o lucro líquido obtido na venda dessa liga (por unidade de peso), seja dado por $L=C_{1}+C_{2}X$. Calcule $E(L)$, o lucro esperado por unidade.

## Solução

## Passo 1: Utilizar a Propriedade da Linearidade da Esperança

O valor esperado de uma função linear de uma variável aleatória, como $L = C_1 + C_2X$, pode ser simplificado. $C_1$ e $C_2$ são constantes.

$$E(L) = E(C_1 + C_2X) = E(C_1) + E(C_2X) = C_1 + C_2E(X)$$

O problema se resume a encontrar o valor esperado de X, $E(X)$.

Resumo: Simplificamos o problema do lucro esperado para o cálculo da porcentagem esperada de chumbo, E(X).



## Passo 2: Montar a Integral para $E(X)$

$$E(X) = \int_{0}^{100} x \cdot f(x) \,dx = \int_{0}^{100} x \cdot [\frac{3}{5}\cdot10^{-5}x(100-x)] \,dx$$

$$E(X) = \frac{3}{5}\cdot10^{-5} \int_{0}^{100} x^2(100-x) \,dx = \frac{3}{5}\cdot10^{-5} \int_{0}^{100} (100x^2 - x^3) \,dx$$

Resumo: Montamos a integral para E(X) multiplicando x pela fdp e simplificando o integrando.



## Passo 3: Resolver a Integral

$$E(X) = \frac{3}{5}\cdot10^{-5} [\frac{100x^3}{3} - \frac{x^4}{4}]_{0}^{100}$$

$$= \frac{3}{5}\cdot10^{-5} [(\frac{100(100)^3}{3} - \frac{(100)^4}{4}) - (0)]$$

$$= \frac{3}{5}\cdot10^{-5} [\frac{100^4}{3} - \frac{100^4}{4}] = \frac{3}{5}\cdot10^{-5} [100^4 (\frac{1}{3} - \frac{1}{4})]$$

$$= \frac{3}{5}\cdot10^{-5} [10^8 (\frac{4-3}{12})] = \frac{3}{5}\cdot10^{-5} \cdot 10^8 \cdot \frac{1}{12}$$

$$= \frac{3 \cdot 10^3}{5 \cdot 12} = \frac{3000}{60} = 50$$

Resumo: Resolvemos a integral polinomial e encontramos que a porcentagem esperada de chumbo na liga é 50.



## Passo 4: Calcular o Lucro Esperado $E(L)$

Agora substituímos o valor $E(X)=50$ na fórmula do Passo 1.

$$E(L) = C_1 + 50C_2$$

Resumo: Inserimos o valor de E(X) na equação do lucro para obter a resposta final.
