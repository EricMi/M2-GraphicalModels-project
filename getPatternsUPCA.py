def getPatternsUPCA():
    patterns = []
    ix = 0
    patterns.append([0,0,0,0,0,0,0])    # 0: space begin
    ix += 1
    patterns.append([0,0,0,0,0,0,0])    # 1: space end
    ix += 1
    patterns.append([1,0,1])            # 2: guard begin
    ix += 1
    patterns.append([1,0,1])            # 3: guard end
    ix += 1
    patterns.append([0,1,0,1,0])        # 4: guard middle
    ix += 1
    patterns.append([0,0,0,1,1,0,1])    # 5: 0 left
    ix += 1
    patterns.append([0,0,1,1,0,0,1])    # 6: 1 left
    ix += 1
    patterns.append([0,0,1,0,0,1,1])    # 7: 2 left
    ix += 1
    patterns.append([0,1,1,1,1,0,1])    # 8: 3 left
    ix += 1
    patterns.append([0,1,0,0,0,1,1])    # 9: 4 left
    ix += 1
    patterns.append([0,1,1,0,0,0,1])    # 10: 5 left
    ix += 1
    patterns.append([0,1,0,1,1,1,1])    # 11: 6 left
    ix += 1
    patterns.append([0,1,1,1,0,1,1])    # 12: 7 left
    ix += 1
    patterns.append([0,1,1,0,1,1,1])    # 13: 8 left
    ix += 1
    patterns.append([0,0,0,1,0,1,1])    # 14: 9 left
    
    for i in range(5,15):
        patterns.append([1-x for x in patterns[i]])    # 15-24: reght parts
        ix += 1
    return patterns