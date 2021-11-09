user_input = input("Enter a phrase:\n")

try:
    print(f"1: {user_input[3]}\n",
          f"2: {user_input[-2]}\n",
          f"3: {user_input[0:5]}\n",
          f"4: {user_input[-2:]}\n",
          f"5: {user_input[::2]}\n",
          f"6: {user_input[1::2]}\n",
          f"7: {user_input[::-1]}\n",
          f"8: {user_input[::-2]}\n",
          f"9: {user_input[-2::-2]}\n",
          f"10: {user_input[-2:1:-1]}\n",
          f"11: Length of the string is {len(user_input)}\n",
          sep=""
          )
except IndexError as e:
    print(e)
