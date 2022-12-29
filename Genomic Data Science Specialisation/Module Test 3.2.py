def count2(dna, base):
    i=0
    for j in rangw(len(dna)):
        if dna[j]==base:
        i+=1
    return i

count2("ctguctguacgu","c")