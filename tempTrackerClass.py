class TempTracker():
	"""This is a tracker class for temperature. """

	def __init__(self):
		
		self._tempTrackerList = []


	def isValid(self,temperature):

			"""This function validates the input type and range

				This takes the temperature value and checks if the temperature is within the 
				range of (0-110) and if its a valid int type
			"""
			if isinstance(temperature, (int,float,long)):
				if temperature>=0 and temperature <= 110:
					return True
			return False


	def insert(self,*listOfTemps):
			"""This function inserts a new temperature into the existing list of temperatures

				This function takes an integer argument and adds it to the tempTrackerList
			"""
			for temperature in listOfTemps:
				if self.isValid(temperature) :
					self._tempTrackerList.append(int(temperature))

				else:
					print "skipped adding '{0}' as it is either an Invalid temperature type or Range".format(temperature)

	def get_max(self):
			"""This will return the maximum of all the temperatures in the Tracker
				
			   This function will return the max of tempTrackerList
			"""

			if self._tempTrackerList:
				return max(self._tempTrackerList)	


	def get_min(self):
			"""This will return the minimum of all the temperatures in the Tracker
				
			   This function will return the min of tempTrackerList
			"""
			if self._tempTrackerList:
				return min(self._tempTrackerList)	

		
	def get_mean(self):
			"""" This functions returns the mean of all the temperatures tracked
				

				This function will calculate the mean of all integer values inside the tempTrackerList. The return type is float
			"""

			if self._tempTrackerList:
				noOfElements = float(len(self._tempTrackerList))
				sumOfElements = float(sum(self._tempTrackerList))
				mean = (sumOfElements/noOfElements)
				return mean	
