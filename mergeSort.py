items = [6,20,8,19,56,23,87,41,49,53]

def mergsort(data):
    if len(data) > 1:
        mid = len(data) // 2
        leftArray = data[:mid]
        rightArray = data[mid:]
        # if len(data) == 1:
        #     return
        mergsort(leftArray)
        mergsort(rightArray)
        i=0 #left array
        j=0 #right array
        k=0 #merged array
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                data[k] = leftArray[i]
                i += 1
            else:
                data[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            data[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            data[k] = rightArray[j]
            j += 1
            k += 1
        
print(items)
mergsort(items)
print(items)