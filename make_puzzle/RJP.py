__author__ = 'TeamA_000'
import random
import pprint
import math

class puzzle_improve:
    def simulated_annealing(original_puzzle, iterations, size, temperature, decay):
        old_puzzle = original_puzzle

        #print(old_answer)
        #Test this stuff
        new_puzzle = old_puzzle
        old_answer = puzzle_evaluate.bfs_path(new_puzzle, size)

        for i in range(0, iterations):
            #Pick an index
            temperature = temperature * decay
            pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            # Because you can never be too sure
            while (pick_index == (size - 1, size - 1)):
                pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            #pick a replacement number
            #print(str(pick_index[0]) + ", " + str(pick_index[1]) + " replace "  + str(new_puzzle[pick_index[0]][pick_index[1]]) + " with:")

            new_puzzle[pick_index[0]][pick_index[1]] = random.randint(1, puzzle_gen.generate_num(pick_index[0], pick_index[1], size))
            #print(new_puzzle[pick_index[0]][pick_index[1]])

            #pp = pprint.PrettyPrinter(depth = input)
            #pp.pprint(new_puzzle)

            new_answer = puzzle_evaluate.bfs_path(new_puzzle, size)
            #print(new_answer)
            if (new_answer <= old_answer) | (random.uniform(0,1) < temperature):
                #print(str(old_answer) + "replaced by: ")
                #print(new_answer)
                old_answer = new_answer
                old_puzzle = new_puzzle
                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(old_puzzle)
        #print(old_answer)
        return old_puzzle

    def gradient_descent_rand_up(original_puzzle, iterations, size, chance):
        old_puzzle = original_puzzle

        #print(old_answer)

        new_puzzle = old_puzzle
        old_answer = puzzle_evaluate.bfs_path(new_puzzle, size)

        for i in range(0, iterations):
            #Pick an index
            pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            # Because you can never be too sure
            while (pick_index == (size - 1, size - 1)):
                pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            #pick a replacement number
            #print(str(pick_index[0]) + ", " + str(pick_index[1]) + " replace "  + str(new_puzzle[pick_index[0]][pick_index[1]]) + " with:")

            new_puzzle[pick_index[0]][pick_index[1]] = random.randint(1, puzzle_gen.generate_num(pick_index[0], pick_index[1], size))
            #print(new_puzzle[pick_index[0]][pick_index[1]])

            #pp = pprint.PrettyPrinter(depth = input)
            #pp.pprint(new_puzzle)

            new_answer = puzzle_evaluate.bfs_path(new_puzzle, size)
            #print(new_answer)
            if (new_answer <= old_answer) | (random.uniform(0,1) < chance):
                #print(str(old_answer) + "replaced by: ")
                #print(new_answer)
                old_answer = new_answer
                old_puzzle = new_puzzle
                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(old_puzzle)
        #print(old_answer)
        return old_puzzle

    def gradient_descent_rand_restart(original_puzzle, iterations, restarts, size):
        old_puzzle = original_puzzle
            # print(old_answer)

        new_puzzle = old_puzzle
        old_answer = puzzle_evaluate.bfs_path(new_puzzle, size)
        for h in range(0, restarts):
            new_puzzle_answer = puzzle_improve.hill_climbing_ans(original_puzzle, iterations, size)
            if (new_puzzle_answer[1] <= old_answer):
                old_answer = new_puzzle_answer[1]
                #print(old_answer)
                old_puzzle = new_puzzle_answer[0]
        #print(old_answer)
        return old_puzzle

    def hill_climbing_ans(original_puzzle, iterations, size):

        old_puzzle = original_puzzle
        # print(old_answer)

        new_puzzle = old_puzzle
        old_answer = puzzle_evaluate.bfs_path(new_puzzle, size)

        for i in range(0, iterations):
            # Pick an index
            pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            # Because you can never be too sure
            while (pick_index == (size - 1, size - 1)):
                pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            # pick a replacement number
            # print(str(pick_index[0]) + ", " + str(pick_index[1]) + " replace "  + str(new_puzzle[pick_index[0]][pick_index[1]]) + " with:")

            new_puzzle[pick_index[0]][pick_index[1]] = random.randint(1, puzzle_gen.generate_num(pick_index[0],
                                                                                                 pick_index[1], size))
            # print(new_puzzle[pick_index[0]][pick_index[1]])

            # pp = pprint.PrettyPrinter(depth = input)
            # pp.pprint(new_puzzle)

            new_answer = puzzle_evaluate.bfs_path(new_puzzle, size)
            # print(new_answer)
            if (new_answer <= old_answer):
                # print(str(old_answer) + "replaced by: ")
                # print(new_answer)
                old_answer = new_answer
                old_puzzle = new_puzzle
                # pp = pprint.PrettyPrinter(depth = input)
                # pp.pprint(old_puzzle)
        return (old_puzzle, old_answer)

    def gradient_descent_unused(original_puzzle, iterations, size):
        old_puzzle = original_puzzle

        #print(old_answer)

        new_puzzle = old_puzzle
        old_answer = puzzle_evaluate.bfs_path_expanded(new_puzzle, size)

        for i in range(0, iterations):
            #Pick an index
            pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            # Because you can never be too sure
            while (pick_index == (size - 1, size - 1)):
                pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            #pick a replacement number
            #print(str(pick_index[0]) + ", " + str(pick_index[1]) + " replace "  + str(new_puzzle[pick_index[0]][pick_index[1]]) + " with:")

            new_puzzle[pick_index[0]][pick_index[1]] = random.randint(1, puzzle_gen.generate_num(pick_index[0], pick_index[1], size))
            #print(new_puzzle[pick_index[0]][pick_index[1]])

            #pp = pprint.PrettyPrinter(depth = input)
            #pp.pprint(new_puzzle)

            new_answer = puzzle_evaluate.bfs_path_expanded(new_puzzle, size)
            #print(new_answer)
            #print(puzzle_evaluate.bfs_path(new_puzzle, size))
            if (new_answer <= old_answer):
                #print(str(old_answer) + "replaced by: ")
                #print(new_answer)
                old_answer = new_answer
                old_puzzle = new_puzzle
                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(old_puzzle)
        return old_puzzle

    def gradient_descent(original_puzzle, iterations, size):
        old_puzzle = original_puzzle

        #print(old_answer)

        new_puzzle = old_puzzle
        old_answer = puzzle_evaluate.bfs_path(new_puzzle, size)

        for i in range(0, iterations):
            #Pick an index
            pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            # Because you can never be too sure
            while (pick_index == (size - 1, size - 1)):
                pick_index = (random.randint(1, size - 1), random.randint(1, size - 1))
            #pick a replacement number
            #print(str(pick_index[0]) + ", " + str(pick_index[1]) + " replace "  + str(new_puzzle[pick_index[0]][pick_index[1]]) + " with:")

            new_puzzle[pick_index[0]][pick_index[1]] = random.randint(1, puzzle_gen.generate_num(pick_index[0], pick_index[1], size))
            #print(new_puzzle[pick_index[0]][pick_index[1]])

            #pp = pprint.PrettyPrinter(depth = input)
            #pp.pprint(new_puzzle)

            new_answer = puzzle_evaluate.bfs_path(new_puzzle, size)
            #print(new_answer)
            if (new_answer <= old_answer):
                #print(str(old_answer) + "replaced by: ")
                #print(new_answer)
                old_answer = new_answer
                old_puzzle = new_puzzle
                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(old_puzzle)
        return old_puzzle



