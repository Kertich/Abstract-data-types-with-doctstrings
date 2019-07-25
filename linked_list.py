class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        '''
        O(1)
        get the point of the next node

        Parameters:
        ----------
            Takes no parameter.

        Returns:
        -------
            The point pointer to the next node
        '''
        return self.next_node

    def set_next(self, n):
        '''
        O(1)
        sets the pointer of the node

        Parameters:
        ----------
            n:Takes one parameter

        Returns:
        --------
            Returns the pointer to the node assinged to n
        '''
        self.next_node = n

    def get_data(self):
        '''
        O(1)
        Gets the data of a node

        Parameters:
        ----------
            Takes no parameters

        Returns:
        --------
            Returns the data of the node
        '''
        return self.data

    def set_data(self, d):
        '''
        O(1)
        Sets the data to the node

        Parameters:
        ----------
            d(iterables): list, tuple, str
        Returns:
        --------

            Returns the data of the node assinged to d 
        '''
        self.data = d 

class Linkedlist(object):        
    
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        '''
        O(1)
        get the size of a linked list

        Parameters:
        -----------
            Takes no parameters

        Returns:
        --------
            Returns  the size of a listed list
        '''
        return self.size

    def add(self, d):
        '''
        O(n)
        adds a node to a linked list

        Parameters:
        -----------
            d(iterable):list, tuple, str

        Returns:
        --------
            Returns a linked list which has been populated.
        '''
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1

    def remove (self, d):
        '''
        O(n)
        removes a node from a linked list.

        Parameters:
        -----------
            n(iterable): list, tuple, str

        Returns:
        --------
            Bool:True if a node is removed and False is no node is removed
        '''
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # Data not found

    def find(self, d):
        '''
        O(n)
        finds the root of the data of the node

        Parameters:
        -----------
            d(iterable): list, str, tuple

        Returns:
        -------
            Returns the data of the node else return None if it does not find the data
        '''
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
