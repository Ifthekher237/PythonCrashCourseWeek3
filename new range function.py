# this program shows how to create your own range function
# this program also shows how to convert centigrade to fahrenhaite.

def cent_to_fahren(centigrade):
    fahrenhaite = ((9 * centigrade) / 5) + 32
    print("{:>7.2f} C   |   {:>7.2f} F".format(centigrade, fahrenhaite))


def range_creator(start, end, difference):
    created_range = []  # using this range_creator() function we can easily create
    while start <= end:  # a list of float/integer number of desired difference within a given range.
        created_range.append(start)
        start = start + difference
    return created_range


# c/5=(f-32)/9   #formula for converting centigrade to fahrenhaite or vice verse

start = float(input("starting:"))  # take input from user about starting temperature, ending temp and difference
end = float(input("ending:"))  # these inputs are also passed as argumets of range_creator() function
difference = float(input("difference:"))

my_range_function = range_creator(start, end,
                                  difference)  # calls the function and returned list is stored in my_range_function variable.
for i in my_range_function:  # here my_range_function is working like range() function.
    cent_to_fahren(i)  # every elements of my_range_function are temperature in centegrade, so they are passed
