def encode(message, rails):
    cycle = 2 * rails - 2
    mid_range = [int(x) for x in range(1, rails - 1)]
    message = list(message)
    list_of_rails = [list() for x in range(rails)]
    while message:
        #walk down rails
        for rail in range(rails):  
            if len(message) == 0: break
            list_of_rails[rail].append(message[0])
            message.pop(0)
        #walk up rails
        for rail in mid_range[::-1]:
            if len(message) == 0: break
            list_of_rails[rail].append(message[0])
            message.pop(0)
    rails = ["".join(x) for x in list_of_rails] 
    return "".join(rails)



def decode(encoded_message, rails):
    pass



"""
 TODO: 1 - define loop to create lists relative to amount of rails; cycle = 2x -2
 TODO: 2 - concatenate lists for encode

"""

def main():
    # print(encode("WEAREDISCOVEREDFLEEATONCE", 3)) #WECRLTEERDSOEEFEAOCAIVDEN
    print(encode("EXERCISES",4)) #ESXIEECSR

if __name__ == '__main__':
    main()