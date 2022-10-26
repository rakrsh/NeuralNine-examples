#Type Hinting : https://www.youtube.com/watch?v=6KidYEtspNc&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=6
# install mypy module for checking - pip install mypy
# Use: mypy filename.py

def myfunction(parameter : int) -> int:
    return parameter + 10

def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction(10))