def fib_rec(n):
    if n <= 1:
        return n
    else:
        return(fib_rec(n-1)+fib_rec(n-2))

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
            
    print("The Fib sequence = ", fib_rec(sequenceNumber))
