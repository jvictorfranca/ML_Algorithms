# A diet is to contain at least 2400 units of vitamins, 1800 units of minerals, and 1200 calories.
# Two foods, Food A and Food B are to be purchased.
# Each unit of Food A provides 50 units of vitamins, 30 units of minerals, and 10 calories.
# Food A costs $2 per unit.
# Each unit of Food B provides 20 units of vitamins, 20 units of minerals, and 40 calories.
# Food B cost $1 per unit. 
# How many units of each food should be purchased to keep costs at a minimum?"

import scipy.optimize as opt 

a = {
    "cost": 2,
    "vitamin": 50,
    "mineral": 30,
    "calories": 10
}

b = {
    "cost": 1,
    "vitamin": 20,
    "mineral": 20,
    "calories": 40
}

diet = {
    "vitamin": 2400,
    "mineral": 1800,
    "calories": 1200
}


def least_vitamins (params):
    amount_a = params[0]
    amount_b = params[1]

    return (amount_a*a["vitamin"] + amount_b*b["vitamin"]) - diet["vitamin"]

def least_calories (params):
    amount_a = params[0]
    amount_b = params[1]

    return (amount_a*a["calories"] + amount_b*b["calories"]) - diet["calories"]


def least_mineral (params):
    amount_a = params[0]
    amount_b = params[1]

    return (amount_a*a["mineral"] + amount_b*b["mineral"])-diet["mineral"]


def minimize_cost(params):
    amount_a = params[0]
    amount_b = params[1]
    return (amount_a*a["cost"] + amount_b*b["cost"])

minimun = opt.minimize(minimize_cost, (0, 0), constraints=[{"type": "ineq", "fun": least_vitamins}, {"type": "ineq", "fun": least_mineral}, {"type": "ineq", "fun": least_calories}])

print(minimun)