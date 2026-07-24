from src.threadsafe_cachedemo import ThreadSafeCacheDemo
def main():
    print("The list of projects implemented so far are:\n")
    print("1 - ThreadSafeCacheDemo\n")
    project = input("Project Number: you want to run\n")
    if project == "1":
        cache_demo = ThreadSafeCacheDemo()
        cache_demo.run()

if __name__ == "__main__":
    main()