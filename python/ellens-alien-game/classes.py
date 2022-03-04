class Alien:
    """
    Creates the Aliens object
    """
    total_aliens_created = 0

    def __init__(self, x_coord, y_coord):
        self.health = 3
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        Alien.total_aliens_created += 1

        # return self.x_coordinate, self.y_coordinate

    def hit(self, amount=1):
        self.health -= amount
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_new, y_new):
        self.x_coordinate += x_new
        self.y_coordinate += y_new
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, other_object=0):
        self.other_object = other_object
        pass

   
def new_aliens_collection(positions):
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """
    output = []
    for position in positions:
        x_coor, y_coor = position
        output.append(Alien(x_coor,y_coor))
    return output    





# def main():
 

#     alien_start_positions = [(4, 7), (-1, 0)]
#     aliens = new_aliens_collection(alien_start_positions)
#     for alien in aliens:
#     	print(alien.x_coordinate, alien.y_coordinate)
    

# if __name__ == "__main__":
#     main()