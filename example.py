import math
from mlflow.pyfunc import PythonModel


def greeting(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


print(greeting("World"))
print(add(1, 2))
