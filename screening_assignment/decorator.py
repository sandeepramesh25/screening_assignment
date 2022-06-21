#Decorator

def decorator_function(func):
    def inner_function():
        print("This is before actual function")
        func()
        print("This is after actual function")
    return inner_function()

@decorator_function
def actual_function():
    print("This is the actual function")