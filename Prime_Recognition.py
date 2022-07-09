def odd_even (number):
    if number%2 == 0:
        return "even"
    else:
        return "odd"
def prime_r (number):
    if number == 0 or number == 1 or number == -1:
        returning = "number " + str(number) + " cannot be solve"
        return returning
    elif number == 2 or number == 3 or number == 5:
        return "Prime"
    elif number%2 == 0:
        return "Not Prime"
    elif number%3 == 0:
        return "Not Prime"
    elif number%5 == 0:
        return "Not Prime"
    else:
        counter = []
        #create counter
        for i in range(2, number+1):
            counter.append(i)
        #remove multiples of 2
        for j in range(2 , number , 2):
            counter.remove(j)
        # remove multiples of 3
        for k in range(3 , number , 6):
            if k in counter:
                counter.remove(k)
        # remove multiples of 5
        for l in range(5 , number , 5):
            if l in counter:
                counter.remove(l)

        m = 0
        n = len(counter)
        while True:
            if m+1 == n:
                return "Prime"
                break
            if number/counter[m] == int(number/counter[m]):
                return "Not Prime"
                break
            else:
                m = m + 1
def ABS (number):
    if number < 0 :
        return_number = (-(number))
        return return_number
    else:
        return number
