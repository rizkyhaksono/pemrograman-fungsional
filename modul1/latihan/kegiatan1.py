__author__      = "rizkyhaksono"
__copyright__   = "Copyright 2023, Malang"

# fungsi pengurangan
def minus (node):
  if type(node) in (int, float):
    return node
  elif type(node) is tuple and len(node) == 3:
    operator, left_operand, right_operand = node
    if operator == '+':
      return tree(left_operand) + tree(right_operand)
    elif operator == '-':
      return tree(left_operand) - tree(right_operand)
    elif operator == '*':
      return tree(left_operand) * tree(right_operand)
    elif operator == '/':
      return tree(left_operand) / tree(right_operand)

# fungsi perkalian
def mult (node):
  if type(node) in (int, float):
    return node
  elif type(node) is tuple and len(node) == 3:
    operator, left_operand, right_operand = node
    if operator == '+':
      return tree(left_operand) + tree(right_operand)
    elif operator == '-':
      return tree(left_operand) - tree(right_operand)
    elif operator == '*':
      return tree(left_operand) * tree(right_operand)
    elif operator == '/':
      return tree(left_operand) / tree(right_operand)

# fungsi pembagian
def div ():
  if type(node) in (int, float):
    return node
  elif type(node) is tuple and len(node) == 3:
    operator, left_operand, right_operand = node
    if operator == '+':
      return tree(left_operand) + tree(right_operand)
    elif operator == '-':
      return tree(left_operand) - tree(right_operand)
    elif operator == '*':
      return tree(left_operand) * tree(right_operand)
    elif operator == '/':
      return tree(left_operand) / tree(right_operand)

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)