---
id: "questoes-q24-livro-exemplo-284-fgm-exponencial"
titulo: "Exemplo 2.8.4 (FGM Exponencial)"
topicos: ["modelos-continuos", "funcao-geradora-momentos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Seja X uma variável aleatória com densidade de probabilidade $f(x)=\lambda e^{-\lambda x}$ para $x\ge0$ onde $\lambda$ é uma constante positiva. Determinar a função geradora de momentos de X.

## Solução

## Passo 1: Usar a Definição de FGM

A Função Geradora de Momentos (FGM) é definida como $\phi_X(t) = E(e^{tX})$. Para uma variável contínua, isso se traduz em:

$$\phi_X(t) = \int_0^\infty e^{tx} f(x) \,dx = \int_0^\infty e^{tx} (\lambda e^{-\lambda x}) \,dx$$

Resumo: Aplicamos a definição da FGM para uma variável contínua, montando a integral correspondente.



## Passo 2: Simplificar e Resolver a Integral

Combinamos os termos exponenciais:

$$\phi_X(t) = \lambda \int_0^\infty e^{tx - \lambda x} \,dx = \lambda \int_0^\infty e^{-(\lambda - t)x} \,dx$$

A integral converge somente se o expoente for negativo, ou seja, $\lambda - t > 0$, o que implica $t < \lambda$.

Resolvendo a integral:

$$= \lambda [\frac{e^{-(\lambda - t)x}}{-(\lambda - t)}]_0^\infty$$

$$= \frac{-\lambda}{\lambda-t} [e^{-(\lambda-t)x}]_0^\infty = \frac{-\lambda}{\lambda-t} (0 - 1) = \frac{\lambda}{\lambda - t}$$

Resumo: Resolvemos a integral exponencial, prestando atenção à condição de convergência que define o domínio da FGM.



## Conclusão

A FGM da distribuição exponencial é:

$$\phi_X(t) = \frac{\lambda}{\lambda - t}, \text{ para } t < \lambda$$
