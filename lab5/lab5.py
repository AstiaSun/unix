import struct
from math import log, fabs

from multiprocessing import Pipe, Process


EPS = 0.0000001


def factorial(x):
    if x == 1:
        return x
    return x * factorial(x - 1)


def library_function(x):
    return log(1 + x**2)


def summary_function(x):
    total_sum = 0
    n = 1
    previous_x = 1
    x_2 = x * x
    while True:
        s = 1
        if n % 2 == 0:
            s = -1
        previous_x = previous_x * x_2
        new_sum = total_sum + (s * previous_x / n)
        if (abs(new_sum - total_sum)) < EPS:
            break
        total_sum = new_sum
        n += 1
    return total_sum


def binary(num):
    return ''.join(bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))


def to_float(ff):
    f = int(ff, 2)
    return struct.unpack('f', struct.pack('I', f))[0]


def printer(pipe):
    output_, input_ = pipe
    i = 0
    while True:
        try:
            if i % 4 == 0:
                print("===========\n")
            msg = output_.recv()
            print(to_float(msg))
            i += 1
        except EOFError:
            break


def main():
    print("Enter amount of samples.")
    N = int(input("N = "))
    a = -1
    b = 1
    step = (fabs(a) + fabs(b)) / N
    i = a + EPS

    consumer, producer = Pipe()

    proc = Process(target=printer, args=[(consumer, producer)])
    proc.start()

    while i <= b:
        lib_value = library_function(i)
        sum_value = summary_function(i)
        producer.send(binary(i))
        producer.send(binary(lib_value))
        producer.send(binary(sum_value))
        producer.send(binary(fabs(fabs(lib_value) - fabs(sum_value))))
        i += step

    proc.join()


if __name__ == '__main__':
    main()

