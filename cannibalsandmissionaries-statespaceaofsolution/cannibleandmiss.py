
maxno = 3 #defined the maximum no of missionary or cannible that can exit

boatsize = 2#defined the max no of character a boat can carry


def equals(state1, state2):#when two states are same then are detected. For detecting the states can will create loop

	return state1[0] == state2[0] and state1[1] == state2[1] and state1[2] == state2[2] and state1[3] == state2[3] and state1[4] == state2[4]


def valid(state):#checking the condition of the game. Ignore the state space violating the condition

	
	if state[0] < 0 or state[1] < 0 or state[2] < 0 or state[3] < 0:
		return False

	
	if state[0] > maxno or state[1] > maxno or state[2] > maxno or state[3] > maxno:
		return False

   
	if state[1] > state[0] > 0:
		return False

	
	if state[3] > state[2] > 0:
		return False

	return True


def numberinshore(cstate, missionary, canibals, pile):#calculation of the no of the missionary and cannibals left after the transportation


	boat_multiplier = 1 if cstate[4] == 'R' else -1

	
	next_boat_side = 'L' if cstate[4] == 'R' else 'R'

   
	next_missionary_number = cstate[0] + missionary * boat_multiplier
	next_canibal_number = cstate[1] + canibals * boat_multiplier
	#calculation of the new space that can occur in the process
	new_state = [next_missionary_number, next_canibal_number, maxno - next_missionary_number,
				 maxno - next_canibal_number, next_boat_side,
				 cstate[5] + 1,  cstate]

	addifvalid(new_state, pile)#checking the validity of the new_state thus created


def charactervalue(cstate, pile):# checking the condition for the boat limit and initating the transportation for creating new state space

	canibals = 0
	missionary = 0
	state_name = 1

	for i in range(3):
		for j in range(3):

			if i == 0 and j == 0:
				continue

			if i + j > boatsize:
				break

			missionary = i
			canibals = j
			state_name = state_name + 1

			numberinshore(cstate, missionary, canibals, pile)


def addifvalid(state, pile):# adds the new state into pile if it satisfies the condition of the game

	if not valid(state):
		return

	pile.append(state)


def solve(i_state, g_stare):# For the traversal and finding the possible solution


	bestsolution = 0
	finish = False
	first_solution = False

	solutionspace = []# stores all the possible solution space

	searchspace = []# stores the searched state to detected the repetation

	addifvalid(i_state, searchspace)

	while len(searchspace) > 0 and not finish:

		current_state = searchspace.pop(0)

		if equals(current_state, g_stare):
			if first_solution:
				if current_state[5] <= bestsolution:

					solutionspace.append(current_state)

				else:
					finish = True
			else:

				first_solution = True
				bestsolution = current_state[5]
				solutionspace.append(current_state)

		else:

			charactervalue(current_state, searchspace)

	return solutionspace# all the solution possible for the game


def printstate(state):# breakes the solutionspace which is 2d list into the smaller form and prints the results
	list_left = []
	list_right = []

	while not len(state) == 0:
		boat_side = "Left" if state[4] == 'L' else "right"
		list_left.append("M" + str(state[0]) + " and C" + str(state[1]))
		list_right.append("M" + str(state[2]) + " and C" + str(state[3]))

		state = state[6]
		

	list_left.reverse()

	list_right.reverse()

	print("Left shore"+"   "+"Right shore")
	for i in range(len(list_left)):
		print (list_left[i]+"    "+ list_right[i])

def treeimplement(state):# representation of the tree in a single list
	list_left = []
	list_right = []
	extra = []

	while not len(state) == 0:
		boat_side = "Left" if state[4] == 'L' else "right"
		list_left.append("M" + str(state[0]) + " C" + str(state[1]))
		list_right.append("M" + str(state[2]) + " C" + str(state[3]))

		state = state[6]
		

	list_left.reverse()

	for i in range(len(list_left)):
		extra.append(list_left[i])
	return extra


def formatstate(state_list): #for the good formate of the output

	extralist = []
	new_list =[]
	new_list1 =[]
	new_list2 = []

	for i in range(len(state_list)):
		print ("\n")
		print ("Solution #" + str(i + 1))
		printstate(state_list[i])
	print("\n\n")
	print("\n\n")
	print("list representation of all the possible states:")# two possible solution with max difference is detected and appended as one to make the output list with all the possible solution space
	for i in range(len(state_list)):# not an efficient way
		extralist.append(treeimplement(state_list[i]))


	for j in range(len(extralist[0])):
		if extralist[0][j]== extralist[3][j]:
			new_list2.append(extralist[0][j])
		else:
			new_list2.append([extralist[0][j],extralist[3][j]])
	print(new_list2)

# Each state is a 6-tuple
# Missionary Left, Canibals Left, Missionary Right, Canibals Right, Boat Side, Tree Level, Movement Path
def main():

	print("All the state space ending in loops and violating the conditions are igonred:")

	initial_state = [3, 3, 0, 0, 'L', 1,  []]


	goal_state = [0, 0, 3, 3, 'R', 800,  []]



	result = solve(initial_state, goal_state)


	formatstate(result)




if __name__ == '__main__':
	main()