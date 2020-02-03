# very simple calculator
def check(a, b=0):
  if(type(a) is str or type(b) is str):
    return False
  else:
    return True

def plus(a, b):
  if (check(a, b)):
    return a + b
  else:
    print("Please input number")

def substract(a, b):
  if (check(a, b)):
    return a - b
  else:
    print("Please input number")

def multiple(a, b):
  if check(a, b):
    return a * b
  else:
    print("Please input number")

def division(a, b):
  if check(a, b):
    if b == 0:
      print("Can't divide with zero")
    else:
      return a / b
  else:
    print("Please input number")

def remainder(a, b):
  if check(a, b):
    return a % b
  else:
    print("Please input number")

def negation(a):
  if check(a):
    return -a
  else:
    print("Please input number")

def power(a, b):
  if check(a, b):
    return a ** b
  else:
    print("Please input number")

s_result = substract(22, 1)
print(s_result)

d_result = division(20, 5)
print(d_result)

d_result2 = division(20, 0)
print(d_result2)

p_result = power(2, 3)
print(p_result)

n_result = negation(165)
print(n_result)

m_result = multiple(3, 2)
print(m_result)

r_result = remainder(9,2)
print(r_result)

pl_result = plus(10,"22")
print(pl_result)
