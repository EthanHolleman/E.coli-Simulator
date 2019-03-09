#read each line as a string then do math on each string
import numpy as np

def baseComp(filePath): #calculates base composition of a files
    sums = [0,0,0,0]

    with open(filePath) as seqFile:
        seqFile.readline()
        line = seqFile.readline()

        while line:
            for line in seqFile:
                line = line.strip()

                sums[0] += line.count('A')
                sums[1] += line.count('T')
                sums[2] += line.count('G')
                sums[3] += line.count('C')

            seqFile.readline()
            line = seqFile.readline()

    total = sum(sums)
    sums = map(lambda x: x / total, sums)
    return list(sums)

def createMatrix(filePath):
    #creates a dictionary which will contains the conditional probility of
    #any given two letter word occuring
    dict = {}
    count = 0
    with open(filePath) as seqFile: #only reading one sequence from fasta currently
        seqFile.readline()
        line = seqFile.readline()
        line = line.strip()

        while line:

            for i in range(len(line)-1):
                word = line[i] + line[i+1]

                if word in dict:
                    dict[word] +=1
                    count += 1
                else:
                    dict[word] = 1
                    count += 1

            seqFile.readline()
            line = seqFile.readline()
            line = line.strip()

    for word in dict:
        dict[word] = dict[word] / count
    print(count)
    return dict


def simulate(theMatrix, lengthSim, baseComposition):
    #Simulates a given length of e. Coli genome and returns the sequence
    #theMatrix should be dictionary from createMatrix

    bases = ['A', 'T', 'G', 'C'] #list of canidates
    pi = baseComposition #first matrix based on A, T, G, C comps
    combos = []
    seq = []

    firstBase = str(np.random.choice(bases,1,pi))
    seq.append(firstBase)

    for i in range(0,lengthSim):

        current = str(seq[i])
        current = current[2]
        combos = [current + letter for letter in bases]
        pi = [theMatrix[x] for x in combos]

        next = str(np.random.choice(bases,1,pi))
        seq.append(next)


    return seq

def bulkSim(theMatrix, lengthSim, baseComposition, numSims, runName):

    for i in range(0,numSims):
        seq = simulate(theMatrix, lengthSim, baseComposition)

        with open("output.fasta", "a") as out:
            out.write("< " + runName + "Run: " + i)
