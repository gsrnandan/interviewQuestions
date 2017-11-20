import unittest

input = [1,-2,[3,4],[5,[6,7],8],'e',[10,20,[30,40],[50,[60,70],80]],1,2,[3,4],[5,[6,7],8],9,[10,20,[30,40],[50,[60,70],80]]]



def flattenList(inputList):
    outputList = []
    for i in inputList:
        if isinstance(i,int):
            outputList.append(i)
        elif isinstance(i,list):
            outputList.extend(flattenList(i))
        else:
            raise TypeError("Element {0} has unsupported type ({1})".format(i,type(i).__name__))
    return outputList



class FlattenListTestCase(unittest.TestCase):
    """Tests for the flattenList function"""
    
    def test_EmptyList(self):
        """Test to check if the input list is empty
        """
        self.assertEqual(flattenList([]),[])
        
    def test_singleElement(self):
        """ Test to check if there is only one element in the list
        """
        self.assertEqual(flattenList([10]),[10])
        
    def test_flattenedList(self):
        """ Test to check a flattened input list
        """
        self.assertEqual(flattenList([33,45,67,88]),[33,45,67,88])
    
    def test_multipleNestedSingleElementList(self):
        """ Test to check a nested list with a single element
        """
        self.assertEqual(flattenList([[6]]),[6])
        
    def test_nestedList(self):
        """ Test to check a nested List
        """
        actual = [1,[2],[3,4],[[5],6]]
        expected = [1,2,3,4,5,6]
        self.assertEqual(flattenList(actual, expected)
        
    def test_emptyNestedList(self):
        """ Test to check a nested list with an empty list
        """
        self.assetEqual(flattenList([1,[[],2]]),[1,2])
        
    def test_invalidInput(self):
        """ Test to check a list with invalid input type
        """
        self.assertRaises(TypeError, flatlist, 365)
        with self.assertRaises(TypeError):
            flattenList(365)
        with self.assertRaises(TypeError):
            flattenList([3,"et"])
        with self.assertRaises(TypeError):
            flattenList(None)
            
if __name__ == '__main__':
    unittest.main()
