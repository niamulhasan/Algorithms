
class Sort:
    #Marge Sort
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:] 

            Sort.mergeSort(L)
            Sort.mergeSort(R)

            i = j = k = 0


            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1


            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1




    #Insertion Sort 
    def insertionSort(arr): 
        for i in range(1, len(arr)): 
      
            key = arr[i] 

            j = i-1
            while j >=0 and key < arr[j] : 
                    arr[j+1] = arr[j] 
                    j -= 1
            arr[j+1] = key



    #Quick Sort
    def partition(arr, low, high):
    	i = ( low - 1 )
    	pivot = arr[high]

    	for j in range(low, high):
    		if arr[j] <= pivot:
    			 i = i + 1
    			 arr[i], arr[j] = arr[j], arr[i]

    	arr[i+1], arr[high] = arr[high], arr[i+1]
    	return ( i+1 )


    def quickSort(arr, low, high):
    	if low < high:
    		pi = Sort.partition(arr, low, high)
    		Sort.quickSort(arr, low, pi-1)
    		Sort.quickSort(arr, pi+1, high)







    # Code to print the list
    def printList(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()







class IO:
	#inserting element into a list
	def populate():
		arr = []
		size = int(input("How many elements you want to insert: \n"))
		
		i = 0
		while i < size:
			print("Enter element at index", i, ": ", end = '')
			element = int(input())
			arr.append(element)
			i+=1

		return arr


	#printing the given list
	def printList(arr):
		for i in range(len(arr)):
			print(arr[i], end = " ")
		print()


	def SelectSortOptions(arr):
		print("Please Select a sorting alogrithm to apply: ")
		print("   1. Marge Sort")
		print("   2. Insertion Sort")
		print("   3. Quick Sort")
		print("      ----")
		print("Select a number: ", end = " ")
		x = int(input())
		
		if x == 1:
			print("Applying Merge Sort")
			Sort.mergeSort(arr)
		if x == 2:
			print("Applying Insertion Sort")
			Sort.insertionSort(arr)
		if x == 3:
			print("Applying Quick Sort")
			n = len(arr)
			Sort.quickSort(arr, 0, n-1)

		return arr


	def startAgain():
		print("\n \n ------- \n   Want to start again: \n     0. No\n     1. Yes")
		x = int(input())
		return x









# driver code to test the above code
if __name__ == '__main__':

	i = 1
	while i:
		pass
		arr = IO.populate()

		print("\n \nYour Array")
		print("---------")
		IO.printList(arr)
		print("---------\n \n")

		arr = IO.SelectSortOptions(arr)
		print("\n\nSORTED ARRAY \n======")
		IO.printList(arr)
		print("======\n")

		i = IO.startAgain()

    # arr = [12, 11, 13, 5, 6, 7]
    # print("Given array is", end="\n")
    # Sort.printList(arr)
    # Sort.insertionSort(arr)
    # print("Sorted array is: ", end="\n")
    # Sort.printList(arr)



    #for Quick sort
 	#arr = [10, 7, 8, 9, 1, 5] 
	# n = len(arr) 
	# print(arr)
	# Sort.quickSort(arr,0,n-1)
	# print(arr)
