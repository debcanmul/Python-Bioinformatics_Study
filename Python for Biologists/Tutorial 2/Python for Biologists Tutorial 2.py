
from os import read


print("Hello World")

#Calculating AT Content
shortDNASeq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

adenine_count=shortDNASeq.count('A')
print(adenine_count)

thymine_count=shortDNASeq.count('T')
length=len(shortDNASeq)
print(length)

print("length: "+str(length))
print("adenine: "+str(adenine_count))
print("thymine: "+str(thymine_count))

#run the same code with a smaller DNA Sequence to check the code works
DNASeqTest="ACTG"
lengthtest=len(DNASeqTest)
adenine_test=DNASeqTest.count("A")
thymine_test=DNASeqTest.count("T")
content_AT=(adenine_test+thymine_test)/lengthtest
print(content_AT)

#the code worked on the test code so it can now be used on the main data
content_AT_short=(adenine_count+thymine_count)/length
print(content_AT_short)

#complementing DNA - lower case was used to prevent changes to already changed in a previous line of code
print(shortDNASeq)

replacement1=shortDNASeq.replace("A","t")
print(replacement1)

replacement2=replacement1.replace("T","a")
print(replacement2)

replacement3=replacement2.replace("C","g")
print(replacement3)

replacement4=replacement3.replace("G","c")
print(replacement4)

print(replacement4.upper())

#Restriction Fragment Lengths
Fragment="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print(str(Fragment.find("GAATTC")))
length_Frag=(len(Fragment))
print(length_Frag)
Fragment2=length_Frag-22
print(str(Fragment2))

#splicing out introns, part one
splicingintron1="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=splicingintron1[0:62]
exon2=splicingintron1[90:10000]
print(exon1+exon2)

#splicing out introns, part two
coding_length=len(exon1+exon2)
total_length=len(splicingintron1)
print(100*coding_length/total_length)

#splicing out introns, part three
intron=splicingintron1[62:90]
print(exon1+intron.lower()+exon2)

#the lower case could be used when setting the name of the string instead of in the print command
intron_lower=splicingintron1[62:90].lower()
print(intron_lower)

#the whole exercise could be completed in a single print command but this is less open and reproducible
print(splicingintron1[0:62]+splicingintron1[62:90].lower()+splicingintron1[90:10000])