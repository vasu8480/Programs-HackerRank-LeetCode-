def print_formatted(number):
    pad = len('{0:b}'.format(number))
    for i in range(1,number+1):
        print(str(i).rjust(pad), oct(i)[2:].rjust(pad), hex(i)[2:].upper().rjust            (pad), bin(i)[2:].rjust(pad) )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)