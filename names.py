from name_function import get_formatted_name as gfn

print("press q at any time to quit")

while True:
    first = input("Please enter a first name")
    if first == 'q':
        break
    last = input("Please enter a last name")
    if last == 'q':
        break

    formatted_name = gfn(first, last)
    print(f"\t Neatly formatted name: {formatted_name}.")