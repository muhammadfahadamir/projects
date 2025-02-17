thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(len(thisdict))
print(type(thisdict))

thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)

x = thisdict["colors"]

y = thisdict.get("electric")

z = thisdict.keys()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


n = car.values()
print(n)


m = thisdict.items()


if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")