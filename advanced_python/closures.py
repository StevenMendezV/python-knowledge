def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas de caracteres"
        return string * n 
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola "))

if __name__=="__main__":
    run()