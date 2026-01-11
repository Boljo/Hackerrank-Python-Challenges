if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrlist = list(arr)
    
    seen = set()
    
    arrListUnique = [x for x in arrlist if x not in seen and not seen.add(x)]
    arrListUnique.sort()
    
    print(arrListUnique[len(arrListUnique)- 2])
    
    
    
    
