number_of_lines = int(input())

unique_compounds = set()

for _ in range(number_of_lines):
    compounds = input().split()
    for compound in compounds:
        unique_compounds.add(compound)

for compound in unique_compounds:
    print(compound)
