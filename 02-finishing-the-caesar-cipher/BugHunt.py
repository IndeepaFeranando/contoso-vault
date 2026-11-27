item_code: str = "TEA-250G"
letters: int = 0
for character in item_code:
 if "A" <= character <= "Z":
    letters += 1
print("Letters:", letters)
