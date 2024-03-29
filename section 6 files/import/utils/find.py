#import example
from common.file_operations import save_to_file #inside current folder.
def find_in(iterable, finder, expected): #finds an element inside list.
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f"{expected} not found in provided iterable.")

class NotFoundError(Exception):
    pass

print(__name__)