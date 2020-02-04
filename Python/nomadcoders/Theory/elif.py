# if else ( == elif)
def age_check(age):
  print(f"you are {age}")
# use braces on variables
  if age < 18:
    print("You can't drink")
  elif age == 18 or age == 19:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print(" you are still kind of young")
  else:
    print("enjoy your drink")
age_check(19)
