#Python for Biologists
#Notes and Exercises

#Chapter 2 Printing and Manipulating Text
# print a friendly greeting
print("Hello World")

#how to add a new line
print("Hello\nWorld")
#Other useful special characters \t and \r


#store a short DNA Sequence in the variable my_dna
my_dna="ATGCGTA"
#now print the DNA sequence
print(my_dna)

#Concatenation~stick together 2 strings using + symbol
my_dna="AATT"+"GGCC"
print(my_dna)

#we can also use variables that point to strings
upstream="AAA"
my_dna=upstream + "ATGC"
print(my_dna)

#we can combine multiple strings in one go
upstream="AAA"
downstream="GGG"
my_dna=upstream + "ATGC" + downstream
print(my_dna)

#Concatenation results in a string, therefore this can be used directly in a print statement
print("Hello"+" "+"world")

#Finding the length of a string
dna_length=len("AGTC")
print(dna_length)

#To be able to print the value of the length which is a number you have to change the data type to a string
my_dna="ATGCGAGT"
dna_length=len(my_dna)
print("The length of the DNA sequence is " + str(dna_length))

#The method lower belongs to the string type. The code below prints the variable my_dna in lower case
my_dna="ATGC"
print(my_dna.lower())
#note above when we use a method we type the varaible name then a period then then method name and then parentheses. There is no argument in the parentheses in this case.
#The variable my_dna is not permanently changed to lower case. It would need to be saved as a new varaible.

#replacement
protein = "vlspadktnv"
# replace valine with tyrosine
print(protein.replace("v", "y"))
# we can replace more than one character
print(protein.replace("vls", "ymt"))
# the original variable is not affected
print(protein)

#Extracting Part of a String (substring)
protein = "vlspadktnv"
# print positions three to five
print(protein[3:5])
# positions start at zero, not one
print(protein[0:6])
# if we use a stop position beyond the end, it's the same as using the end
print(protein[0:60])
#Note index starts at zero, the first number in brackets is inclusive the second number is exclusive.

#Counting and Finding Substrings
protein = "vlspadktnv"
# count amino acid residues
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')
# now print the counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))

#Finding the location of a substring in a sequence (Index)
protein = "vlspadktnv" 
print(str(protein.find('p'))) 
print(str(protein.find('kt'))) 
print(str(protein.find('w'))) 
#Note if you ask to find a charater that is not in the string the output will be -1
#Note: If you need to count the number of occurrences of a variable protein motif, or find the position of a variable transcription factor binding site, they will not help you.

#Exercises
#Calculating AT content
#Define a variable for the DNA Sequence
dna_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Find the number of Adenine Nucleotides in the DNA Sequence 
Adenine_count=dna_seq.count('A')
#Find the number of Thymine Nucleotides in the DNA Sequence 
Thymine_count=dna_seq.count('T')
#Find the total AT content by adding the Adenine_count and Thymine_count variables
AT_content=Adenine_count+Thymine_count
#print the total content using the string function to print the numerical value of the variable AT_content
print("AT_content: " + str(AT_content))

#Find the total length of the DNA Sequence
dna_seq_length=len(dna_seq)
print(str(dna_seq_length))

#Find the percentage of the total AT content in the DNA sequence
Percent_AT_Content=(AT_content/dna_seq_length)*100
print("The total content of AT is: "+str("%d" % Percent_AT_Content)+"%")
#Note: the %d gives the number to the nearest decimal. I need to work out how to get 1 decimal place.

#The best thing to do is to run a test on a shorter dna sequence. Write the whole code and test it on a shorter sequence. 
#This is the test example from the book.
test_dna = "ATGC"
length = len(test_dna)
a_count = test_dna.count('A')
t_count = test_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))

#This is the full solution from the book. I've calculated it differently but the final answer is the same. I've left it as a percentage.
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))

#Complementing DNA pdf page 50

#Define a variable for the DNA Sequence
DNA_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#Change DNA_seq to lower case
DNA_seq_lower=DNA_seq.lower()
#Print to check the variable is in lower case
print(DNA_seq_lower)

#Tried to work out a loop for this exercise but it didn't work. 
for n in DNA_seq_lower:
    DNA_seq_lower.replace("a","T")
    DNA_seq_lower.replace("t","A")
    DNA_seq_lower.replace("c","G")
    DNA_seq_lower.replace("g","C")
print(DNA_seq_lower)

#Will use a different method for finding the complement
#Define a new variable to assign the change of a to the complement T
DNA_seq_a=DNA_seq_lower.replace("a","T")
print(DNA_seq_a)
#Define a new variable, but use the previous variable with the replace method
DNA_seq_t=DNA_seq_a.replace("t","A")
print(DNA_seq_t)
DNA_seq_c=DNA_seq_t.replace("c","G")
print(DNA_seq_c)
DNA_seq_g=DNA_seq_c.replace("g","C")
print(DNA_seq_g)

#This is the answer in the book. I get the same answer but I did it differently. 
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())

#Now on Restriction Fragment Lengths Exercise - pdf 45
#Define the DNA Sequence variable
dna_seq="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
#Find the position of the motif "GAATTC"
position_dna_seq=(dna_seq.find("GAATTC"))
#print the position of the first nucleotide of the motif
print(str(position_dna_seq))
#Find the length of the entire DNA Seq
dna_seq_length=len(dna_seq)
#Print the length of the DNA seq
print(dna_seq_length)
#Calculate the length of the first fragment
section1=position_dna_seq-1
#Calculate the length of the second fragment
section2=dna_seq_length-section1
#Print the length of the first fragment
print("The first section has " + str(section1)+" nucelotides.")
#Print the length of the second fragment
print("The second section has "+ str(section2)+" nucelotides.")

#This is the solution, I should have added one instead of subtract 1 because the index starts at zero.
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))

