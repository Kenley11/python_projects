from tabulate import tabulate
all_items_data = []

print('\nWelcome to the Nutrition Facts Calculator!\n')

while True:
    item = input('Name your item: \n').title()
    print('\nIs this a standalone item with pre-calculated nutrition facts?')
    standalone = input("\n[1] Yes, a standalone item (e.g., a bottle of Muscle Milk Protein) [2] No, calculate nutrition facts separately.\n")

    if standalone == '1':
        ingredient_calories =float(input('Enter calories per serving: \n'))
        ingredient_protein =float(input('Enter protein per serving: \n'))
        ingredient_carbs =float(input('Enter carbs per serving: \n'))
        ingredient_fat = float(input('Enter fat per serving: \n'))

        # print(f'\nNutrition facts for {item} are:\n ')
        # print(f'Total Calories: {ingredient_calories}')
        # print(f'Total Protein: {ingredient_protein}g')
        # print(f'Total Carbs: {ingredient_carbs}g')
        # print(f'Total Fat: {ingredient_fat}g\n')

        item_data = {
            'Item': item,
            'Calories': ingredient_calories,
            'Protein (g)': ingredient_protein,
            'Carbs (g)': ingredient_carbs,
            'Fat (g)': ingredient_fat
        }

        all_items_data.append(item_data)

    elif standalone == '2':
        while True:
            print('\nHow would you like to enter the quantities?')
            unit_type = input('[1] Slices (e.g., bread, cheese) [2] Normal units (e.g., grams, mL)\n')
            if unit_type == '1':
                ingredient_calories =float(input('Enter calories per serving: \n'))
                ingredient_serving_size =float(input('Enter serving size in slices : \n'))
                ingredient_protein =float(input('Enter protein per slice: \n'))
                ingredient_carbs =float(input('Enter carbs per slice: \n'))
                ingredient_fat = float(input('Enter fat per slice: \n'))
                desired_serving_size =float(input('Enter desired slices: \n'))
                break
                
            elif unit_type == '2':
                ingredient_calories =float(input('Enter calories per serving: \n'))
                ingredient_serving_size =float(input('Enter serving size: [g][mL][tsp][tbspn]\n'))
                ingredient_protein =float(input('Enter protein per serving: \n'))
                ingredient_carbs =float(input('Enter carbs per serving: \n'))
                ingredient_fat = float(input('Enter fat per serving: \n'))
                desired_serving_size =float(input('Enter desired serving size: \n'))
                break

            else:
                print('Invalid response. Try again.')
                unit_type = input('[1] Slices (e.g., bread, cheese) [2] Normal units (e.g., grams, mL)\n')

        #Calculating calories per serving
        desired_calories = round((desired_serving_size * ingredient_calories) / (ingredient_serving_size))

        #Calculating protein per serving
        desired_protein = round((desired_serving_size * ingredient_protein) / (ingredient_serving_size))

        #Calculating carbs per serving
        desired_carbs = round((desired_serving_size * ingredient_carbs) / (ingredient_serving_size))

        #Calculating fat per serving
        desired_fat = round((desired_serving_size * ingredient_fat) / (ingredient_serving_size))

        # print(f'\nNutrition facts for {item} are:\n ')
        # print(f'Total Calories: {desired_calories}')
        # print(f'Total Protein: {desired_protein}g')
        # print(f'Total Carbs: {desired_carbs}g')
        # print(f'Total Fat: {desired_fat}g\n')

        item_data = {
            'Item': item,
            'Calories': desired_calories,
            'Protein (g)': desired_protein,
            'Carbs (g)': desired_carbs,
            'Fat (g)': desired_fat
        }

        all_items_data.append(item_data)

    more_items = input('Do you have more items to enter?: [y][n]\n').lower()
    if more_items == 'y':
        continue
    else:
        break

total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0

for item_data in all_items_data:
    total_calories += item_data['Calories']
    total_protein += item_data['Protein (g)']
    total_carbs += item_data['Carbs (g)']
    total_fat += item_data['Fat (g)']

total_row ={
    'Item': 'Total',
    'Calories': total_calories,
    'Protein (g)': total_protein,
    'Carbs (g)': total_carbs,
    'Fat (g)': total_fat
}

all_items_data.append(total_row)

print('\nSummary of Nutrition Facts:\n')
print(tabulate(all_items_data, headers='keys', tablefmt='grid'))