Tuples_immutable sequence / Dictionary
days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))
print(days)

name = "Une"
age = 21
Korean = False
fav_food = ["Kimchi", "Bibimbob"]
# -> just variables
# Use dictionary
une = {
  "name": "Une",
  "age": 21,
  "Korean": False,
  "fav_food": ["Kimchi", "Bibimbob"]
}
print(une)
print(une["age"])
une["handsome"] = True
print(une)

une["fav_food"].append("Chocolate")
print(une["fav_food"])
