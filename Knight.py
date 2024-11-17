from Chromosome import Chromosome
import random
class Knight:
    def __init__(self,chromosome=None):
        self.chromosome=chromosome if chromosome else Chromosome()
        self.position=(0,0)
        self.path=[self.position]
        self.fitness=0
    def move_forward(self,direction):
        x,y=self.position
        moves=[(2, 1), (1, 2), (-1, 2), (-2, 1), 
            (-2, -1), (-1, -2), (1, -2), (2, -1)]
        dx,dy=moves[direction]
        return x+dx,y+dy
    def move_backward(self):
        if len(self.path)>1:
            self.path.pop()
            self.position=self.path[-1]
        return self.position
    def check_moves(self):
        visited = set(self.path)
        random_direction=random.choice([True,False])
        for i in range(len(self.chromosome.genes)):
            move=self.chromosome.genes[i]
            next_position=self.move_forward(move)
            if(0<=next_position[0]<8 and 0<=next_position[1]<8 and next_position not in visited):
                self.path.append(next_position)
                self.position=next_position
            else:
                self.move_backward()
                directions=list(range(8))
                if random_direction:
                    directions = directions[directions.index(move) + 1:] + directions[:directions.index(move)]
                else:
                    directions = directions[:directions.index(move)][::-1] + directions[directions.index(move) + 1:][::-1]
                valid_move_found = False
                for new_move in directions:
                    new_position=self.move_forward(new_move)
                    if (0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and new_position not in visited):
                        self.chromosome.genes[i] = new_move
                        self.path.append(new_position)
                        self.position = new_position
                        valid_move_found = True
                        break
                if not valid_move_found:
                    self.path.append(self.position)

    def evaluate_fitness(self):
        visited_positions = set()
        self.fitness=0
        for pos in self.path:
            if pos not in visited_positions:
                visited_positions.add(pos)
                self.fitness += 1
            else:
                break
# knight = Knight()

# # Validate and correct the knight's moves
# knight.check_moves()

# # Evaluate the knight's fitness
# knight.evaluate_fitness()

# # Print results
# print("Path:", knight.path)
# print("Fitness:", knight.fitness)
