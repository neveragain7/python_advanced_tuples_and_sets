number_of_lines = int(input())

longest_set = set()

for _ in range(number_of_lines):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(number) for number in first_range.split(",")]
    second_start, second_end = [int(number) for number in second_range.split(",")]

    first_set = set()
    second_set = set()

    for number in range(first_start, first_end + 1):
        first_set.add(number)

    for number in range(second_start, second_end + 1):
        second_set.add(number)

    unique_set = first_set.intersection(second_set)

    if len(unique_set) > len(longest_set):
        longest_set = unique_set

longest_list = [str(number) for number in longest_set]
longest_intersection = ', '.join(longest_list)
longest_length = len(longest_list)

print(f"Longest intersection is [{longest_intersection}] with length {longest_length}")
