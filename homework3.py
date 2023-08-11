'''
IDP for learning of Python from scratch
Python 3.10 or higher is required 

Homework #3
'''

def union_even_and_odd(list1, list2):
    # Union of odd elements of one list and even elements of another
    lists_union = []
    for idx, el in enumerate(list1):
        if idx%2 == 0:
            lists_union.append(el)
    for idx, el in enumerate(list2):
        if idx%2 == 1:
            lists_union.append(el)
    return lists_union

def sort_asc(ulist):
    #Insertion Sort
    for i in range(len(ulist)):
        j = i
        while(j >0 and ulist[j] < ulist[j-1]):
            temp = ulist[j]
            ulist[j]= ulist[j-1]
            ulist[j-1]=temp
            j=j-1
    return ulist

def sort_desc(ulist):
    #Selection Sort
    el_count = len(ulist)
    for i in range(el_count):
        max_index= i
        j=i+1
        while(j<el_count):
            if ulist[j]>ulist[max_index]:
                max_index=j
            j=j+1
        temp = ulist[i]
        ulist[i]= ulist[max_index]
        ulist[max_index] = temp
    return ulist

def main(list1, list2):
    while True:
        print("Select an action (enter a letter):")
        
        print("\tA: Display a list that consists of all the even index elements (let's think that 0 is even) of the first list and the odd index ones from the second.")
        print("\tB: Display a list that consists of all the even index elements of the second list and the odd index ones from the first.")
        print("\tNote: the original indexes of the elements must be preserved (the first element in the first position of the new list, the second element in the second position, etc.).")
        print("\tC: Display a list from the task item a, but sorted in ascending order.")
        print("\tD: Display a list from the task item a, but sorted in descending order.")
        print("\tE: Display a list from the task item b, but sorted in ascending order.")
        print("\tF: Display a list from the task item b, but sorted in descending order.")
        print("\tG: Finish")
        print(">>", end=" ")

        user_choice = str(input()).lower()

        match user_choice:
            case "a":
                print(union_even_and_odd(list1, list2), end="\n\n")
                continue
            case "b":
                print(union_even_and_odd(list2, list1), end="\n\n")                
                continue
            case "c":
                print(sort_asc(union_even_and_odd(list1, list2)), end="\n\n")
                continue
            case "d":
                print(sort_desc(union_even_and_odd(list1, list2)), end="\n\n")
                continue
            case "e":
                print(sort_asc(union_even_and_odd(list2, list1)), end="\n\n")
                continue
            case "f":
                print(sort_desc(union_even_and_odd(list2, list1)), end="\n\n")
                continue
            case "g":
                print("Finished!")
                break
            case _:
                print("Wrong option! Please try again...")
                


if __name__ == "__main__":

    #Test data for the task:
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67, 55, 11, 2]
    
    main(list1, list2)