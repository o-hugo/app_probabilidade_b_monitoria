---
id: "dantas-cap07-q22"
titulo: "TLC — Teste de Moeda Honesta"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 22"
---

## Enunciado

Em 10.000 lançamentos de uma moeda, obtiveram-se 6.400 caras. É razoável assumir que a moeda é honesta? Justifique com o TLC.

## Solução

Sob $H_0$: moeda honesta, $p=1/2$. $S_{10000}=$ número de caras.

$E(S_n)=np=5000$, $\text{Var}(S_n)=np(1-p)=2500$, $\sigma=50$.

Pelo TLC: $Z=(S_n-5000)/50\approx N(0,1)$.

$$Z=\frac{6400-5000}{50}=\frac{1400}{50}=28.$$

$P(|Z|\ge 28)\approx 0$ — extremamente improvável sob moeda honesta.

**Conclusão:** Não é razoável assumir que a moeda é honesta. O desvio de 1400 caras acima do esperado representa 28 desvios padrão — probabilidade virtualmente nula.
