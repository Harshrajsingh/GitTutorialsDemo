def question_1(A, B):
    
    dis1 = -1
    value1 = None
    dis2 = -1
    value = None

    for i in range(len(B)):
        val = B[i]
        dist = val - A
        abs_dist = dist if dist >= 0 else -dist 

      
        if abs_dist > dis1 or (abs_dist == dis1 and val < value1):
          
            dis2 = dis1
            value2 = value1
         
            dis1 = abs_dist
            value1 = val
        elif abs_dist > dis2 or (abs_dist == dis2 and val < value2):

            dis2 = abs_dist
            value2 = val

    return value2
print(question_1(5,[1,4,8]))
print(question_1(22,[19,20,21,24]))
        