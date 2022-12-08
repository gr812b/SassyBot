from contextlib import redirect_stdout
import random
import sys
import time
import threading
import queue
import io

# Create a queue to communicate between the threads


class QueueWriter(io.TextIOBase):
    def __init__(self, queue):
        self.queue = queue

    def write(self, s):
        self.queue.put(s)
 

def benchmark(function, iterations=1):
    # Print the start message with the animation
    print("Running benchmark for '%s'..." % function.__name__, end="")
    sys.stdout.flush()
    loading = ["|", "/", "-", "\\"]
    i = 0

    output_queue = queue.Queue()

    # Start a thread to run the function

    def run_function():
        global start_time, end_time
        start_time = time.time()
        for i in range(iterations):
        # Redirect the function's output to the queue
            with redirect_stdout(QueueWriter(output_queue)):
                function()
        end_time = time.time()

    thread = threading.Thread(target=run_function)
    thread.start()

    # Display the animation in the main thread
    while thread.is_alive():
        print("\b%s" % loading[i], end="", flush=True)
        sys.stdout.flush()
        time.sleep(0.1)
        i = (i + 1) % len(loading)

        # Print any output from the queue
        while not output_queue.empty():
            line = output_queue.get_nowait()
            print(line, end="")
            sys.stdout.flush()

    # Print the benchmark results and the function's output
    print("\bDone!\n")
    print("Total time: %s seconds" % (end_time - start_time))
    print("Time per iteration: %s seconds" %
            ((end_time - start_time) / iterations))
    print("\nFunction output:\n")

    # Print any remaining output from the queue
    try:
        while True:
            line = output_queue.get_nowait()
            print(line, end="")
    except queue.Empty:
        pass


def bogosort(arr):
    # bogosort implementation
    while not is_sorted(arr):
        random.shuffle(arr)


def is_sorted(arr):
    # check if array is sorted
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


def fibonacci(n):
    # fibonacci sequence implementation
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def hello_world():
    # output "Hello, World" using complex numbers, bogosort,
    # at least 6 if statements, and fibonacci numbers

    # create a list of characters
    chars = list("hello world")

    # sort the list using bogosort
    bogosort(chars)

    # create a complex number using the n-th fibonacci number
    # as the real part and the (n+1)-th fibonacci number as
    # the imaginary part, for each character in the sorted list
    complex_chars = [complex(fibonacci(i), fibonacci(i+1))
                     for i in range(len(chars) + 30)]

    # iterate over the complex numbers and output the corresponding
    # character if the real part is even, the imaginary part is odd,
    # and both the real and imaginary parts are greater than 10
    j = 0
    for i, c in enumerate(complex_chars):
        bogosort(list("123451" + str(i) + str(i) + "a"))
        if c.real % 2 == 0 and c.imag % 2 == 1:
            if c.real > 10 and c.imag > 10:
                if (j == 0):
                    print(chars[3], end="", flush=True)
                elif (j == 1):
                    print(chars[2], end="", flush=True)
                elif (j == 2):
                    print(chars[5], end="", flush=True)
                elif (j == 3):
                    print(chars[4], end="", flush=True)
                elif (j == 4):
                    print(chars[7], end="", flush=True)
                elif (j == 5):
                    print(chars[0], end="", flush=True)
                elif (j == 6):
                    print(chars[-1], end="", flush=True)
                elif (j == 7):
                    print(chars[8], end="", flush=True)
                elif (j == 8):
                    print(chars[-2], end="", flush=True)
                elif (j == 9):
                    print(chars[6], end="", flush=True)
                elif (j == 10):
                    print(chars[1], end="", flush=True)

                j += 1

    print()  # add a newline at the end


hello_world()


# benchmark(test_function, iterations=10)
