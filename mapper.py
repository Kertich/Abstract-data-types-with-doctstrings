class Mapper:
    def __init__(self):
        self.iterable=[]
        
    def map(self, func, iterable):
        """
        O(1)
        This method maps a given function using the values of an iterable
​
        Parameters
        ----------
        func : function
            The function that it is to be used to map
​
        iterable : list, tuple, str
            The iterable to be mapped to a given function
​
        Returns:
        --------
        list:
            A list of the mapped values
        """
        ans=[]
        try:
            for x in iterable:
                s=func(x)
                ans.append(s)
        except TypeError:
            ans='Ensure that you enter an iterable object (list, tuple or str) of the right type with regards to the function used'
        return ans