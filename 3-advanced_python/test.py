
def make_division(divisor: int) -> object:
    def number(dividend: int) -> int:
        return dividend / divisor

    return number

def run():
    division_by_3: function = make_division(3)
    print(int(division_by_3(18)))

    division_by_3: function = make_division(5)
    print(division_by_3(100))

    division_by_3: function = make_division(18)
    print(division_by_3(54))

if __name__ == "__main__":
    run()