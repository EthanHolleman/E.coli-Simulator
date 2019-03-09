from gen import baseComp, createMatrix, simulate

def main():
  sums = baseComp("GMR30.txt")
  dict = createMatrix("GMR30.txt")

  seq = simulate(dict, 10000, sums)
  out = ""
  for i in range(1,len(seq)):
     letter = str(seq[i])
     letter = letter[2]
     out = out + letter

print(out)

if __name__ == "__main__": main()
