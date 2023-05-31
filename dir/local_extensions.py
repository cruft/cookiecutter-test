from cookiecutter.utils import simple_filter

@simple_filter
def add_1(s: str):
    return s + "1"

@simple_filter
def new_filter(s: str):
    # a new filter to test the extension update
    return s + " updated"
