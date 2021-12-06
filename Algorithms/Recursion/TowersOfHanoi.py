
def towers_of_hanoi(n, start='1', spare='2', target='3'):
    if n >= 1:
        towers_of_hanoi(n-1, start, spare, target)
        print(f'Move {start} to {target}.')
        towers_of_hanoi(n-1, spare, start, target)
    else:
        return


if __name__ == "__main__":

    towers_of_hanoi(4)
