

def bucket_sort(s):
    '''Function takes a unsorted list floats and seperated them into 9 different list base on 
        which category they fall in (betwen [0 and 1), between [2 and 3)) etc.
    '''

    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []
    sorted_list = []
    for ele in s:                                           #for loop goes throught each element in given float listen and places it in the appropriate bucket
        if ele*10 < 2:
            list_1.append(ele)
        if ele*10 < 3 and ele*10 > 2 or ele*10 == 2:
            list_2.append(ele)
        if ele*10 < 4 and ele*10 > 3 or ele*10 == 3:
            list_3.append(ele)
        if ele*10 < 5 and ele*10 > 4 or ele*10 == 4:
            list_4.append(ele)
        if ele*10 < 6 and ele*10 > 5 or ele*10 == 5:
            list_5.append(ele)
        if ele*10 < 7 and ele*10 > 6 or ele*10 == 6:
            list_6.append(ele)
        if ele*10 < 8 and ele*10 > 7 or ele*10 == 7:
            list_7.append(ele)
        if ele*10 < 9 and ele*10 > 8 or ele*10 == 8:
            list_8.append(ele)
        if ele*10 < 10 and ele*10 > 9 or ele*10 == 9:
            list_9.append(ele)
    list_1 = insertionSort(list_1)                          #Each list is sorted using the insertion sort function
    list_2 = insertionSort(list_2)
    list_3 = insertionSort(list_3)
    list_4 = insertionSort(list_4)
    list_5 = insertionSort(list_5)
    list_6 = insertionSort(list_6)
    list_7 = insertionSort(list_7)
    list_8 = insertionSort(list_8)
    list_9 = insertionSort(list_9)
    sorted_list.append(list_1)                              #After each list is sorted, it is append in the appropriate order to the final sorted list 
    sorted_list.append(list_2)
    sorted_list.append(list_3)
    sorted_list.append(list_4)
    sorted_list.append(list_5)
    sorted_list.append(list_6)
    sorted_list.append(list_7)
    sorted_list.append(list_8)
    sorted_list.append(list_9)
    nice_sorted_list = []
    for ele in sorted_list:                                 #For loop goes throught every element and adds it to the list so it is jsut a singluar list instead of a list of lists
        for val in ele:
            nice_sorted_list.append(val)
    return nice_sorted_list

def insertionSort(s):
    ''' Function given a list sorts it from smallest to greatest using insertion sort
    '''
    for i in range(len(s)):                 #for loop goes till the end of the given list using variable i
        val = s[i]                      
        x = i-1
        while x >= 0 and val < s[x]:        #while loop repeats until the selected value is larger then the value befor it
            s[x+1] = s[x]
            x -=1
        s[x+1] = val
    return s

# Your "program" is driven by the main method
def main():
    s = [0.16,0.12,0.22,0.47,0.87,0.49,0.34]
    print(bucket_sort(s))


# Guard for main function 
if __name__ == "__main__":
    main()