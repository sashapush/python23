class RuntimeErrorWithCode(TypeError):  # inherit existing error class
    # multiline string. When it's directly under class/method - it can be docstring (documentation)/ OR AT THE START OF THE FILE - as module/file definition
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):  # redefine init method to introduce additional data (code in this example)
        super().__init__(f'Error code {code}:{message}')  # call superclass with message as argument
        self.code = code  ##



err = RuntimeErrorWithCode("An arrow to the knee", 500)
print(err.__doc__) # == string#3-5
raise RuntimeErrorWithCode("An arrow to the knee", 500)
