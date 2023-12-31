import math, random, time

def driver():
    print("All functions will return a position if the item is in the list, or \"no\" otherwise")
    list = [10, 9, 12, 8, 13, 16, 4, 4, 7, 6, 5, 4, 3, 2, 1, 0]
    print(list)
    print(merge_sort(list))

## Generates a list of a given length
## List is populated with random integers between 0 and 500
def generate_list(length):
    list = []
    for i in range(length):
        list.append(random.randint(0, 500))
    return list

## Search through each element to find target
## O(n)
def linear_search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return "no"

## Only works on sorted list
## Uses an upper and lower pointer to know in which portion of the list the value is
## Can use recursion is position isn't needed
## Halves list each time, checking middle of possible area
## O(log n)
def binary_search(list, value):
    head = 0
    tail = len(list) - 1  ## -1 as len counts all values, index starts at 0
    mid = (tail + head)//2
    while True:
        if list[mid] == value:
            return mid
        elif list[mid] > value:  ## If the value is at a lower point in list
            tail = mid - 1
            mid = (tail + head)//2
        elif list[mid] < value:  ## If value is at a higher point in list
            head = mid + 1
            mid = (tail + head)//2
        
        ## If checked enough times for head = tail (last possible place to check)
        ## If checked enough times for tail < head (gone past last possible check)
        if head > tail or (head == tail and list[mid] != value):
            return "no"

## Moves linearly through list, compares and swaps if higher than next element
## After each pass, next greatest will be in place
## i.e. first pass, largest is at end. Second pass, second largest is next to end
## Can be imporved by reducing number of positions checked by 1 each pass
## O(n**2)
def bubble_sort(list):
    for i in range(len(list) - 1): ## Loop through whole list
        for j in range(len(list) - 1): ## Iterate through each item
            if list[j] > list[j+1]: ## If next value is less than current
                temp = list[j+1]  ## Store j+1
                list[j+1] = list[j]  ## Set j+1 to j
                list[j] = temp  ## Set j to j+1

    return list

## Divide and conquer algorithm
## Splits lists in half until there is a list for each element
## Combine and compare lists next to each other, working back to having full list
def merge_sort(list):
    if len(list) > 1:

        # Split the list into 2 sublists
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Call merge_sort for all sublists until lists of single items are generated
        merge_sort(left)
        merge_sort(right)

        # Values used as pointers to use in comparisons
        i = j = k = 0

        # Compare the first item of each list
        # Place the smallest in the original list in position k
        # Do so for all elements of both lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        
        # If all values of one list have been added, add all from other list into the original list
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        return list

## Chooses a pivot, places all items greater than pivot in right list, all less than in left list
## Do the same for each new list created
## Combine all lists at end
## Recursive algorithm
def quick_sort(list):
    if len(list) <= 1:
        return list
    
    sorted_list = []
    head = 0
    tail = len(list) - 1
    pivot_index = tail
    
    pivot_value = list[pivot_index]
    right = []
    left = []
    for i in range(tail):
        if list[i] < pivot_value:
            left.append(list[i])
        else:
            right.append(list[i])

    sorted_list.extend(quick_sort(left))
    sorted_list.append(pivot_value)
    sorted_list.extend(quick_sort(right))
    return sorted_list

    


    ##return sorted_list

## Check each value in list with the first element
## If lower, swap
## Do the same for the new first element until end of list
## Lowest element is then in index 0
## Do the same for second element, so on, until all list is sorted
## O(n**2)
def insertion_sort(list):
    for i in range(1, len(list) - 1):
        key = list[i]
        j = i-1
        while (j >= 0 and list[j] > key):
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

## Randomise the list
## If sorted, good
## If not sorted, Randomise again
## Continue until sorted
## O(n!)
def bogo_sort(list):
    while not isSorted(list):
        random.shuffle(list)

    return list

## Check if list is sorted
## If yes, good
## If not, wait some amount of time
## Check again after some time between 0 and 5 seconds
## Relies on the concept of very large numbers and non-zero probability of bit flipping to suggest that given enough time, any list will become sorted due to chance
def miracle_sort(list):
    while not isSorted(list):
        time.sleep(random.randint(0, 5)*1000)

    return list

## Takes list as input
## Checks if any values are out of order
## If yes, list is not sorted, return false
## Else return true
def isSorted(list):
    for i in range(0, len(list) - 1):
        if list[i] > list[i+1]:
            return False
        
    return True


driver()