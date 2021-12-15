# AI-Sudoku-AC3
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

# Sudoku and AC3

We can think like in a Excel spreadsheet, each little square is a cell

Each Cell is a constraint that contains (Value, Domain)

An Cell with a digit between 1 to 9 is a occupied cell that his value is the digit itself and his Domain is the value itself too.
An cell with value 0 is a unoccupied, and so his Domain at start is numbers between 1 to 9.

Each cell has 20 neighbors:
- 8 neighbors from the Horizontal Line
- 8 neighbors from the Vertical line
- 4 neighbors from the Same Square
Why u ask? Well the cell cant count itself as neighbor and neither can he recount the same cells as neighbors (so no repeats), leaving us with so called 20 neighbors

To recude the domains we will have to arc reduce them
And so we have to compare cell by cell
Revising a Chell1 with a Cell2 to remove values from the domain



