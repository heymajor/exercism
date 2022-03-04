# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    coordinates = (0, 0)
    direction = NORTH

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        Robot.coordinates = (x_pos, y_pos)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, string):
        self.string = string
        directions_list = list(self.string)

        for dir in directions_list:
            if self.direction == NORTH:
                if dir == "R":
                    self.direction = EAST
                    continue
                elif dir == "L":
                    self.direction = WEST
                    continue
                else:
                    self.y_pos += 1
                    continue
            if self.direction == EAST:
                if dir == "L":
                    self.direction = NORTH
                    continue
                elif dir == "R":
                    self.direction = SOUTH
                    continue
                else:
                    self.x_pos += 1
                    continue
            if self.direction == WEST:
                if dir == "L":
                    self.direction = SOUTH
                    continue
                elif dir == "R":
                    self.direction = NORTH
                    continue
                else:
                    self.x_pos -= 1
                    continue
            if self.direction == SOUTH:
                if dir == "R":
                    self.direction = WEST
                    continue
                elif dir == "L":
                    self.direction = EAST
                    continue
                else:
                    self.y_pos -= 1
                    continue
        print("final x:", self.x_pos)
        print("final y:", self.y_pos)
        Robot.coordinates = (self.x_pos, self.y_pos)
        print(Robot.coordinates)
        Robot.direction = self.direction
        return self.x_pos, self.y_pos, self.direction

def main():
    # a = "aabb"
    # robot = Robot("BOOP", 0, 0)
    # print(robot.move(a))
    robot = Robot(NORTH, 7, 3)
    robot.move("RAALAL")
    print(robot.coordinates) # (9, 4)
    print(robot.direction) # WEST


if __name__ == '__main__':
    main()