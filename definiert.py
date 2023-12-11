# Define variables
a = True
b = False
c = True

# Expressions
expression_1 = not a and not b
expression_2 = a or not c
expression_3 = False
expression_4 = a
expression_5 = a and not b
expression_6 = a and c
expression_7 = not (a and b) or not c
expression_8 = (a and b) and not c

# Print results
print("1. ¬a ∧ ¬b:", expression_1)
print("2. a ∨ ¬c:", expression_2)
print("3. False:", expression_3)
print("4. a:", expression_4)
print("5. a ∧ ¬b:", expression_5)
print("6. a ∧ c:", expression_6)
print("7. ¬(a ∧ b) ∨ ¬c:", expression_7)
print("8. (a ∧ b) ∧ ¬c:", expression_8)
