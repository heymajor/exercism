def slices(series, length):
    if length < 0: raise ValueError('slice length cannot be negative')
    if length == 0: raise ValueError('slice length cannot be zero')
    if len(series) == 0: raise ValueError('series cannot be empty')
    if len(series) < length: raise ValueError('slice length cannot be greater than series length')

    chunked_list = []
    for i in range(0, len(series)):
        if len(series[i:length + i]) == length:
            chunked_list.append(series[i:length + i])
        else: break
    
    return chunked_list


def main():
    print(slices("777777", 3)) 

if __name__ == '__main__':
    main()