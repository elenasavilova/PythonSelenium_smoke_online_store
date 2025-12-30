import pytest

@pytest.fixture()
def set_up_test():
    print("Start test")

    yield

    print("Finish test")


@pytest.fixture(scope="module")
def group():
    print("Start test module")

    yield

    print("Finish test module")



