# Showing the use of __name__ and __main__
def main():
    print(f"I'm in messages.py's main function")
    print("Hello from:", __name__)

if __name__ == "__main__":
    print(f"{__name__}")
    main()