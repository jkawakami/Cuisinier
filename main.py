# -*- coding: utf-8 -*-

import json
import logging

from Cuisinier import Recipe
from Cuisinier import ClassifiedRecipe
from Cuisinier import Cuisinier

LOGGING_LEVEL = logging.INFO
TRAINING_FILE = "resources/train.json"
TEST_FILE = "resources/test.json"

# Configure logging
logging.basicConfig(filename="log.txt", filemode="w", level=LOGGING_LEVEL)


def getClassifiedRecipes(file):
    f = open(file)
    recipes = json.loads(f.read())
    f.close()
    return [ClassifiedRecipe(recipe["id"], recipe["cuisine"],
                             recipe["ingredients"])
            for recipe in recipes]


def getRecipes(file):
    f = open(file)
    recipes = json.loads(f.read())
    f.close()
    return [Recipe(recipe["id"], recipe["ingredients"]) for recipe in recipes]


def selfTest():
    # Read and parse JSON data
    recipes = getClassifiedRecipes(TRAINING_FILE)
    cuisinier = Cuisinier()
    cuisinier.addRecipes(recipes)

    success = 0
    for recipe in recipes:
        result = cuisinier.classifyRecipe(Recipe(recipe.id,
                                                 recipe.ingredients))
        if result.cuisine == recipe.cuisine:
            success += 1
        print(str(result.id) + ":\t" + result.cuisine + " / " + recipe.cuisine)

    print("Self-test: " + str(success) + "/" + str(len(recipes)))


def main():
    selfTest()

main()
