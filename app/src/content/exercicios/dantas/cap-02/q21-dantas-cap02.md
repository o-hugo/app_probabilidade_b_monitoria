---
id: "q21-dantas-cap02"
titulo: "Questão 21"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Seja X uma variável aleatória cuja função geradora de momentos é $\phi_1$; seja $Y = aX + b$, onde $a$ e $b$ são constantes reais e, por fim, seja $\phi_2$ a função geradora de momentos de Y. Então, para todo valor de t tal que $\phi_1(at)$ existe, $\phi_2(t) = e^{bt}\phi_1(at)$.

## Solução

A Função Geradora de Momentos (FGM) de uma variável aleatória genérica $Z$ é definida como o valor esperado da função exponencial $e^{tZ}$:
$$ \phi_Z(t) = E[e^{tZ}] $$

Para a variável $Y = aX + b$, podemos aplicar essa mesma definição:
$$ \phi_2(t) = E[e^{tY}] $$
Substituindo $Y$ pela sua definição em função de $X$:
$$ \phi_2(t) = E[e^{t(aX + b)}] $$
Usando as propriedades de potenciação, podemos desmembrar a exponencial:
$$ \phi_2(t) = E[e^{atX + bt}] = E[e^{atX} \cdot e^{bt}] $$
A expressão $e^{bt}$ não possui qualquer componente aleatório (já que $b$ e $t$ são constantes ou parâmetros determinísticos fixos). Pela propriedade de linearidade da esperança, uma constante multiplicativa pode ser retirada do operador $E[\cdot]$:
$$ \phi_2(t) = e^{bt} E[e^{(at)X}] $$
Agora observamos o termo $E[e^{(at)X}]$. Ele tem o exato formato da FGM da variável $X$, avaliada não no ponto $t$, mas no ponto $at$. Ou seja:
$$ E[e^{sX}] = \phi_1(s) \implies E[e^{(at)X}] = \phi_1(at) $$
Substituindo de volta na equação:
$$ \phi_2(t) = e^{bt} \phi_1(at) $$
O que demonstra a propriedade.
