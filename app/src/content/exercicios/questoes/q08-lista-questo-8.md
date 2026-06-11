---
id: "questoes-q08-lista-questo-8"
titulo: "Questão 8"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
tags: ["esperanca"]
---

## Enunciado

O tempo de vida, medido em horas, de uma válvula eletrônica é uma variável aleatória com função densidade de probabilidade dada por $f(x)=xe^{-x}$, $x\ge0$. Calcule o tempo de vida esperado dessa válvula.

## Solução

## Passo 1: Definir a Esperança E(X)

O tempo de vida esperado é a esperança matemática da variável aleatória X. Montamos a integral:

$$E(X) = \int_{0}^{\infty} x \cdot f(x) \,dx = \int_{0}^{\infty} x \cdot (xe^{-x}) \,dx = \int_{0}^{\infty} x^2 e^{-x} \,dx$$

Esta integral é um caso particular da Função Gama, $\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt$. No nosso caso, $z-1=2 \implies z=3$. Sabemos que $\Gamma(n) = (n-1)!$ para inteiros $n$. Logo, $\Gamma(3) = 2! = 2$. Vamos confirmar o resultado usando integração por partes.

Resumo: Formulamos a esperança como uma integral definida e a reconhecemos como uma Função Gama.



## Passo 2: Resolver a Integral por Partes (duas vezes)

Usamos a fórmula $\int u \,dv = uv - \int v \,du$.

**Primeira aplicação:** Para $\int x^2 e^{-x} dx$.

Seja $u=x^2$ e $dv=e^{-x}dx$. Então $du=2xdx$ e $v=-e^{-x}$.

$$\int x^2 e^{-x} dx = -x^2e^{-x} - \int (-e^{-x})(2x) dx = -x^2e^{-x} + 2 \int xe^{-x} dx$$

**Segunda aplicação:** Para $\int xe^{-x} dx$.

Seja $u=x$ e $dv=e^{-x}dx$. Então $du=dx$ e $v=-e^{-x}$.

$$\int xe^{-x} dx = -xe^{-x} - \int (-e^{-x}) dx = -xe^{-x} - e^{-x}$$

Juntando tudo, a integral indefinida é: $-x^2e^{-x} + 2(-xe^{-x} - e^{-x}) = -e^{-x}(x^2+2x+2)$.

Resumo: Aplicamos a técnica de integração por partes duas vezes para encontrar a primitiva da função.



## Passo 3: Avaliar a Integral Definida

$$E(X) = [-e^{-x}(x^2+2x+2)]_0^\infty$$

Avaliando no limite superior ($x \to \infty$), o termo $e^{-x}$ vai a zero mais rápido do que qualquer polinômio, então o resultado é 0.

Avaliando no limite inferior ($x = 0$): $-e^{-0}(0^2+2(0)+2) = -1(2) = -2$.

$$E(X) = (0) - (-2) = 2$$

O tempo de vida esperado é de **2 horas**.

Resumo: Aplicamos os limites de integração na primitiva encontrada, confirmando o resultado da Função Gama.
