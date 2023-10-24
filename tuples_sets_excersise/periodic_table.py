n = int(input())
chem_compounds = set()

for _ in range(n):
    items = input().split()

    # for i in range(len(items)):
    #     compound = items[i]
    #     chem_compounds.add(compound)

    for item in items:
        chem_compounds.add(item)

print(*sorted(chem_compounds), sep="\n")