#Assignment found in the lab 1

1.We use Big O cause we need to check every member or element to make sure we have found the largest number in the array of numbers 

def is_max(arr):
    max_number = 0

    for num in arr:
        if num > [num + 1]:
            num = max_number

    return max_number

2.We use big O in counting the number of times that an element occurs in an array of numbers or something like cause we need to check every possible element to make sure all the occurences have been account for

def is_counted(arr):
    count = 0
    number = 2

    for i in arr:
        if i === number:
            count += 1

    return count

3.Again, we use Big O when checking for ordering cause as started we using this helps us to check the elements one after the order to make sure that they are arranged in a particular order 
When we check the element and its not in the order we want it to be we have it perform a certain command

def is_ordered(arr):
    for i in length(arr - 1):
        if i > i + 1:
            return False
    return True

##Assigment number 2
#Writing pseudocode for long division
BEGIN LongDivision(dividend,divisor)
    IF divisor = 0 THEN  
        PRINT "Error:Dividing by zero"
    END if

    SET quotient TO 0
    SET remainder TO dividend

    WHILE remainder >= divisor
        remainder -= divisor
        quotient += 1
    END WHILE 

    PRINT "Quotient:", quotient 
    PRINT "Remainder: ", remainder
END LongDivision

def LongDivision(dividend, divisor):
    if divisor = 0:
        print("Error: Dividing by zero")

    qoutient = 0
    remainder  = dividend

    while remainder >= divisor:
       remainder = remainder - 1
       quotient = qoutient + 1

    print("Quotient: ",quotient)
    print("Remainder: ",quotient)

    


   