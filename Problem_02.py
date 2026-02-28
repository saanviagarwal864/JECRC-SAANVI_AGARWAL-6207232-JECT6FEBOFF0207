'''
Question 2:
Student Marks Performance Tracker
'''
class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        for student in students:
            for subject, marks in student["marks"].items():
                if subject not in subject_total:
                    subject_total[subject]=0
                    subject_count[subject]=0
                subject_total[subject]+=marks
                subject_count[subject]+=1
        subject_average={}
        for subject in subject_total:
            subject_average[subject]=subject_total[subject] / subject_count[subject]
        highest_subject=None
        highest_average=-1

        for subject in subject_average:
            if subject_average[subject]>highest_average:
                highest_average=subject_average[subject]
                highest_subject=subject
        return subject_average, highest_subject