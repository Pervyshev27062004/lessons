first = [4, 3]
last = [6, 1]
if __name__ == "__main__":
    if first[0] + 2 == abs(last[0]) and first[1] + 1 == abs(last[1]):
        print("Can bit")
    else:
        if first[0] + 2 == abs(last[0]) and first[1] == abs(last[1]) + 1:
            print("Can bit")
        else:
            if abs(first[0]) + 1 == last[0] and abs(first[1]) + 2 == last[1]:
                print("Can bit")
            else:
                if first[0] + 2 == last[0] and first[1] - 1 == last[1]:
                    print("Can bit")
                else:
                    print(" I know as it do")

