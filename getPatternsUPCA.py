def getPatternsUPCA():
    patterns = []
    patterns.append([0,0,0,0,0,0,0])    # 0: space begin
    patterns.append([0,0,0,0,0,0,0])    # 1: space end
    patterns.append([1,0,1])            # 2: guard begin
    patterns.append([1,0,1])            # 3: guard end
    patterns.append([0,1,0,1,0])        # 4: guard middle
    patterns.append([0,0,0,1,1,0,1])    # 5: 0 left
    patterns.append([0,0,1,1,0,0,1])    # 6: 1 left
    patterns.append([0,0,1,0,0,1,1])    # 7: 2 left
    patterns.append([0,1,1,1,1,0,1])    # 8: 3 left
    patterns.append([0,1,0,0,0,1,1])    # 9: 4 left
    patterns.append([0,1,1,0,0,0,1])    # 10: 5 left
    patterns.append([0,1,0,1,1,1,1])    # 11: 6 left
    patterns.append([0,1,1,1,0,1,1])    # 12: 7 left
    patterns.append([0,1,1,0,1,1,1])    # 13: 8 left
    patterns.append([0,0,0,1,0,1,1])    # 14: 9 left
    for i in range(5,15):
        patterns.append([1-x for x in patterns[i]])    # 15-24: right parts
    return patterns