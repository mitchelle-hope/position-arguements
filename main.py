def greet_and_multy(*args,**kwargs):
     multiply=1
     for i in args:
        multiply*=i
        print(multiply)
     print(f"Hello{kwargs}")