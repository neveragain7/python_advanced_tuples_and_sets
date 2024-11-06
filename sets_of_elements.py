first_range, second_range = [int(number) for number in input().split()]

first_set = set()
second_set = set()

for _ in range(first_range):
    number = int(input())
    first_set.add(number)

for _ in range(second_range):
    number = int(input())
    second_set.add(number)

unique_numbers = first_set.intersection(second_set)

for number in unique_numbers:
    print(number)
