---
id: "questoes-q10-lista-questo-10"
titulo: "Questão 10"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

Num teste educacional com crianças, o tempo para a realização de uma bateria de questões de raciocínio verbal e lógico é medido e anotado para ser comparado com o modelo teórico. Este teste é utilizado para identificar o desenvolvimento das crianças e auxiliar a aplicação de medidas corretivas. O modelo teórico considerado T, tempo de teste em minutos, como uma variável aleatória contínua com fdp dada por: $f(t)=\begin{cases}\frac{1}{16}(t-4),&se&s\le t\le10;\\ \frac{3}{26},&se&10\le t\le15;\\ 0,&caso~contrario.\end{cases}$

## Solução

## Passo 1: Analisar o Problema

O enunciado descreve uma fdp, mas não fornece um valor para o limite inferior 's' e não faz uma pergunta explícita. Uma tarefa comum nesses casos é verificar se a expressão pode ser uma fdp válida.

Para que $f(t)$ seja uma fdp, a integral total sobre seu domínio deve ser igual a 1. Vamos testar se isso é possível.

Resumo: O problema está incompleto. Nossa tarefa será testar a validade da expressão como uma fdp.



## Passo 2: Fazer uma Suposição para 's' e Calcular a Integral

Uma suposição razoável é que a função comece onde $f(t)=0$. Para a primeira parte, $\frac{1}{16}(t-4)=0$ quando $t=4$. Vamos assumir $s=4$ e calcular a área total.

$$\text{Área Total} = \int_4^{15} f(t) \,dt = \int_{4}^{10} \frac{1}{16}(t-4) \,dt + \int_{10}^{15} \frac{3}{26} \,dt$$

**Cálculo da primeira integral:**

$$\frac{1}{16} [\frac{t^2}{2} - 4t]_{4}^{10} = \frac{1}{16} [(\frac{100}{2} - 40) - (\frac{16}{2} - 16)] = \frac{1}{16}[10 - (-8)] = \frac{18}{16} = \frac{9}{8}$$

**Cálculo da segunda integral:**

$$\frac{3}{26} [t]_{10}^{15} = \frac{3}{26}(15-10) = \frac{15}{26}$$

Resumo: Assumimos $s=4$ e calculamos a área sob cada parte da função separadamente.



## Passo 3: Somar as Áreas e Concluir

$$\text{Área Total} = \frac{9}{8} + \frac{15}{26} = 1.125 + 0.5769... \approx 1.702 \ne 1$$

Como a área total sob a curva não é 1, **a expressão fornecida não é uma função densidade de probabilidade válida** com a suposição de $s=4$. Não há valor de $s$ que possa corrigir isso, pois a área já excede 1.

Resumo: A soma das áreas é diferente de 1, provando que a função, como escrita, não pode ser uma fdp.
