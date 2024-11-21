from Chromosome import Chromosome
import random
class Knight:
    def __init__(self,chromosome=None):
        self.chromosome=chromosome if chromosome else Chromosome()
        self.position=(0,0)
        self.path=[(0,0)]
        self.fitness=0
    def move_forward(self,direction):
        x,y=self.position
        moves=[(2, 1), (1, 2), (-1, 2), (-2, 1), 
            (-2, -1), (-1, -2), (1, -2), (2, -1)]
        dx,dy=moves[direction]
        return x+dx,y+dy


    def move_backward(self, direction):
        # Undo the last move by moving in the opposite direction
       # x, y = self.path.pop()
        x,y=self.position
        moves = [ (-2, -1),   (-1, -2), (1, -2),  (2, -1),(2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        dx, dy = moves[direction]
        return x + dx, y + dy

    def check_moves(self):
        visited = set(self.path)
        random_direction=random.choice([True,False])
        for i in range(len(self.chromosome.genes)):
            valid_move_found = False

            move=self.chromosome.genes[i]
            next_position=self.move_forward(move)
            if(0<=next_position[0]<8 and 0<=next_position[1]<8 and next_position not in visited):
                self.path.append(next_position)
                visited.add(next_position)
                self.position=next_position
                valid_move_found=True
            else:
                self.move_backward(move)
                directions=list(range(8))
                if random_direction:
                    directions = directions[directions.index(move) + 1:] + directions[:directions.index(move)]
                else:
                    directions = directions[:directions.index(move)][::-1] + directions[directions.index(move) + 1:][::-1]
                for new_move in directions:
                    new_position=self.move_forward(new_move)
                    if (0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and new_position not in visited):
                        self.chromosome.genes[i] = new_move  #check this later
                        self.path.append(new_position)
                        visited.add(new_position)
                        self.position = new_position
                        valid_move_found = True
                        break
            if not valid_move_found:
                return

                    
                    
    def evaluate_fitness(self):
        self.fitness=len(self.path)
        return len(self.path)

# knight = Knight()

# # Validate and correct the knight's moves
# knight.check_moves()

# # Evaluate the knight's fitness
# knight.evaluate_fitness()

# # Print results
# print("Path:", knight.path)
# print("Fitness:", knight.fitness)
