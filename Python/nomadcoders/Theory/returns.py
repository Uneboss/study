# returns
def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

p_result = p_plus(2, 4) # -> variable could not be saved 
r_result = r_plus(2, 4)

print(p_result, r_result)

def plus(a, b):
  return a + b
  print("lololollolollollol") #<- This can't be printed because as soon as python returns, the fuction is finshed  
result = plus(2, 4)
print(result)

# Keyworded Arguments
def plus(a, b):
  return a + b

result = plus(2, 4)
r_result = plus(b=4, a=2)
print(result, r_result)

def say_hello(name, age):
  #return "Hello name you are age years old" <- text (X)
  return f"Hello {name} you are {age} years old"
  #return "Hello " + name + " you are " + age + " years old" <- another way (O)

hello = say_hello("Une", 12)
print(hello)
hello2 = say_hello(age = 12, name = "Une") # No need to remember the order
print(hello2)
