---
id: "lista02-q18-tamanho-de-amostra"
titulo: "Tamanho de Amostra"
topicos: ["distribuicao-normal"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Qual deve ser o tamanho da amostra $n$ para que $|\hat{p} - p| \le 0.005$ com 95% de probabilidade?

## Solução

Pelo Teorema Central do Limite, o erro $|\hat{p} - p|$ é limitado por $z_{\alpha/2} \sqrt{\frac{p(1-p)}{n}}$. Para 95% de confiança, $z_{0.025} = 1.96$.<br>$1.96 \sqrt{\frac{p(1-p)}{n}} \le 0.005 \implies n \ge (\frac{1.96}{0.005})^2 p(1-p)$.

**Caso 1: $p$ desconhecido.** A variância $p(1-p)$ é máxima quando $p=0.5$.<br>$ n \ge (392)^2 (0.5)(0.5) = 38416 $.

**Caso 2: $p \le 0.2$.** A função $p(1-p)$ é crescente em [0, 0.5], então o pior caso na restrição é $p=0.2$.<br>$ n \ge (392)^2 (0.2)(0.8) \approx 24586.24 $. O tamanho da amostra deve ser 24587.
