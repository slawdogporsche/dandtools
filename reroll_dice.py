from random import randint

def dice_function(number_of_dice, dice_sides, reroll):
	dice_list = []
	for i in range(number_of_dice):
		dice_list.append(randint(1,dice_sides))
	if reroll == ('Yes' or 'yes'):
		print("Your initial rolls are:")
		print(dice_list)
		print("Your final rolls are")
		print([randint(1,dice_sides) if (x > 0 and x < 3) else x for x in dice_list ])

			

dice_input = int(input("How many dice are you rolling?"))
dice_sides = int(input("How many sides do the dice have?"))
reroll_1_2 = input("Do you want to reroll 1s and 2s?")

dice_function(dice_input,dice_sides,reroll_1_2)