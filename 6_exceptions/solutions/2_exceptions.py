# 1. ZeroDivisionError
# 1/0

# 2. FileNotFoundError
# open("this_file_not_exist")

# 3. PermissionError
# open("C:\\Windows\\a","w")

# 4. TypeError
# 2 << 1.5

# 5. AssertionError
# assert False

# 6. ValueError
# open("file","e")

# 7. MemoryError
# [10] * 5_000_000_000_000

# 8. StopIteration
# def gen():
#     yield 10
# a = gen()
# next(a)
# next(a)

# 9. NameError (jeżeli name nie zostało zdefiniowane)
# 2 * name

# 10. ModuleNotFoundError
# import not_found
