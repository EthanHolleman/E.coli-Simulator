# E.coli-Simulator
This is a very in progress personal project that attempts to use Markov chains to simulate different aspects of the E. coli genome 

# Overview 
Markov chains are a basic tool of simulation which attempt to predict a future result from previously seen data. This program will use a first order Markov chain meaning it will attempt to simulate the base pair in the n+1 position from a given nucleotide sequence from the n position. 

Markov chains attempt to make this predication by constructing probability matrices from known data. In this case the known data will be the sequence of the E. coli genome. 

# Planned Structure 

### First 
The program will read the Escherichia coli str. K-12 substr. MG1655 taken from NCBI which can be downloaded in fasta format (here)[https://www.ncbi.nlm.nih.gov/genome/167?genome_assembly_id=161521]. The script will then extract the overall base composition and frequency of each two-base combination.

A given sequence will effectively be read two lines at a time and be parsed like this
```
AA TT GT AT GT AG TA ... NN
```

### Second
A probability matrix will then be constructed from the data produced in step one. An initial probability matrix based on the base composition will also be created.

### Third 
Many E. coli genomes will be sequenced and then the average sequence will become the output and compared to the original.
