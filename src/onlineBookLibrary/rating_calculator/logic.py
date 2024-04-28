def calculate_average_rating(total_rating_score, number_of_read_times):
    average_rating = round((total_rating_score / number_of_read_times), 2)
    return average_rating


def calculate_total_rating_score(total_rating_score, book_rating):
    total_rating_score = total_rating_score + book_rating
    return total_rating_score


def calculate_number_of_read_times(number_of_read_times):
    number_of_read_times = number_of_read_times + 1
    return number_of_read_times
