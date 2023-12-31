from setuptools import setup , find_packages
from typing import List

def get_requirements(flie_path : str) -> List[str] :
    with open(file_path) as f :
        requirements = f.read().split('\n')
    return requirements[:-1]
    
setup(
    name = 'ML Practice' ,
    version = '1.0.0' ,
    author = 'ABC' ,
    author_email = 'abcd575@gmail.com' , 
    install_requires = ['numpy' , 'pandas' , 'Flask'] ,
    packages = find_packages()
)
