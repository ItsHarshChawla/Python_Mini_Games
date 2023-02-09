print('----------------------------------------')
print('    Welcome to My Computer Quiz!        ')
print('----------------------------------------')

print ('This Quiz comprise of 4 Questions!\n')

playing = input("Do You Want To Play? (yes/no)\nAns: ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's Play :)\n")
score = 0

answer = input("1. What does CPU stands for?\nAns: ")
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("2. What does GPU stands for?\nAns: ")
if answer.lower() == 'graphics processing unit':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("3. What does RAM stand for?\nAns: ")
if answer.lower() == "random access memory":
    print('Correct!\n')
    score += 1
else:
    print("Incorrect!\n")

answer = input("4. What does PSU stand for?\nAns: ")
if answer.lower() == "power supply unit":
    print('Correct!\n')
    score += 1
else:
    print("Incorrect!\n")

percentile = (score/4) * 100
if percentile == float(100):
    print('You are Smart!')

if percentile == float(75):
    print('Good Job!')

if percentile <= float(50):
    print('Better Luck Next Time!')

print("You got " + str(score) + " questions correct!")
print("You got " + str(percentile) + "%.\n")