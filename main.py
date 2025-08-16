print("-----------------------------------")
print(" $$ WELCOME TO EXPENSE TRACKER $$  ")
print("-----------------------------------")

def segment_inputs(user_input: str) -> None:
  segments: list = user_input.lower().strip().split()
  print(segments)

def get_inputs():
  user_input: str = input("expense-tracker > ")
  segment_inputs(user_input)

def main():
  while True:
    user_input: str = get_inputs()
  
if __name__ == "__main__":
  main()
