
from app import hello_world, welcome_message


# Exercise 1: Test the Hello World message
def test_hello_world():
    assert hello_world() == "Hello, DevOps!"


# Exercise 5: Test the return type
def test_return_type():
    assert isinstance(hello_world(), str)


# Exercise 6: Test personalized welcome messages
def test_welcome_yash():
    assert welcome_message("Yash") == "Welcome to DevOps, Yash!"


def test_welcome_satvik():
    assert welcome_message("Satvik") == "Welcome to DevOps, Satvik!"

