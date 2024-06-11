from day2 import grad


class studentinfo:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name


class studentmarks:
    def __init__(self, rollno, marks1, marks2, marks3):
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        sum = self.marks1+self.marks2+self.marks3

        self.avg = sum/3
        print(f"Average is {self.avg}")
        # print(grad(self.avg))



class main:
    def __init__(self, students):
        self.students = students
        for i in range(1, self.students+1):
            rollno = int(input(f"Enter the rollno of student{i} "))
            name = input(f"Enter the name of student{i} ")
            si = studentinfo(rollno, name)

        for i in range(1, self.students+1):
            rollno = int(input(f"Enter the rollno of student{i} "))
            m1 = int(input("Enter marks1 "))
            m2 = int(input("Enter marks2 "))
            m3 = int(input("Enter marks3 "))
            sm = studentmarks(rollno, m1, m2, m3)
            sm.average()



        # def average(self):
        #     sum = sm.marks1+sm.marks2+sm.marks3
        #     avg = sum/3
        #     print("Average is",self.avg)
n = int(input("Enter the number of student "))
m = main(n)
