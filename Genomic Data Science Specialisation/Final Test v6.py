from email import header
import Bio
fasta_string=open("dna2.fasta")


my_dict={}
for line in fasta_string:
        #let's discard the newline at the end (if any)
    line=line.rstrip()
        #distinguish header from sequence
    if line[0]==">":
        words=line.split()
        name=words[0][1:]
        my_dict[name]=''
    else: #sequence, not header
        my_dict[name]=my_dict[name]+line
        
#Q1

print(len(my_dict))

#Q2
lengths = [len(v) for v in my_dict.values()]
print(lengths)
#Q3
lengths_sorted=(sorted(lengths))
min_len=lengths_sorted[0]
max_len=lengths_sorted[-1]
print(min_len)
print(max_len)
#Q4
if min_len==lengths_sorted[1]:
    print("TRUE")
else:
    print("FALSE")

if max_len==lengths_sorted[-2]:
    print("TRUE")
else:
    print("FALSE")

#Q5

print(my_dict)
position_max=lengths.index(max_len)
print(position_max)
print(my_dict[name])



