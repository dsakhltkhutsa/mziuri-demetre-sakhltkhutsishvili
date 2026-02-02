
with open("titanic.txt", "r") as f:
    content = f.readlines()[1:]

female = 0
male = 0
survived = 0
unsurvived = 0
for line in content:
    person = line.strip().split(",")
    if len(person) > 4:
        gender = person[4].strip()
        if gender == "female":
            female += 1
        elif gender == "male":
            male += 1
    if len(person) > 1:
        if person[1] == "1":
            survived += 1
        elif person[1] == "0":
            unsurvived += 1
    if len(person) > 3:
        if person[2] == "1"
            













print(survived)
print(unsurvived)
print(342*100/891)
print(549*100/891)
print(male)
print(female)
print(577 *100 / 891)
print(314 * 100 / 891)


















