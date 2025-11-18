# Fix this so it prints the correct Part 1 of a secret code.
# Hint: Read the comment carefully.

encoded = "xaHR0cHM6Ly9naXRodWIuY29tL0VsbGVzbm93Zmxha2UvQWxs"

# The first character of 'encoded' is junk and should be removed.
# Your goal is to make 'part1' contain the secret string WITHOUT that junk character.

part1 = encoded[0:]  

print("Part 1:", part1)
