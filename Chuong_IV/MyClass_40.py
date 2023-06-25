class MyClass:
    def __init__(self):
        self._protected_variable = "Protected Variable"

    def _protected_method(self):
        print("This is a protected method")

class MySubClass(MyClass):
    def __init__(self):
        super().__init__()

    def access_protected(self):
        print(self._protected_variable)
        self._protected_method()