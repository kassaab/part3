def print_many_times(text, times):
    while times > 0:
        print(text)
        print()
        times -= 1

if __name__ == "__main__":
    print_many_times("python", 5)