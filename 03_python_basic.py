def sum():
    while True:
        try:
            line = input()
            a = line.split()
            print('The result is {0}', int(a[0]) + int(a[1]))
            return a[0] + a[1]
        except:
            return None

if __name__ == '__main__':
    sum()