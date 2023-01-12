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
### It is a new solution from IT-teacher
def check_coords(x1: int, y1:int, x2: int, y2: int) -> bool:
    return (
        abs(x1 - x2) == 1 and abs(y1-y2) == 2
    ) or (
        abs(x1 - x2) == 2 and abs(y1 - y2) == 1
    )


if __name__ == "__main__":
    x1 = int(input("Enter X1:"))
    y1 = int(input("Enter Y1:"))

    x2 = int(input("Enter X2:"))
    y2 = int(input("Enter Y2:"))

    if check_coords(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")


