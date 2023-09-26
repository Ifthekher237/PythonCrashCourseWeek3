#this program show first n elements of fibonacci series.


n=int(input("How many elements dou you want to see from fibonacci series:"))

fibonacci=[0,1]                             #declearing the first 2 elements of fibonacci sequence and putting them into a list.
for i in range(2,n):
    fn=fibonacci[i-2]+fibonacci[i-1]
    fibonacci.append(fn)                    #now appending every sum of fn-2 and fn-1 into fibonacci list.
print("\n{fibonacci}, this is your fibonacci sequence of {n} elements.".format(fibonacci=fibonacci,n=n))