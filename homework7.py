'''
Homework #7

Make a console application which uses exception handling. You can use the code from any previous homework. 
All you need is just modify the error handling to use try/except features (if you didn't use it already).
Try to catch some special exception type, for example ValueError() and all other exceptions.
'''
from homework4 import quit_program

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            contents = file.read()
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return e
    except PermissionError as e:
        print(f"Permission error: {e}")
        return e
    except IOError as e:
        print(f"IO error: {e}")
        return e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return e
    else:
        print("File read successfully:")
        return contents
    finally:
        print("Execution completed")

def main():
    while True:
        print("\nInput file name:\n>>", end=" ")
        ufile_name = input()
        if ufile_name == "q":
            quit_program()
        else:
            print(read_file(file_name=ufile_name))

if __name__ == "__main__":
    main()