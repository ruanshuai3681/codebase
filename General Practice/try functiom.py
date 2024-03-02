def error_notification(_):
    while True:
        try:
            return int(input(_))
        except ValueError:
            print("This is not an integer")
            break
def main():
    num=error_notification("what is your number?")
    print(f"your number is {num}")

main()
