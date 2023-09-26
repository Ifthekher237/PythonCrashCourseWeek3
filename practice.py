'''
#an infinite loop
x=0
while x%2==0:
    x=x/2
    print(x)
'''
'''
#Fill in the blanks  to make the print_prime_factors function print all
#the prime factors of a  number.A prime factor is a number that is prime and divides
#another without  a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
'''
'''
def is_prime(count):
    if count ==1:
        print("\nYou have entered a prime number")
    else:
        print("\nYou have entered a composite number")

#no_of_divisor() functio finds the total number of divisor of number "number"
# and send this number to an another function is_prime() to determine whether the given number is prime or not.
def no_of_divisor(n):
    count=0
    i=0
    while i<=pow(n,.5):
        i = i + 1
        if n%i==0:
            count=count+1
    is_prime(count)



number=int(input("Enter a number to check whether it is a prime or not:"))    #takes input from user and convert it to an integer

if number==2:
    print("\nYou have entered a prime number")
elif number==1:
    print("\nThe number of divisor of 1 is 1.", end="")
    print("So 1 is neither composite nor prime.Because a composite number")
    print(" must have minimum of 3 divisors and a prime have exactly 2 divisor.")
else:
    no_of_divisor(number)                                                                 #calls the no_of_divisor() function

'''


'''
list=[]
n=int(input("how many values do you want to put into list:"))
for i in range(1,n+1):
   numbers=int(input())
   list.append(numbers)
print(list)

'''
'''
#this code prints out all combination of domino tiles.
for left in range(0,7):
    for right in range(left,7):
        print("["+str(left)+"|"+str(right)+"]",end=" ")

    print()

'''
'''

Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        if number == 1:
            return True
        return False

        # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False
'''
'''
Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits.
 Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
'''
'''
def digits(n):
    count = 0
    if n == 0:
        count=1
    while (n != 0):
        count += 1
        n=n//10
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1

'''
'''
def counter(start, stop):
	x = start
	if x>stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x>stop:
				return_string += ","
			x-=1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x<stop:
				return_string += ","
			x+=1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
'''
'''
#this function replace the old domain by a new domain in an outdated email address

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain("ifthekher.du@gmail.com","gmail.com","yahoo.com"))
'''
