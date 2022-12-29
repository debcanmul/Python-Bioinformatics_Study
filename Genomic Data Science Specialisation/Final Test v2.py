from email import header
import Bio
fasta_string=open("dna.example.fasta")


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
        


print(len(my_dict))

print(max(my_dict.values()))
my_keys=list(my_dict.keys())

print(list(my_dict.values()))

lengths = [len(v) for v in my_dict.values()]

my_dict_numbers=my_dict.fromkeys(my_keys:str(lengths))
lengths_sorted=(sorted(lengths))
min_len=lengths_sorted[0]
max_len=lengths_sorted[-1]
print(min_len)
print(max_len)
print(my_dict_no)


if min_len==lengths_sorted[1]:
    print("TRUE")
else:
    print("FALSE")

if max_len==lengths_sorted[-2]:
    print("TRUE")
else:
    print("FALSE")

key_list=list(my_dict_no.keys())
val_list=list(my_dict_no.values())

position=val_list.index(min_len)
print(key_list[position])

