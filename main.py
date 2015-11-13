# -*- coding: utf-8 -*-

import logging
import Cuisinier

# Configure logging
LOGGING_LEVEL = logging.INFO
logging.basicConfig(filename="log.txt", filemode="w", level=LOGGING_LEVEL)

cuisinier = Cuisinier.Cuisinier()
cuisinier.addFile("resources/train.json")
for recipe in cuisinier.classifyFile("resources/test.json"):
    print(str(recipe.id) + ":\t" + recipe.cuisine)
