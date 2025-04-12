from setuptools import find_packages, setup#find_packages will automatically find out all the packages available in the entire machine learning application(the directory C:\Users\syedh\mlproject that we have created)
# The setup function is the core of the setuptools library allowing developers to specify metadata and configuration for their python projects such as the package name, version, dependencies, and more.
from typing import List

HYPEN_E_DOT='-e .'
# we can directly install the setup.py file or whenever we are trying to install the packages from requirements.txt, at that time also the setup.py file should run to build the packages.
#In order to enable that feature we write "-e ." in requirements.txt because this will automatically trigger the setup.py file.

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)#if we are installing the packages from requirements.txt file in the form of a list, then -e . will also come. so in order to avoid that, we used this code.
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Hyder Syed',
author_email='Syedhyder40.hs@gmail.com',
packages=find_packages(),#when we run find_packages(), it will go and see that how folders have __init__.py file in them. If any folder has this __init__.py file, then find_packages() will consider that folder as a package itself and tries to build that folder as a package. Once we build that package, we will be able to import it anywhere we want by putting it in the pypi package itself.
install_requires=get_requirements('requirements.txt')

)

# whenever our next version comes, we can keep updating this setup() so that the entire packages will be automatically built and will be going to the pypi again.
