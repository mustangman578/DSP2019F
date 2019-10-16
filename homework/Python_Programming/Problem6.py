def fib_rec(n):
    if n <= 1:
        return n
    else:
        return(fib_rec(n-1)+fib_rec(n-2))

def fib_loop(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for c in range(0,n-1):
            c = a + b
            a = b
            b = c
    return c


def fib():
    import timeit

    while True:
        try:
            userInput = input("Please enter a non-negative integer or type stop:")
        
            if userInput == "Stop" or userInput == "stop":
                break
            
            sequenceNumber = int(userInput)
        except:
            print("Cannot be a string")
            continue
            
        if sequenceNumber < 0:
            print("Should be a positive integer")
            continue
            
        
        elif sequenceNumber == 0:
            print("Fib(0) = ",sequenceNumber)
            continue
        
        else:
            start1 = timeit.default_timer()
            fib_seq_rec = fib_rec(sequenceNumber)
            start2 = timeit.default_timer()
            fib_seq_loop = fib_loop(sequenceNumber)
            print("fib(%d) = %d" %(sequenceNumber,fib_seq))
            print("average runtime recursive = %s" %(timeit.default_timer() - start1))
            print("average runtime for loop = %s" %(timeit.default_timer() - start2))
            continue   
        
            
#The for loop is faster because recursive requires the function the called multiple times to make a calculation

'''
Please enter a non-negative integer or type stop:10
fib(10) = 3524578
average runtime recursive = 0.0004054000000905944
average runtime for loop = 0.00038850000009915675
Please enter a non-negative integer or type stop:15
fib(15) = 3524578
average runtime recursive = 0.0007722000000285334
average runtime for loop = 0.0006905000000188011
Please enter a non-negative integer or type stop:20
fib(20) = 3524578
average runtime recursive = 0.004241999999976542
average runtime for loop = 0.0005214000002524699
Please enter a non-negative integer or type stop:25
fib(25) = 3524578
average runtime recursive = 0.0245521000001645
average runtime for loop = 0.00045439999985319446
Please enter a non-negative integer or type stop:30
fib(30) = 3524578
average runtime recursive = 0.25564570000005915
average runtime for loop = 0.00015200000007098424
Please enter a non-negative integer or type stop:35
fib(35) = 3524578
average runtime recursive = 2.8147796000002927
average runtime for loop = 0.00015950000033626566
Please enter a non-negative integer or type stop:stop
'''
