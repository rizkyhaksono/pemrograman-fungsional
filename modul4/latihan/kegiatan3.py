__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

# Percobaan 3
def title_decoration(function):
  def wrapper():
    func = function()
    make_title = func.title()
    print(make_title + " " + "- Data is convert to title case")
    return make_title
  
  return wrapper

def split_string(function):
  def wrapper():
    func = function()
    splitted_string = func.split()
    print(str(splitted_string) + " " + "- Then Data is splitted")
    return splitted_string
  
  return wrapper

@split_string
@title_decoration
def say_hi():
  return 'hello there'

print(say_hi())

