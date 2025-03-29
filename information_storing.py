# ---------------------------------------------------------------------------
#  This program is used to store information of a person in a txt file named    after the person.
#--------------------------------------------------------------------------



# This is the structure of informatrion that will be stored in the file
class programmer:

  def __init__(self, name, salary, language):
    self.name = name
    self.salary = salary
    self.language = language
    print(f"Information of {self.name} is stored")

  def show_info(self):
    print(
        f"The name of the programmer is {self.name} \nHis salary is    {self.salary}\nHis language is {self.language}"
    )


# This function will store the information of the person in a file
def store_info(x):
  return f"The name of the programmer is {x.name} \nHis salary is {x.salary}\nHis language is {x.language}"


# This will take the number of employe as input that will be used to store the information of the employe
number_employe = int(input("Enter the number of employe: "))

# This will store the information of the employe
for i in range(1, number_employe + 1):
  name_employe = input(f"Enter the name of employe {i}: ")
  salary_employe = int(input(f"Enter the salary of employe {i}: "))
  language_employe = input(f"Enter the language of employe {i}: ")

  i = programmer(name_employe, salary_employe, language_employe)
  next = store_info(i)
  with open(F"{i.name}.txt", "w") as f:
    f.write(next)
