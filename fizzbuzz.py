def fizzbuzz(sus):
    match sus:
        case _ if sus % 5 == 0 and sus % 3 == 0: print(f'{sus} -> FizzBuzz')
        case _ if sus % 3 == 0: print(f'{sus} -> Fizz')
        case _ if sus % 5 == 0: print(f'{sus} -> Buzz')
        case _: print(f'{sus} -> None')
def main():
    for n in range(1, 100):
        fizzbuzz(n)
if __name__ == '__main__':
    main()
