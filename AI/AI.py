"""
I confirm that this assignment is my own work.

This program solves a maze using the Breadth-First Search (BFS) algorithm. The maze is stored in a text file where 0 represents an open path and 1 represents a wall and the program can run any size.
The goal of the program is to find the shortest path from the start position (top-left corner) to the goal position (bottom-right corner).
The first step of the program is reading the maze from the file using the read_maze function.
Each line of the file is processed and converted into a list of integers, forming a two-dimensional grid that represents the maze.
The function also checks for basic input errors, such as an empty file or rows with different lengths.
After reading the maze, the program converts the grid into a graph structure using the create_matrix function.
In this step, each open cell in the maze is assigned a node number. 
A dictionary is used to map maze coordinates to node numbers, while a list stores the reverse mapping.
The program then creates an adjacency matrix that represents connections between neighbouring open cells (up, down, left, and right). 
The BFS algorithm is implemented in the bfs_shortest_path function. 
BFS explores nodes level by level using a queue, which ensures that the first time the goal node is reached, the shortest path has been found. 
A visited list prevents revisiting nodes, while a parent list stores where each node came from, allowing the path to be reconstructed once the goal is found.
Finally, the path is converted back from node numbers to maze coordinates and displayed along with the maze visualization. 
This shows the shortest route from start to end.

"""
"""
Code Attribution

Adjacency matrix representation inspired by:https://www.programiz.com/dsa/graph-adjacency-matrix

The concept of representing a graph using nodes and a matrix of connections
is based on this source. In this program, this idea is applied by converting
each open cell in the maze into a node using the code: "cell_to_node[(row, column)] = node_number"

The adjacency matrix is then created using: "adjacency_matrix.append([0] * number_of_nodes)"
to represent connections between nodes.
"""
"""
Code Attribution

The concept of using a queue (FIFO - First In, First Out) in
Breadth-First Search (BFS) is inspired by:https://youtu.be/HZ5YTanv5QE?si=DRxfmCc9nJ9tc8nE

The video explains how nodes are explored level by level using a queue,
where elements are added to the back and removed from the front.

In this program, this concept is implemented using Python's deque for
efficiency:
- queue.append(...) adds elements to the back
- queue.popleft() removes elements from the front

This provides the same behaviour as a standard queue.
"""
from collections import deque


def read_maze(file_name):
    """
    Name: read_maze
    Description: Reads the maze from a text file and stores it as a list.
    Inputs: file_name
    Outputs: A maze . If there is no maze or the maze is in incorrect order, it will display the problem
    Process: Opens the file, reads each row, converts values into integers,
             checks that the maze is not empty, and checks that all rows
             have the same length.
    """
    maze = [] # create an empty list for the maze

    with open(file_name, "r") as file: # open the file from what user input (which is connected in the main function) and read it  
            for line in file: # read every line in the file by making a for loop 
                line = line.strip() # remove the spaces in each line

                if line != "": # check if the line is not empty
                    row = []
                    for x in line.split():
                        row.append(int(x)) # if not empty, then turn each number into seperated number then changed it to integer so that it can be added to the list 
                    maze.append(row) # added that row into the maze list. This will loop for every line in the file

    if len(maze) == 0: # if the length of the maze is zero (meaning there is nothing in the list), then print that "maze is empty"
        print("Maze file is empty.") 
        return None

    number_of_columns = len(maze[0]) # store the first row of maze in "number of column" variable

    for row in maze: # for loop for each row in maze
        if len(row) != number_of_columns: # when the program notice that one of the row in the maze list is not the same as the first row, it will print that the maze rows are not the same leng
            print("Maze rows are not the same length.")
            return None

    return maze # if there is not error, it will return the completed list of maze


def create_matrix (maze):
    """
    Name: create_matrix
    Description: Converts the maze grid into a graph using an adjacency matrix.
    Inputs: maze
    Outputs: adjacency_matrix, cell_to_node, node_to_cell
    Process: Gives every open cell a node number, then connects neighbouring
             open cells in the adjacency matrix.
    """
    number_of_rows = len(maze) # number of rows for the maze
    number_of_columns = len(maze[0]) # numbers of columns for the maze

    cell_to_node = {} # the maze uses cell [basically (1,2) for example] but the BFS runs on nodes(such as 0, 1,2,3 for example), therefore, a converstion between these two is needed for the progra to work
    node_to_cell = [] # same, this is changin node to cell

    for row in range(number_of_rows): # for loop for the numbers of row
        for column in range(number_of_columns): # for loop for the number of column (these two are using a nested loop so that the program can go every column then move to next row then repeate the process again). In another word, loop thorugh every cell in the maze
            if maze[row][column] == 0: # check if the current cell is 0 (identifying if it is open path or closed path)
                node_number = len(node_to_cell) #Use the current list length as the next node number.
                cell_to_node[(row, column)] = node_number # this stores which node number belongs to a cell in the maze.
                node_to_cell.append((row, column)) #Save the cell position to know which cell each node represents.

    number_of_nodes = len(node_to_cell) # see how many open cells are there. In another word , in this stage, the program is preparing data for the BFS to run.

    adjacency_matrix = [] # create a new list
    for i in range(number_of_nodes):
        adjacency_matrix.append([0] * number_of_nodes) # this will create a same number of row and column matrix filled with zeros, so each node will become a row, the row number and column number are the same so that the program can know which nodes have connections

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # This store possilbe moves to make from the node. how the nodes will connect to the other opened pathes ( so for example if the nodes is at (2,3), then (-1,0) will make it (1,3) which is top, the other three are also like that)

    for row, column in cell_to_node: #loops through the keys of the cell to node dictionary
        current_node = cell_to_node[(row, column)] # get the node number for the cell (which the program is currently at)
        
        for d in directions:
            row_change = d[0]
            column_change = d[1] # this change the every row and column based from the direction list
            new_row = row + row_change#Calculates the neighbouring cell.
            new_column = column + column_change#Calculates the neighbouring cell also

            if (new_row, new_column) in cell_to_node: ##Calculates the neighbouring cell. this decide whether if it is possible to move there or not.
                next_node = cell_to_node[(new_row, new_column)] # take the node number of that cell 
                adjacency_matrix[current_node][next_node] = 1 # this make a connection in the matrix ( in above, we make matrix of ( n  x  n) of the nodes, in there all of htem are 0, but here, we turned it 1 for the possible path way)

    return adjacency_matrix, cell_to_node, node_to_cell


