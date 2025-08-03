myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Deeksha": "Friend",
    "Shubham": "Friend",
    "harry": "A Dancer"
}

# Updates the dictionary by adding key value pairs from updateDict
myDict.update(updateDict)
print(myDict)

# prints value associated with key "harry"
print(myDict.get("harry"))
# prints value associated with key "harry"
print(myDict["harry"])

# the difference between .get and [] syntax in Dictionaries?
# Returns none as harry2 is not present in the dictionary
print(myDict.get("harry2"))
# Throws an error as harry2 is not present in the dictionary
# It is not use this method
print(myDict["harry2"])
