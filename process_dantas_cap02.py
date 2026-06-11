#!/usr/bin/env python3
"""
Processa as questoes do Dantas Cap. 2 e as adiciona ao projeto
com frontmatter completo e topicos corretos.
"""

import os
import re

SRC = "source/dantas/cap-02"
DST = "app/src/content/exercicios/dantas/cap-02"

# (titulo, topicos, tags, dificuldade)
QUESTOES = {
    1:  ("Distribuicao de Probabilidade Discreta Empirica",
         ["variaveis-aleatorias-continuas"],
         ["probabilidade", "esperanca", "variancia"], "baixa"),
    2:  ("Distribuicao Discreta com Probabilidade Geometrica",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida", "probabilidade"], "media"),
    3:  ("Distribuicao Discreta Linear e Constante Normalizadora",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida", "probabilidade"], "media"),
    4:  ("Distribuicao do Maximo de Dois Dados",
         ["variaveis-aleatorias-continuas"],
         ["probabilidade", "fda"], "media"),
    5:  ("Funcao Densidade Arbitraria e Constante Normalizadora",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida", "probabilidade"], "media"),
    6:  ("Distribuicao Exponencial: FDP e Probabilidades",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida", "probabilidade"], "media"),
    7:  ("Distribuicao Triangular: FDP e Probabilidades",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida", "probabilidade"], "media"),
    8:  ("FDP Cosseno: Constante e Probabilidade",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida", "probabilidade"], "media"),
    9:  ("Esperanca e Variancia para Distribuicoes das Questoes 1 a 8",
         ["variaveis-aleatorias-continuas"],
         ["esperanca", "variancia"], "alta"),
    10: ("Linearidade da Esperanca: Prova e Generalizacao",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "alta"),
    11: ("Propriedades da Esperanca Matematica",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "media"),
    12: ("Propriedades da Variancia e Transformacoes Lineares",
         ["variaveis-aleatorias-continuas"],
         ["variancia"], "media"),
    13: ("Minimizacao de E[(X-a)^2] e Interpretacao como Variancia",
         ["variaveis-aleatorias-continuas"],
         ["esperanca", "variancia"], "media"),
    14: ("Variancia de Soma de Variaveis Aleatorias Dependentes",
         ["variaveis-aleatorias-continuas"],
         ["variancia"], "media"),
    15: ("Distribuicao com Esperanca Finita mas Variancia Infinita",
         ["variaveis-aleatorias-continuas"],
         ["esperanca", "variancia"], "alta"),
    16: ("Propriedades de Distribuicoes Simetricas e Esperanca",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "alta"),
    17: ("FGM de Distribuicoes Continuas das Questoes 5 a 8",
         ["02-funcao-geradora-momentos"],
         ["fgm", "esperanca", "variancia"], "alta"),
    18: ("FGM de Variaveis Aleatorias Discretas",
         ["02-funcao-geradora-momentos"],
         ["fgm"], "media"),
    19: ("FGM, Funcao Geradora de Probabilidade e Funcao Caracteristica",
         ["02-funcao-geradora-momentos"],
         ["fgm"], "alta"),
    20: ("Funcao Caracteristica e Limitacao por 1",
         ["02-funcao-geradora-momentos"],
         ["fgm"], "alta"),
    21: ("FGM de Transformacao Linear Y = aX + b",
         ["02-funcao-geradora-momentos"],
         ["fgm"], "media"),
    22: ("Funcao Geradora de Cumulantes e Derivadas em t=0",
         ["02-funcao-geradora-momentos"],
         ["fgm", "esperanca", "variancia"], "media"),
    23: ("FDA Mista: Continuidade e Probabilidades",
         ["variaveis-aleatorias-continuas"],
         ["fda", "probabilidade"], "alta"),
    24: ("Propriedades da FDA com Definicoes Alternativas",
         ["variaveis-aleatorias-continuas"],
         ["fda"], "media"),
    25: ("Combinacoes Convexas de Funcoes Densidade",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida"], "media"),
    26: ("FDA do Maximo em Amostragem sem Reposicao",
         ["variaveis-aleatorias-continuas"],
         ["fda"], "alta"),
    27: ("Distribuicao do Tamanho de Subconjunto Aleatorio",
         ["variaveis-aleatorias-continuas"],
         ["fda", "esperanca", "variancia"], "alta"),
    28: ("Distribuicao Zeta de Riemann",
         ["variaveis-aleatorias-continuas"],
         ["probabilidade", "fda"], "alta"),
    29: ("Roleta: Estrategia de Aposta e Esperanca",
         ["variaveis-aleatorias-continuas"],
         ["esperanca", "probabilidade"], "media"),
    30: ("Distribuicao Mista: Esperanca e Variancia",
         ["variaveis-aleatorias-continuas"],
         ["esperanca", "variancia"], "alta"),
    31: ("Problema do Aniversario: Distribuicao e Esperanca",
         ["variaveis-aleatorias-continuas"],
         ["fda", "esperanca"], "alta"),
    32: ("FDA do Quadrado da Distancia em Disco",
         ["variaveis-aleatorias-continuas"],
         ["fda"], "media"),
    33: ("FDP da Distancia em Triangulo Aleatorio",
         ["variaveis-aleatorias-continuas"],
         ["fdp-valida"], "media"),
    34: ("Esperanca do Comprimento do Maior Pedaco de Palito",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "media"),
    35: ("FDA de Y = max(X, c) para Uniforme",
         ["05-funcao-de-variavel-aleatoria"],
         ["fda", "metodo-fda"], "media"),
    36: ("FDA de Y = max(X, c) para FDP Generica",
         ["05-funcao-de-variavel-aleatoria"],
         ["fda", "metodo-fda"], "alta"),
    37: ("Distribuicao Geometrica por Discretizacao de Exponencial",
         ["05-funcao-de-variavel-aleatoria"],
         ["fda", "metodo-fda"], "media"),
    38: ("Numero Esperado de Dias com Exatamente k Aniversarios",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "alta"),
    39: ("Media e Variancia do Numero de Tentativas com Chaves",
         ["variaveis-aleatorias-continuas"],
         ["esperanca", "variancia"], "media"),
    40: ("Nivel de Estoque Otimo para Maximizar Lucro Esperado",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "alta"),
    41: ("Estoque Otimo de Flores para Maximizar Lucro",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "media"),
    42: ("Funcao de Score para Meteorologistas: Maximizacao de Esperanca",
         ["variaveis-aleatorias-continuas"],
         ["esperanca"], "alta"),
}

FRONTMATTER_PAT = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def build_frontmatter(num, titulo, topicos, tags, dificuldade):
    topicos_yaml = "[" + ", ".join(f'"{t}"' for t in topicos) + "]"
    tags_yaml = "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    return (
        "---\n"
        f'id: "dantas-cap02-q{num:02d}"\n'
        f'titulo: "{titulo}"\n'
        f'topicos: {topicos_yaml}\n'
        f'dificuldade: "{dificuldade}"\n'
        f'origem: "livro"\n'
        f'solucao_verificada: false\n'
        f'tags: {tags_yaml}\n'
        f'referencia: "Dantas, Cap. 2, Q. {num}"\n'
        "---\n"
    )


def process_file(src_path, dst_path, num):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    titulo, topicos, tags, dificuldade = QUESTOES[num]
    new_fm = build_frontmatter(num, titulo, topicos, tags, dificuldade)

    body = FRONTMATTER_PAT.sub("", content, count=1)
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
        fname = f"q{num:02d}-dantas-cap02.md"
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
