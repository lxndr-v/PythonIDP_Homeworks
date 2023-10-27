import json

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
    
    def write_project_info_to_file(self, filename):
        project_info = {
            "project_name" : project_name,
            "customers_country" : customers_country,
            "project_type" : project_type,
            "number_of_devs" : number_of_devs,
            "number_of_qas" : number_of_qas,
            "project_duration" : project_duration
        }
        # Serializing json
        json_object = json.dumps(project_info, indent=4)
        try:
            # Append the new JSON object to the file
            with open(filename, "a+") as outfile:
                outfile.seek(0, 2)  # Move to the end of the file
                if outfile.tell() > 1:
                    # If the file is not empty, move the cursor back to find the last closing square bracket "]"
                    outfile.seek(outfile.tell() - 1)
                    last_char = outfile.read(1)
                    if last_char == "]":
                        # Remove the last closing square bracket
                        outfile.seek(outfile.tell() - 1)
                        outfile.truncate()
                    # Add a comma to separate the new JSON object
                    outfile.write(",")
                    outfile.write(json_object)
                    outfile.write("]")  # Add a closing square bracket to close the JSON array

                # Write the new JSON object
                else:
                    outfile.write(json_object)
                
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    #initialize class data from file
    @classmethod
    def read_project_info_from_file(cls, filename, search_key):
        try:
            with open(filename, "r") as openfile:
                data = json.load(openfile)
            
            for project_info in data:
                if search_key in project_info.values():
                    return cls(
                        project_info["project_name"],
                        project_info["customers_country"],
                        project_info["project_type"],
                        project_info["number_of_devs"],
                        project_info["number_of_qas"],
                        project_info["project_duration"],
                    )
            else:
                print(f"{search_key} was not found.")
                return None
        except FileNotFoundError:
            print(f"{filename} not found!")
            return None
        except json.JSONDecodeError:
            print(f"JSON decoding error in {filename}")
            return None

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

        if is_num >= 0:
            return is_num
        else:
            print("Input must contain only number that is >= 0. Try again, pls...")
            return num_input_validation()
    except:
        print("EXP:Input must contain only number that is >= 0. Try again, pls ...")
        return num_input_validation()

def write_user_output_to_file(project_name, user_data):
    try:
        with open(f"{project_name}.txt", "+a") as outfile:
            outfile.write(user_data+"\n")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occured: {e}")    

def quit_program():
    print("Exiting the program. Bye-bye!")
    exit()
    

if __name__ == "__main__":
    file_name= "projects_data.json"
    # Project class init

    while True:
        print("Choose input type:\n"+
              "\ta) Input from keyboard\n"+
              "\tb) Input from file\n")
        choise = str_input_validation().lower()

        #data input type selection
        if choise == "a":
            
            print("Type necessary project info:")

            print("Project name:\n>>", end=" ")
            project_name = str_input_validation()
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
            project = Project(project_name, customers_country, project_type, number_of_devs, number_of_qas, project_duration)
            project.write_project_info_to_file(filename=file_name)
            break
        elif choise == "b":
            while True:
                print("Type file name:\n>>", end=" ")
                file_name = str_input_validation()
                print("Type project name to import:\n>>", end=" ")
                search_key = str_input_validation()
                project = Project.read_project_info_from_file(filename=file_name, search_key=search_key)
                if project==None:
                    continue
                else:
                    print("Project data was imported successfully!")
                    break
            break
        else:
            print("Invalid input. Try again...")   

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
            write_user_output_to_file(project.project_name, project.show_project_info())
        elif choice == "b":
            write_user_output_to_file(project.project_name, f"DEVs price per month: {project.devs_price_per_month()}")
        elif choice == "c":
            write_user_output_to_file(project.project_name, f"QAs price per month: {project.qas_price_per_month()}")
        elif choice == "d":
            write_user_output_to_file(project.project_name, f"DEVs+QAs price per year: {project.full_price()}")
        elif choice == "q":
            quit_program()
        else:
            print("Invalid choice. Please select a valid option.")

