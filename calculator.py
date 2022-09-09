class InputHandler:
    def __init__(self):
        self.oper = ''
        self.numbers = []
    
    def take_operator(self):
        # First method that takes the operator
        # While loop works until the proper operator is provided
        while True:
            self.oper = input("Operation type: ")
            if self.oper not in ['-', '+', '*', '/']:
                print("Please provide only +, -, * or /")
                continue
            else:
                break     
        return self.oper
    
    def take_numbers(self):
        # Second method that takes the numbers
        # global str_add variable is set to True if at least one string is provided
        # counter variable is used to interrupt the main while loop and prevent dividing by 0
        global str_add
        counter = 0
        
        # First loop - asks for input until the user presses Enter
        while counter >= 0:
            # Second loop - checks if the proper input is provided
            while True:
                n = input("Provide number (press Enter to stop): ")
                if n == '':
                    # If empty string is provided, counter is set to -1, which ends the main while loop
                    counter = -1
                    break
                try:
                    # try-except block is used to check if the input is a number
                    n_float = float(n)
                    if counter > 0 and self.oper == '/' and n_float == 0:
                        print("You cannot divide by 0")
                        continue
                    self.numbers.append(n_float)
                    counter += 1
                    break
                except ValueError:
                    # If exception is raised, but addition was defined, input will be concatenated
                    if self.oper == '+':
                        self.numbers.append(n)
                        str_add = True
                        counter += 1
                        break
                    else:
                        print("Please provide a number.")
                        continue             
        return self.numbers
    

class Calculator:
    def __init__(self, oper, numbers):
        self.oper = oper
        self.numbers = numbers

    def calculate(self):
        # Method that performs math operations or concatenates strings
        if self.oper == '+' and str_add is True:
            # All elements of the list are converted to strings
            numbers_str = [str(n) for n in self.numbers]
            result = ''.join(numbers_str)
        else:
            result = self.numbers[0]
            for n in self.numbers[1:]:
                if self.oper == '+':
                    result += n
                elif self.oper == '-':
                    result -= n
                elif self.oper == '*':
                    result *= n
                else:
                    result /= n
        return result
        

str_add = False

print("Simple calculator: add (+), subtract (-), multiply (*) or divide (/).")
# Instance of the FileHandler class
inp = InputHandler()
calc_oper = inp.take_operator()
calc_numbers = inp.take_numbers()
print("Provided numbers: ", calc_numbers)

# Check if enough numbers were provided
if len(calc_numbers) < 2:
    print("Operation cannot be done. Please provide at least 2 numbers.")
else:
    # Instance of the Calculator class
    calc = Calculator(calc_oper, calc_numbers)
    result = calc.calculate()
    print("Result:", result)
