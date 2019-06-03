########### Sort algorithms
### The array being ordered will always be:

arr = [ 12, -3, 56, 59, 1, -15, 21 ]

def swap( arr_ref, arr_idx1, arr_idx2 ):
    temp = arr_ref[ arr_idx1 ]
    arr_ref[ arr_idx1 ] = arr_ref[ arr_idx2 ]
    arr_ref[ arr_idx2 ] = temp

# Bubble Sort
# O( n^2 ), in-place and stable algorithm
for j in range( len( arr ) - 1, 0, -1 ):
    for i in range( 0, j, 1 ):
        if arr[ i ] > arr[ i + 1 ]:
            swap( arr, i, i + 1 )
print( arr )

# Selection Sort
# Worst case O( n^2 ), in-place and unstable algorithm
# Should perform better than bubble sort due to fewer swap() calls required
for j in range( len(arr) - 1, 0, -1 ):
    maxindex = 0
    for i in range( 1, j + 1, 1 ):
        if( arr[ i ] > arr[ maxindex ] ):
            maxindex = i
    if maxindex != j:
        swap( arr, maxindex, j )
print( arr )

# Insertion Sort
for i in range( 1, len( arr ), 1 ):
    temp_value = arr[i]
    j = i
    while temp_value < arr[j - 1] and j > 0:
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = temp_value
print( arr )