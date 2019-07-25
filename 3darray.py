class Array:

    def __init__(self):
        self.row=0
        self.col=0
        self.z=0

    def create_array(self, row,col,z):
        """
        O(n)
        This method creates an array with row number of rows, col number of columns and z on the z axis
        
        Parameters
        ----------
        row : int
            The number of rows of the 3D matrix to be formed
            
        col : int
            The number of columns of the 3D matrix to be formed
​
        z : int
            The number of Z axis of the 3D matrix to be formed
             
        Returns
        -------
        Array
            A 3D array of 0's
        """
        
        self.row=row
        self.col=col
        self.z=z
        self.array=[[[0 for _ in range(z)] for _ in range(col)] for _ in range(row)]
        return self.array
    
    def shape(self):
        """
        O(n)
        This method return the number of rows, columns, z axis of the 3D array
        
        Returns
        -------
        Tuple:
            A tuple containing the number of rows, columns and z axis
        """
        return (self.row, self.col, self.z)
        
    def clear_array(self, value):
        """O(1)
        This method clears the array with the arguement value
​
        Parameter:
        ----------
        value : int, float, str
            The value to be filled in when clearing the array
​
        Returns:
        --------
        Array
            An array filled with the replacement value
        """
        self.array=[[[value for _ in range(self.z)] for _ in range(self.col)] for _ in range(self.row)]
        return self.array
        
    def get_element(self,row ,col,z):
        """
        O(1)
        This method gets the element in the specified row, column and z axis
​
        Parameters:
        -----------
        row : int
            The row to accessed
        col : int
        The column to be accessed
        z : int
        The z axis to be accessed
​
        Returns:
        --------
        int, float, str
        The value of the selected element in the array
        """
        if (row > self.row) or (col > self.row) or (z > self.z):
            raise IndexError('Index is out of Range')
        return self.array[row][col][z]
        
    def set_element(self, row, col, z,value):
        """
        O(n)
        This method sets the element of a selected row, column, z axis
        
        Parameters:
        -----------
        row : int
            The row to accessed
        col : int
        The column to be accessed
        z : int
        The z axis to be accessed
        value : int,float,str
            the value to be inserted
​
        Returns:
        --------
        Array
        The array with the value replaced
        """
        if (row > self.row) or (col > self.row) or (z > self.z):
            raise IndexError('Index is out of Range')
        else:
            self.array[row][col][z]=value
        return self.array
        
    #Collapse



