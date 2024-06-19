# # challenge #1
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for key in student_scores:
#     grade = "Fail"
#     if student_scores[key] >= 91:
#         grade = "Outstanding"
#     elif student_scores[key] >= 81:
#         grade = "Exceed Expectation"
#     elif student_scores[key] >= 71:
#         grade = "Acceptable"
#     student_grades[key] = grade
#
# print(student_grades)


# # challenge #2
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Parish", "Lille", "Dijon"],
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"],
#     }
# ]
#
#
# def add_new_country(country, visits, cities):
#     new_value = {"country": country, "visits": visits, "cities": cities}
#     travel_log.append(new_value)
#
#
# add_new_country("Russia", 2, ["Moscow", "San Petersburg"])
# print(travel_log)
