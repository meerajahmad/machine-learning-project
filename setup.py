'''
The setup.py file is an essential part of packaging and
distributing Python projects. It is used by setuptools
(or distributing in older python version) to define the configuration
of your project, such as its metadata. dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
        
    return requirements_lst

setup(
    name= 'mlproject',
    version= '0.0.1',
    author= 'Meeraj',
    author_email= 'meeraj.ahmad06@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements()
)