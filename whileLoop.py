
# prompts you to add number until it arrives the set number in the while loop

i = 1
while i <= 6:              # while i is less than or equal to 5, print i
        print(i)
        i += 2           # adds 1 to i and keeps adding till it reaches 5


name = ''                                                              # so the loop runs at least once
while name != 'exit':
      name = input("Enter your name (or 'exit' to quit): ")            # Uses input() to get a name
      if name != 'exit':
        print(f"You entered: {name}")                                  # Repeats as long as the user doesn’t type "exit"
