number_of_usernames = int(input())

unique_usernames = set()

for _ in range(number_of_usernames):
    username = input()
    unique_usernames.add(username)

for name in unique_usernames:
    print(name)
