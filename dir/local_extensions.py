from cookiecutter.utils import simple_filter

@simple_filter
def add_1(s: str):
    return s + "1"
