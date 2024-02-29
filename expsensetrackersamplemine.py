expenses=[]
sum =0
print()
print("-----Expense Tracker-----")
print()
budget_amount=5000  

class Expense:
   def __init__(self,name,amount):
      self.name=name
      self.amount=amount

def Saveuserexp():
   #  expense_budget=input("Enter the expense budget")
   #  print('expensebudget = ',expense_budget)
    expense_name = input("Enter expense name: ")
    try:
     expense_amount = float(input("Enter expense amount: "))
     if expense_amount >0:
      newexpense=Expense(name=expense_name,amount=expense_amount)
    #   print(newexpense)
      with open('myfile.txt','a') as samplefile:
        samplefile.write(f"{newexpense.name} - {newexpense.amount}\n")
        print('Added successfully')
     else:
       print("Expense amount should not be less than zero")
       Saveuserexp()
    except ValueError:
       print("Expense amount should be numbers")
       Saveuserexp()



def Viewexpense():
   with open('myfile.txt','r') as samplefiles:
      #  samplefiles.readlines()
       for i in samplefiles:
         expense_name, expense_amount= i.strip().split("-")
         newexpense=Expense(name=expense_name,amount=expense_amount)
         print (f"{newexpense.name} - Rs.{newexpense.amount}")


def Calcexpense():
      sum =0
      # with open('samplefile333','r') as samplefiles:
      with open('myfile.txt','r') as samplefiles:
       for i in samplefiles:
         expense_name, expense_amount= i.strip().split("-")
         newexpense=Expense(name=expense_name,amount=expense_amount)
         expenses.append(newexpense.amount)
      for i in expenses:
         #   print("expense_amount = ",i)
         #   print("coverting str to float",float(i))
           sum=sum+float(i)
      print("Budget Amount = ",budget_amount)
      print("Total expenses =",sum)
      print("balance amount= ",float(budget_amount)-float(sum))
      

# f = open("myfile.txt", "x")

while(True):
     print("select an option :")
     print("1.Add a new expense")
     print("2.View all expenses ")
     print("3.Calculate expenses")
     try:
      choice = int(input())
      if (choice==1):
        Saveuserexp()
      elif(choice ==2):
        Viewexpense()
      elif(choice ==3):
        Calcexpense()
      else:
        exit()
     except ValueError:      # if input not numeric
      print("Input should be numeric")

    
       

