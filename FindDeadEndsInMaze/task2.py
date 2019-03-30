pathToCheck = [] #List of tuple matrix indice pairs
dead_ends = 0

def check(r,c,h,w):
	# print('r->',r,'c->',c,'h->',h,'w->',w)
	if r in range(h) and c in range(w):
		# print('r is in{a} and c is in {b}'.format(a=range(h),b=range(w)))
		return True
	# print('False')
	return False

def deadEndCheck(cr,cc):
	global dead_ends
	hash_count = 0
	try:
		if maze[cr][cc-1] == '#':
			hash_count +=1
	except: pass
	try:
		if maze[cr][cc+1] == '#':
			hash_count +=1
	except: pass
	try:
		if maze[cr+1][cc] == '#':
			hash_count +=1
	except: pass
	try:
		if maze[cr-1][cc] == '#':
			hash_count +=1
	except: pass

	if hash_count == 3:
		dead_ends += 1
		return True
	return False
	


def search(maze,cr,cc,h,w):
	global pathToCheck
	if deadEndCheck(cr,cc):
		# print('DeadCount After DC...Returning->',dead_ends)
		return
	else:
		# print('Path Checks Started')
		
		# print('Checking Up...')
		try:
			if maze[cur_row-1][cur_col]=='.' and ((cur_row-1,cur_col) not in pathToCheck) and check(cur_row-1,cur_col,h,w):
				pathToCheck.append((cur_row-1,cur_col))
				# print('Up . found')
				# print('Path to Check is now->',pathToCheck)
			# else: print('No Up available/Up already exists')
		except: pass

		# print('Checking Left...')
		try:
			if maze[cur_row][cur_col-1]=='.' and ((cur_row,cur_col-1) not in pathToCheck) and check(cur_row,cur_col-1,h,w):
				pathToCheck.append((cur_row,cur_col-1))
				# print('Left . found')
				# print('Path to Check is now->',pathToCheck)
			# else: print('No Left available/Left already exists')
		except: pass
		# print('Checking Right...')
		try:
			if maze[cur_row][cur_col+1]=='.' and ((cur_row,cur_col+1) not in pathToCheck) and check(cur_row,cur_col+1,h,w):
				pathToCheck.append((cur_row,cur_col+1))
				# print('Right . found')
				# print('Path to Check is now->',pathToCheck)
			# else: print('No Right available/Right already exists')
		except: pass 
		# print('Checking Down...')
		try:
			if maze[cur_row+1][cur_col]=='.' and ((cur_row+1,cur_col) not in pathToCheck) and check(cur_row+1,cur_col,h,w):
				pathToCheck.append((cur_row+1,cur_col))
				# print('Down . found')
				# print('Path to Check is now->',pathToCheck)
			# else: print('No Down available/Down already exists')
		except: pass
	


if __name__ == '__main__':
	
	t_cases = int(input())
	# print('Test Cases->',t_cases)

	for t in range(t_cases):
		
		blank_line = input()
		# print('Line read->',blank_line)
		order = list(map(int,input().split()))
		height = order[0]
		width = order[1]
		# print('order->',order)
		maze = []
		pathToCheck = []
		dead_ends = 0
		for _ in range(height):
			row = [c for c in input()]
			maze.append(row)

		# print('Maze is ->\n')
		# for row in maze: print(''.join(row))
		cur_row = 0
		cur_col = 1


		if maze[cur_row][cur_col-1]=='.': pathToCheck.append((cur_row,cur_col-1))
		if maze[cur_row][cur_col+1]=='.': pathToCheck.append((cur_row,cur_col+1))
		pathToCheck.append((cur_row+1,cur_col)) #Guaranteed dot
		# print('Initial Path to Check->',pathToCheck)
		point_considered = 0
		while(point_considered <  len(pathToCheck)):
			cur_row = pathToCheck[point_considered][0]
			cur_col = pathToCheck[point_considered][1]
			# print('Consider:({a},{b})->{c}'.format(a=cur_row,b=cur_col,c=maze[cur_row][cur_col]))
			search(maze,cur_row,cur_col,height,width)
			point_considered += 1

		print('Case #{num}:'.format(num=t+1),dead_ends)
		