def bfs_shortest_path(adjacency_matrix, start_node, goal_node):
    """
    Name: bfs_shortest_path
    Description: Uses Breadth-First Search to find the shortest path.
    Inputs: adjacency_matrix, start_node, goal_node
    Outputs: path_nodes or None
    Process: Explores nodes level by level using a queue, stores visited nodes
             and parent nodes, then rebuilds the shortest path if the goal is found.
    """
    number_of_nodes = len(adjacency_matrix) #Gets the total number of nodes in the graph.

    visited = [False] * number_of_nodes #Creates a list to track which nodes have already been visited. cureenly everthing is false in the list
    
    parent = [-1] * number_of_nodes #Creates a list to store where each node came from.

    queue = deque()#Creates the BFS queue to stores nodes waiting to be explored.
    queue.append(start_node)
    visited[start_node] = True #putting the start node into the queue and marking it as visited

    while queue: # use a while loop
        current_node = queue.popleft() #Removes the first node from the queue since the current node is already explored .

        if current_node == goal_node:#Checks whether current node is at the end.
            path_nodes = [] # list to do the backward nodes so that we can rebuild the path from the end
            node = goal_node # to make the backward nodes, the nodes is equaled to the End aka goal node

            while node != -1: #it will run until the node will become -1 (which is teh start)
                path_nodes.append(node)# Add the current node to the path list
                node = parent[node]# Move to the parent node (the node we came from)

            path_nodes.reverse() # Reverse the path because we built it from goal to start

            return path_nodes  # Return the final shortest path

        for next_node in range(number_of_nodes):# Check every possible node to see if it is connected
            if adjacency_matrix[current_node][next_node] == 1 and visited[next_node] == False: # If there is a connection AND the node has not been visited
                visited[next_node] = True  # Mark the node as visited
                parent[next_node] = current_node # Record that we reached this node from current_node
                queue.append(next_node)   # Add the node to the queue so it can be explored later


    return None


def print_maze_solution(maze, path_cells):
    """
    Name: print_maze_solution
    Description: Prints the shortest distance, the path, and a maze view.
    Inputs: maze, path_cells
    Outputs: Printed result on screen
    Process: Checks if a path exists, prints the distance and coordinates,
             then draws the maze using symbols.
    """


    shortest_distance = len(path_cells) - 1 # cells and distnace is not the same we need to subsstitude 1 from the cells lenght to give the correct distnace

    print("Shortest distance:", shortest_distance)

    print(f"Path: {path_cells}" ) # this show the path from start to end

    number_of_rows = len(maze)
    number_of_columns = len(maze[0])

    print("\nMaze view:")
    print("S = start, E = end, # = wall, .= path, blank space = explored\n")

    for row in range(number_of_rows):# Loop through each row of the maze
        display = [] # a list for the display of the path

        for column in range(number_of_columns):  # Loop through each column in the current row
            if (row, column) == (0, 0):
                display.append("S")
            elif (row, column) == (number_of_rows - 1, number_of_columns - 1):
                display.append("E")
            elif maze[row][column] == 1: # check if its a wall or not
                display.append("#")
            elif (row, column) in path_cells:# Check if this cell is part of the shortest path
                display.append(".")
            else: # if not it would be the explored one
                display.append(" ")

        print("".join(display))


def main():
    file_name = "AI/maze.txt"

    maze = read_maze(file_name) # read the maze
    if maze is None:
        return

    number_of_rows = len(maze)
    number_of_columns = len(maze[0])

    start_cell = (0, 0)# start position
    goal_cell = (number_of_rows - 1, number_of_columns - 1) # end position

    if maze[0][0] != 0:#in case if the user put close path at the start
        print("Start cell is wrong,start cell should be 0.")
        return

    if maze[number_of_rows - 1][number_of_columns - 1] != 0:#in case if the user put close path at the start
        print("Goal cell is wrong, it should be 0.")
        return

    adjacency_matrix, cell_to_node, node_to_cell = create_matrix(maze)# Convert the maze grid into a graph structure:

    start_node = cell_to_node[start_cell]  # Convert start cell coordinates into its node number
    goal_node = cell_to_node[goal_cell]# Convert goal cell coordinates into its node number


    path_nodes = bfs_shortest_path(adjacency_matrix, start_node, goal_node) # Run BFS to find the shortest path between the start node and goal node

    if path_nodes is None:# If BFS did not find a path
        print("No path found.")
        return
    else:
        path_cells = [] # Create an empty list to store maze coordinates if it find the path
        for node in path_nodes:# Loop through each node in the BFS path
            path_cells.append(node_to_cell[node])# Convert each node number back into its maze coordinate

    print_maze_solution(maze, path_cells)  # Call the function to print the distance, path, and maze visualization


if __name__ == "__main__":
    main()
 