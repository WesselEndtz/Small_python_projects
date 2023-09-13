"""
Problem =
There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.
"""

def sortTheStudents(score: list[list[int]], k: int) -> list[list[int]]:
    # Create a list to store the test scores for the specified test (k)
    test_scores = []

    # Extract the test scores for the specified test (k) from each student's score list
    for studentscore in score:
        test_scores.append(studentscore[k])

    # Sort the test scores in descending order
    test_scores = list(sorted(test_scores, reverse=True))

    # Create a list to store the sorted students' data
    answlist = [''] * len(score)

    # Assign each student to their sorted position based on their test score
    for studentscore in score:
        place = test_scores.index(studentscore[k])
        answlist[place] = studentscore

    return answlist


#Test functionality
print(sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))
print(sortTheStudents([[3,4],[5,6]], 0))