import unittest

class ftuple:
    __internal = ()

    def __init__(self):
        # Constructor, initializes an empty ftuple
        self.__internal = ()
    def __str__(self):
        # toString, represents the ftuple to a string
        return ''.join('self.__internal')
    def __repr__(self):
        # toStringRepr, represents the ftuple to a string. 
        # Used for proper integration in the REPL
        return ''.join('self.__internal')
    def __getitem__(self, key):
        return self.__internal[key]
    def __len__(self):
        return len(self.__internal)

    @staticmethod
    def tuple_from(list):
        # converts a list or array to a tuple
        acc = ftuple()
        acc.__internal = tuple(list)
        return acc

    def push(self, val):
        # Pushes a value at the end of a tuple
        ret = ftuple()
        if type(val) == tuple or type(val) == list:
            t = ftuple.tuple_from(val)
            innerTuple = t.map(lambda x: x)
            ret.__internal = self.__internal + innerTuple.__internal
        else:
            ret.__internal = self.__internal + (val,)
        return ret

    def pop(self):
        # Pops the last value of a tuple
        return ftuple.tuple_from(self.__internal[:-1])

    def car(self):
        # Returns the first element of a tuple
        # If confused, check out lisp
        return self.__internal[0]

    def cdr(self):
        # Returns the tuple without the first element
        # If confused, check out lisp
        return ftuple.tuple_from(self.__internal[1:])

    def sort(self):
        # sorts a given tuple
        list = sorted(self.__internal)
        ret = ftuple.tuple_from(list)
        return ret

    def map(self, fn):
        # Applies a given function to all the elements of a tuple, list or array. 
        # Returns a tuple reflecting the changes made by the function
        ret = ftuple()
        for i in self.__internal:
            val = fn(i)
            ret = ret.push(val)
        return ret

    def filter(self, cond):
        # returns an array containing only the elements that cause comp to return true.
        return self.map(lambda x: x if (cond(x) == True) else ())
    
    def find(self, cond):
        # Returns the first element that causes cond to return true. 
        # Returns False if no elements were found
        found = self.filter(cond)
        return found[0] if len(found) >= 1 else False

    def sum(self):
        # Sums the value of all the elements in the tuple
        # If objects are store, 
        # be sure they implement the necessary interfaces for the + operator
        if len(self.__internal) == 1:
            return self.__internal[0]
        elif len(self.__internal) == 0:
            return 0
        else:
            return self.car() + self.cdr().sum()

class testFtuple(unittest.TestCase):
    def test_construction(self):
        self.assertTrue(len(ftuple()) == 0)

    def test_push(self):
        self.assertEqual(ftuple().push(1)[0], ftuple.tuple_from((1,))[0])
        self.assertEqual(ftuple().push((1,2))[1], ftuple.tuple_from((1,2))[1])

    def test_pop(self):
        self.assertTrue(len(ftuple().push(1).pop()) == 0)
        self.assertEqual(ftuple().push((1,2)).pop()[0], (1))
    
    def test_car_cdr(self):
        self.assertEqual(ftuple().push(1).car(), (1))
        self.assertEqual(ftuple().push((1,2)).cdr()[0], (2))
    
    def test_sort(self):
        self.assertEqual(ftuple().push((2,1)).sort()[0], (1))
        self.assertEqual(ftuple().push((2,1)).sort()[1], (2))
    
    def test_map(self):
        self.assertEqual(ftuple().push((1,2)).map(lambda x: x + 1)[0], (2))
        self.assertEqual(ftuple().push((1,2)).map(lambda x: x + 1)[1], (3))
    
    def test_filter(self):
        self.assertEqual(ftuple().push((1,2,3)).filter(lambda x: x > 1)[0], (2))
        self.assertEqual(ftuple().push((1,2,3)).filter(lambda x: x > 1)[1], (3))

    def test_find(self):
        self.assertEqual(ftuple().push((1,2,3)).find(lambda x: x == 4), False)
        self.assertEqual(ftuple().push((1,2,3)).find(lambda x: x == 1), 1)

    def test_sum(self):
         self.assertEqual(ftuple().push((1,2,3)).sum(), 6)
         self.assertEqual(ftuple().push((1)).sum(), 1)
         self.assertEqual(ftuple().push(()).sum(), 0)

if __name__ == '__main__':
    unittest.main()
