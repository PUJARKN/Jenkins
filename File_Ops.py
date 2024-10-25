
def create_file(file_name,content):
    with open(file_name,'w') as file:
        file.write(content)
    print("file {0} created successfully".format(file_name))


file_name = "C:\Arbeit\Learning\MyPythonFiles\demo.txt"
content = "This is demo for my first file \n Hello I am learning Python File Operation \n Third Line Content \n"

create_file(file_name,content)
