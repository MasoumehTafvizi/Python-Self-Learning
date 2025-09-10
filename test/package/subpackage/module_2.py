from package.module_1 import function_in_module_1

def function_in_module_2():
    print("This a function in module 2")
    function_in_module_1()
    
    
    
print(f"Package structure in module_2.py: {__package__}")