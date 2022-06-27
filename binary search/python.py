#he binary_search function takes a sorted array and an item.
#If the item is in the array, the function returns its position.

def binary_search(list: any, item: int):
  #low and high keep track of which part of the list you’ll search in.
  low = 0 
  high = len(list) - 1
  # While you haven’t narrowed it down to one element …
  while low <= high:
    #… check the middle element.
    mid = (low + high) 
    guess = list[mid]
    # Found the item.
    if guess == item: 
      return mid
    # The guess was too high.
    if guess > item: 
      high = mid - 1
    # The guess was too low.
    else: 
      low = mid + 1
  #The item doesn’t exist.
  return None 

my_list = [1,2,3,4,5,6,7,8,9,10]

#return the position in the array

print (binary_search (my_list, 3)) 
print (binary_search (my_list, -1))
