import random
import time

OPERATORS = ['+',"-","*"]
MIN_OPERANDS = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

def generate_problem():
  left = random.randint(MIN_OPERANDS,MAX_OPERAND)
  right = random.randint(MIN_OPERANDS,MAX_OPERAND)
  operator = random.choice(OPERATORS)
  
  expr = str(left) + " " +operator + " " + str(right)
  # print(expr)
  answer = eval(expr)
  return expr, answer

# expr, answer = generate_problem()
# print(expr, " = " ,answer)

wrong = 0
input("Press any button to start!")
print("------------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
  expr, answer = generate_problem()
  while True:
    guess = input("Problem $" + str(i+1) + ": " + expr + " = ")
    if guess == str(answer):
      break
    wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("---------------")
print(f"You completed in {total_time} sec")
  