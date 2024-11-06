text = input()

symbols = {}

for letter in text:
    if letter not in symbols:
        symbols[letter] = 1
    else:
        symbols[letter] += 1

for letter, count in sorted(symbols.items()):
    print(f"{letter}: {count} time/s")
