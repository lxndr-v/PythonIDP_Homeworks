import random
from homework4 import Project, str_input_validation, num_input_validation, quit_program

class SubProject(Project):
    def __init__(self, projectName, customersCountry, projectType, numberOfDevs, numberOfQas, projectDuration, parentProject, devManagerPricePerMonth, qaManagerPricePerMonth ):
        super().__init__(projectName, customersCountry, projectType, numberOfDevs, numberOfQas, projectDuration)

        self.parent_project = parentProject
        self.dev_manager_price_per_month = devManagerPricePerMonth
        self.qa_manager_price_per_month = qaManagerPricePerMonth

    def show_project_info(self):
        return f"Parrent project: {self.parent_project}\n" + super().show_project_info()
    
    def devs_price_per_month(self):
        if self.number_of_devs != 0:
            return super().devs_price_per_month()+self.dev_manager_price_per_month
        else:
            return 0
    
    def qas_price_per_month(self):
        if self.number_of_qas != 0:
            return super().qas_price_per_month()+self.qa_manager_price_per_month    
        else:
            return 0
        
    
    def dev_qa_managers_info(self):
        managers = [
            "Sarah Johnson",
            "Michael Smith",
            "Emily Davis",
            "Kevin Anderson",
            "Jessica Lee",
            "David Wilson",
            "Lisa Martinez",
            "Jason Brown",
            "Amanda Taylor",
            "Brian Miller",
            "Rachel Garcia",
            "Mark Jackson",
            "Olivia White",
            "Jennifer Clark",
            "Daniel Hall",
            "Lauren Turner",
            "Matthew Walker",
            "Karen Baker",
            "Anthony Green",
            "Laura Carter"
        ]
        if self.number_of_devs >0 and self.number_of_qas > 0:
            return f"Our dev manager {random.choice(managers)} is better then the dev manager {random.choice(managers)} of {self.parent_project}!\nOur QA manager {random.choice(managers)} is better then the QA manager {random.choice(managers)} of {self.parent_project}!"
        elif self.number_of_devs == 0:
            return f"Our QA manager {random.choice(managers)} is better then the QA manager {random.choice(managers)} of {self.parent_project}!"
        elif self.number_of_qas == 0:
            return f"Our dev manager {random.choice(managers)} is better then the dev manager {random.choice(managers)} of {self.parent_project}!\n"



    
if __name__ == "__main__":

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
        print("e: Secret about our manager(s)")
        print("q: Quit")

        choice = input("\n\nEnter your choice: ").lower()

        if choice == "a":
            print(sub_project.show_project_info())
        elif choice == "b":
            print(sub_project.devs_price_per_month())
        elif choice == "c":
            print(sub_project.qas_price_per_month())
        elif choice == "d":
            print(sub_project.full_price())
        elif choice == "e":
            print(sub_project.dev_qa_managers_info())
        elif choice == "q":
            quit_program()
        else:
            print("Invalid choice. Please select a valid option.")