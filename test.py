import sys

def f():
    try:
        print("this is a test")
    except:
        sys.exit(1)
    finally:
        print("finally reached")
    sys.exit(0)

def test_f():
    f()
    assert sys.last_value == 0

if __name__=='__main__':
    f()

