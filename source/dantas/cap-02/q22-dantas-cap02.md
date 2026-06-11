---
id: "q22-dantas-cap02"
titulo: "Questão 22"
topicos: ["03-modelos-continuos","02-funcao-geradora-momentos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Suponha que X é uma variável aleatória com função geradora de momentos $\phi$, média $\mu$ e variância $\sigma^2$. Seja $c(t) = \log \phi(t)$. Verifique que $c'(0) = \mu$ e $c''(0) = \sigma^2$.

## Solução

A função $c(t)$ referenciada no enunciado é chamada de **Função Geradora de Cumulantes** ($K_X(t)$ na literatura padrão). 
A derivada do logaritmo natural é dada por $\frac{d}{dt} \ln(f(t)) = \frac{f'(t)}{f(t)}$.
Avaliando as propriedades da FGM $\phi(t)$ em $t=0$, temos $\phi(0) = E[e^0] = 1$, $\phi'(0) = E[X] = \mu$ e $\phi''(0) = E[X^2]$.

- **Verificação de $c'(0) = \mu$:**
Derivando $c(t)$ pela regra da cadeia:
$$ c'(t) = \frac{d}{dt} \log \phi(t) = \frac{\phi'(t)}{\phi(t)} $$
Substituindo $t=0$:
$$ c'(0) = \frac{\phi'(0)}{\phi(0)} = \frac{\mu}{1} = \mu $$

- **Verificação de $c''(0) = \sigma^2$:**
Derivando $c'(t)$ novamente usando a regra do quociente:
$$ c''(t) = \frac{d}{dt} \left( \frac{\phi'(t)}{\phi(t)} \right) = \frac{\phi''(t)\phi(t) - (\phi'(t))^2}{(\phi(t))^2} $$
Substituindo $t=0$ e usando as propriedades básicas em $0$:
$$ c''(0) = \frac{\phi''(0)\phi(0) - (\phi'(0))^2}{(\phi(0))^2} $$
$$ c''(0) = \frac{E[X^2](1) - (E[X])^2}{(1)^2} $$
$$ c''(0) = E[X^2] - (E[X])^2 $$
A expressão obtida é exatamente a definição de variância. Logo:
$$ c''(0) = \text{Var}(X) = \sigma^2 $$
