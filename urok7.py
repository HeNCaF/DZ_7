# try:
#     print("start")
#     print(error)
#     print("OK")
# except:
#     print("Error")
# print("code after")
# try:
#     print("start")
#     print(10/0)
#     print("Oki")
# # except NameError:
# #     print("We have a NameError")
# # except ZeroDivisionError:
# #     print("We have ZeroDivisionError")
# # except (NameError, ZeroDivisionError):
# #     print("ERROR")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Uncorrect type of file {type(var_1)}, "
#         f"you need string")
#     else:
#         return var_1
# first_var = 10
# checker(first_var)
# class BuildingError(Exception):
#     def __str__(self):
#         return f"Need more gold"
#  def check_material(amount_of_material, limit_value):
#      if amount_of_material > limit_value:
#          return "enough material"
#      else:
#         raise BuildingError(amount_of_material)
# #
# import warnings
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.warn("Syntax is gone", SyntaxWarning)
# try:
#     prant("test")
# except:
#     print("Warning processed")
# list = [1, 2, 3]
# iterator = iter(list)
# for elem in iterator:
#     print(elem)
 class Counter:
     def __init__(self, max_number):
         self.i = 0
         self.max_number = max_number
     def __iter__(self):
         self.i = 0
         return self
     def __next__(self):
         self.i += 1
         def kvadrat(number, max_degree):
             i = 0
             for __ in range(max_degree):
                 yield number ** i
                 i += 1
         res = kvadrat(self.i, self.max_number)
         print(res)
         for _ in res:
             print(_)
         if self.i > self.max_number:
             raise StopIteration
         return self.i
 count = Counter(5)
 for elem in count:
     print(elem)
#def checker(function):
#   def checkef(*args, **kwargs):
#        try:
#            result = function(*args, **kwargs)
#        except Exception as exc:
#            print(f"Problem with {exc}")
#        else:
#            print(f"No problem. Result - {result}")
#    return checker
#@checker
#def calculate(expression):
#    return eval(expression)
#calculate("2+2")
