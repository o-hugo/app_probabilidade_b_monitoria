---
id: "dantas-cap06-q27"
titulo: "Normal Bivariada — Idades de Pais em Hospital"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "padronizacao-z"]
referencia: "Dantas, Cap. 6, Q. 27"
---

## Enunciado

Idades de pais seguem normal bivariada com $\mu_M=28{,}4$, $\sigma_M=6{,}8$, $\mu_P=31{,}6$, $\sigma_P=7{,}4$, $\rho=0{,}82$. Determine:

(a) A proporção de mães com mais de 30 anos.
(b) A proporção de casais em que ambos têm menos de 25 anos.

## Solução

**(a) $P(M>30)$:**

Marginal $M\sim N(28{,}4;\ 6{,}8^2)$.

$$P(M>30)=P\!\left(Z>\frac{30-28{,}4}{6{,}8}\right)=P(Z>0{,}235)=1-\Phi(0{,}235)\approx 1-0{,}593=0{,}407.$$

Aproximadamente **40,7%** das mães têm mais de 30 anos.

**(b) $P(M<25,P<25)$:**

Para a normal bivariada, a probabilidade conjunta requer integração numérica.

Padronizando: $U=(M-28{,}4)/6{,}8$, $V=(P-31{,}6)/7{,}4$. Queremos $P(U<u_0,V<v_0)$ com $u_0=(25-28{,}4)/6{,}8=-0{,}5$ e $v_0=(25-31{,}6)/7{,}4=-0{,}892$.

$$P(M<25,P<25)=\Phi_2(-0{,}5;-0{,}892;\rho=0{,}82),$$

onde $\Phi_2$ é a FDA da normal bivariada padrão. Numericamente $\approx 0{,}029$ (≈ 2,9%).
