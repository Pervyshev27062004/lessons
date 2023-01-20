from lesson_10.classwork_101 import check_string

if __name__ == "__main__":
    assert check_string("+375 (29) 299-00-00") is not None
    assert check_string("+3333333333") is None
