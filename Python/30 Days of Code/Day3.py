if __name__ == '__main__':
    N = int(input())

    if N % 2 == 0:
        if N in range(2,5) or N > 20:
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")
