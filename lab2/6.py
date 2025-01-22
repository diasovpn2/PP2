sdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#updste
sdict["year"] = 2018
#add
sdict["color"] = "red"
#remove
sdict.pop("model")
print(sdict)
#print for
for x in sdict:
  print(sdict[x])
#copy
mydict = sdict.copy()
print(mydict)
#clear
print(sdict.clear())