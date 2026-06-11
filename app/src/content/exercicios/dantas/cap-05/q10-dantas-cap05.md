---
id: "dantas-cap05-q10"
titulo: "Localização Ótima de Estações de Reparo"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "probabilidade"]
referencia: "Dantas, Cap. 5, Q. 10"
---

## Enunciado

Um ônibus percorre 100 km entre cidades A e B. A avaria ocorre em $X \sim U(0,100)$. Configuração atual: estações em 0, 50 e 100 km. Proposta: estações em 25, 50 e 75 km. Você concorda com a proposta?

## Passo 1: Distância esperada — configuração atual (0, 50, 100)

A distância à estação mais próxima é $D = \min(X, 50-X, X-50, 100-X)$ dependendo do trecho. Por simetria, em cada metade $[0,50]$ e $[50,100]$, a distância esperada à estação mais próxima é $E[\min(X, 50-X)]$ para $X \sim U(0,50) = 50/4 = 12{,}5$ km.

**Resumo:** $E[D_{\text{atual}}] = 12{,}5$ km.

## Passo 2: Configuração proposta (25, 50, 75)

Cada zona de cobertura tem 25 km de comprimento centrados nas estações. A distância esperada em $[0,25]$ à estação em 25 é $E[25-X]$ para $X \sim U(0,25) = 25/2 = 12{,}5$ km. Mas há cobertura de $[0,25]$ pela estação em 25 — distância máxima 25 km, média esperada $= 25/4 = 6{,}25$ km por trecho de 25 km.

Para $X \sim U(0,25)$ com estação em 25: $E[25-X] = 12{,}5$. Para $X \sim U(12{,}5, 37{,}5)$ com estação em 25: $E[|X-25|] = 6{,}25$.

**Configuração proposta:** cada ponto pertence a um intervalo de 25 km em torno de uma estação. Distância esperada $= 25/4 = 6{,}25$ km.

## Passo 3: Comparação

$E[D_{\text{proposta}}] = 6{,}25$ km $< 12{,}5$ km $= E[D_{\text{atual}}]$.

**Concordo com a proposta:** as estações igualmente espaçadas em 25, 50 e 75 km reduzem a distância esperada ao local de reparo de 12,5 para 6,25 km — metade da original.
