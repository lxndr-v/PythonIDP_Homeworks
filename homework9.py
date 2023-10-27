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
       
    print("Type necessary project info:")

    print("Project name:\n>>", end=" ")
    ui_project_name = str_input_validation()
    print("Customers_country:\n", end=" ")
    ui_customers_country = str_input_validation()
    print("Project type:\n>>", end=" ")
    ui_project_type = str_input_validation()

    print("Numbers of DEVs:\n>>", end=" ")
    ui_number_of_devs = num_input_validation()
    print("Numbers of QAs\n>>", end=" ")
    ui_number_of_qas = num_input_validation()
    print("Project duration (in months)\n>>", end=" ")
    ui_project_duration = num_input_validation()

    print("Parrent project name:\n>>", end=" ")
    ui_parrent_prj = str_input_validation()
    print("DEV Manager salary\n>>", end=" ")
    ui_dev_manager_price_per_month = num_input_validation()
    print("QA Manager salary\n>>", end=" ")
    ui_qa_manager_price_per_month = num_input_validation()


    # Project class init
    sub_project = SubProject(
        projectName = ui_project_name,
        customersCountry = ui_customers_country,
        projectType = ui_project_type,
        numberOfDevs = ui_number_of_devs,
        numberOfQas= ui_number_of_qas,
        projectDuration= ui_project_duration,
        parentProject= ui_parrent_prj,
        devManagerPricePerMonth= ui_dev_manager_price_per_month,
        qaManagerPricePerMonth= ui_qa_manager_price_per_month
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
            print(sub_project.show_project_info())
        elif choice == "b":
            print(sub_project.devs_price_per_month())
        elif choice == "c":
            print(sub_project.qas_price_per_month())
        elif choice == "d":
            print(sub_project.full_price_per_year())
        elif choice == "q":
            quit_program()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    #initialize SubClass and process menu
    main()