b1 = 0
b2 = 0
b1_max = 0
b2_max = 0
counter = 1
b2_is_full = False
b1_is_full = False
b2_is_empty = True
b1_is_empty = True

def reset(): 
    global b1, b2, b1_max, b2_max, counter, b2_is_full, b1_is_full, b1_is_empty, b2_is_empty
    b1 = 0
    b2 = 0
    b1_max = 0
    b2_max = 0
    counter = 1
    b2_is_full = False
    b1_is_full = False
    b2_is_empty = True
    b1_is_empty = True

def pour_b1_into_b2():
    global b1, b2, b2_max, counter
    while b1 > 0 and b2 != b2_max: 
        b1 -= 1
        b2 += 1
    counter +=1

def pour_b2_into_b1():
    global b1, b2, b1_max, counter
    while b2 > 0 and b1 != b1_max: 
        b2 -= 1
        b1 += 1
    counter +=1
    
def empty_b1(): 
    global b1, counter
    b1 = 0
    counter +=1

def empty_b2(): 
    global b2, counter
    b2 = 0
    counter +=1

def fill_b1(): 
    global b1, b1_max, counter
    b1 = b1_max
    counter +=1

def fill_b2(): 
    global b2, b2_max, counter
    b2 = b2_max
    counter +=1

def fill_check():
    global b1, b2, b1_max, b2_max, b1_is_full, b2_is_full, b1_is_empty, b2_is_empty
    if b2 == b2_max:
        b2_is_full = True
        b2_is_empty = False
    else:
        b2_is_full = False
        if b2 == 0: b2_is_empty = True
    if b1 == b1_max: 
        b1_is_full = True
        b1_is_empty = False
    else:
        b1_is_full = False
        if b1 == 0: b1_is_empty = True

def measure(bucket_one, bucket_two, goal, b_start):
    if goal > bucket_two: raise ValueError("Goal can't be larger than provided buckets")
    global b1_max, b2_max, b1, b2, counter, b1_is_full, b2_is_full
    b1_max = bucket_one
    b2_max = bucket_two
    b1 = 0
    b2 = 0

    if b_start == "one": b1 = b1_max
    if b_start == "two": b2 = b2_max
    
    while b1 != goal and b2 != goal:
        if counter > 20: raise ValueError("Not Possible.")
        fill_check()
        
        if b2_is_full: empty_b2(); continue
        if b1_is_full: pour_b1_into_b2(); continue
        if not b1_is_full and not b1_is_empty: pour_b1_into_b2(); continue
        if b1_is_empty: fill_b1(); continue

    # reset()
    if b1 == goal: return counter, "one", b2
    if b2 == goal: return counter, "two", b1




def main():
    # print(measure(3,5,1,"one")) #(4, "one", 5)
    print(measure(3, 5, 1, "two")) #(8, "two", 3) TODO
    # print(measure(7, 11, 2, "one")) #(14, "one", 11)
    # print(measure(7, 11, 2, "two")) #(18, "two", 7) TODO
    # print(measure(6, 15, 5, "one")) #Raise ValueError
    # print(measure(6, 15, 9, "one")) #(10, "two", 0)

if __name__ == '__main__':
    main()