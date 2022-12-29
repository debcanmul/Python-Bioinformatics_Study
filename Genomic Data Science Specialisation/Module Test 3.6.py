def count6(dna, base):
    return sum(c==base for c in dna)

print(count6("ctguctguacguc","c"))