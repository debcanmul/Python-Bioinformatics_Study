Testseq="ACGT"
print(Testseq)
adeninetest=Testseq.count("A")
thyminetest=Testseq.count("T")
length=len(Testseq)
contentAT=(adeninetest+thyminetest)/length
print(contentAT)