# some ideas for psuedo-code

# focus: get comfortable doing the following tasks:
#  1) organizing food varieties (e.g. brands, groups, items) for daily eating. 
#  2) saving meals
#  3) expressing food amounts
#  
# approach: 
#  1) compile a representative list of daily foods and beverages. To simplify matters consider only one nutrient (e.g. calories [kcal]).
#  2) list different ways to group foods (e.g. places to eat)
#  3) list potential code statements


# ==============================================================================
# list of different ways to group foods
# ==============================================================================


# a database can hold all foods
# a more specialized collection of foods can be held in a python module
#  each python module will be based on food_group.brand
#
# food.groups.brands
#
#   group: veggies
#   group: fruits
#   group: grains
#   group: protein
#   group: dairy
#   group: oils
#
#   brand: stater bros.
#   brand: jennie-o
#   brand: heinz
#   brand: planters
#   brand: international delight
#   brand: jack daniel's
#   brand: kikkoman
#   brand: chipotle
#   brand: silk
#   brand: ralph's (papa johns?)
#   brand: grey poupon
#   brand: usda 11529
#   brand: heritage farm
#   brand: ra
#   brand: vlasic
#   brand: hawaiian host
#   brand: so delicious

# group
# -------------
# vegetables
# fruits
# grains
# protein
# dairy
# oils

# group
# -------------
# break room snacks
# restaurants
# store

# group
# -------------
# treat
# snack
# meal

# group
# -------------
# breakfast
# lunch
# dinner
# desert


# ==============================================================================
# daily foods and beverages
# ==============================================================================

# simple name: brocolli
# detailed name: brocolli florets
# portion: 1 bag, 382.5 g
# nutrients: energy 135 kcal
# prep details: cooked frozen brocolli on stove. added seasonings.
# brand: stater bros.

# simple name: olive oil
# detailed name: extra virgin olive oil
# portion: 6 tbsp, ? g (need to measure this)
# nutrients: energy 720 kcal
# prep details: cooked into food on stove
# brand: stater bros.

# simple name: turkey burger
# detailed name: all white meat turkey burgers (93% lean, 7% fat)
# portion: 1 burger, 149 g
# nutrients: energy 200 kcal
# prep details: cooked on stove
# brand: jennie-o

# simple name: ketchup
# detailed name: tomato ketchup 57 varieties
# portion: 8 tbsp, 136 g
# nutrients: energy 160 kcal
# prep details: none
# brand: heinz

# simple name: cashews
# detailed name: salted cashews
# portion: 1 pack, 42 g
# nutrients: energy 240 kcal
# prep details: none
# brand: planters

# simple name: creamer
# detailed name: french vanilla creamer
# portion: 1 creamer, ? g
# nutrients: energy 30 kcal
# prep details: none
# brand: international delight

# simple name: whiskey
# detailed name: tennessee sour mash whiskey (80 proof)
# portion: 2 fl oz, 84 g
# nutrients: energy 130 kcal
# prep details: none
# brand: jack daniel's

# simple name: honey whiskey
# detailed name: tennessee honey liquer blended with jack daniels tennessee whiskey (70 proof)
# portion: 2 fl oz
# nutrients: energy 144 kcal
# prep details: none
# brand: jack daniel's

# simple name: soy sauce
# detailed name: traditionally brewed soy sauce
# portion: 4 tbsp, ? g
# nutrients: energy 40 kcal
# prep details: cooked on stove
# brand: kikkoman

# simple name: chipotle taco
# detailed name: chipotle taco
# portion: 1 taco
# nutrients: energy 290 kcal
# prep details: restaurant served. selected items: soft flour tortilla, sofritas, brown rice, black beans, fajita vegetables, fresh tomato salsa, roasted chili-corn salsa, romaine lettuce
# brand: chipotle

# simple name: chipotle taco
# detailed name: chipotle taco
# portion: 1 taco
# nutrients: energy 286.7 kcal
# prep details: restaurant served. selected items: soft flour tortilla, sofritas, brown rice, black beans, fajita vegetables, tomatillo-green chili salsa, roasted chili-corn salsa, romaine lettuce
# brand: chipotle

# simple name: almond milk
# detailed name: unsweetened almond milk
# portion: 361 g, 361 g
# nutrients: energy ? kcal
# prep details: none
# brand: silk

# simple name: almond milk
# detailed name: unsweetened almond milk
# portion: 400 mL, ? g
# nutrients: energy 50 kcal
# prep details: none
# brand: silk

# simple name: edamame caviar salad
# detailed name: edamame caviar salad
# portion: 1 cup, ? g
# nutrients: energy 220? kcal
# prep details: none
# brand: ralph's (papa johns?)

