#!/usr/bin/python3
def find_peak(list_of_integers):
    n = len(list_of_integers)
    if (list_of_integers == None or n == 0):
         return None
    if (len(list_of_integers) == 1):
        return list_of_integers[0]
    # elif (list_of_integers[0] >= list_of_integers[1]):
    #     return list_of_integers[0]
    # elif (list_of_integers[-1] >= list_of_integers[-2]):
    #     return list_of_integers[-1]
    else:
        low = 1
        high = n-1
        while (low <= high):
            mid = int((low + high) / 2)
            if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
                return list_of_integers[mid]
            elif list_of_integers[mid -1] >= list_of_integers[mid]:
                high = mid - 1
            elif list_of_integers[mid + 1] >= list_of_integers[mid]:
                low = mid + 1