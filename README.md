# Seq Sim
This is a very in progress personal project that attempts to use Markov chains to simulate nucleotide sequences given in fasta formatted files. 

# Overview 
Markov chains are a basic tool of simulation which attempt to predict a future result from previously seen data. This program will use a first order Markov chain meaning it will attempt to simulate the base pair in the n+1 position from a given nucleotide sequence using the n position where n is a known nucleotide. 

Markov chains attempt to make this predication by constructing probability matrices from known data. In this case the known data will be the sequence or sequences provided in the fasta format.

# Planned Structure 

### Start 
The program starts by reading in a fasta file provided by the user. Two test files are included in this project. The GMR30.txt file was taken from the collection of transposable elements within the *Glycine max* (Modern Soybean) Williams 82 assembly. You can download the complete assembly from NCBI (here)[https://www.ncbi.nlm.nih.gov/assembly/GCF_000004515.5].
The ecoli sequence is from *Escherichia coli* str. K-12 substr. MG1655 taken from NCBI which can be downloaded in fasta format (here)[https://www.ncbi.nlm.nih.gov/genome/167?genome_assembly_id=161521].


The methods contained in gen.py can be used to extract the base composition and generate the probability matrix used by the simulate and bulkSim methods. It is important to note that currently if you use a fasta file that contains multiple sequences the program will calculate the base composition and probability matrix based on all sequences included in the file and therefore effectively create a consensus matrix. This is best suited for simulations of family grouped elements such as LTR retrotranspososns. 

### Middle

Once you have created a probability matrix and calculated the overall base composition you can then run a simulation. The intial matrix used to start the chain is determined by the base composition calculated in the previous step. A current issue is that the matrix probabilities are the total count of a given two letter word divided by the total words counted. This is incorrect and should be instead the total count of a two letter word divided by the row total for the word's first letter. This correction is coming soon. 

### End
The sequences from all simulations can then be saved in a txt or fasta file. A R script that preforms basic analysis on the results will be coming soon.
