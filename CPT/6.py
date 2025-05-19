# handling ZeroDivisionError
# a=10
# try:
#     print(a/0)
# except ZeroDivisionError:
#     print("a number can't divisible by 0")




'''Types of Errors
1 . ZeroDivisionError(denominator is 0)
2 . NameError(variable name not defined)
3 . TypeError
4 . KeyboardInterrupt
5 . Exception(built-in exception) used for base class / all exceptions
6 . SystemExit - sys.exit()
7 . StandardError - except sys.exit()/StopIteration
8 . OverflowError - numeric type errors exceeds limit
9 . ArthematicError - base class for all clac
10. IoError - Import file error
11. FloatingPontError
12. AssertionError
13. AttributeError
14. ImportError
15. KeyError
16. EnvironmentError
17. EOFError
18. LookupError
19. StopIterationError
20. SyntaxError
21. SystemError
22. IndentationError
'''



#Multiple Exception Hadling
# try:
#     num=int(input("enter the number:"))
#     print(num**3)
# except (KeyboardInterrupt):
#     print("you have to enter number not string")
# except ValueError:
#     print("enter valid number")
# print("you have entered this")



#Raise an exception
# try:
#     num=10
#     print(num)
#     raise ValueError
# except:
#     print("esafhsuhvlwaWVUv")


# re-=raise an error
# try:
#     raise NameError
# except:
#     print("re-raise")
#     raise


#using instance
# try:
#     raise Exception('hi','mhesh','hdtd')
# except Exception as rerf:
#     print(type(rerf))
#     #print(rerf.args)
#     print(rerf)
#     a,b,c=rerf.args
#     print(a,b,c)


# def div(n,m):
#     try:
#         k=n/m
#         print(k)
#     except ZeroDivisionError:
#         print("m is 0")
# a=int(input("enter:"))
# b=int(input("enter"))
# div(a,b)


# class myerror(Exception):
#     def __init__(self,value):
#         self.value=value
#     def __str__(self):
#         return repr(self.value)
# try:
#     raise myerror(99)
# except myerror as m:
#     print(type(m))


class Calculator:
    def input_numbers(self):
        try:
            self.one=float(input("Enter value1:"))
            self.two=float(input("Enter value2:"))
        except ValueError:
            print("Invalid input....please enter numbers")
            self.input_numbers()
    def add(self):
        return self.one+self.two
    def sub(self):
        return self.one-self.two
    def mul(self):
        return self.one*self.two
    def divide(self):
        if self.two==0:
            raise ZeroDivisionError("cannot divide with zero")
        return self.one/self.two
    def modulo(self):
        return self.one%self.two
    def expo(self):
        return self.one**self.two
    def floor_division(self):
        return self.one//self.two




def main():
    cal=Calculator()
    while True:
        display_menu()
        choice=input("enter operation you want to perform (1-8):")
        if choice=='8':
            print("Exit")
            break
        cal.input_numbers()
        try:
            if choice=='1':
                print(f"Result: {cal.add()}\n")
            elif choice=='2':
                print(f"Result: {cal.sub()}\n")
            elif choice=='3':
                print(f"Result: {cal.mul()}\n")
            elif choice=='4':
                print(f"Result: {cal.divide()}\n")
            elif choice=='5':
                print(f"Result: {cal.modulo()}\n")
            elif choice=='6':
                print(f"Result: {cal.expo()}\n")
            elif choice=='7':
                print(f"Result: {cal.florr_divide()}\n")
            else:
                print("Invalid Choice , select from 1-8")
        except ZeroDivisionError as e:
            print(f"Error : {e}")
        except Exception as e:
            print(f"Unexpected error : {e}")
def display_menu():
    print("\n ===== Calculator Menu ====  \n1.Addition\n2.Suntraction\n3.Multiplication\n4.division\n5.modulo\n6.Exponent\7.Floor_division\n8.Exit")
main()