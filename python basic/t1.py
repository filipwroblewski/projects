'''

A list of integers is given. 
It is required to "shrink" it by moving all non-zero elements to the left side of the list 
without changing their order, and all zeros to the right side. 
The order of the non-zero elements cannot be changed, an additional list cannot be used, 
and the task must be completed in one pass through the list. Print the resulting list.
Example input data:
4 0 5 0 3 0 0 5 

Example result: 

4 5 3 5 0 0 0 0

Important. The isalpha operator may not work on the platform. If you use it in your solution, write it in the code comments :)
'''

list_of_integers = [4, 0, 5, 0, 3, 0, 0, 5]
for elem in list_of_integers:
	if elem == 0:
		list_of_integers.remove(elem)
		list_of_integers.append(0)
print(list_of_integers)