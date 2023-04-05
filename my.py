def cakes(recipe, available):
    default = []
    for r in recipe:
        if r not in available:
            return 0
        else:
             default.append(available[r]/recipe[r])
    return int(min(default))
                
def cakes_better(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))

print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000, "milk": 2000}))