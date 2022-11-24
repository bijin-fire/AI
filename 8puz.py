def generate_child(state, visited):
    x,y = empty_tile(state)
    aval_pos = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
    children = []
    for i in aval_pos:
        child = position(state,x,y,i[0],i[1]) 
        if child is not None and child not in visited:
            children.append(child)
    return children

# Function to find the position of empty tile
def empty_tile(node):
    for i in range(0,3):
        for j in range(0,3):
            if node[i][j] == '_': return i,j
           
# Function to check if a child node is valid or not
def position(node,x1,y1,x2,y2):
        if x2 in range(0,3) and y2 in range(0,3):
            temp_node = []
            temp_node = copy(node)
            temp_node[x1][y1], temp_node[x2][y2] = temp_node[x2][y2], temp_node[x1][y1]
            return temp_node
        else:
            return None

# Function to create copy of a state
def copy(root):
    temp = []
    for i in root:
        t = []
        for j in i:
            t.append(j)
        temp.append(t)
    return temp

# Driver Code
# Input Start State
print("\nEnter The Start State:")
initial_state = []
for i in range(0,3):
    temp = input().split(" ")
    initial_state.append(temp)

# Define Goal State
goal_state = [
	[ '1', '2', '3' ],
	[ '8', '_', '4' ],
	[ '7', '6', '5' ]
]

print("\nThe Goal State is:")
for i in range(3) :
    for j in range(3) :
        print(goal_state[i][j], end=" ")
    print("")
print("\n-----------------------\n")
print("      Game Begins")
print("\n-----------------------\n")

# Check if initial and goal state are same or not
if(initial_state == goal_state):
    print("Initial State is same as Goal State")
    print("\n-----------------------\n")
    print("      Game Over")
    print("\n-----------------------\n")

# Game Starts
else:
    state = initial_state
    T = 0
    g_score = 0
    visit = []

    while(T == 0) :
        g_score += 1 # Calculate G-Score
        min_f = 100
        child = []
        visit.append(state)
        child = generate_child(state, visit)
        for i in range(3) :
            for j in range(3) :
                print(state[i][j], end=" ")
            print("")
        print("")
        print("  | ")
        print(" \\'/ \n")
        for k in child:
            h_score=0
            for i in range(3) :
                for j in range(3) :
                    if(k[i][j] != goal_state[i][j]) : h_score += 1 # Calculate H-score
            if(h_score == 0) :
                for i in range(3) :
                    for j in range(3) : print(goal_state[i][j], end=" ")
                    print("")
                print("\n-----------------------\n")
                print("      Game Over")
                print("\n-----------------------")
                T = 1

            else:
                f_score = h_score + g_score # Calculate F-score
                if (min_f == f_score and k[1][1] != '_'): state = copy(k)
                elif (min_f > f_score) :
                    state = copy(k)
                    min_f = f_score
