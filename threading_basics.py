import threading


def do_some_work(param: str):
    print(f"Doing some work in thread with param={param}")


val: str = "hello"
worker = threading.Thread(target=do_some_work, args=(val,))
worker.start()
worker.join()
print("The end")


