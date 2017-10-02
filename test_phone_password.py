from phone_password import words_from_number
import nose

def test_squidward():
    squidward = "778439273"
    words = words_from_number(squidward)
    assert "squidward" in words
    print "squidward test passed"

def test_daniel():
    random_num = "326435"
    words = words_from_number(random_num)
    print words
    assert "daniel" in words
    print "daniel test passed"

if __name__ == "__main__":
    nose.run()
