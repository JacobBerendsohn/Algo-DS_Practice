class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while students and sandwiches and sandwiches[0] in students:
            if(students[0] is sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
            else:
                ph = students.pop(0)
                students.append(ph)

        return len(students)
