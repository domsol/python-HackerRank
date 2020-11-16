# Sales by Match - 2020/11/16
def sockMerchant(n, ar):
    
    socktype = {} #  Dic to store differnt types

    for elem in ar:  # loops all elm of the given array (ar)
        while True:  
            if elem in socktype: #if elm already in stocktype +1 to total
                socktype[elem] += 1
                break
            else:
                socktype[elem] = 1 #  else if not found make a new elm in stocktype
                break

    total = 0  # total to return
    for x in socktype: # loops all socktype
        pairs = socktype[x] 
        total += pairs//2 # divides by 2


    return(total)
