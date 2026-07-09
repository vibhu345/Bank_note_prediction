from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT="-e."
def requirements_download(file_path:str)-> List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements ]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements





setup(
    name="Bank_prediction_Project",
    author="Vibhanshu_Gupta",
    author_emil="vibhanshugupta875@gmail.com",
packges=find_packages(),
install_requires=requirements_download("requirements.txt"),
version="0.0.0.1"
)
