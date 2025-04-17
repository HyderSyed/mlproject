import logging
import os
from datetime import datetime

# Now lets create our log file
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"#our log file is text file which will be created in this name convention of date and time.
#we also need to give the path of the log file where we want to create it.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#creating the path of the log file in the current working directory which is src.
#we are joining the current working directory with the logs folder and the log file name.
#Every file name will start with logs followed by the value in the LOG_FILE variable.
os.makedirs(logs_path,exist_ok=True)#here, exist_ok=True means even though there is a folder, keep on appending the files in that folder

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#if we want to override the functionality of logging, we have to probably set this up in the basic config.
logging.basicConfig(
    filename=LOG_FILE_PATH,#first we will give the file name where we basically want to save it. we will give the file name as LOG_FILE_PATH with respect to the file name.
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",#this is the format of the log file. we will give the timestamp, line number, name of the logger, level of the logger and the message.
    level=logging.INFO,#in the case of info only we are going to print these specific messages.


)

