'''

Write a program that asks the user for the number of lines for the entered poem. It then allows the user to enter the desired number of lines.
Then output the number of lines, vowels and consonants in the poem and in each line.
For simplicity, let us enter the poem in small English letters only. 
Input example: 
How many lines will there be? 4
Once there was an elephant,
Who tried to use the telephant
No! No! I mean an elephone
Who tried to use the telephone

Example result: 
Number of vowels: 40
Number of consonants: 51

'''

num_of_lines = input('How many lines will there be? ')
poem = ''
for line in range(int(num_of_lines)):
	poem+=input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
num_of_vowels = 0
num_of_consonants = 0
for letter in poem:
	if letter.isalpha():
		if letter.lower() in vowels:
			num_of_vowels += 1
		else:
			num_of_consonants += 1
	
# print(f'Number of vowels: {num_of_vowels} \nNumber of consonants: {num_of_consonants}')

print('Number of vowels:', num_of_vowels, '\nNumber of consonants:', num_of_consonants)

