import unittest


if __name__ == '__main__':
    tests = unittest.TestLoader().discover('./test', 'test_*.py')
    print(tests)
    # for test in tests:
    #     unittest.TextTestRunner(verbosity=2).run(test)
