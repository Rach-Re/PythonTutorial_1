S=input()
count=0
vowels='a,e,i,o,u,A,E,I,O,U'
for char in S:
    if char in vowels:
        count+=1
if count>0:
    print("Total number of vowels:",count)
else:
    print("No vowels were found.")
