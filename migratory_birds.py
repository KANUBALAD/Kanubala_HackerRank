def migratoryBirds(arr):
    keep_counts = {}
    for i in range(len(arr)):
        keep_counts[arr[i]] = +1
    print(keep_counts)
    keep_max = []
    max_val = max(keep_counts.values())
    [keep_max.append(val) for val in keep_counts if keep_counts[val] == max_val]
    return(min(keep_max))
   