class puzzle_evaluate:
    #Check how good the maze is

    def evaluate(parent_list, size):
        #print("evaluating")
        #pp = pprint.PrettyPrinter(depth = size)
        #pp.pprint(parent_list)
        cost = -1
        #Add the goal and the parent of the goal first
        path = [(size-1, size-1), parent_list[size-1][size-1]]
        #print(path)
        #Go from the goal at top right to it's parent, then it's parent,..., until you get back to the top left
        while(1):
            #Get the parent of that parent
            path.append(parent_list[path[-1][0]][path[-1][1]])
            cost = cost - 1
            if(path[-1] == (0, 0)):
                return(path, cost)
        return (path, cost)

    def check_right(x, y, jump, size):
        if (x + jump < size):
            return (x + jump, y)
        else:
            return (-1, -1)

    def check_down(x, y, jump, size):
        if (y + jump < size):
            return (x, y + jump)
        else:
            return (-1, -1)

    def check_left(x, y, jump, size):
        if (x - jump > -1):
            return (x - jump, y)
        else:
            return (-1, -1)

    def check_up(x, y, jump, size):
        if (y - jump > -1):
            return (x, y - jump)
        else:
            return (-1, -1)

    #Tells how many nodes were not expanded
    def bfs_path_expanded(puzzle, input):
        #leave it at that if no path is found
        cost = 99999
        parent_list = [[(-1, -1)]*input for a in range(input)]


        parent = (0, 0)
        #Traverse back from parent_list after the end, if there is no path to the end leave blank
        path = []
        #for bfs
        queue = []
        queue.append((0, 0))

        x = 0
        y = 0
        jump = puzzle[x][y]
        while queue:
            #remove old number from queue
            queue.pop(0)
            #evaluate it and add children, put parent that was removed into parent_list
            right = puzzle_evaluate.check_right(x, y, jump, input)
            down = puzzle_evaluate.check_down(x, y, jump, input)
            left = puzzle_evaluate.check_left(x, y, jump, input)
            up = puzzle_evaluate.check_up(x, y, jump, input)
            #If it is within bounds and hasn't been put on the queue before
            #if flag triggered, prepare to return and get a new cost function
            if (right[0] != -1) & (parent_list[right[0]][right[1]] == (-1, -1)):
                parent_list[right[0]][right[1]] = parent
                queue.append(right)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)

                if (right[0] == (input -1)) & (right[1] == (input -1)):
                    unused = 0
                    for i in range(0, input-1):
                        for j in range(0, input-1):
                            if parent_list[i][j] == (-1, -1):
                                unused = unused + 1
                    return unused

            if (down[0] != -1) & (parent_list[down[0]][down[1]] == (-1, -1)):
                parent_list[down[0]][down[1]] = parent
                queue.append(down)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)

                if (down[0] == (input -1)) & (down[1] == (input -1)):
                    unused = 0
                    for i in range(0, input-1):
                        for j in range(0, input-1):
                            if parent_list[i][j] == (-1, -1):
                                unused = unused + 1
                    return unused

            if (left[0] != -1) & (parent_list[left[0]][left[1]] == (-1, -1)):
                parent_list[left[0]][left[1]] = parent
                queue.append(left)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)

            if (up[0] != -1) & (parent_list[up[0]][up[1]] == (-1, -1)):
                parent_list[up[0]][up[1]] = parent
                queue.append(up)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)
            #queue_parent_flag = puzzle_evaluate.queue_add(queue, x, y, jump, input, parent_list, parent)

            #change parent to next node, get new coordinates, parent, and jump
            if queue:
                #print(queue)
                parent = queue[0]
                x = parent[0]
                y = parent[1]

                jump = puzzle[x][y]
                #print("jump is " + str(jump))
            #repeat


            #print(queue)
        return cost

    #cost is a decrement for each rook jump
    # if we hit the end of the nodes but never get to the bottom right corner use 99999
    def bfs_path(puzzle, input):
        #leave it at that if no path is found
        cost = 99999
        parent_list = [[(-1, -1)]*input for a in range(input)]


        parent = (0, 0)
        #Traverse back from parent_list after the end, if there is no path to the end leave blank
        path = []
        #for bfs
        queue = []
        queue.append((0, 0))

        x = 0
        y = 0
        jump = puzzle[x][y]
        while queue:
            #remove old number from queue
            queue.pop(0)
            #evaluate it and add children, put parent that was removed into parent_list
            right = puzzle_evaluate.check_right(x, y, jump, input)
            down = puzzle_evaluate.check_down(x, y, jump, input)
            left = puzzle_evaluate.check_left(x, y, jump, input)
            up = puzzle_evaluate.check_up(x, y, jump, input)
            #If it is within bounds and hasn't been put on the queue before
            #if flag triggered, prepare to return and get a new cost function
            if (right[0] != -1) & (parent_list[right[0]][right[1]] == (-1, -1)):
                parent_list[right[0]][right[1]] = parent
                queue.append(right)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)

                if (right[0] == (input -1)) & (right[1] == (input -1)):
                    ans = puzzle_evaluate.evaluate(parent_list, input)
                    return ans[1]

            if (down[0] != -1) & (parent_list[down[0]][down[1]] == (-1, -1)):
                parent_list[down[0]][down[1]] = parent
                queue.append(down)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)

                if (down[0] == (input -1)) & (down[1] == (input -1)):
                    ans = puzzle_evaluate.evaluate(parent_list, input)
                    return ans[1]

            if (left[0] != -1) & (parent_list[left[0]][left[1]] == (-1, -1)):
                parent_list[left[0]][left[1]] = parent
                queue.append(left)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)

            if (up[0] != -1) & (parent_list[up[0]][up[1]] == (-1, -1)):
                parent_list[up[0]][up[1]] = parent
                queue.append(up)

                #pp = pprint.PrettyPrinter(depth = input)
                #pp.pprint(parent_list)
            #queue_parent_flag = puzzle_evaluate.queue_add(queue, x, y, jump, input, parent_list, parent)

            #change parent to next node, get new coordinates, parent, and jump
            if queue:
                #print(queue)
                parent = queue[0]
                x = parent[0]
                y = parent[1]

                jump = puzzle[x][y]
                #print("jump is " + str(jump))
            #repeat


            #print(queue)
        return cost

