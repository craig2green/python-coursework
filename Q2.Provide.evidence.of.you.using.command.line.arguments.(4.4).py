import sys

# sys.argv[0] is the script name itself
# sys.argv[1] onwards are the passed arguments

if len(sys.argv) > 2:
    user_name = sys.argv[1]
    item_quantity = sys.argv[2]
    print(f"Hello, {user_name}!")
    print(f"You requested {item_quantity} items.")
else:
    print("Please provide a name and quantity as command line arguments.")
