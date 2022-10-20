import ethernet

verbose = True


def check(test_number: int):
    with open(f"./tests/{test_number}.in", "r") as inp:
        with open(f"./tests/{test_number}.out", "r") as out:
            data = inp.read()
            out = out.read()
            expected_points, expected_length = list(map(int, out.split()))
            if verbose:
                print(f"\nTesting on:\n{data}\nExpected points: {expected_points}\nExpected length: {expected_length}")

            points, length = ethernet.solution(data)
            assert points == expected_points
            assert length == expected_length


def test1():
    check(1)


def test2():
    check(2)


def test3():
    check(3)


def test4():
    check(4)


def test5():
    check(5)


def test6():
    check(6)


def test7():
    check(7)


def test8():
    check(8)


def test9():
    check(9)


def test10():
    check(10)
