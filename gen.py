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

def createMatrix(filePath):
    #creates a dictionary which will contains the conditional probility of
    #any given two letter word occuring
    dict = {}
    with open(filePath) as seqFile:
        line = seqFile.readline()
        line = line.strip()

        for i in range(len(line)-1):
            word = line[i] + line[i+1]

            if word in dict:
                dict[word] +=1
            else:
                dict[word] = 1
        #need to divide by total words for each "row" to get conditional probs

        return dict


def simulate(theMatrix, lengthSim, baseComposition):
    #Simulates a given length of e. Coli genome and returns the sequence
    bases = ['A', 'T', 'G', 'C'] #list of canidates
    pi = [0.25,0.25,0.25,0.25]
    seq = []
    firstBase = numpy.random.choice(bases,pi)
    seq.append(firstBase)

    for i in range(len(lengthSim)):
        current = seq[i]
        combos = list(map((lambda x: current + x), bases))
        pi = list(map((lambda x: dict[x]), combos))
        next = numpy.random.choice(bases,pi)
        seq.append(next)
    return seq

def simulate(theMatrix, lengthSim, baseComposition, outputPath):
    #Simulates a given length of e. Coli genome and prints to a file
    bases = ['A', 'T', 'G', 'C'] #list of canidates
    pi = [0.25,0.25,0.25,0.25]
    seq = []
    firstBase = numpy.random.choice(bases,pi)
    seq.append(firstBase)

    for i in range(len(lengthSim)):
        current = seq[i]
        combos = list(map((lambda x: current + x), bases))
        pi = list(map((lambda x: dict[x]), combos))
        next = numpy.random.choice(bases,pi)
        seq.append(next)
    with open(outputPath) as out:
        out.write(out)
