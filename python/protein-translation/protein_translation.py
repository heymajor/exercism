def proteins(strands):

    translations = {"AUG":"Methionine", "UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", "UUG":"Leucine", "UCU":"Serine","UCC":"Serine","UCA":"Serine","UCG":"Serine","UAU":"Tyrosine","UAC":"Tyrosine","UGU":"Cysteine","UGC":"Cysteine","UGG":"Tryptophan","UAA":"STOP","UAG":"STOP","UGA":"STOP"}

    chunked_list = []
    chunk_size = 3
    for i in range(0, len(strands), chunk_size):
        chunked_list.append(strands[i:chunk_size + i])
    
    strands = chunked_list
    print(strands)

    temp = []
    for strand in strands: 
        temp.append(translations.get(strand))

    out = []
    for thing in temp: 
        if thing == "STOP":
            break
        else:
            out.append(thing)

    return out

