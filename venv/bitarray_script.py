from bitarray import bitarray

# Create a bit array of size 10, all bits initialized to 0
bit_arr = bitarray(10)
bit_arr.setall(0)

print("Initial bit array:", bit_arr)

# Set the 3rd and 5th bits to 1
bit_arr[2] = 1
bit_arr[4] = 1

print("Updated bit array:", bit_arr)

# Check the value of the 3rd and 5th bits
print("3rd bit:", bit_arr[2])
print("5th bit:", bit_arr[4])

# Check the value of the 6th bit (which is 0)
print("6th bit:", bit_arr[5])