# simple name: edamame caviar salad
# detailed name: edamame caviar salad
# portion: 182 g, 182 g
# nutrients: energy ? kcal
# prep details: none
# brand: ralph's (papa johns?)

# simple name: dijon mustard
# detailed name: dijon mustard made with white wine
# portion: 3 tbsp, 15 g
# nutrients: energy 15 kcal
# prep details: none
# brand: grey poupon

# simple name: tomatoe
# detailed name: Tomatoes, red, ripe, raw, year round average
# portion: 1 full, 344 g
# nutrients: energy 61.92 kcal
# prep details: none
# brand: usda 11529

# simple name: turkey slices
# detailed name: white turkey cured slices
# portion: 3 slices, 84 g
# nutrients: energy 105 kcal
# prep details: none
# brand: heritage farm

# simple name: sandwich sprouts
# detailed name: nano-shoots bold brocolli
# portion: 0.75 oz, 21.25 g
# nutrients: energy 8.75 kcal
# prep details: none
# brand: ra

# simple name: pickle sandwich slices
# detailed name: stackers kosher dill pickles
# portion: 5 slices, 70 g
# nutrients: energy 0 kcal
# prep details: none
# brand: vlasic

# simple name: chocolate
# detailed name: selected whole and halves chocolate covered macadamia nuts
# portion: 1 piecce, 14 g
# nutrients: energy 86.7 kcal
# prep details: none
# brand: hawaiian host

# simple name: yogurt
# detailed name: dairy free coconut milk yogurt alternative strawberry
# portion: 1 container
# nutrients: energy 120 kcal
# prep details: none
# brand: so delicious

# simple name: soup
# detailed name: grilled chicken & sausage gumbo chunky soup
# portion: 1 container, 
# nutrients: energy 310 kcal
# prep details: cooked on stove
# brand: campbell's

# simple name: ...
# detailed name: ...
# portion: ...
# nutrients: ...
# prep details: ...
# brand: ...

# simple name: ...
# detailed name: ...
# portion: ...
# nutrients: ...
# prep details: ...
# brand: ...

# simple name: ...
# detailed name: ...
# portion: ...
# nutrients: ...
# prep details: ...
# brand: ...

# simple name: ...
# detailed name: ...
# portion: ...
# nutrients: ...
# prep details: ...
# brand: ...

# simple name: ...
# detailed name: ...
# portion: ...
# nutrients: ...
# prep details: ...
# brand: ...

# simple name: ...
# detailed name: ...
# portion: ...
# nutrients: ...
# prep details: ...
# brand: ...

# k-cups

# ==============================================================================
# notes from USDA database user's guide
# ==============================================================================


# Info from the USDA (United States Department of Agriculture) National Nutrient Database for Standard Reference
# 
# NDB 09003 Apples, raw, with skin
# 
# NDB 01129 Egg, whole, cooked, hard-boiled
# 
# NDB 21237 McDONALD'S, BIG MAC
# 
# NDB 21275, PIZZA HUT 12" Pepperoni Pizza, Pan Crust



# Water
# Unit: g

# Energy
# Unit: kcal

# Protein
# Unit: g

# Total lipid (fat)
# Unit: g

# Carbohydrate (by difference)
# Unit: g

# Fiber (total dietary)
# Unit: g

# Sugars
# Unit: g


# Minerals
# Mineral: Calcium (Ca), Iron (Fe), Magnesium (Mg), Phosphorus (P), Potassium (K), Sodium (Na), Zinc (Zn)
# Unit: mg

# Vitamins
# Vitamin: Vitamin C, Thiamin, Riboflavin, Niacin, Vitamin B-6, Folate, Vitamin B-12, Vitamin A (RAE), Vitamin A (IU), Vitamin E (alpha-tocopherol), Vitamin D (D2 + D3), Vitamin D (IU), Vitamin K (phylloquinone)
# Unit: mg, microg

# Lipids
# Lipid: Fatty acids, total saturated; Fatty acids, total monounsaturated; Fatty acids, total polyunsaturated; Fatty acids, total trans; Cholesterol
# Unit: g, mg


# Caffeine
# Unit: mg 


# Amounts
# # Value Per # g
# # item # oz # g
# # pizza # g
# # slice # g
# # cup, chopped # g
# # cup, quartered or chopped # g
# # cup slices # g
# # tbsp # g
# # large # g
# # large (3-1/4" dia) # g
# # medium (3" dia) # g
# # small (2-3/4" dia) # g
# # extra small (2-1/2" dia) # g
# # NLEA serving # g

