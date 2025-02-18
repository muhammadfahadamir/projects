thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict.update({"year": 2020})

thisdict["color"] = "red"
print(thisdict)

thisdict.update({"price": "200000"})
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

thisdict.clear()
print(thisdict)

del thisdict
#print(thisdict)