class puzzle_gen:
    #makes the maximum distance a rook can jump from a square
    def generate_num(x, y, size):
        sizes = [x, size - x - 1, y, size - y - 1]
        return max(sizes)


    #Puts random numbers in the array based on puzzle_gen
    def fill_puzzle(array, size):
        for x in range(0, size):
            for y in range(0, size):
                #print("This is " + str(x) + ", " + str(y) + "\n")
                array[x][y] = random.randint(1, puzzle_gen.generate_num(x, y, size))

        #Goal state is bottom right, a 0
        array[size - 1][size - 1] = 0
        return array

    def make_space(input):
        #Is actually a list of lists?
        array = [[-1]*input for a in range(input)]
        return array

if __name__ == "__main__":

    input = input("Please input a puzzle size between 5 and 10: ")
    try:
        input = int(input)
    except ValueError:
        print("That was not a valid answer. The default size will now be 5.")
        input = 5
    else:
        if( input < 5):
            print("That was not a valid answer. The default size will now be 5.")
            input = 5
        if(input > 10):
            print("That was not a valid answer. The default size will now be 5.")
            input = 5



    #Make a puzzle
    #input = 5
    puzzle = puzzle_gen.make_space(input)
    #print(puzzle[4][4])
    #print(math.floor(24/5))
    #Use for rounding down

    puzzle = puzzle_gen.fill_puzzle(puzzle, input)

    #Used for the writeup
    puzzle_stat = [[2, 2, 1, 4, 1],
                 [4, 3, 2, 3, 1],
                 [2, 3, 2, 2, 2],
                 [1, 2, 2, 1, 1],
                 [3, 2, 4, 1, 0]]

    pp = pprint.PrettyPrinter(depth = input)
    pp.pprint(puzzle)

    #Get minimum jumps

    evaluation = puzzle_evaluate.bfs_path(puzzle, input)
    print(evaluation)


    #If our puzzle is invalid
    while(evaluation == 99999):
        puzzle = puzzle_gen.fill_puzzle(puzzle, input)
        pp.pprint(puzzle)

        #Get minimum jumps

        evaluation = puzzle_evaluate.bfs_path(puzzle, input)
        print(evaluation)

    #Hill climbing
    print("Gradient Descent")
    iterations = 5000
    puzzle_two = puzzle_improve.gradient_descent(puzzle, iterations, input)
    #print(puzzle_evaluate.bfs_path(puzzle_two, input))
    pp.pprint(puzzle_two)


    print("Gradient Descent with random restart")
    restarts = 5
    iterations = int(10000/restarts)

    puzzle_three = puzzle_improve.gradient_descent_rand_restart(puzzle, iterations, input, restarts)
    pp.pprint(puzzle_three)

    print("Gradient Descent with random uphill steps")
    iterations = 5000
    chance = .001
    puzzle_four = puzzle_improve.gradient_descent_rand_up(puzzle, iterations, input, chance)
    pp.pprint(puzzle_four)

    print("Simulated Annealing")
    iterations = 5000
    temperature = .1
    decay = .99
    puzzle_four = puzzle_improve.simulated_annealing(puzzle, iterations, input, temperature, decay)
    pp.pprint(puzzle_four)

    #Check new way of doing things
    print("Gradient Descent New Metric")
    iterations = 5000
    puzzle_two = puzzle_improve.gradient_descent_unused(puzzle_stat, iterations, input)
    #print(puzzle_evaluate.bfs_path(puzzle_two, input))
    pp.pprint(puzzle_two)
