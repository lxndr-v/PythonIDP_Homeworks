import random
from homework4 import Project, str_input_validation, num_input_validation, quit_program

class SubProject(Project):
    def __init__(self, project_name, customers_country, project_type, number_of_devs, number_of_qas, project_duration, parent_project, dev_manager_price_per_month,        qa_manager_price_per_month ):
        super().__init__(project_name, customers_country, project_type, number_of_devs, number_of_qas, project_duration)

        self.parent_project = parent_project
        self.dev_manager_price_per_month = dev_manager_price_per_month
        self.qa_manager_price_per_month = qa_manager_price_per_month

    def show_project_info(self):
        return f"Parrent project: {self.parent_project}\n" + super().show_project_info()
    
    def devs_price_per_month(self):
        return super().devs_price_per_month()+self.dev_manager_price_per_month
    
    def qas_price_per_month(self):
        return super().qas_price_per_month()+self.qa_manager_price_per_month    
    
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
        return f"Our dev manager {random.choice(managers)} is better then the dev manager {random.choice(managers)} of {self.parent_project}\nOur QA manager {random.choice(managers)} is better then the QA manager {random.choice(managers)} of {self.parent_project}!"

    
if __name__ == "__main__":
    '''
    #test data
    project_name = "Fabula"
    customer = "Ferodir LTD"
    customers_country = "Argentina"
    project_type = "reversing"
    number_of_devs = 3
    number_of_qas = 1
    project_duration = 4

    parrent_prj = Project(project_name, customer, customers_country, project_duration, number_of_devs, number_of_qas, project_duration)
    sub_prj_test = SubProject(
        "Reborit",
        "Perru",
        "development",
        2,
        1,
        5,
        "",
        12000,
        7500
        )
    print(isinstance(sub_prj_test, Project))
    print(isinstance(sub_prj_test, SubProject))

    print(f"Parrent: {parrent_prj.project_name}")
    print(f"SubPrj: {sub_prj_test.project_name}")
    '''

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
    print("Customer:\n", end=" ")
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