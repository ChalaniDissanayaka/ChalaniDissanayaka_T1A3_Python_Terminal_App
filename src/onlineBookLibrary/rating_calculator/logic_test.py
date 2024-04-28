import logic


# Test calculate_average_rating

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

answer7 = logic.calculate_number_of_read_times(0)
print(answer7)
assert answer7 == 1


answer8 = logic.calculate_number_of_read_times(14)
print(answer8)
assert answer8 == 15
