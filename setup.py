from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('Requirements.txt not found!')
    return requirement_lst

setup(
    name='Breast_Cancer',
    version='0.0.1',
    author='Santu',
    author_email='saisanthoshvc@rice.edu',
    packages=find_packages(),
    install_requires=get_requirements()
)