def measure(b1_max, b2_max, goal, b0):
    counter = 0
    b1 = 0
    b2 = 0
    if goal > b2_max and goal > b1_max:
        raise ValueError("Goal can't be larger than provided buckets")
    else:
        while b1 != goal and b2 != goal:
            if counter > 30:
                raise ValueError("Not possible")
    
            elif b0 == "one":
    
                if b1 == 0:
                    b1 = b1_max
                    counter = counter + 1

                elif goal == b2_max:
                    b2 = b2_max
                    counter = counter + 1
    
                elif b2 == b2_max:
                    b2 = 0
                    counter = counter + 1
                else:
                    if b1 + b2 <= b2_max:
                        b2 = b2 + b1
                        b1 = 0
                        counter = counter + 1
                    else:
                        b1 = b1 - (b2_max - b2)
                        b2 = b2_max
                        counter = counter + 1
            else:
                
    
                if b2 == 0:
                    b2 = b2_max
                    counter = counter + 1
                    
                elif goal == b1_max:
                    b1 = b1_max
                    counter = counter + 1
    
                elif b1 == b1_max:
                    b1 = 0
                    counter = counter + 1

                else:
                    if b1 + b2 <= b1_max:
                        b1 = b2 + b1
                        b2 = 0
                        counter = counter + 1
                    else:
                        b2 = b2 - (b1_max - b1)
                        b1 = b1_max
                        counter = counter + 1

    if b1 == goal: return counter, "one", b2
    if b2 == goal: return counter, "two", b1




