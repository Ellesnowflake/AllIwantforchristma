import base64

print("Paste the values exactly as printed by Step 1 and Step 2.\n")

part1 = input("Part 1: ").strip()
part2 = input("Part 2: ").strip()

combined = part1 + part2

try:
    url = base64.b64decode(combined).decode("utf-8")
    print("\n🎅 Merry Christmas! Open this link to see your surprise:\n")
    print(url)
except Exception as e:
    print("Hmm, something went wrong decoding. Check that you pasted Part 1 and Part 2 correctly.")
