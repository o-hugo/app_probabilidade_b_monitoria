---
id: "q01-dantas-cap01"
titulo: "Questão 1"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Defina o espaço amostral para cada um dos seguintes experimentos aleatórios:
(a) lançam-se dois dados e anota-se a configuração obtida;
(b) conta-se o número de peças defeituosas, no intervalo de uma hora, de uma linha de produção;
(c) investigam-se famílias com quatro crianças e anota-se a configuração obtida, segundo o sexo;
(d) numa entrevista telefônica com dez assinantes, pergunta-se se o proprietário tem ou não máquina de secar roupa;
(e) de um fichário com seis nomes, sendo três de mulheres e três de homens, seleciona-se ficha após ficha até que o último nome de mulher seja selecionado.

## Solução

- **(a)** $\Omega = \{(i, j) : i, j \in \{1, 2, 3, 4, 5, 6\}\}$.
- **(b)** $\Omega = \{0, 1, 2, \dots, N\}$, onde $N$ é a capacidade máxima de produção em uma hora (ou $\mathbb{N}$ se não houver limite superior).
- **(c)** $\Omega = \{(x_1, x_2, x_3, x_4) : x_i \in \{M, F\}\}$, totalizando $2^4 = 16$ possibilidades.
- **(d)** $\Omega = \{(x_1, x_2, \dots, x_{10}) : x_i \in \{S, N\}\}$, totalizando $2^{10} = 1024$ possibilidades.
- **(e)** O espaço amostral consiste em sequências ordenadas do conjunto de 3 homens ($H$) e 3 mulheres ($M$), terminando obrigatoriamente com a terceira mulher selecionada. O tamanho da sequência (número de seleções) varia de 3 a 6. Exemplo de ponto em $\Omega$: $(M, M, M)$ ou $(H, M, H, M, H, M)$.
