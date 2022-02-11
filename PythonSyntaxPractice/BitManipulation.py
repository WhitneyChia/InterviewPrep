print("\n")
print("AND Operator -> &")
print("Only becomes 1 if bits of both ints are 1, else 0")
five = bin(5)
thirty = bin(30)

five_and_thirty = 5 & 30
print(f"five -> : {five}")
print(f"thirty -> : {thirty}")
print(f"five_and_thirty -> : {bin(five_and_thirty)}")
print(f"five_and_thirty -> : {five_and_thirty}")

print("\n")
print("OR Operator -> |")
print("Only becomes 1 if bits of at least one of the ints are 1, if both 0, then 0")
five = bin(5)
thirty = bin(30)

five_or_thirty = 5 | 30
print(f"five -> : {five}")
print(f"thirty -> : {thirty}")
print(f"five_or_thirty -> : {bin(five_or_thirty)}")
print(f"five_or_thirty -> : {five_or_thirty}")


print("\n")
print("XOR Operator -> ^")
print("Only becomes 1 if bits of exactly one of the ints are 1, if both 0, then 0")
five = bin(5)
thirty = bin(30)

five_xor_thirty = 5 ^ 30
print(f"five -> : {five}")
print(f"thirty -> : {thirty}")
print(f"five_or_thirty -> : {bin(five_xor_thirty)}")
print(f"five_or_thirty -> : {five_xor_thirty}")

print("\n")
print("XOR Operator -> ^ to fip bits")
flip_me = 0b101
mask = 0b111
print(f"flip_me -> : {flip_me}")
print(f"mask -> : {mask}")
print(f"5 flipped bits -> : {flip_me ^ mask}")
print(f"Our expectation is 5 which is 101 flipped bits = 010 -> 2")

print("\n")
print("Bitshift left <<")
print("Moves Everything to the left, essentially inserting zeroes to the right")
five = bin(5)

five_left_shift_2 = 5 << 2
print(f"five -> : {five}")
print(f"five_left_shift_2 -> : {bin(five_left_shift_2)}")
print(f"five_left_shift_2 -> : {five_left_shift_2}")


print("\n")
print("Bitshift right >>")
print("Moves Everything to the right, essentially moving everything to the right, right bits essentially disappear")
five = bin(5)

five_right_shift_2 = 5 >> 2
print(f"five -> : {five}")
print(f"five_right_shift_2 -> : {bin(five_right_shift_2)}")
print(f"five_right_shift_2 -> : {five_right_shift_2}")


print("\n")
print("Cancel out duplicates using XOR")
print("A number XOR with the same number leads to all 0s")
five = bin(5)

five_xor_five = 5 ^ 5
print(f"five -> : {five}")
print(f"five_xor_five -> : {bin(five_xor_five)}")
print(f"five_xor_five -> : {five_xor_five}")


print("\n")
print("Multiplying using bitshift left")
print("A number x bit shifted left some y is the same as x * (2 ** y)")
five = bin(5)

five_bit_shift_left_three = 5 << 3
print(f"five -> : {five}")
print(f"We are expecting this to be 5 ** 8 -> 40")
print(f"five_bit_shift_left_three -> : {bin(five_bit_shift_left_three)}")
print(f"five_bit_shift_left_three -> : {five_bit_shift_left_three}")


print("\n")
print("Dividing using bitshift right")
print("A number x bit shifted right some y is the same as x / (2 ** y)")
forty = bin(40)

forty_bit_shift_right_three = 40 >> 3
print(f"five -> : {five}")
print(f"We are expecting this to be 40 / 8 -> 5")
print(f"five_bit_shift_two -> : {bin(forty_bit_shift_right_three)}")
print(f"five_bit_shift_two -> : {forty_bit_shift_right_three}")