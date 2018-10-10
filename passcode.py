dic = { 1: [[4,7], [2,3], [5,9]],
	2: [[5,8]],
	3: [[2,1],[6,9], [5,7]],
	4: [[5,6]],
	5: [],
	6: [[5,4]],
	7: [[4,1], [5,3],[8,9]],
	8: [[5,2]],
	9: [[5,1], [8,7], [6,3]],
}
def count(init, length, occupied_dots):
	#Cross off the initial dot.
	occupied_dots.add(init)		

	## Calculate possible next dots.
	# Start from all dots.
	dots = set(range(1,10))

	# Discard elements by consulting the dictionary and current occupied list.
	for el in dic[init]:
		if not occupied_dots.__contains__(el[0]):	
			dots.discard(el[1])			
							
	# Remove all occupied dots.
	dots = dots.difference(occupied_dots)			

	# Base case	
	if length == 1:
		return len(dots)
	# Non-base cases
	cnt = 0
	for dot in dots:
		cnt = cnt + count(dot, length-1, occupied_dots.copy())
	return cnt

def countFromUpto(minn, maxx):
	cnt = 0
	for l in range(minn,maxx+1):
		cnt += 4*count(1, l, set([])) + 4*count(2, l, set([])) + count(5, l, set([]))

	return cnt


def count2(init, min_len, max_len, occupied_dots):
	
	#Cross off the initial dot.
	occupied_dots.add(init)		

	## Calculate possible next dots.
	# Start from all dots.
	dots = set(range(1,10))

	# Discard elements by consulting the dictionary and current occupied list.
	for el in dic[init]:
		if not occupied_dots.__contains__(el[0]):	
			dots.discard(el[1])			
							
	# Remove all occupied dots.
	dots = dots.difference(occupied_dots)			

	# Base case	
	if max_len == 1:
		return len(dots)

	cnt = 0
	for dot in dots:
		cnt = cnt + count2(dot, min_len-1, max_len-1, occupied_dots.copy())

	# Add the number of possible entry at every recurssion stage
	# provided min_len constraint
	if min_len <= 1:
		cnt = cnt + len(dots)
	return cnt


# Enumerate all patterns consisting of more than 4 dots (3 segments)
# For count
print("Method1", countFromUpto(3, 8))

# For count2
ans = 4*count2(1,3, 8, set([])) + 4*count2(4, 3, 8, set([])) + count2(5, 3, 8, set([]))
print("Method2", ans)	


"""
### TEST
def soln2():
	return 4*count2(1,3, 8, set([])) + 4*count2(4, 3, 8, set([])) + count2(5, 3, 8, set([]))

import timeit
print(timeit.timeit("countFromUpto(3, 8)", setup="from __main__ import countFromUpto", number=100))
print(timeit.timeit("soln2()", setup="from __main__ import soln2", number=100))	
"""
