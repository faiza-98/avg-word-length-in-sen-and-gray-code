def avg_length(line):
    count=0
    total=0
    for word in line.split():
        length=len(word)
        total+=length
        count+=1
        average = total/count
    return average
n=input("Enter a sentence \n")
value=avg_length(n)
print("the average length of a word in a sentence is", value)
