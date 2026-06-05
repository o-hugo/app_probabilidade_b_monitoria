---
id: "04-distribuicao-normal"
titulo: "Distribuição Normal"
ordem: 4
ementa_ref: "Distribuição normal"
tags: ["normal", "gaussiana", "teorema-limite-central", "padronizacao"]
visualizador: "normal"
---

# Distribuição Normal

A distribuição Normal, denotada por $N(\mu, \sigma^2)$, é o modelo contínuo mais importante da estatística e da teoria das probabilidades. Sua relevância deriva da sua ocorrência natural e do **Teorema do Limite Central (TLC)**.

## Função Densidade de Probabilidade

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \quad \text{para } -\infty < x < \infty$$

A curva tem o formato de "sino", é simétrica em relação à sua média $\mu$, e tem dispersão controlada pelo seu desvio padrão $\sigma$.

- **Média, Mediana e Moda** coincidem no centro da distribuição: $\mu$.

## Teorema do Limite Central

O TLC estabelece que a soma (ou média) de um número suficientemente grande de variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) com variância finita será aproximadamente normalmente distribuída, não importando a distribuição original das variáveis.

> "Regardless of the shape of the population distribution, the distribution of the sample mean $\bar{X}$ is approximately $N(\mu, \sigma/\sqrt{n})$ provided that $n$ is large."
> -- Johnson & Bhattacharyya (2010). Statistics. p. 289.

## A Normal Padrão e a Padronização

A Distribuição Normal Padrão é uma normal com média $0$ e variância $1$, denotada por $Z \sim N(0, 1)$.

A FDP da normal padrão é $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$, e a sua função acumulada (FDA) é denotada por $\Phi(z)$.

### Padronização (Escore Z)

Qualquer variável aleatória normal $X \sim N(\mu, \sigma^2)$ pode ser convertida para a normal padrão através da seguinte transformação:

$$Z = \frac{X - \mu}{\sigma}$$

Assim, podemos calcular probabilidades para qualquer variável normal usando apenas a tabela da distribuição normal padrão:
$$P(a \le X \le b) = P\left( \frac{a - \mu}{\sigma} \le Z \le \frac{b - \mu}{\sigma} \right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$

## Regra Empírica (68-95-99.7)

Para qualquer distribuição normal, as seguintes aproximações são válidas para a proporção dos dados contidos em intervalos em torno da média:

- $P(\mu - \sigma < X < \mu + \sigma) \approx 68.27\%$
- $P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 95.45\%$
- $P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 99.73\%$

## Aplicações Práticas na Vida Real

Por que a Normal é a distribuição mais famosa do mundo? Devido ao Teorema do Limite Central, quase qualquer processo que seja o resultado da soma de muitos pequenos efeitos independentes acaba tendo o formato de um sino. Onde isso é usado na prática?

- **Controle de Qualidade na Indústria (Seis Sigma):** Fábricas (como a produção de peças de carro ou chips de computador) usam a Curva Normal para definir limites aceitáveis de tamanho/peso. O nome "Seis Sigma" refere-se a manter os defeitos além de 6 desvios padrões ($6\sigma$) da média, o que significa apenas 3.4 peças defeituosas por milhão.
- **Mercado Financeiro e Risco (VaR):** O *Value at Risk* (VaR), métrica essencial usada por bancos de investimento, assume que os retornos das ações se aproximam de uma Normal (ou Log-Normal) para calcular qual o prejuízo máximo esperado num dia ruim ($5\%$ da cauda da distribuição).
- **Medicina e Farmacologia:** Quando você faz um exame de sangue, os "valores de referência" que vêm impressos do lado do seu resultado são calculados usando a Distribuição Normal. Os laboratórios testam milhares de pessoas saudáveis e definem o intervalo "normal" como $\mu \pm 2\sigma$ (cobrindo $\approx 95\%$ da população saudável). Se você estiver na cauda de $5\%$, o médico investiga.
- **Machine Learning e IA:** Algoritmos modernos, incluindo processamento de imagens e linguagem (como as redes neurais que treinam LLMs), usam distribuições normais para inicializar seus pesos antes de aprenderem, garantindo estabilidade matemática ao modelo.
