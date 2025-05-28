stack = []

stack.append("A")
stack.append("B")
stack.append("C")
print("Stack :", stack)

top_element = stack[-1]
print("Peek Or Top Element:", top_element)

popElemnt=stack.pop()
print ("Popped Element:", popElemnt)

print("Stack after pop:", stack)

isEmpity = not bool(stack)
print("Is Stack Empty:", isEmpity)

print("the Length of the stack is :" , len(stack))