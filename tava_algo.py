# #binary search using recursion
# def binary_search(arr,x):
#     if len(arr)==0:
#         return False
#     else:
#         mid=len(arr)//2
#         if arr[mid]==x:
#             return True
#         else:
#             if x<arr[mid]:
#                 return binary_search(arr[:mid],x)
#             else:
#                 return binary_search(arr[mid+1:],x)
# print(binary_search([1,2,3,4,5,6,7,8,9,10],5))
# #binary search using recursion
# def binary_search(arr, low, high, x):
#     if high >= low:
#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
#         else:
#             return binary_search(arr, mid + 1, high, x)
#     else:
#         return -1
# print(binary_search([1,2,3,4,5,6,7,8,9,10],0,9,5))
#---------------------------------------------------------------------------------------------------
from LinkedLists import LinkedList #import the LinkedList class from the LinkedLists.py file created by me

def merge_sort(linked_list):
    if linked_list.NodeCount() <= 1:
        return linked_list
    else:
        left_half, right_half = split(linked_list)
        left = merge_sort(left_half)
        right = merge_sort(right_half)
        return merge(left, right)

def split(linked_list):
    if linked_list.NodeCount() == 0 or linked_list.NodeCount() == 1:
        left = linked_list
        right = LinkedList()
        return left, right
    else:
        mid = linked_list.NodeCount() // 2
        mid_node = linked_list.root
        for i in range(mid - 1):
            mid_node = mid_node.next
        right = LinkedList()
        right.root = mid_node.next
        mid_node.next = None
        left = linked_list
        return left, right

def merge(left, right):
    l = left.root
    r = right.root
    result = LinkedList()
    while l != None and r != None:
        if l.value < r.value:
            result.insert_end(l.value)
            l = l.next
        else:
            result.insert_end(r.value)
            r = r.next
    while l != None:
        result.insert_end(l.value)
        l = l.next
    while r != None:
        result.insert_end(r.value)
        r = r.next
    return result

l=LinkedList()
l.insert_end(15)
l.insert_end(10)
l.insert_end(5)
l.insert_end(20)
l.insert_end(3)
l.insert_end(2)
print(l) #prints the linked list
merge_sort(l) #sorts the linked list
print(l)