# Exercises of comprehension: which is of the class and which is of the instance

class A:

    counter = 0 

if __name__ == "__main__":
    if False:
        n = A()
        m = A()
        print(n.__dict__)       #content of dict "n" 
        print(m.__dict__)       #content of dict "m"
        print(A.__dict__)       #content of dict "A"
        n.counter = 2
        print(n.counter)        # 2
        print(m.counter)        # 0
        print(A.counter)        # 0
        print(n.__dict__)
        print(m.__dict__)
        print(A.__dict__)
        A.counter = 5
        print(n.counter)       # 2
        print(m.counter)       # 5
        print(A.counter)       # 5
        print(n.__dict__)
        print(m.__dict__)
        print(A.__dict__)
        n.__class__.counter = 9
        print(n.counter)       # 2
        print(m.counter)       # 9
        print(A.counter)       # 9
        print(n.__dict__)
        print(m.__dict__)
        print(A.__dict__)
        print(isinstance(n, A))
        n = A()
        print(n.counter)       # 9
        print(m.counter)       # 9
        print(A.counter)       # 9
        print(n.__dict__)
        print(m.__dict__)
        print(A.__dict__)







