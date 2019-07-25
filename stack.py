class Stack:
    def __init__(self):
        self.val = []

    def isempty(self):
        '''
        O(n)
        Checks if the list is empty

        Parameters:
        ----------
            Takes no parameter

        Returns:
        -------
            Bool:True if list is empty else returns False
        '''

        if len(self.val) == 0:
            return True
        else:
            return False
        
    def push(self, value):
        '''
        O(n)
        adds an item to a list

        Parameters:
        ----------
            value(iterable):tuple, list, str

        Returns:
        -------
            Returns a populated list
        '''
        return self.val.append(value)

    def lenght(self, value):
        '''
        O(1)
        Checks the length of a list

        Parameters:
        ----------
            value(iterable):Tuples, list, str

        Returns:
        -------
            legth:Returns the length of a list
        '''
        return len(value)

    def pop(self, value):
        '''
        O(1)
        Removes the top item in a list

        parameters:
        ----------
            value(iterables): tuples, list, str

        
        Returns:
        -------
            Returns a list which its top value has been removed
        '''
        if value == 0:
            raise ValueError("Can not remove item from an empty list")
        else:
            return value.pop()