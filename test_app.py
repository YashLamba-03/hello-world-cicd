
from app import hello_world, welcome_message, main



def test_hello_world():
    assert hello_world() == "Hello, DevOps!"



def test_return_type():
    assert isinstance(hello_world(), str)



def test_welcome_yash():
    assert welcome_message("Yash") == "Welcome to DevOps, Yash!"


def test_welcome_satvik():
    assert welcome_message("Satvik") == "Welcome to DevOps, Satvik!"



def test_main():
    assert callable(main)


