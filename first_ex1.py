import re
import threading
import time
def passwd_create(input1, pattern):
    if len(input1)>6 and len(input1)<=12:
        out = re.search(pattern, input1)
        if out:
            print(f"Valid password found: {out.group()}")
        else:
            print(f"Invalid password found: {input1}")


def thread_function(input1, pattern):
    passwd_create(input1, pattern)


if __name__ == "__main__":
    pattern = r"[A-Z]{1}[a-z]{1,4}\d+[$#@&]{1}\d{1}"

    inputs = [
        "Suma2#4","1234","Sathdhk123$1","fsdj3245#0","SWATHI@!@#","Swat1123#1","adv123@5"
    ]

    threads = []

    for user_input in inputs:
        thread = threading.Thread(target=thread_function, args=(user_input, pattern))
        threads.append(thread)
        time.sleep(2)
        thread.start()

    for thread in threads:
        thread.join()

    print("Password validation complete.")