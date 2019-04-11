import timeit
def merge_sort(lst):
    # if the list is this short, no sorting is necessary
    if len(lst) <= 1:
        # return a copy, out-of-place
        return list(lst)
    
    # half the length, rounded down
    m = len(lst) // 2
    
    # list slicing
    A = lst[:m]
    B = lst[m:]
    
    # sort both halves recursively
    A = merge_sort(A)
    B = merge_sort(B)
    
    return linear_merge(A, B)

def linear_merge(A, B):
    # merge two sorted lists
    output = []
    i, j = 0, 0
    
    while i + j < len(A) + len(B):
        if i < len(A) and (j == len(B) or A[i] <= B[j]):
            output.append(A[i])
            i += 1
        else:
            output.append(B[j])
            j += 1
    
    return output

lis = [4,1,7,5,2]
print("Original list: " + str(lis))
start_time = timeit.default_timer()
elapsed = timeit.default_timer() - start_time
li = merge_sort(lis)
print(elapsed)
print(li)