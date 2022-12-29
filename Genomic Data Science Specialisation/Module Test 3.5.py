def count5(dna, base):
    return len([i for i in range(len(dna)) if dna[1]== base])

print(count5("ctguctguacgu","c"))