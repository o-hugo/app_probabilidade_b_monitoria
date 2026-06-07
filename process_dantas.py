#!/usr/bin/env python3
"""
Processa as questoes do Dantas Cap. 1 e as adiciona ao projeto
com frontmatter completo.
"""

import os
import re
import shutil

SRC = "source/dantas/cap-01"
DST = "app/src/content/exercicios/dantas/cap-01"

# Mapeamento: numero da questao -> (titulo, tags, dificuldade)
QUESTOES = {
    1:  ("Espaco Amostral de Experimentos Aleatorios",         ["probabilidade"],            "media"),
    2:  ("Operacoes com Eventos em Lancamento de Moeda",       ["probabilidade"],            "media"),
    3:  ("Operacoes em Espaco Amostral Continuo [0,1]",        ["probabilidade"],            "media"),
    4:  ("Identificacao de Relacoes Verdadeiras entre Eventos",["probabilidade"],            "media"),
    5:  ("Expressoes para Eventos Compostos (A, B, C)",        ["probabilidade"],            "media"),
    6:  ("Identidades do Coeficiente Binomial",                ["probabilidade"],            "media"),
    7:  ("Demonstracao do Teorema Binomial",                   ["probabilidade"],            "media"),
    8:  ("Identidades de Somatorios com Coeficientes Binomiais",["probabilidade"],           "alta"),
    9:  ("Calculo de P(A cap B cap C) via Probabilidade Condicional", ["condicional"],       "media"),
    10: ("Probabilidade da Diferenca Simetrica",               ["probabilidade"],            "media"),
    11: ("Limites de P(A cap B) com Probabilidades Fixadas",   ["probabilidade"],            "media"),
    12: ("Eventos Independentes Dois a Dois com Intersecao Vazia", ["probabilidade"],        "alta"),
    13: ("Independencia Preservada em Complementares",         ["probabilidade"],            "media"),
    14: ("Exclusividade Mutua vs. Independencia",              ["condicional"],              "media"),
    15: ("Desigualdade de Bonferroni e Monotonicidade Condicional", ["condicional"],         "alta"),
    16: ("De Morgan e Complementar da Uniao",                  ["probabilidade"],            "media"),
    17: ("Urna com Bolas Brancas e Pretas sem Reposicao",      ["condicional"],              "media"),
    18: ("Dado Viciado: Par Duas Vezes Mais Provavel",         ["probabilidade"],            "media"),
    19: ("Eventos em Sorteio de Inteiros de 1 a 20",           ["probabilidade"],            "media"),
    20: ("Probabilidade em Espacos Equiprovaveis",             ["probabilidade"],            "media"),
    22: ("Selecao de Membros de Comite sem Reposicao",         ["condicional"],              "media"),
    23: ("Leitores de Jornais (Inclusao-Exclusao)",            ["probabilidade"],            "media"),
    24: ("Probabilidade Condicional em Tabela de Contingencia",["condicional"],              "media"),
    25: ("Teorema de Bayes: Preferencia em Restaurante",       ["condicional"],              "media"),
    26: ("Chaves e Porta: Probabilidade na k-esima Tentativa", ["condicional"],              "media"),
    27: ("Probabilidade de Quina na Loto",                     ["probabilidade"],            "media"),
    28: ("Probabilidade em Extracao de Cartas do Baralho",     ["probabilidade"],            "media"),
    29: ("Arranjo de Livros com Restricao de Assunto",         ["probabilidade"],            "baixa"),
    30: ("Distribuicao de Jornalistas em Funcoes",             ["probabilidade"],            "baixa"),
    31: ("Probabilidades de Maos de Poker",                    ["probabilidade"],            "alta"),
    32: ("Primeira Cara em Lancamento Par ou Impar",           ["probabilidade"],            "media"),
    33: ("Probabilidade de Falha de Dispositivo Eletronico",   ["probabilidade"],            "media"),
    34: ("Bayes: Peca Defeituosa por Maquina",                 ["condicional"],              "media"),
    35: ("Probabilidade de Entrada com Porta Possivelmente Trancada", ["condicional"],       "media"),
    36: ("Bayes: Cor da Bola Perdida",                         ["condicional"],              "alta"),
    37: ("Bayes: Resposta Correta em Multipla Escolha",        ["condicional"],              "media"),
    38: ("Distribuicao de Bolas em Urnas Numeradas",           ["probabilidade"],            "alta"),
    39: ("Probabilidade de Inclusao em Amostragem",            ["probabilidade"],            "media"),
    40: ("Distribuicao Multinomial de Bolas em Urnas",         ["probabilidade"],            "alta"),
    41: ("Distribuicao de Bolas Indistinguiveis em Urnas",     ["probabilidade"],            "alta"),
    42: ("Problema dos Encontros (Derangements)",              ["probabilidade"],            "alta"),
    43: ("Distribuicao Binomial em Urna Especifica",           ["probabilidade"],            "media"),
}

FRONTMATTER_PAT = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def build_frontmatter(num, titulo, tags, dificuldade):
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    return (
        "---\n"
        f'id: "dantas-cap01-q{num:02d}"\n'
        f'titulo: "{titulo}"\n'
        f'topicos: ["variaveis-aleatorias-continuas"]\n'
        f'dificuldade: "{dificuldade}"\n'
        f'origem: "livro"\n'
        f'solucao_verificada: false\n'
        f'tags: {tags_yaml}\n'
        f'referencia: "Dantas, Cap. 1, Q. {num}"\n'
        "---\n"
    )


def process_file(src_path, dst_path, num):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    titulo, tags, dificuldade = QUESTOES[num]
    new_fm = build_frontmatter(num, titulo, tags, dificuldade)

    # Remove existing frontmatter
    body = FRONTMATTER_PAT.sub("", content, count=1)

    # Remove NOTE callout blocks that were auto-inserted
    body = re.sub(r'\n?> \[!NOTE\]\n> .*?\n\n?', '\n', body)
    body = body.lstrip('\n')

    new_content = new_fm + "\n" + body

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  Q{num:02d} -> {os.path.basename(dst_path)}")


def main():
    os.makedirs(DST, exist_ok=True)
    processed = 0

    for num in sorted(QUESTOES.keys()):
        fname = f"q{num:02d}-dantas-cap01.md"
        src_path = os.path.join(SRC, fname)
        dst_path = os.path.join(DST, fname)

        if not os.path.exists(src_path):
            print(f"  AVISO: {src_path} nao encontrado, pulando.")
            continue

        process_file(src_path, dst_path, num)
        processed += 1

    print(f"\nTotal processado: {processed} questoes")


if __name__ == "__main__":
    main()
