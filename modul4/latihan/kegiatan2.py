__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

# Percobaan 2
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return func.upper()
  
  return wrapper

@uppercase_decorator
def say_hi():
  return 'hello there'

print(say_hi())