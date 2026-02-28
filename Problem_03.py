'''
Question 3:
Hospital Patient Visit Counter
'''
class Solution:

    def department_patient_count(self, visits):
        dept_count = {}
        for record in visits:
            dept=record["department"]
            if dept in dept_count:
                dept_count[dept]+=1
            else:
                dept_count[dept]=1

        max_department=None
        max_count=0

        for dept in dept_count:
            if dept_count[dept]>max_count:
                max_count=dept_count[dept]
                max_department=dept
     

        return [dept_count,max_department]