if __name__ == '__main__':
    
    
    records= []
    scores = []
    
    smallest = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    scores = sorted(set([record[1] for record in records]))
    smallest = scores[1]
    names = sorted([record[0] for record in records if record[1] == smallest])    
    for name in names:
        print(name)        
        
        
