'''
Take the code from homework #5 and modify it.

- Project class, SubProject class and main() method should be stored in different files.
- Import the file with Project class to the file with SubProject class.
- Import the file with SubProject class to the file with main() method.
- The updated homework should work as it worked before the update.
'''
from homework4 import str_input_validation, num_input_validation, quit_program
from homework5 import SubProject


def main():
    ###     
    #take project data from user
    project_name = "None"
    customer = "None"
    customers_country = "None"
    project_type = "None"
    number_of_devs = 0
    number_of_qas = 0
    project_duration = 0
    parrent_prj = "None"
    dev_manager_price_per_month = 0
    qa_manager_price_per_month = 0
    
    print("Type necessary project info:")

    print("Project name:\n>>", end=" ")
    project_name = str_input_validation()
    print("Customer:\n>>", end=" ")
    customer = str_input_validation()
    print("Customers_country:\n", end=" ")
    customers_country = str_input_validation()
    print("Project type:\n>>", end=" ")
    project_type = str_input_validation()

    print("Numbers of DEVs:\n>>", end=" ")
    number_of_devs = num_input_validation()
    print("Numbers of QAs\n>>", end=" ")
    number_of_qas = num_input_validation()
    print("Project duration (in months)\n>>", end=" ")
    project_duration = num_input_validation()

    print("Parrent project name:\n>>", end=" ")
    project_duration = str_input_validation()
    print("DEV Manager salary\n>>", end=" ")
    project_duration = num_input_validation()
    print("QA Manager salary\n>>", end=" ")
    project_duration = num_input_validation()


    # Project class init
    project = SubProject(
        project_name = project_name,
        customer = customer,
        customers_country = customers_country,
        project_type = project_type,
        number_of_devs = number_of_devs,
        number_of_qas = number_of_qas,
        project_duration = project_duration,
        parent_project= parrent_prj,
        dev_manager_price_per_month= dev_manager_price_per_month,
        qa_manager_price_per_month= qa_manager_price_per_month
        )
    
    #Menu processing
    while True:
        print("Menu:")
        print("a: Project Info")
        print("b: DEVs price per month")
        print("c: QAs price per month")
        print("d: DEVs+QAs price per year")
        print("q: Quit")

        choice = input("\n\nEnter your choice: ").lower()

        if choice == "a":
            print(project.show_project_info())
        elif choice == "b":
            print(project.devs_price_per_month())
        elif choice == "c":
            print(project.qas_price_per_month())
        elif choice == "d":
            print(project.full_price_per_year())
        elif choice == "q":
            quit_program()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    #initialize SubClass and process menu
    main()