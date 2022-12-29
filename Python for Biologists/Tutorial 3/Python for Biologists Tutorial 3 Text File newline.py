# open the file
my_file = open("dna.txt")

# read the contents
my_dna = my_file.read()

# calculate the length
dna_length = len(my_dna)

# print the output
print("sequence is " + my_dna +  " and length is " + str(dna_length))

#Exercises
#split the data into coding and non-coding parts and write these sequences as two separate files. 
#open the file and read its contents

dna_file=open("genomic_dna.txt")
my_dna=dna_file.read()

#extract the difference bits of DNA sequence
exon1=my_dna[0:62]
intron=my_dna[62:90]
exon2=my_dna[90:1000]

#open the two output files
coding_file=open("coding_file.txt","w")
noncoding_file=open("noncoding_dna.txt","w")

#write the sequences to the output files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)

#print the results
print(coding_file)