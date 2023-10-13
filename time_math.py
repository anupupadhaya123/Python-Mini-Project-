import random

OPERATORS = ['+',"-","*"]
MIN_OPERANDS = 3
MAX_OPERAND = 12

def generate_problem():
  left = random.randint(MIN_OPERANDS,MAX_OPERAND)
  right = random.randint(MIN_OPERANDS,MAX_OPERAND)
  operator = random.choice(OPERATORS)
  
  expr = str(left) + " " +operator + " " + str(right)
  # print(expr)
  answer = eval(expr)
  return expr, answer

expr, answer = generate_problem()
print(expr, " = " ,answer)