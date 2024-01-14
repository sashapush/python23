from utils.common.file_operations import read_file, save_to_file #utils is package (not a folder, since it has __init__.py)
from utils.find import find_in #will show __name__ as __utils.find__ since importing runs the file.
#from file_operations import save_to_file #also can be

# save_to_file("Rolf", "data.txt")
# read_file("data.txt")
print(__name__)

#OR
#from file_operations import save_to_file, read_file
#print(save_to_file("Rolf", "data.txt"))
#print(read_file("data.txt"))