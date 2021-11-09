user_input = input("Enter a phrase:\n")
length = len(user_input)

if length//2:
    length_of_a_half = length//2
else:
    length_of_a_half = length//2 + 2

left_part = user_input[0:length_of_a_half]
right_part = user_input[length_of_a_half:]
print(right_part+left_part)
