
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
