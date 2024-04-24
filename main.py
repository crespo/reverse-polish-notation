from Stack import Stack


s = Stack()

while True:
    userInput = input("Type a operand (0...9) or a operator (+, -, *, /) . . . ")
    
    if not userInput:
        break
    else:
        if userInput.isdecimal():
            s.push(userInput)
        else:
            if s.size() < 2:
                print("Need two integers on the stack to operate.")
            else:
                n2 = int(s.pop())
                n1 = int(s.pop())
                if userInput == "+":
                    s.push(n1 + n2)
                elif userInput == "-":
                    s.push(n1 - n2)
                elif userInput == "*":
                    s.push(n1 * n2)
                elif userInput == "/":
                    s.push(int(n1 / n2))
                else:
                    s.push(n1)
                    s.push(n2)
                    print("Invalid input.")

        s.toString()