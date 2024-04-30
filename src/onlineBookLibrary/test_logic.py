from src.onlineBookLibrary.rating_calculator import logic


# Test calculate_average_rating
def test_calculate_average_rating():
    answer1 = logic.calculate_average_rating(89, 11)
    print(answer1)
    assert answer1 == 8.09

    answer2 = logic.calculate_average_rating(80, 20)
    print(answer2)
    assert answer2 == 4.0

    answer3 = logic.calculate_average_rating(75, 18)
    print(answer3)
    assert answer3 == 4.17


# Test calculate_total_rating_score
def test_calculate_total_rating_score():
    answer4 = logic.calculate_total_rating_score(0, 4)
    print(answer4)
    assert answer4 == 4

    answer5 = logic.calculate_total_rating_score(4, 3.5)
    print(answer5)
    assert answer5 == 7.5

    answer6 = logic.calculate_total_rating_score(75.4, 4.25)
    print(answer6)
    assert answer6 == 79.65


# Test calculate_number_of_read_times
def test_calculate_number_of_read_times():
    answer7 = logic.calculate_number_of_read_times(0)
    print(answer7)
    assert answer7 == 1

    answer8 = logic.calculate_number_of_read_times(14)
    print(answer8)
    assert answer8 == 15


def test_validate_rating_score():
    answer9 = logic.validate_rating_score(4)
    assert answer9 is True

    answer10 = logic.validate_rating_score(0)
    assert answer10 is False

    answer11 = logic.validate_rating_score(8)
    assert answer11 is False

    answer12 = logic.validate_rating_score(-1)
    assert answer12 is False
