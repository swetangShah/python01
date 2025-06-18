marks = {
    "Swetang" : 100,
    "rishi" : 90,
    "printa" :80, 
    0: "swetang"
}


#print(marks.items())

#print(marks.keys())
#print(marks.values())
#marks.update({"swetang" : 78})
#print(marks)

print(marks.get("mansi")) # prints none 
print(marks["mansi"]) #returns error