def create_File():
    try:
      with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("This is line number 2\n")
        file.write("This is line number 3")
    except PermissionError as q:
        print("Permission Error", q)
    except Exception as p:
        print("Exception:", p)
    finally:
        print("Done writing the file.")

def read_File():
    try:
      with open("my_file.txt", "r")as file:  
        content = file.read()
        print(content)
    except PermissionError as q:
        print("Permission error:", q)
    except FileNotFoundError as h:
        print("File not found error:", h)
        
def append_File():
    try:
        with open("my_file.txt", "a") as file:
          file.write("This is the fourth line\n")
          file.write("This is another appended line\n")
          file.write("This is the last appended line\n")
    except PermissionError as q:
        print("Permission Error:", q)
    except Exception as p:
        print("Exception:", p)
    finally:
        print("Done writing the file.")
        

    