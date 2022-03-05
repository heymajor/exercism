singles = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
adults = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
# elders = ["billion", "million", "thousand", "hundred"]
elders = ["", "thousand", "million", "billion"]
out = ""


def say(n):
    global singles, teens, adults, elders, out

    if n < 100: out += sub_100(n)
    
    n_list = [x for x in str(n)]
    n_list.reverse()
    chunked_list = []
    chunk_size = 3
    for i in range(0, len(n_list), chunk_size):
        chunked_list.append(n_list[i:chunk_size + i])

    chunked_list = [x[::-1] for x in chunked_list]    
    # print(chunked_list)
    chunked_list.reverse()
    # print(chunked_list)
    chunked_list = [int("".join(x)) for x in chunked_list]
    old_ppl_counter = 0
    elders = elders[0:len(chunked_list)]
    elders.reverse()
    for chunk in chunked_list:
        chunk_str = str(chunk)
        if chunk == 0: continue
        if chunk >= 100: 
            first_num = int(chunk_str[0])
            last_num = int(chunk_str[1::])
            word_1 = singles[first_num]
            word_2 = sub_100(last_num)
            word_3 = elders[old_ppl_counter]
            out += f"{word_1} hundred {word_2} {word_3} "
        # word_1 = singles[chunk]
        # word_2 = elders[old_ppl_counter]
        # out += f"{word_1} {word_2} "
        old_ppl_counter += 1
        # if chunk < 100: 
            # out += f"{sub_100(chunk)} {elders[old_ppl_counter]} z "
            # old_ppl_counter += 1
        # elif chunk >= 100:
            # first_num = int(chunk_str[0])
            # last_num = int(chunk_str[1::])
            # out += f"{singles[first_num]} hundred {elders[old_ppl_counter]} {sub_100(last_num)}"
            # old_ppl_counter += 1
            # out += elders[int(chunk_str[0])]
            # out += sub_100(last_num)
        # print(out)
    elder_list = ["", "thousand", "million", "billion"]
    return out

def sub_100(n):
    remainder = 0
    global singles, teens, adults, elders
    temp_out = str()
    
    if n < 10: return singles[n]
    
    remainder = n % 10
    
    if 10 <= n < 20: 
        temp_out += teens[n - 10]
        return out
    if remainder == 0:
        temp_out += adults[n//10]
    else:
        temp_out += f"{adults[n//10]}-{singles[remainder]}"
    return temp_out



def main():
    # print(say(30))  # 
    # print(say(98))  # 
    # print(say(18))  # 
    # print(say(1))  # 
    # print(say(99))
    # print(say(12345))
    # print(say(345))
    # print(say(1000000))
    print(say(100011))
    # print(say(1000))
    # print(say(1234567890))

if __name__ == '__main__':
    main()

