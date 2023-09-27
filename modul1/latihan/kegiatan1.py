__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"


# # Definisikan pohon ekspresi sebagai fungsi
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            # return tree(left_operand) * tree(right_operand)
            return mult(node)
        elif operator == '/':
            # return tree(left_operand) / tree(right_operand)
            return div(node)

# fungsi pengurangan


def minus(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        return minus(left_operand) - minus(right_operand)

# fungsi perkalian


def mult(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        return print((left_operand, operator, right_operand))

# fungsi pembagian


def div(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        return div(left_operand) / div(right_operand)


# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
# expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
