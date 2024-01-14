def save_to_file(content, filename):
    with open("../file.txt", "w") as file:
        file.write(content)
    pass
def read_file(filename):
    with open("../file.txt", "r") as file:
        return file.read()  #string.split(\n) etc

print(__name__)