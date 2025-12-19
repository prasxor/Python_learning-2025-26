# python json 
# json is a syntax for storing and exchanging data
# JSON is text, written with js object notation 

import json

# converting from json to python 

#some json
x = '{"name" : "prashant", "age": 22, "city": "new york"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary 
print(y["age"])

# converting from python to json

# xx is a python object (dict)
xx = {"name": "prashant",
      "age": 30,
      "gender": "male"}

# convert into json 
yy = json.dumps(xx)

# the result is a json string 
print(yy)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# example for converting a python object containing all the legal data types 
minidictData = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(minidictData))
# indent 
print(json.dumps(minidictData, indent=4))
# separators
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# sort_keys
print(json.dumps(x, indent=4, sort_keys=True))

# python regex 

import re
pattern = "cat"

text = "hello baby cat vat dat rat nat mat sat wat"

resutlt = re.search(pattern, text)
print(resutlt)

# example 
# Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
macthly = re.search("^The.*Spain$", txt)
print(macthly)

