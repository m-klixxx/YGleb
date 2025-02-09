def checker(var1):
    if type(var1) !=str:
        raise TypeError(f"mi n mojemo pracuvati z takim tipom danih - {type(var1)}, treba tip str!")
    else:
        return var1
    

my_var = 10
my_var2 = "hjhj"
checker(my_var)
checker(my_var2)