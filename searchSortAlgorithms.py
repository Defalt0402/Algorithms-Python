import math, random

def driver():
    print("All functions will return a position if the item is in the list, or \"no\" otherwise")

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
    mid = math.floor((tail + head)/2)
    while True:
        if list[mid] == value:
            return mid
        elif list[mid] > value:  ## If the value is at a lower point in list
            tail = mid - 1
            mid = math.floor((tail + head)/2)
        elif list[mid] < value:  ## If value is at a higher point in list
            head = mid + 1
            mid = math.floor((tail + head)/2)
        
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
    pass

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
    pivot_index = math.floor((tail + head)/2)
    pivot_value = list(pivot_index)
    right, left = []
    for i in range(tail):
        if list[i] < pivot_value:
            left.append(list[i])
        else:
            right.append(list[i])

    


    ##return sorted_list

## Check each value in list with the first element
## If lower, swap
## Do the same for the new first element until end of list
## Lowest element is then in index 0
## Do the same for second element, so on, until all list is sorted
## O(n**2)
def insertion_sort(list):
    pass

## Randomise the list
## If sorted, good
## If not sorted, Randomise again
## Continue until sorted
## O(n!)
def bogo_sort(list):
    pass

## Check if list is sorted
## If yes, good
## If not, wait some amount of time
## Check again
## Relies on the concept of very large numbers and non-zero probability of bit flipping to suggest that given enough time, any list will become sorted due to chance
def miracle_sort(list):
    pass