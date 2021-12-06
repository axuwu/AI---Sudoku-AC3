# AI---Sudoku-AC3
AI - Solving a 9x9 Sudoku using AC3 algorithm

Objetivo: Resolver a grelha 9x9 do Sudoku

Regras:
1. Cada linha contém os números de 1 a 9
2. Cada coluna contém os números de 1 a 9
3. Cada caixa contém os números de 1 a 9

# CSP
Variáveis

Cada bloco na grade do sudoku representa uma variável, com um total de 81 variáveis.

A variável é uma combinação de uma letra que indica a linha e um dígito que indica a coluna.

X = {X1, X2, ..., X81}

Dominios

Cada variável Xi possui o domínio dos dígitos [1,9]

D = {D1, D2, ..., D81}

Di = {1, 2, 3, 4, 5, 6, 7, 8, 9}

Constraints

O valor de cada variável Xi não pode ser igual a nenhum valor em sua:

- Linha
- Coluna
- Caixa
