# function return the number list 
def process_numbers(args):
    numbers = []

    if isinstance(args, list):
        for arg in args:
            if isinstance(arg, int):
                numbers.append(arg)
            elif arg.isnumeric():
                numbers.append(int(arg))
        numbers.sort()
        return numbers
    else: 
        return numbers

# function return the name list
def process_names(args):
    names = []

    if isinstance(args, list):
        for arg in args:
            if isinstance(arg, str):
                if not arg.isnumeric():
                    names.append(arg)
        names.sort()
        return names
    else: 
        return names