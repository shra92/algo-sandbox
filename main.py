from src.threadsafe_cachedemo import ThreadSafeCacheDemo
from src.parse_huge_file import ParseHugeFile
def main():
    print("The list of projects implemented so far are:\n")
    print("1 - ThreadSafeCacheDemo\n")
    print("2 - ParseLargeFile\n")
    project = input("Project Number: you want to run\n")
    if project == "1":
        cache_demo = ThreadSafeCacheDemo()
        cache_demo.run()
    elif project == "2":
        parse_file = ParseHugeFile()
        parse_file.generate_huge_file()
        parse_file.run()


if __name__ == "__main__":
    main()