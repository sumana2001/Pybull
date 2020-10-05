def binary_search(item_list, item):
    first_value = 0
    item_list.sort() # to make search valid with unsorted list too
    last_value = len(item_list)-1
    found = False

    while(first_value <= last_value and not found):
      mid_value = (first_value + last_value)//2
      if item_list[mid_value] == item :
        found = True
      else:
        if item < item_list[mid_value]:
          last_value = mid_value - 1
        else:
          first_value = mid_value + 1	
    return found
    
# print(binary_search([18,23,11,3,1], 12)) # False case
# print(binary_search([2, 5, 1, 9, 3], 3)) # True case