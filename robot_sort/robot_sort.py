class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        """
        Thoughts:
        An optimal solution feels like it would be structured like so:
        - As we move right, find the largest element and place it at 
        the end.
        - As we move left, find the smallest element and place it at 
        the beginning.
        - Now, each end is sorted. Perhaps we could set indices as 
        sorted-unsorted boundaries?

        After some reflection, we only have one "boundary" to work with 
        (the None value left behind when the robot picks up an item) so 
        2-way sorting doesn't seem possible to implement (at least with 
        my knowledge rn)
        """

        """ 
        Plan:
        - Turn light on
        -  While can_move_right:
        -   Move right
        -   Compare
        -   Swap if item in list is smaller. Once we reach the end of 
        the list, we are holding the smallest element in the unsorted 
        list.
        - Now we move left until we find our None value in the list. We
        place the smallest element in the beginning. We immediately 
        move to the right (if possible) and pick up the value there, 
        leaving a None value at the next position. This None value 
        serves as our sorted-unsorted boundary.
        - Repeat this process until we've reached the end of the list.
        """
        
        # Turns robot's light on so it can see.
        self.set_light_on
        
        """
        Picks up item at first index of unsorted array, leaving None at 
        that index. This while loop allows us to repeat the process of 
        traversing the list to the right, searching for the smallest 
        element and traversing back to the left and placing it at the
        sorted-unsorted barrier. When we are no longer able to move 
        right, our list is sorted.
        """
        while self.can_move_right():
            self.swap_item()

            """
            While we are able to move right, move right and compare 
            currently held item. Swap if necessary. At the end of this 
            while loop our robot is holding the smallest element in the 
            unsorted portion of the list.
            """
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == 1:
                    self.swap_item()

            """
            Traverse left in the list until we find our None value 
            (sorted-unsorted barrier)
            """
            while self.compare_item() != None:
                self.move_left()
                
            """
            Our robot is currently holding the smallest element in the 
            unsorted array and is at the sorted-unsorted barrier. Place 
            smallest element at this barrier and move right.
            """
            self.swap_item()
            self.move_right()
        
        # List is now sorted. Robot's light can be turned off. Good job, bud.
        self.set_light_off()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)