#read each line as a string then do math on each string
from numpy.random import choice

dict = {}
sums = [0,0,0,0] #in format A, T, G, C

def baseComp(filePath): #calculates base composition of a files
    with open(filePath) as seqFile:
        seqFile.readline()
    count = [0]*10
    for line in seqFile:
        noWhite = line.strip()
        count[0] += noWhite.count('A')
        count[1] += noWhite.count('T')
        count[2] += noWhite.count('G')
        count[3] += noWhite.count('C')

    #this method will then send the base composition list to the simulate Method and createMatrix
    #next step is to create the probabilty matrix
        #count composition overall and use to calculate conditional compositions in create matrix


def createMatrix(filePath):
    with open(filePath) as seqFile:
        seqFile.readline()

            for i in range(0,(len(noWhite)-1)):
                first = noWhite[i]
                read = noWhite[i] + noWhite[i+1] #creates two letter words

                if read in dict:
                    dict[read] +=1
                else:
                    dict[read] = 1
                    print('new one')

    keys = dict.keys()
    #next need to divide number of hits by total read to get overall composition
    #divide overall comp by first base composition to create conditional composition



def basePicker()

#Now we want to simulate the data
def simulate(theMatrix, lengthSim, baseComposition):
    bases = ['A', 'T', 'G', 'C'] #list of canidates

    #retrive probability
        #for loop
            #takes first base from bases list and loops through all possible and
            #uses that as the key to generate probabilty distrabutions
            #returns a matrix (nested lists in A, T, G, C )
            #each base will be a list with the four possible 2 letter words

            
    #want to create a simulated sequence
    #first base is determined by overall composition of ecoli
    #use choice fuction here need to create a better probability matrix from the dictionary
