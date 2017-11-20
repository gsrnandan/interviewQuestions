""" Defines a tracker class for tracking the input temperatures
"""

class TempTracker():
	"""Temperature Tracker class 
	"""

	def __init__(self):
		
		#A list to store the input temperature values
		self._tempTrackerList = []


	def isValid(self,temperature):
	     """Method to validate the input temperature type and range
		 
		 This method reads the input value and checks if the temperature is within the
		 range of (0-110) and if its a valid int type
		 
		 Args:
		     temperature (int): The temperature value
		     
		 Return:
		     (bool): Returns True if its a valid input, if not returns False
		 
	      """
			if isinstance(temperature, (int,float,long)):
				if temperature>=0 and temperature <= 110:
					return True
			return False


	def insert(self,*listOfTemps):
			"""Method to insert a new temperature into the existing list of temperatures

			    This function takes an integer argument and adds it to the tempTrackerList
			    
			    Args:
			    	listOfTemps (list): List of temperatures 
			 """
			for temperature in listOfTemps:
				if self.isValid(temperature) :
					self._tempTrackerList.append(int(temperature))

				else:
					print "skipped adding '{0}' as it is either an Invalid temperature type or Range".format(temperature)

	def get_max(self):
			"""Method to return the maximum of all the temperatures in the Tracker
				
			   This function will return the max of tempTrackerList
			   
			   Return:
			   	(int): The maximum value in the list of temperatures
			 """

			if self._tempTrackerList:
				return max(self._tempTrackerList)	


	def get_min(self):
			"""Method to return the minimum of all the temperatures in the Tracker
				
			   This function will return the min of tempTrackerList
			   
			   Return:
			   	(int): The minimum value in the list of temperatures
			"""
			if self._tempTrackerList:
				return min(self._tempTrackerList)	

		
	def get_mean(self):
			"""" Method to return the mean of all the temperatures tracked
				
			      This function will calculate the mean of all integer values inside the tempTrackerList. The return type is float
			      
			      Return:
			      	    (float): Returns the average of all the temperatures in the list of temperatures.
			"""

			if self._tempTrackerList:
				noOfElements = float(len(self._tempTrackerList))
				sumOfElements = float(sum(self._tempTrackerList))
				mean = (sumOfElements/noOfElements)
				return mean	


if __name__ == '__main__':
    unittest.main()
    tt = TempTracker()
    tt.insert(33,34,108)
    print tt.get_mean()
    print tt.get_max()
    print tt.get_min()


