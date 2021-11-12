import sys
cookbook = {
    'sandwich': {"ingredients": ["ham", "bread", "cheese", "tomatoes"],         "course": "lunch",      "cookingTime": 10},
    'cake':     {"ingredients": {"floor", "sugar", "eggs"},                     "course": "dessert",    "cookingTime": 60},
    'salad':    {"ingredients": {"avocado", "arugula", "tomatoes", "spinach"},  "course": "lunch",      "cookingTime": 15},
    }
def printCookbook():
    for name, recipe in cookbook.items():
        print("Recipe for {}".format(name))
        print("Ingredient list {}".format(recipe["ingredients"]))
        print("To be eaten for {}".format(recipe["course"]))
        print("Takes {} minutes of cooking\n".format(recipe["cookingTime"]))

def addRecipe():
    print("What is the name of the recipe you want to add?")
    recipeName = input('>>')
    print("What is the first ingredient of {}?".format(recipeName))
    i = 0
    while True:
        ing = input('>>')
        if ing == "":
           break
        # ing.format(cookbook[recipeName[i]])
        i += 1
        cookbook[recipeName] = ing
        print("{} is added, what is the next ingredient?\nif there is no more ingredients just press ENTER".format(ing))
    printCookbook()
    print("You're doing a great job!\nNow can you please tell me how many minutes are needed to prepare {}?".format(recipeName))
    print("Last question: can you tell me the meal or the course in wich you eat {}?".format(recipeName))


def printRecipe(thing):
    for name, recipe in cookbook.items():
        if name == thing:
            print("Recipe for {}".format(name))
            print("Ingredient list {}".format(recipe["ingredients"]))
            print("To be eaten for {}".format(recipe["course"]))
            print("Takes {} minutes of cooking".format(recipe["cookingTime"]))



def main():
    # for i in cookbook.keys():
        # print(i)
    # for j in cookbook.items():
        # print(j)
    # for k in cookbook.values():
        # print(k['ingredients'])
    
    # print("{}\n".format(cookbook.items()))
    # for name, recipe in cookbook.items():
    #     # print(type(name))
    #     # print(type(recipe))
    #     if name == "sandwich":
    #         print("Recipe for {}".format(name))
    #         print("Ingredient list {}".format(recipe["ingredients"]))
    #         print("To be eaten for {}".format(recipe["course"]))
    #         print("Takes {} minutes of cooking".format(recipe["cookingTime"]))

    print("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
    userChoice = input('>>')
    if userChoice == '1':
        addRecipe()
    elif userChoice == '2':
        deleteRecipe()
    elif userChoice == '3':
        printRecipe(input('>>'))
    elif userChoice == '4':
        printCookbook()
    elif userChoice == '5':
        exit

if __name__ == '__main__':
    main()