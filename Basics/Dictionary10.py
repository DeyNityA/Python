st1 = {
    "name" : "Nitya Dey",
    "age" : 24,
    "skin" : "Grey"

}

print(st1)
print(type(st1))

print(st1["name"])
print(st1.get("name"))

print(st1.get("ji"))
#print(st1["ji"]) # will give key error

st1["name"] = "ullu"
st1["sex"] = "Male" #add/update

st1.update({"age" : 80, "name" : "kop", "height" : 6.8}) # add/update

print(st1)

del st1["height"]

print(st1)

st1.pop("age")
print(st1)

st1.popitem()
print(st1)

#iterator

keys = st1.keys()
print(type(keys))
for i in keys :
    print(i)

values = st1.values()
print(type(values))
for j in values :
    print(j)

items = st1.items()
print(type(items))

for e in items :
    print(type(e),e)

for k,v in items :
    print(f"{k} -> {v}")