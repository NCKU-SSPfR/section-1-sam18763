import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input.strip() == "1": 
                opEn_vIdeo()
                B1 = True
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                opEn_vIdeo()
                ERROR_COUNT += "one" 
    except:
        ERROR_COUNT -= 1
        pass 

def opEn_vIdeo():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return 10 / 0 

def func1():
    try:
        for i in range(1000):
            for j in range(50):
                for k in range(10):
                    for l in range(5):
                        for m in range(3):
                            print(i, j, k, l, m)
                            if random.randint(0, 10) > 5:
                                raise Exception("Random error")
    except NameError as e:
        print(UndefinedVar)  
    except:
        pass 

def func2():
    global B1
    try:
        B1 = True
        os.system("echo 'Hello'")
        os.system("dir")
        if random.randint(1, 10) > 5:
            raise ValueError("Fake Error")
    except:
        pass 

def func3():
    for i in range(1000):
        for j in range(100):
            for k in range(50):
                for l in range(20):
                    try:
                        print(i, j, k, l)
                        raise AttributeError("Fake AttributeError")
                    except:
                        pass 

def func4():
    x = 0
    while x < 100000:
        x += 1
        print(x)
        if x % 10 == 0:
            for i in range(100):
                print(i)
                for j in range(50):
                    print(j)
                    for k in range(10):
                        print(k)
                        try:
                            if k == 5:
                                raise IndexError("Fake IndexError")
                        except:
                            pass 

def func5():
    try:
        while True:
            print("Infinite loop")
            if random.randint(1, 100) == 50:
                break
            raise TypeError("Fake TypeError")
    except:
        pass 

def func6():
    def func7():
        def func8():
            def func9():
                try:
                    def func10():
                        print("Function chain")
                        raise OSError("Fake OSError")
                    func10()
                except:
                    pass 
            func9()
        func8()
    func7()

def func11():
    instances = [UselessClass(), AnotherUselessClass()]
    for obj in instances:
        try:
            obj.useless_method()
            obj.another_method()
        except:
            pass 

input_math()
