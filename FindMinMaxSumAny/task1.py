def rsum(row):
	return sum(row)


if __name__ == '__main__':
	
	t_cases = int(input())
	# print('Test Cases->',t_cases)

	for t in range(t_cases):
		cur_max = 0
		cur_min = 0
		blank_line = input()
		# print('Line read->',blank_line)
		order = int(input())
		# print('order->',order)
		matrix = []
		columns = []
		right_diag_sum = 0
		left_diag_sum = 0
		for _ in range(order):
			row = list(map(int,input().split()))
			if len(columns) == 0: # columns not yet set or first row just considered
				cur_max = rsum(row)
				cur_min = cur_max
				columns = [[matrix_integer] for matrix_integer in row]
			else:
				for i in range(len(columns)):
					columns[i].append(row[i])
			row_sum = rsum(row)
			if row_sum >= cur_max:
				cur_max = row_sum
			if row_sum <= cur_min:
				cur_min = row_sum 
			matrix.append(row)
		#Calculating Max Column sum
		for col in columns:
			col_sum = rsum(col)
			if col_sum >= cur_max:
				cur_max = col_sum
			if col_sum <= cur_min:
				cur_min = col_sum 		

		#Right & Left Diagonal Sum
		start = 0
		end = order - 1
		for row in matrix:
			right_diag_sum += row[start]
			left_diag_sum += row[end]
			start += 1
			end -= 1

		if right_diag_sum >= cur_max:
			cur_max = right_diag_sum

		if right_diag_sum <= cur_min:
			cur_min = right_diag_sum

		if left_diag_sum >=cur_max:
			cur_max = left_diag_sum

		if left_diag_sum <=cur_min:
			cur_min = left_diag_sum

		print('Case #{num}:'.format(num=t+1),cur_max,cur_min)





