class MyClass:
    def __init__(self):
        self.public_attribute="im a public attribute"
        self._protected_attribute="im a protected attribute"
        self._private_attribute= "im a private attribute"
    def _public_method(self):
        print("Im a public method")
    def _protected_method(self):
        print("im a protected method")
    def _private_method(self):
        print("Im a private method ")
obj=MyClass()
print(obj.public_attribute)
obj._public_method()
print(obj._protected_attribute)
obj._protected_method()
print(obj._private_attribute)
obj._private_method()
