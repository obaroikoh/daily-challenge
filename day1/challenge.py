def target_pair(arr, target):
    if target < 1:
        return False
    
    number_seen = {}
    for i, v in enumerate(arr):
        if (target - v) in number_seen:
            return True
        else:
            number_seen[v] = i
    return False 