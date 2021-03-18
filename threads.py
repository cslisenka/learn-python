import threading


def my_task():
    print("Hello {}".format(threading.current_thread()))


my_thread = threading.Thread(target=my_task)
my_thread.start()

# printing of the main thread
print(threading.current_thread())
