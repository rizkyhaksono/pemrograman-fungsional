__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"


# Percobaan 1
def perkalian(a):
    def dengan(b):
        return a * b

    return dengan


# High Order Function
def return_perkalian_hof():
    kali = perkalian(2)
    result = kali(2)
    print("Result HOF:", result)


return_perkalian_hof()


# Currying
def return_perkalian_currying():
    result = perkalian(2)(2)
    print("Result Currying:", result)


return_perkalian_currying()
