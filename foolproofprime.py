counter=0
comparer=0

def collatz(n):
    global counter
    if n==1:
        return counter
    elif n%2==0:
        n/=2
        counter+=1
        reducer(n)
    else:
        n=3*n+1
        counter+=1
        reducer(n)

    #print(counter)
def reducer(n):
    n-=1
    collatz(n)

collatz(1000000)
