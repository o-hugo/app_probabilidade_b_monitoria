---
id: "q20-dantas-cap02"
titulo: "Questão 20"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Seja X uma variável aleatória. A função característica de X é a função $\psi : \mathbb{R} \to \mathbb{C}$ dada por $\psi_X(t) = E(e^{itX})$, onde $i = \sqrt{-1}$. Lembrando que $e^{itX} = \cos(tX) + i\sin(tX)$ e $|a+bi|^2 = a^2 + b^2$, verifique que a função característica é limitada por 1, isto é, $|\psi_X(t)| \le 1, \forall t \in \mathbb{R}$. 
*(A função característica de variáveis aleatórias é de grande importância em teoria das probabilidades, dentre outros motivos, por ser limitada e portanto sempre existir. Os pré-requisitos adotados não nos permitem tratar da função característica nesse texto.)*

## Solução

A função característica é o valor esperado da variável aleatória complexa $e^{itX}$.

Pela propriedade fundamental das integrais e esperanças de variáveis complexas, sabemos que o módulo da esperança é sempre menor ou igual à esperança do módulo. Esta é uma generalização da Desigualdade Triangular para integrais:
$$ |\psi_X(t)| = \left| E\left[ e^{itX} \right] \right| \le E\left[ \left| e^{itX} \right| \right] $$

Vamos calcular o módulo interno $\left| e^{itX} \right|$. Pela Fórmula de Euler:
$$ e^{itX} = \cos(tX) + i\sin(tX) $$
O módulo de um número complexo $z = a + bi$ é $|z| = \sqrt{a^2 + b^2}$. Portanto:
$$ \left| e^{itX} \right| = \sqrt{\cos^2(tX) + \sin^2(tX)} $$
Pela identidade trigonométrica fundamental, $\cos^2(\theta) + \sin^2(\theta) = 1$ para qualquer ângulo real $\theta$. Assim:
$$ \left| e^{itX} \right| = \sqrt{1} = 1 $$

Substituindo essa constatação na nossa desigualdade da esperança:
$$ |\psi_X(t)| \le E\left[ \left| e^{itX} \right| \right] = E[1] $$
Como a esperança de uma constante (1) é a própria constante:
$$ |\psi_X(t)| \le 1 $$

A função característica é de fato uniformemente limitada por 1 em todo o eixo real $\mathbb{R}$.
