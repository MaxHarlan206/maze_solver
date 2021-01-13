import time 

maze = [
          [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
          [" ","X","X","X","X"," ","X"," ","X"," ","X","X"," ","X"," "],
          [" "," "," "," "," "," "," "," ","X"," ","X","X"," ","X"," "],
          [" ","X","X"," ","X"," ","X"," "," "," "," ","X"," ","X"," "],
          [" "," ","X"," ","X","X","X"," ","X","X"," ","X"," ","X","X"],
          [" ","X","X"," "," "," "," "," "," "," "," ","X"," "," "," "],
          [" "," ","X"," ","X"," ","X","X","X","X","X","X"," ","X"," "],
          [" "," "," ","X"," "," "," "," "," "," "," ","X"," ","X"," "],
          [" "," "," "," "," "," ","X"," ","X","X"," ","X","X"," "," "],
          [" ","X","X"," ","X","X"," ","X","X","X"," "," "," "," "," "],
          [" "," "," "," "," "," "," "," "," ","X"," ","X","X","X","X"],
          [" "," ","X","X","X","X"," ","X"," ","X"," "," "," "," "," "],
          [" "," "," "," "," ","X"," "," ","X","X","X","X","X","X"," "],
          [" ","X","X","X"," "," ","X"," "," "," "," "," ","X"," ","X"],
          [" "," "," "," "," "," "," "," ","X"," ","X"," "," "," ","H"],

]

def print_maze(maze, pos_row, pos_col):
	"""Creates a copy of the maze with an R added to the appropriate cell (to indicate the location of our robot in the maze
	also leaves a trail of .'s to show where the robot has already been)"""
	mazetemp = maze.copy()
	mazetemp[pos_row][pos_col] = "R"
	print("------------------------------")
	for row in mazetemp:
		rowstr = ""
		for item in row:
		  rowstr += f"{item}|"
		print(rowstr)
	print("------------------------------\n\n\n")
	mazetemp[pos_row][pos_col] = "."

def solve_maze(maze):
	""" Shows users a visualization of the maze of their choice + an instructioni list to solve it"""
	rows = len(maze)
	cols = len(maze[0])
	_maze_helper(maze, [], rows, cols)

	# maze_instructions = "How to finish this maze: "
	for item in(_maze_helper(maze, [], 0,0)):
		pass
		# maze_instructions += f"{item},"
	# print(maze_instructions)

def _maze_helper(maze, sol, pos_row, pos_col): 
	#get size of maze 
	num_rows = len(maze)
	num_cols = len(maze[0])
	
	#BASE CASES 
	#1 robot is already home
	if pos_row == num_rows-1 and pos_col == num_cols-1:
		print_maze(maze, pos_row, pos_col)
		return sol
	#2 robot out of bounds 
	if pos_row >= num_rows or pos_col >= num_cols:
		return None
	#3 robot at square with val x
	if maze[pos_row][pos_col] == "X":
		return None 
	#4 the robot has already tried this section of the maze
	if maze[pos_row][pos_col] == ".":
		return None 

	#print the maze at each recursive step
	print_maze(maze, pos_row, pos_col)
	time.sleep(.1)

	#RECURSIVE CASE
	#try going right 
	sol.append("r")
	sol_going_right = _maze_helper(maze, sol, pos_row, pos_col +1)
	if sol_going_right is not None:
		return sol_going_right

	# if going right doesn't work, backtrack, remove the r, try going down 
	sol.pop()
	sol.append("d")
	sol_going_down = _maze_helper(maze, sol, pos_row +1, pos_col)
	if sol_going_down is not None:
		return sol_going_down

	# no solution, impossible, so backtrack 
	sol.pop()

solve_maze(maze)