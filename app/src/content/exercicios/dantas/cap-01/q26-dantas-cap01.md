---
id: "q26-dantas-cap01"
titulo: "Questão 26"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Um indivíduo tem $n$ chaves, das quais somente uma abre uma porta. Ele seleciona, a cada tentativa, uma chave ao acaso sem reposição e tenta abrir a porta. Qual é a probabilidade de que ele abra a porta na $k$-ésima tentativa ($k = 1, 2, ..., n$)?

## Solução

O problema diz que as chaves são sorteadas sem reposição. A porta será aberta exatamente na $k$-ésima tentativa se, e somente se, o indivíduo falhar nas primeiras $k-1$ tentativas e acertar na tentativa $k$.

Podemos resolver usando a probabilidade condicional passo a passo:
- Na 1ª tentativa, a probabilidade de errar é $\frac{n-1}{n}$.
- Na 2ª tentativa, restam $n-1$ chaves, sendo $n-2$ incorretas. A probabilidade de errar novamente é $\frac{n-2}{n-1}$.
- Na $(k-1)$-ésima tentativa, restarão $n - (k-2)$ chaves, com a probabilidade de erro de $\frac{n-k+1}{n-k+2}$.
- Na $k$-ésima tentativa, restarão $n - (k-1)$ chaves, e há 1 correta. A probabilidade de acertar é $\frac{1}{n-k+1}$.

A probabilidade do evento é o produto de todas essas probabilidades:
$$ P(\text{Acerto na } k\text{-ésima}) = \left(\frac{n-1}{n}\right) \times \left(\frac{n-2}{n-1}\right) \times \dots \times \left(\frac{n-k+1}{n-k+2}\right) \times \left(\frac{1}{n-k+1}\right) $$

Note que os termos das frações adjacentes vão se cancelando em cascata ("efeito telescópico"): o $n-1$ corta com o $n-1$, o $n-2$ com o $n-2$, e assim sucessivamente até que o $n-k+1$ também é cancelado.

O único termo no denominador que sobra é o primeiro $n$, e o único termo no numerador que sobra é o $1$ da última fração. Portanto:
$$ P(\text{Acerto na } k\text{-ésima}) = \frac{1}{n} $$

**Interpretação alternativa e mais direta:** Como as chaves são testadas aleatoriamente sem reposição, a chave correta tem chances idênticas de estar em qualquer uma das $n$ posições da sequência de testes. Logo, a probabilidade de que ela seja a $k$-ésima a ser sorteada é simplesmente $\frac{1}{n}$, para qualquer $1 \le k \le n$.
