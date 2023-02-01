'''
You are given an array A representing heights of students. All the students are asked to stand in rows. The students arrive by one, sequentially (as their heights appear in A). For the i-th student, if there is a row in which all the students are taller than A[i], the student will stand in one of such rows. If there is no such row, the student will create a new row. Your task is to find the minimum number of rows created.


Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns the minimum number of rows created.


For example, given A = [5, 4, 3, 6, 1], the function should return 2.


Students will arrive in sequential order from A[0] to A[N−1]. So, the first student will have height = 5, the second student will have height = 4, and so on.


For the first student, there is no row, so the student will create a new row.


Row1 = [5]

For the second student, all the students in Row1 have height greater than 4. So, the student will stand in Row1.


Row1 = [5, 4]

Similarly, for the third student, all the students in Row1 have height greater than 3. So, the student will stand in Row1.


Row1 = [5, 4, 3]

For the fourth student, there is no row in which all the students have height greater than 6. So, the student will create a new row.


Row1 = [5, 4, 3]

Row2 = [6]

For the fifth student, all the students in Row1 and Row2 have height greater than 1. So, the student can stand in either of the two rows.


Row1 = [5, 4, 3, 1]

Row2 = [6]

Since two rows are created, the function should return 2.


Assume that:


N is an integer within the range [1..1,000]

each element of array A is an integer within the range [1..10,000]


In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''

import sys

def find_rows(student, rows):
  row_indicies = []
  for i, row in enumerate(rows):
    good_row = True
    for e in row:
      if e < student:
        good_row = False
        break
    
    if good_row:
      row_indicies.append(i)
    
    
  return row_indicies
    

def solution(A):
  """Your solution goes here."""
  all_answers = [len(a) for a in find_solution(A)]
  return min(all_answers)


def find_solution(A_sub):
  student = A_sub[-1]
  if len(A_sub) == 1:
    return [[[student]]]
  all_solns = find_solution(A_sub[:-1])
  new_all_solns = []
  for soln in all_solns:
    acceptable_rows_i = find_rows(student, soln)
    if not acceptable_rows_i:
      new_soln = soln.copy()
      new_soln.append([student])
      new_all_solns.append(new_soln)
      continue
    
    for i in acceptable_rows_i:
      new_soln = soln.copy()
      new_soln[i].append(student)
      new_all_solns.append(new_soln)
      
  return new_all_solns


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
