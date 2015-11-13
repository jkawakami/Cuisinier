# -*- coding: utf-8 -*-

import json
import logging
from collections import namedtuple

Recipe = namedtuple("ClassifiedRecipe", "id, ingredients")
ClassifiedRecipe = namedtuple("ClassifiedRecipe", "id, cuisine, ingredients")

"""
Uses ingredients to categorize the cuisine of a recipe.
@author: Alan Kha
"""


class Cuisinier:
    def __init__(self):
        self.recipes = {}  # <id, Recipe>
        self.cuisineMatrix = {}  # <cuisine, <ingredient, frequency>>
        self.ingredientMatrix = {}  # <ingredient, <cuisine, frequency>>
        self.ingredientHistogram = {}  # <ingredient, global frequency>

    """
    Adds a ClassifiedRecipe to the knowledge base.
    @param  recipe  ClassifiedRecipe Recipe to be added
    @return         True if successful, false otherwise
    """
    def add(self, recipe: ClassifiedRecipe):
        if not isinstance(recipe, ClassifiedRecipe):
            raise TypeError("Cuisinier.add() takes a ClassifiedRecipe")

        # Add new recipes to knowledge base
        if recipe.id not in self.recipes:
            self.recipes[recipe.id] = recipe
            if recipe.cuisine not in self.cuisineMatrix:
                self.cuisineMatrix[recipe.cuisine] = {}

            # Iterate through ingredients
            for ingredient in recipe.ingredients:
                # Add to cuisine matrix
                if ingredient not in self.cuisineMatrix[recipe.cuisine]:
                    self.cuisineMatrix[recipe.cuisine][ingredient] = 0
                self.cuisineMatrix[recipe.cuisine][ingredient] += 1

                # Add to ingredient matrix
                if ingredient not in self.ingredientMatrix:
                    self.ingredientMatrix[ingredient] = {}
                if recipe.cuisine not in self.ingredientMatrix[ingredient]:
                    self.ingredientMatrix[recipe.cuisine] = 0
                self.ingredientMatrix[recipe.cuisine] += 1

                # Add to global ingredient histogram
                if ingredient not in self.ingredientHistogram:
                    self.ingredientHistogram[ingredient] = 0
                self.ingredientHistogram[ingredient] += 1

            # Return true if successful
            logging.info("Add recipe " + str(recipe.id) + ":\tSUCCESS")
            return True

        logging.info("Add recipe " + str(recipe.id) + ":\tFAIL")
        return False

    """
    Add ClassfiedRecipes from a training JSON file.
    @param  file    Training JSON filepath
    """
    def addFile(self, file):
        # Read and parse JSON data
        recipes = json.loads(open(file).read())

        # Iterate through recipes
        success = 0
        for recipe in recipes:
            if (self.add(ClassifiedRecipe(recipe["id"], recipe["cuisine"],
                                          recipe["ingredients"]))):
                success += 1

        logging.info(file + ": " + str(success) + "/" +
                     str(len(recipes)) + " successful")

    """
    Classifies a given Recipe.
    @param  recipe  Recipe to be classified
    @return         ClassfiedRecipe
    """
    def classify(self, recipe: Recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("Cuisinier.classify() takes a Recipe")

        # TODO Perform classification
        return ClassifiedRecipe(recipe.id, "unknown", recipe.ingredients)

    """
    Classifies the recipes from a JSON file.
    @param  file    Unclassified recipe JSON filepath
    @return         Array of ClassfiedRecipes
    """
    def classifyFile(self, file):
        # Read and parse JSON data
        recipes = json.loads(open(file).read())

        # Iterate through recipes
        return [self.classify(Recipe(recipe["id"], recipe["ingredients"]))
                for recipe in recipes]
