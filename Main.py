# List
game = ["Games", "Video Games", "Board Games"]
# Variable name is game
print(game)

print(game[2])

# New Game has been added it is called Mental Games
game.append("Mental Games")
print(game)

game.append("Physical Games")
print(game)

#Tuple
student1 = ("Jimit", 13, 7, "uttappam")
print(student1)
print("my fav. food is", student1[3])
print("my name is", student1[0])
print("my age is", student1[1])

#Dictionary
student = {"name": "jimit", "age": 13, "grade": 7, "food": "uttappam"}
print("Dictionary")
print(student["name"])
print(student["age"])
print(student["grade"])
print(student["food"])

student["country"]= "U.S and India"
print(student)

student["food"]= "biryani"
print(student)
del student["age"]
print(student)