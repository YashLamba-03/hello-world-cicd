from app import hello_Devops

def test_hello_Devops():
    assert hello_Devops() == "Hello, DevOps!"

def test_return_type():
    assert isinstance(hello_Devops(), str)
