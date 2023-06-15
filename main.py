from typing import List

def get_requirements(file_path : str) -> List[str] :
    with open(file_path) as f :
        requirements = f.read().split('\n')
    return requirements[:-1]
print(get_requirements('requirements.txt'))