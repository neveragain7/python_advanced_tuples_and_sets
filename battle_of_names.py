number_of_lines = int(input())

odd_set = set()
even_set = set()

for row in range(1, number_of_lines + 1):
    name = input()
    name_sum = sum([ord(letter) for letter in name]) // row
    if not name_sum % 2 == 0:
        odd_set.add(name_sum)
    else:
        even_set.add(name_sum)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    result = odd_set.union(even_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

results = [str(value) for value in result]
result_values = ', '.join(results)

print(result_values)
