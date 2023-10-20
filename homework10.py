'''
docker exec -it homework-10-pg psql -U prgmgr -d projects

'''

import psycopg2
from homework4 import Project, str_input_validation, num_input_validation, quit_program

def handle_database_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except psycopg2.Error as e:
            args[0].rollback()
            print(f"DB error in {func.__name__}: {e}")
            raise
    return wrapper


#Establich db connection
def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname='projects',
            user='prgmgr',
            password='homework10',
            host='localhost',
            port=54329
        )
        
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

@handle_database_exceptions
def create_tables(connection):
    with connection.cursor() as cursor:
        #Create Projects table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                project_id serial PRIMARY KEY,
                project_name VARCHAR(50) UNIQUE NOT NULL,
                customer VARCHAR(50),
                customers_country VARCHAR(50),
                project_type VARCHAR(50),
                number_of_devs FLOAT,
                number_of_qas FLOAT,
                project_duration FLOAT
            )
        """)

        #Create Results table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                result_id serial PRIMARY KEY,
                project_id INT NOT NULL,
                devs_price_per_month FLOAT,
                qas_price_per_month FLOAT,
                devs_and_qas_price_per_year FLOAT,
                project_info TEXT,
                CONSTRAINT fk_project
                    FOREIGN KEY (project_id) 
                    REFERENCES projects(project_id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )
        """)
    connection.commit()

#Insert data 
@handle_database_exceptions
def insert_project(connection, data):
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO projects (
                    project_name,
                    customer,
                    customers_country,
                    project_type,
                    number_of_devs,
                    number_of_qas,
                    project_duration
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s
                )""",
               (data.project_name, data.customer, data.customers_country, data.project_type, data.number_of_devs, data.number_of_qas, data.project_duration))

    connection.commit()

def insert_results(connection, projectID, devs_price_per_month, qas_price_per_month, devs_and_qas_price_per_year, project_info):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO results (
                                project_id,
                                devs_price_per_month,
                                qas_price_per_month,
                                devs_and_qas_price_per_year,
                                project_info
                ) VALUES (                                   
                            %s, %s, %s, %s, %s
                )""", (projectID,devs_price_per_month, qas_price_per_month, devs_and_qas_price_per_year, project_info))
        connection.commit()
    except psycopg2.Error as e:
        print(f"Result insertion error: {e}")

# TODO 
'''
a - add new Project properties from the keyboard. If the user chose this one, then the new properties should be stored to DB as a new Project. Also, the results of every methods execution should be stored to Results table.
b - read the existing from DB. If the user selected this one, then he/she needs to enter the Project ID to read from DB.
As a next step the user should select a/b/c/d to choose what method results should be displayed for the selected project. This result should be taken from Results table.
''' 
@handle_database_exceptions
def get_project_id(connection, project_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT project_id FROM projects WHERE project_name = %s",(project_name,))
        result = cursor.fetchone()
    return result

@handle_database_exceptions
def get_devs_price_per_month_from_db(connection, projectID):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT devs_price_per_month FROM results WHERE project_id = %s""", (projectID,))
        result = cursor.fetchone()
    return result

@handle_database_exceptions
def get_qas_price_per_month_from_db(connection, projectID):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT qas_price_per_month FROM results  WHERE project_id = %s""", (projectID,))
        result = cursor.fetchone()
    return result

@handle_database_exceptions
def get_devs_and_qas_price_per_year_from_db(connection, projectID):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT devs_and_qas_price_per_year FROM results  WHERE project_id = %s""", (projectID,))
        result = cursor.fetchone()
    return result

@handle_database_exceptions
def get_project_info_from_db(connection, projectID):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT project_info FROM results  WHERE project_id = %s""", (projectID,))
        result = cursor.fetchone()
    return result
    #make sure that only numbers >=0 can be entered
def int_input_validation():
    user_input = input()

    try:
        # Count the number of numeric characters in the input
        is_num = int(user_input)

        # Convert the input to an integer if there's exactly one numeric character
        if is_num >= 0:
            return is_num
        else:
            print("Input must contain only number that is >= 0. Try again, pls...")
            return num_input_validation()
    except:
        print("Input must contain only number that is >= 0. Try again, pls ...")
        return num_input_validation()

    
if __name__ == "__main__":
    init_connection = connect_to_db()
    create_tables(init_connection)
    init_connection.close()
    
    while True:
        user_choise = input("Type:\n\ta - add new Project\n\tb - get project data\n>>").lower()
        if user_choise == "a":
            #A
            # Read prj properties from keyboard
            print("Type necessary project info:")

            print("Project name:\n>>", end=" ")
            u_project_name = str_input_validation()
            print("Customer:\n>>", end=" ")
            u_customer = str_input_validation()
            print("Customers_country:\n>>", end=" ")
            u_customers_country = str_input_validation()
            print("Project type:\n>>", end=" ")
            u_project_type = str_input_validation()

            print("Numbers of DEVs:\n>>", end=" ")
            u_number_of_devs = num_input_validation()
            print("Numbers of QAs\n>>", end=" ")
            u_number_of_qas = num_input_validation()
            print("Project duration (in months)\n>>", end=" ")
            u_project_duration = num_input_validation()

            project_data = Project(
                project_name = u_project_name,
                customer = u_customer,
                customers_country = u_customers_country,
                project_type = u_project_type,
                number_of_devs = u_number_of_devs,
                number_of_qas = u_number_of_qas,
                project_duration = u_project_duration
            )
            #Connect to DB
            db_connection = connect_to_db()
            #  Save Project data to DB
            insert_project (
                connection = db_connection,
                data = project_data
            )
            ## Calculate results AND Store results in DB
            project_id = get_project_id(db_connection, project_data.project_name)
            insert_results(
                connection=db_connection,
                projectID=project_id,
                devs_price_per_month=project_data.devs_price_per_month(),
                qas_price_per_month=project_data.qas_price_per_month(),
                devs_and_qas_price_per_year=project_data.full_price_per_year(),
                project_info=project_data.show_project_info()
            )
            db_connection.close()
        elif user_choise == "b":
            #TODO only int validation function
            #read prj index from input
            print("Provide project id:\n", end='\n>>')
            project_choise = int_input_validation()
            #B
            while True:
                # a/b/c/d/ options processing by query every time
                print("Choose the data you need:",end='\n>>')
                print("Menu:")
                print("a: Project Info")
                print("b: DEVs price per month")
                print("c: QAs price per month")
                print("d: DEVs+QAs price per year")
                print("q: Quit")
                prj_data_choice = input("\n\nEnter your choice: ").lower()
                
                db_connection = connect_to_db()
                if prj_data_choice == "a":
                    print(get_project_info_from_db(connection=db_connection, projectID=project_choise))
                elif prj_data_choice == "b":
                    print(get_devs_price_per_month_from_db(connection=db_connection, projectID=project_choise))
                elif prj_data_choice == "c":
                    print(get_qas_price_per_month_from_db(connection=db_connection, projectID=project_choise))
                elif prj_data_choice == "d":
                    print(get_devs_and_qas_price_per_year_from_db(connection=db_connection, projectID=project_choise))
                elif prj_data_choice == "q":
                    quit_program()
                else:
                    print("Invalid choice. Please select a valid option.")
                db_connection.close()
            #?? WHY NOT store project results in memore after reading from db
        elif user_choise == "q":
            quit_program()
        else:
            print("Invalid choice. Please select a valid option.")



