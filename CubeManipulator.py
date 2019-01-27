import Side as Side


class CubeManipulator(object):

    def __init__(self, all_sides, LENGTH_OF_CUBE=3):
        self.all_sides = all_sides
        self.front = all_sides[0]
        self.top = all_sides[1]
        self.right = all_sides[2]
        self.left = all_sides[3]
        self.bottom = all_sides[4]
        self.back = all_sides[5]
        self.LENGTH_OF_CUBE = LENGTH_OF_CUBE
        self.clockwise_transform = {"Top": "Right", "Right": "Bottom", "Bottom": "Left", "Left": "Top"}
        self.anti_clockwise_transform = {"Right": "Top", "Bottom": "Right", "Left": "Bottom", "Top": "Left"}
        self.right_edge_of_neighbour_given_face = {"Front": ["Left", False], "Top": ["Top", True],
                                                   "Back": ["Right", True], "Bottom": ["Left", False]}
        self.left_edge_of_neighbour_given_face = {"Front": ["Right", False], "Top": ["Top", False],
                                                  "Back": ["Right", True], "Bottom": ["Left", True]}

    def printCubeState(self):
        for side in self.all_sides:
            side.printSide()

    def rotateSide(self, side_from_front_view, direction_clockwise=True):
        side_from_front_view.rotateFromFront(direction_clockwise)
        row_edge_copy = {}

        if side_from_front_view.identifier == "Right" or side_from_front_view.identifier == "Left":
            edge_location_to_amend = side_from_front_view.identifier

            for edge in side_from_front_view.all_neighbours.keys():
                print(edge, side_from_front_view.all_neighbours[edge].identifier)
                row_edge_copy[edge] = side_from_front_view.all_neighbours[edge].getRowOrColumnCopyForRotation(
                    edge_location_to_amend)

            if side_from_front_view.identifier == "Right":
                direction_clockwise = not direction_clockwise
                print("clockwise check, direction_clockwise is", direction_clockwise)

            for edge in side_from_front_view.all_neighbours.keys():

                if direction_clockwise:
                    replacement_edge_key = self.clockwise_transform[edge]
                else:
                    replacement_edge_key = self.anti_clockwise_transform[edge]

                print()
                print(side_from_front_view.all_neighbours[edge].identifier,
                      side_from_front_view.all_neighbours[edge].getRowOrColumnCopyForRotation(
                          edge_location_to_amend),
                      "\nreplaced by\n", replacement_edge_key, row_edge_copy[replacement_edge_key])

                side_from_front_view.all_neighbours[edge].replaceRowOrColumnCopyForRotation(edge_location_to_amend,
                                                                                            row_edge_copy[
                                                                                                replacement_edge_key])

        else:
            True
