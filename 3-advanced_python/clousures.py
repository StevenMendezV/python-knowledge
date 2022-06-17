
def repeater(n: int) -> object:
    def quantity(string: str) -> str:
        assert type(string) == str, "you can only use strings"
        return string * n
    
    return quantity



def run():
    repeat_5: function = repeater(5)
    print(repeat_5('Steven'))

if __name__ == "__main__":
    run()