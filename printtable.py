def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop>
    """

    print('Multiplication Table')
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

"""
Print Power Table for i
"""

    def powertable(power,i):

    print("Power Table")
    for x in range (1, i + 1):
        print (f"{i} ^ {power} = {i**power}")

if __name__ == '__main__':
    multtable(1, 4, 7)
    powertable(2, 4)
