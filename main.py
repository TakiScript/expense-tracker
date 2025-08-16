print("-----------------------------------")
print(" $$ WELCOME TO EXPENSE TRACKER $$  ")
print("-----------------------------------")

def get_inputs():
  user_input: str = input("expense-tracker > ")
  return user_input

def main():
  while True:
    user_input = get_inputs()
    print(user_input)
  
if __name__ == "__main__":
  main()
