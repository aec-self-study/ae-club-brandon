def is_even(x):
  return (x % 2 == 0)
  
def is_odd(x):
  return (x % 2 != 0)

def describe_evenness(x):
  if is_even(x):
    print("It’s even!")
  elif is_odd(x):
    print("It’s odd!")
  else:
    print("It’s neither even nor odd!")



describe_evenness(int(input("Enter a number:")))