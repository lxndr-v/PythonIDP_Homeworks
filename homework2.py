'''
IDP for learning of Python from scratch
Python 3.10 or higher is required 

Homework #2
'''



def print_start():
# Print output for the user
    print("Choose the test data: ")
    print("\ta.Default test data:")
    print("\t\tlist1 = " + str(list1[:]))
    print("\t\tlist2 = " + str(list2[:]), end="\n\n")
    print("\tb.Enter your own data...\n>>", end=" ")
    
def take_int_list():
    # Take user's input and append to its own list
    while True:
        user_list = str(input())
        user_list = user_list.split()
        #check that all array items is decimal number
        try:
            is_number = [int(value) for value in user_list]
            return is_number   
        except ValueError:
            print("Error: Some values are not number\n Try again, pls: ", end="" )

def find_duplicates(list1, list2):
    duplicates = set()
    '''
    list1, list2 = set(list1), set(list2)
    duplicates = list1.intersection(list2)
    '''
    for num_from_list1 in list1:
        for num_from_list2 in list2:
            if num_from_list1 == num_from_list2:
                duplicates.add(num_from_list1)
    return duplicates
             
def find_differences(list1, list2):
    '''
    list1, list2 = set(list1), set(list2)
    differences= list1.symmetric_difference(list2)
    '''
    duplicates = find_duplicates(list1, list2)
    union = set(list1+list2)
    differences = union-duplicates
    
    return differences
    
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




def actions_processing(list1, list2):
    
    # User choice processing of which action should be performed
    while True:
        print("Select an action (enter a letter):")
        print("\tA: Display a list of elements which exist in both lists. For example: if number 5 is present in both links, then display it; if number 10 is present only in one list, then do not display it.")
        print("\tB: Display a list of elements (from both lists) which exist only in one list. For example: if number 5 is present in both links, then do not display it; if number 10 is present only in one list, then display it.")
        print("\tC: Display both lists sorted in ascending order")
        print("\tD: Display both lists sorted in descending order")
        print("\tE: Print a list of all elements of two lists that are less than 30")
        print(">>", end=" ")
        user_choise_action = str(input()).lower()
        
        match user_choise_action:
        #A: Display a list of elements which exist in both lists. For example: if number 5 is present in both links, then display it; if number 10 is present only in one list, then do not display it.
            
            case "a":
                print(find_duplicates(list1, list2))          
                break
                
        #B: Display a list of elements (from both lists) which exist only in one list. For example: if number 5 is present in both links, then do not display it; if number 10 is present only in one list, then display it.
            case "b":
                print(find_differences(list1, list2))
                break
        #C: Display both lists sorted in ascending order
            case "c":
                '''
                print(list1.sort())
                print(list2.sort())
                '''
                print(f"list1 = {sort_asc(list1)}")
                print(f"list1 = {sort_asc(list2)}")

                break
        #D: Display both lists sorted in descending order
            case "d":
                '''
                print(list1.sort(reverse = True))
                print(list2.sort(reverse = True))
                '''
                print(f"list1 = {sort_desc(list1)}")
                print(f"list1 = {sort_desc(list2)}")
                break
        #E: Print a list of all elements of two lists that are less than 30
            case "e":
                less_than_30 = []
                for item in list1+list2:
                    if item<30:
                        less_than_30.append(item)
                print(less_than_30)
                break
            case _ :
                print("Invalid input. Please, try again.")
                continue




if __name__ == "__main__":

    #Test data
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67]


    print_start()

    # User choice processing between test data and typed data 
    while True:
        user_choice_data = str(input())
        if user_choice_data == "a":
            actions_processing(list1, list2)
            break
        elif user_choice_data == "b":
            print("Enter the first list of numbers separated by spaces. For example, '1 2 3 4':")
            user_list1 =  take_int_list()      
            print("Enter the second list of numbers separated by spaces. For example, '1 2 3 4':")
            user_list2 = take_int_list()
        
            actions_processing(user_list1, user_list2)
            break
        else:
            print("Choose a or b option, please: ", end=" ")

    
