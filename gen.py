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

        #still need to divide by row totals for each cell of matrix
        for row in Matrix:
            rowTotal = sum(row)
            for i in range(0,4):
                row[i] /=rowTotal
            #print(sum(row)) check role totals == 1

    return Matrix


def simulate(theMatrix, lengthSim, baseComposition):
    #Simulates a given length of e. Coli genome and returns the sequence
    #theMatrix should be dictionary from createMatrix

    bases = [0,1,2,3] #list of canidates
    refDict = {'A':0, 'T':1, 'G':2, 'C':3}
    pi = baseComposition #first matrix based on A, T, G, C comps

    firstBase = str(np.random.choice(bases,1,pi))
    seq.append(firstBase)

    for i in range(0,lengthSim):
        try:
            row = refDict[seq[i]] #takes current base in seq converts to int key
        except:
            pass

        pi = [theMatrix[row][x] for x in bases] #conditional probs for each row
        next = str(np.random.choice(bases,1,pi)) #pics 1 base from all possible
        seq.append(next)

    return seq

def bulkSim(theMatrix, lengthSim, baseComposition, numSims, runName):

    for i in range(0,numSims):
        seq = simulate(theMatrix, lengthSim, baseComposition)

        with open("output.fasta", "a") as out:
            out.write("< " + runName + "Run: " + i)

