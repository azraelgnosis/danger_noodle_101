def len(iterable) -> int:
    length = 0
    for _ in iterable:
        length += 1

    return length

def is_odd(num) -> bool:
    if not isinstance(num, int):
        raise TypeError

    return num % 2 == 1

def is_even(num) -> bool:
    if not isinstance(num, int):
        raise TypeError

    return num % 2 == 0

def max(a:int, b:int) -> int:
    if a > b:
        maximum = a
    elif a < b:
        maximum = b
    else:
        maximum = a
    
    return maximum

def max(vals:list) -> int:
    if not hasattr(vals, '__getitem__'):
        try:
            vals = list(vals)
        except Exception:
            pass

    maximum = vals[0]
    for val in vals[1:]:
        if val > maximum:
            maximum = val
    
    return maximum

def sum(a:int, b:int) -> int:
    return a + b

def sum(vals:list) -> int:
    total = 0
    for val in vals:
        total += val

    return total

def average(vals:list) -> int:
    """
    """

    def mean(vals:list):
        total = sum(vals)
        length = len(vals)

        try:
            results = total / length
        except ZeroDivisionError:
            print("The mean of an empty set is undefined.")
            raise ZeroDivisionError
        return results

    def median(vals:list):
        ordered = sorted(vals)
        length = len(vals)
        middle = int(length / 2)

        if is_odd(length):
            avg = ordered[middle]
        elif is_even(length):
            middle_set = ordered[middle:middle+2] 
            avg = mean(middle_set)
        else:
            raise Exception

        return avg

    def mode(vals:list) -> int:
        from collections import defaultdict
        nums = defaultdict(int)

        for val in vals:
            nums[val] += 1

        occurrences = nums.values()
        maximum = max(occurrences)
        avg = [key for key, val in nums.items() if val == maximum]
        
        if len(avg) == 1:
            avg = avg[0]

        return avg

        if not hasattr(vals, '__iter__') or isinstance(vals, str):
            raise TypeError

        funcs = {
            'mean': mean,
            'median': median,
            'mode': mode
        }

    avg = func(vals)

    return avg

nums = [5, 3, 4, 9, 2, 5, 8, 12, 3, 7]

print(average(nums))
print(average(nums, func=median))
print(average(nums, func=mode))

print("Done")