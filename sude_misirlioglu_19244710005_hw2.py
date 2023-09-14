def check(answer, answer_key):
    grade=0
    for i in range(10):
        if(answer[i]==answer_key[i]):
            grade=grade+10
        return grade

stu = {}
print ("Enter answer key: ")
answer_key=input()
sum=0
n=5
while (n>0):
    print("Enter name: ")
    name=input()
    print("Enter surname: ")
    surname=input()
    print("Enter answers: ")
    answer=input()
    grade=check(answer, answer_key)
    stu[(name, surname)]=grade
    sum+=grade
    n=n-1

print("Student Dictionary:\n",stu)
Average=float(sum)/5
print("\nAverage: ",Average)
print("\nStudents above average")
for a,b in stu:
    if(stu[(a,b)])>Average: 
        print("Name:",b,",",a[0],".","Grade:",stu[a,b])

print("Who are you searching for?")
search=input()
for i,j in stu:
    if(i==search or j==search):
        print(i,j,"received",stu[i,j])