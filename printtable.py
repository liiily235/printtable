def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop>
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

#POWERTABLE
def powertable(start, stop):
    power1 = 3
    power2 = 2
    for i in range(start, stop):
        print(i**power2)
    for i in range(start, stop+1):
        print(i**power1)

if __name__ == '__main__':
    multtable(1, 4, 7)
