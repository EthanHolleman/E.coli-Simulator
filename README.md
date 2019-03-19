
# Overview 
This is a very in progress personal project that attempts to use Markov chains to simulate nucleotide sequences given in fasta formatted files. 
Markov chains are a basic tool of simulation which attempt to predict a future result from previously seen data. This program will use a first order Markov chain meaning it will attempt to simulate the base pair in the n+1 position from a given nucleotide sequence using the n position where n is a known nucleotide. 

Markov chains attempt to make this predication by constructing probability matrices from known data. In this case the known data will be the sequence or sequences provided in the fasta format.

A simple transition matrix could look like the one below.
```{python]
    A   B
A [0.6][0.4]
B [0.3][0.7]
```
The rows represent the current state in the simulation and the columns the conditional probabilities of a given state occurring next. This is why all row totals will always add to 1.

# Design
  The program starts by reading in a fasta file provided by the user. Two test files are included in this project. The GMR30.txt file was taken from the collection of transposable elements within the *Glycine max* (Modern Soybean) Williams 82 assembly. You can download the complete assembly from NCBI [here](https://www.ncbi.nlm.nih.gov/assembly/GCF_000004515.5).
The ecoli sequence is from *Escherichia coli* str. K-12 substr. MG1655 taken from NCBI which can be downloaded in fasta format [here](https://www.ncbi.nlm.nih.gov/genome/167?genome_assembly_id=161521).

  The methods contained in gen.py can be used to extract the base composition and generate the probability matrix used by the simulate and bulkSim methods. It is important to note that currently if you use a fasta file that contains multiple sequences the program will calculate the base composition and probability matrix based on all sequences included in the file and therefore effectively create a consensus matrix. This is best suited for simulations of family grouped elements such as LTR retrotranspososns. 
  
  # Initial Results
  To test the accuracy of the simulation I ran 100 simulations of 1000 base pairs each and then compared the frequency of occurrence of each base pair from all simulations to the actual composition of GMR 30. 
  
![](https://github.com/EthanHolleman/Seq-Sim/blob/master/Images/plot1.png)

While I have not conducted any formal statistical tests to asses if the simulated sequence differs significantly from the consensus sequence (coming soon to a p-value near you) the graph shows a relatively high degree of similarity between the two. The simulated data came from a single run of 13000 base pairs so accuracy may be improved by conducting multiple trials.
