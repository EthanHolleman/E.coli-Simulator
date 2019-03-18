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
    refDict = {'A':0, 'T':1, 'G':2, 'C':3}

    w, h = 4, 4;
    Matrix = [[0 for x in range(w)] for y in range(h)]

    with open(filePath) as seqFile: #only reading one sequence from fasta currently
        seqFile.readline()
        line = seqFile.readline()

        while line:
            for i in range(len(line)-1):

                try:
                    row = refDict[line[i]]
                    column = refDict[line[i+1]]
                    Matrix[row][column] += 1
                except KeyError:
                    pass

            seqFile.readline()
            line = seqFile.readline()

        for row in Matrix:
            rowTotal = sum(row)
            for i in range(0,4):
                row[i] /=rowTotal

    return Matrix


def simulate(theMatrix, lengthSim, baseComposition):
    #Simulates a given length of e. Coli genome and returns the sequence
    bases = ["A","T","G","C"] #list of canidates
    refDict = {'A':0, 'T':1, 'G':2, 'C':3}
    pi = baseComposition #first matrix based on A, T, G, C comps
    seq = []

    firstBase = np.random.choice(bases,1,pi) #starts the chain
    seq.append(firstBase.item(0))

    for i in range(0,lengthSim):
        pi = theMatrix[refDict[seq[i]]] #reassigns prob for base at current position
        next = (np.random.choice(bases,1,p=pi))
        seq.append(next.item(0))

    return seq

def bulkSim(theMatrix, lengthSim, baseComposition, numSims, runName):

    for i in range(0,numSims):
        seq = simulate(theMatrix, lengthSim, baseComposition)

        with open("output.fasta", "a") as out:
            out.write("< " + runName + "Run: " + i)
