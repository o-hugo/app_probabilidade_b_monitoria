---
id: "q42-dantas-cap02"
titulo: "Questão 42"
topicos: ["03-modelos-continuos"]
dificuldade: "dificil"
origem: "livro"
solucao_verificada: false
---

## Enunciado
A cada noite, diferentes meteorologistas nos fornecem a "probabilidade" de que irá chover no dia seguinte. Para avaliar o quão boas são estas previsões, é possível atribuir-se escores a cada um desses meteorologistas, como segue: se o meteorologista diz que irá chover no dia seguinte com probabilidade $p$, então ele receberá um escore de $1 - (1 - p)^2$ se chover no dia seguinte e de $1 - p^2$ se não chover.

Acompanhando os escores obtidos pelos meteorologistas durante um certo período de tempo, podemos concluir que o meteorologista com maior escore médio é aquele que melhor prediz o tempo. Suponha agora que um certo meteorologista esteja ciente deste procedimento de escores e deseje maximizar seu escore esperado num determinado dia. Se este meteorologista acredita que de fato irá chover no dia seguinte com probabilidade $p^*$, qual o valor de $p$ que ele deve dizer para maximizar seu escore esperado? (Interprete o resultado.)

## Solução

O meteorologista possui a crença pessoal ("true belief" / probabilidade verdadeira internalizada) de que a chance real de chover é $p^*$. 
A probabilidade complementar de não chover é $(1 - p^*)$.
A decisão tática dele é divulgar publicamente uma estimativa artificial (ou não) $p$.
Queremos escrever a função da "Esperança do Escore" $E[S(p)]$ desse meteorologista:
$$ E[S(p)] = P(\text{chove}) \times \text{Escore}(\text{chove}) + P(\text{não chove}) \times \text{Escore}(\text{não chove}) $$
$$ E[S(p)] = p^* \left[ 1 - (1 - p)^2 \right] + (1 - p^*) \left[ 1 - p^2 \right] $$

Queremos maximizar essa função escolhendo o melhor valor de $p$. Recorremos ao Cálculo Diferencial, derivando em relação a $p$ e igualando a zero:
$$ \frac{d}{dp} E[S(p)] = p^* \cdot \frac{d}{dp} \left[ 1 - (1 - p)^2 \right] + (1 - p^*) \cdot \frac{d}{dp} \left[ 1 - p^2 \right] $$
Aplicando a regra da cadeia nos binômios:
$$ \frac{d}{dp} E[S(p)] = p^* \left[ -2(1-p)(-1) \right] + (1 - p^*) \left[ -2p \right] $$
$$ \frac{d}{dp} E[S(p)] = 2 p^* (1 - p) - 2 p (1 - p^*) $$
Para achar os pontos críticos, impomos que a derivada seja nula:
$$ 2 p^* (1 - p) - 2 p (1 - p^*) = 0 $$
Podemos dividir por 2 para simplificar:
$$ p^* (1 - p) = p (1 - p^*) $$
Multiplicando os parênteses:
$$ p^* - p^* p = p - p p^* $$
Cortando os termos $-p^* p$ de ambos os lados:
$$ p^* = p $$
Para garantir que é ponto de máximo, checamos a derivada de segunda ordem:
$$ \frac{d^2}{dp^2} E[S(p)] = \frac{d}{dp} [2p^* - 2p] = -2 $$
Como a concavidade é negativa, de fato é um pico global da curva.

**Interpretação:**
O valor ideal que o profissional deve declarar para maximizar seus pontos é **exatamente a probabilidade em que ele próprio acredita ($p = p^*$)**.
Em Teoria da Decisão, chamamos essa função de pontuação estruturada de uma ***Proper Scoring Rule*** (Regra de Pontuação Estritamente Própria). O intuito principal dessas regras não é dar "prêmios altos", mas sim alinhar os incentivos. A regra torna impossível manipular e inflar artificialmente a pontuação mediante exageros (por exemplo, chutar "100%" ou "0%" para ser impactante na TV), encorajando o meteorologista a ser matematicamente sincero ao comunicar sua verdadeira estimativa incerta.
