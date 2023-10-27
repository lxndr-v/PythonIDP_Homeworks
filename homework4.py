class Project:
    
    price_per_dev = 10000
    price_per_qa = 6000

    def __init__(self, projectName, customersCountry, projectType, numberOfDevs, numberOfQas, projectDuration):
        self.project_name = projectName
        self.customers_country = customersCountry
        self.project_type = projectType
        self.number_of_devs = float(numberOfDevs)
        self.number_of_qas = float(numberOfQas)
        self.project_duration = float(projectDuration)
        
    def devs_price_per_month(self): #- this method calculates the monthly price for all devs on the project. For example the customer pays $10000 every month for one dev.
        return float(self.number_of_devs*self.price_per_dev)
        
    def qas_price_per_month(self): #- this method calculates the monthly price for all QAs the project. For example the customer pays $6000 every month for one QA.
        return float(self.number_of_qas*self.price_per_qa)

    def full_price(self): #- this method calculated the full (QA + dev) price per year.
        monthly_price_per_devs = self.devs_price_per_month()
        monthly_price_per_qas = self.qas_price_per_month()
        return float((monthly_price_per_devs+monthly_price_per_qas)*self.project_duration)
    
    def show_project_info(self): #- this method generates a string with the project information:
        project_info = ""
   
        if self.number_of_devs>0 and self.number_of_qas>0:
            project_info= (
                f"{self.project_type} project {self.project_name} from {self.customers_country} brings us:\n"
                +f"\t- {self.devs_price_per_month()+self.qas_price_per_month()} every month\n"
                +f"\t- Full price: {self.full_price()}"
                )
        
        elif self.number_of_devs>0 and self.number_of_qas==0:
            project_info =(
                f"{self.project_type} project {self.project_name} from {self.customers_country} brings us:\n"
                + f"\t- {self.devs_price_per_month()} per DEVs every month\n"
                + f"\t- Full price: {self.full_price()}\n"
                + "We need to sell them several QAs!"
                )

        elif self.number_of_devs==0 and self.number_of_qas>0:
            project_info =(
                f"{self.project_type} project {self.project_name} from {self.customers_country} brings us:\n"
                + f"\t- {self.qas_price_per_month()} per QAs every month\n"
                + f"\t- Full price: {self.full_price()}\n"
                + "We need to sell them several DEVs!"
                )
        elif self.number_of_devs==0 and self.number_of_qas==0:
                project_info = "Looks like nobody working here!"

        else: 
            project_info = "This area is restricted! Dragons live here!"
        return project_info
        
#make sure that user type atleast 1 letter or number
def str_input_validation():
    user_input = input()
    if any(c.isalnum() for c in user_input):
        return user_input
    else:
        print("Invalid input. Try again...\n>>")
        return str_input_validation()

#make sure that only numbers >=0 can be entered
def num_input_validation():
    user_input = input()

    try:
        # Count the number of numeric characters in the input
        is_num = float(user_input)

        # Convert the input to an integer if there's exactly one numeric character
        if is_num >= 0:
            return is_num
        else:
            print("Input must contain only number that is >= 0. Try again, pls...")
            return num_input_validation()
    except:
        print("Input must contain only number that is >= 0. Try again, pls ...")
        return num_input_validation()


def quit_program():
    print("Exiting the program. Bye-bye!")
    exit()
    

if __name__ == "__main__":
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

    # Project class init
    project = Project(
        ui_project_name, 
        ui_customers_country, 
        ui_project_type, 
        ui_number_of_devs, 
        ui_number_of_qas, 
        ui_project_duration
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
            print(project.full_price())
        elif choice == "q":
            quit_program()
        else:
            print("Invalid choice. Please select a valid option.")

