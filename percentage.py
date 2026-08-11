physics=67
chemistry=41
maths=40
biology=68
computer=48
total=physics+ chemistry+ biology+ maths+ computer
percentage=total/5
if percentage >= 90 :
   grade="a"
elif percentage >= 80 :
   grade="b"
elif percentage >= 70 :
   grade="c"
elif percentage >=60 :
   grade="d"
elif percentage >= 40 :
   grade="e"
else:
   grade="f"

print("total marks=",total)
print("percentage=",percentage)
print("grade=",grade)