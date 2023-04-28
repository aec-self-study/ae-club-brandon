# calc.py
import argparse
 
parser = argparse.ArgumentParser(description = "CLI Calculator.")
 
subparsers = parser.add_subparsers(help = "sub-command help", dest="command")
 
add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

sub = subparsers.add_parser("sub", help='add integers')
sub.add_argument("ints_to_sub", nargs=2, type=int)

def aec_subtract(ints_to_sub):
    arg_1 = ints_to_sub[0]
    arg_2 = ints_to_sub[1]
    our_sub = arg_1 - arg_2
    if our_sub < 0:
        our_sub = 0
    return our_sub

multiply = subparsers.add_parser("multiply", help='multiply integers')
multiply.add_argument("ints_to_multiply", nargs=2, type=int)

divide = subparsers.add_parser("divide", help='divide integers')
divide.add_argument("ints_to_divide", nargs="*", type=int)

def aec_divide(ints_to_divide):
    if len(ints_to_divide) != 2:
        raise Exception("Sorry, you must have 2 arguments")
    arg_1 = ints_to_divide[0]
    arg_2 = ints_to_divide[1]
    try:
        our_divide = arg_1 / arg_2
    except ZeroDivisionError:
        our_divide = 0
    return our_divide  

 
if __name__ == "__main__":
    args = parser.parse_args()
  
    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"The sum of values is: {our_sum}")
    
    if args.command == "sub":
        our_sub = aec_subtract(args.ints_to_sub)
        print(f"The subtracted result of values is: {our_sub}")

    if args.command == 'multiply':
        our_multiply = args.ints_to_multiply[0] * args.ints_to_multiply[1]
        print(f"The multiplied result is  {our_multiply}")

    if args.command == 'divide':
        our_divide = aec_divide(args.ints_to_divide)
        print(f"The divided result of values is: {our_divide}")