# Guia de Autoria de Conteudo

Este guia explica como adicionar ou editar topicos teoricos e exercicios no aplicativo sem alterar codigo.

---

## Estrutura de Conteudo

Todo o conteudo vive em `app/src/content/` organizado em tres colecoes:

```
content/
|-- topicos/            # Teoria organizada por topico
|-- exercicios/         # Exercicios com resolucao passo a passo
|-- revisao/            # Material de revisao rapida
```

## Formato de Arquivo

Cada arquivo e um Markdown (`.md`) com um cabecalho YAML (frontmatter) delimitado por `---`.

### Topico Teorico

```markdown
---
id: "exponencial"
titulo: "Distribuicao Exponencial"
ordem: 3.2
ementa_ref: "Modelos continuos"
tags: ["modelo-continuo", "falta-de-memoria"]
visualizador: "exponencial"
---

# Distribuicao Exponencial

Conteudo teorico em Markdown com formulas KaTeX...

## Definicao

A variavel aleatoria $X$ tem distribuicao exponencial...

## Aplicacoes

Em engenharia de confiabilidade, ...
```

### Exercicio

```markdown
---
id: "lista02-q06-exp-ligacao"
titulo: "Duracao Exponencial de Ligacao"
topicos: ["exponencial", "funcao-sobrevivencia"]
dificuldade: "media"       # baixa | media | alta
origem: "lista-02"         # lista-02 | prova-3 | slides | livro
metodo: "funcao-sobrevivencia"
solucao_verificada: false   # true somente apos revisao
---

## Enunciado

Duracao da ligacao e $X \sim Exp(\lambda=1/10)$. Calcule...

## Passo 1: Identificar a distribuicao

Temos $X \sim Exp(\lambda = 1/10)$, portanto...

## Passo 2: Calcular usando a funcao de sobrevivencia

$$P(X > 10) = e^{-\lambda \cdot 10} = e^{-1} \approx 0.3679$$
```

## Convencoes

### Formulas

- Use `$...$` para formulas inline
- Use `$$...$$` para formulas em bloco (display)
- Siga o glossario de notacao em `docs/glossario-notacao.md`

### Passos de Resolucao

- Cada passo e um heading de nivel 2 (`## Passo N: Descricao`)
- O primeiro `## Enunciado` contem o enunciado do exercicio
- Os passos subsequentes contem a resolucao

### Dificuldade

| Nivel | Criterio |
|---|---|
| `baixa` | Aplicacao direta de uma formula |
| `media` | Requer combinacao de dois conceitos ou manipulacao algebrica moderada |
| `alta` | Requer tecnica avancada, multiplos passos, ou conexao nao-obvia entre conceitos |

### Verificacao de Resolucao

O campo `solucao_verificada` controla a exibicao:
- `false`: a resolucao aparece com aviso de "resolucao nao verificada"
- `true`: a resolucao aparece como definitiva

Nunca mude este campo para `true` sem revisar todos os passos da resolucao.

## Adicionando um Novo Exercicio

1. Crie um arquivo `.md` no diretorio apropriado de `content/exercicios/`
2. Preencha o frontmatter com todos os campos obrigatorios
3. Escreva o enunciado e os passos da resolucao
4. Verifique que os topicos listados no frontmatter existem em `content/topicos/`
5. Teste localmente com `npm run dev`
