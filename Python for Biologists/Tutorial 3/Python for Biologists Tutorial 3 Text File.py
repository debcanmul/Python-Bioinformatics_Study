#open the file
my_file=open("dna.txt")

#read the contents
file_contents=my_file.read()

#remove the newline from the end of the file contents
my_dna=file_contents.rstrip("\n")
my_dna_count=my_dna.count(my_dna)
print(my_dna)

#calculate the length
dna_length=len(my_dna)

#print the output
print("sequence is " +my_dna+ " and length is "+ str(dna_length))