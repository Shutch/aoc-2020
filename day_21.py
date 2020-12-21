#!/usr/bin/env python
# mypy: ignore-errors
import aoc
import logging

logger = logging.getLogger("Part")


class Part1(aoc.Part):
    @staticmethod
    def logic(inp):
        recipes = []
        all_ingredients = []
        all_allergens = []
        for recipe in inp:
            ingredients, allergens = recipe[:-1].split(" (contains ")
            ingredients = ingredients.split(" ")
            all_ingredients = all_ingredients + ingredients
            allergens = allergens.split(", ")
            all_allergens = all_allergens + allergens
            recipes.append({"ingredients": ingredients, "allergens": allergens})
        all_ingredients = list(set(all_ingredients))
        all_allergens = list(set(all_allergens))
        logger.debug(recipes)
        logger.debug(all_ingredients)
        logger.debug(all_allergens)

        recipes_copy = recipes.copy()
        matching_ingredients = {}
        while len(matching_ingredients) < len(all_allergens):
            for allergen in all_allergens:
                containing_recipes = [
                    set(recipe["ingredients"])
                    for recipe in recipes
                    if allergen in recipe["allergens"]
                ]
                intersecting_ingredients = set.intersection(*containing_recipes)
                if len(intersecting_ingredients) == 1:
                    intersecting_ingredient = list(intersecting_ingredients)[0]
                    logger.debug(f"Match {allergen} with {intersecting_ingredient}")
                    matching_ingredients[allergen] = intersecting_ingredient
                    all_ingredients.remove(intersecting_ingredient)
                    for recipe in recipes:
                        if intersecting_ingredient in recipe["ingredients"]:
                            recipe["ingredients"].remove(intersecting_ingredient)
        logger.debug(f"Matches: {matching_ingredients}")
        logger.debug(f"Remaining ingredients: {all_ingredients}")
        count = 0
        for ingredient in all_ingredients:
            for recipe in recipes_copy:
                if ingredient in recipe["ingredients"]:
                    count += 1

        return count


class Part2(aoc.Part):
    @staticmethod
    def logic(inp):
        recipes = []
        all_ingredients = []
        all_allergens = []
        for recipe in inp:
            ingredients, allergens = recipe[:-1].split(" (contains ")
            ingredients = ingredients.split(" ")
            all_ingredients = all_ingredients + ingredients
            allergens = allergens.split(", ")
            all_allergens = all_allergens + allergens
            recipes.append({"ingredients": ingredients, "allergens": allergens})
        all_ingredients = list(set(all_ingredients))
        all_allergens = list(set(all_allergens))
        logger.debug(recipes)
        logger.debug(all_ingredients)
        logger.debug(all_allergens)

        matching_ingredients = {}
        while len(matching_ingredients) < len(all_allergens):
            for allergen in all_allergens:
                containing_recipes = [
                    set(recipe["ingredients"])
                    for recipe in recipes
                    if allergen in recipe["allergens"]
                ]
                intersecting_ingredients = set.intersection(*containing_recipes)
                if len(intersecting_ingredients) == 1:
                    intersecting_ingredient = list(intersecting_ingredients)[0]
                    logger.debug(f"Match {allergen} with {intersecting_ingredient}")
                    matching_ingredients[allergen] = intersecting_ingredient
                    all_ingredients.remove(intersecting_ingredient)
                    for recipe in recipes:
                        if intersecting_ingredient in recipe["ingredients"]:
                            recipe["ingredients"].remove(intersecting_ingredient)
        logger.debug(f"Matches: {matching_ingredients}")
        logger.debug(f"Remaining ingredients: {all_ingredients}")

        matching_ingredients = dict(sorted(matching_ingredients.items()))
        allergen_ingredients = list(matching_ingredients.values())
        allergen_string = ",".join(allergen_ingredients)

        return allergen_string


if __name__ == "__main__":
    day_number = 21
    test_input = [
        "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
        "trh fvjkl sbzzf mxmxvkd (contains dairy)",
        "sqjhc fvjkl (contains soy)",
        "sqjhc mxmxvkd sbzzf (contains fish)",
    ]

    part_1 = Part1(
        day_number=day_number,
        part=1,
        test_input=test_input,
        test_answer=5,
    )
    part_1.submit_answer()

    part_2 = Part2(
        day_number=day_number,
        part=2,
        test_input=test_input,
        test_answer="mxmxvkd,sqjhc,fvjkl",
    )
    part_2.submit_answer()
