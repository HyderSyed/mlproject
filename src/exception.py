import sys#the sys module in python provides various function and variables that are used to manipulate different parts of the python runtime environment. Meaning for any exception that is getting controlled, the sys library will automatically have that information.
from src.logger import logging

def error_message_detail(error,error_detail:sys):#we are creating this function because we want to push our own custom message when error occurs. the first parameter(or input) to this function is the error message that we are getting and the second parameter is the error detail which will be basically present inside the sys.
    _,_,exc_tb=error_detail.exc_info()#the error_detail.exc_info() is talking about the execution info and it will give us three important information. We are not really interested in the first two but the last information will give us imformation (about on which file the exception has occured, on which line number the exception has occured...) which will be stored in exc_tb
    file_name=exc_tb.tb_frame.f_code.co_filename#here we are getting the file name from the exc_tb variable. To learn more about it, you need to read the document on custom exception handling in python.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))#The Python's `str.format()` method allows placeholders in a string to be replaced with specific values. The string template includes three placeholders, denoted by `{0}`, `{1}`, and `{2}`. These placeholders are replaced by the values of `file_name`, `exc_tb.tb_lineno`, and `str(error)` respectively. 
    return error_message

# We will call the error_message_detail() function inside the CustomException class whenever the error raises. The CustomException class is a custom exception class that inherits from the built-in Exception class. It is used to create user-defined exceptions in Python. By inheriting from the Exception class, we can create our own exception types with custom behavior and attributes.
# The __init__ method is a special method in Python that is called when an object of the class is created. In this case, it takes two parameters: error_message and error_detail. The error_message parameter is the message that will be displayed when the exception is raised, and the error_detail parameter is used to get more information about the error.

class CustomException(Exception):#this is our own custom exception class.
    def __init__(self,error_message,error_detail:sys):#this is the constructor method which is called when we create an instance of the class. It takes two parameters: error_message and error_detail of type sys.
        super().__init__(error_message)#since we are inheriting from the Exception class, we need to call the constructor of the parent class using super().__init__(error_message). This initializes the base class with the error_message.
        self.error_message=error_message_detail(error_message,error_detail=error_detail)#You may be surprised but we can do this, see the super keyword file that I have created in OOPs folder.
    
    def __str__(self):
        return self.error_message

