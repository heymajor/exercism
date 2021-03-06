def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    for i, score in enumerate(student_scores):
        # print(score)
        student_scores[i] = round(score)
        # print(score)
    return student_scores


# print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    counter = []
    for _, score in enumerate(student_scores):
        if score <= 40:
            counter.append(score)

    return len(counter)


# print(count_failed_students(student_scores=[90, 40, 55, 70, 30, 25, 80, 95, 38, 40]))


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    counter = []
    for _, score in enumerate(student_scores):
        if score >= threshold:
            counter.append(score)
    return counter


# print(
#     above_threshold(
#         student_scores=[90, 40, 55, 70, 30, 68, 70, 75, 83, 96], threshold=75
#     )
# )


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    score_diff = round((highest - 41) / 4)
    counter = 41
    scores = [counter]
    for _ in range(3):
        counter += score_diff
        scores.append(counter)
    return scores


# print(letter_grades(highest=100))
# print(letter_grades(highest=88))


def student_ranking(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """
    output = []
    counter = 1
    for index, scores in enumerate(student_scores):
        output.append(f"{counter}. {student_names[index]}: {scores}")
        counter += 1
    return output


# student_scores = [100, 99, 90, 84, 66, 53, 47]
# student_names = ["Joci", "Sara", "Kora", "Jan", "John", "Bern", "Fred"]
# print(student_ranking(student_scores, student_names))


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    # for name, score in student_info:
    #     if score == 100:
    for student in student_info:
        # print("boop", student)
        if student[1] == 100:
            return student
    return []


# print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))
# print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))
