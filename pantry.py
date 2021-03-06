## dicts are grocery items, keys are name, cost, store, price, date of purchase, and date of final use(eaten/used for last time)
from datetime import date, timedelta, datetime
class Grocery():
	def __init__(self,buydate,name,price=0,usedate=None):
		self.buydate = buydate
		self.name = name
		self.price = price
		self.usedate = usedate
importList = []
#import from file as lists, to a list
with open('pantry.txt','r') as imp:
        for line in imp:
                importList.append(eval((line)))
pantryList = [Grocery(*x) for x in importList] #found this on stackexchange https://stackoverflow.com/questions/19307169/how-to-assign-a-class-object-to-a-item-in-a-list-python
#update pantryList
def refreshPantry():
        global pantryList
        pantryList = [Grocery(*x) for x in importList]
#update 'database'
def updatedoc():
        f = open('pantry.txt', 'w')
        for item in importList:
                f.write(str(item)+'\n') #allows dictionaries to be written to file properly
        f.close()
#set alternate dates
month = '00'
day = '00'
year = '00'
today = date.today().strftime('%m-%d-%y')
def getmonth():
        global month
        month = str(input('Input month as mm\n'))
        if month.isdigit():
                if 0 < int(month) < 13:
                        if len(month) == 1:
                                month = '0'+month
                                print(month)
                        print('valid')
                else:
                        print('invalid input')
                        getmonth()
        else:
                print('invalid input')
                getmonth()
def getday():
        global day
        day = str(input('Input day as dd\n'))
        if day.isdigit():
                if month in ['01','03','05','07','08','10','12'] and 0 < int(day) < 32:
                        pass
                elif month in ['04','06','09','11'] and 0 < int(day) < 31:
                        pass
                elif month == '02' and 0 < int(day) < 29: #leap years, man
                        pass
                else:
                        print('invalid input')
                        getday()
                if len(day) == 1:
                        day = '0'+day
                        print(day)
                print('valid')
        else:
                print('invalid input')
                getday()
def getyear():
        global year
        year = str(input('Input year as yy\n'))
        if year.isdigit():
                if 0 <= int(year) < 100:
                        if len(year) == 1:
                                year = '0'+year
                                print(year)
                        print('valid')
                else:
                        print('invalid input')
                        getyear()                         
        else:
                print('invalid input')
                getyear()
def addItem():
        newitem = []
        dateask = str.lower(input('Item purchased today? y/n \n'))
        if dateask == 'y' or dateask == 'yes':
                dateassign = today
                newitem.append(dateassign)
                itemask = str.lower(input('Enter item name. \n'))
                newitem.append(itemask)
                try:
                        priceask = int(input('Enter item price. \n'))
                        newitem.append(priceask)
                except:
                        print('Invalid price entered. \n')
        else:
                def getdate():
                        getmonth()
                        getday()
                        getyear()
                        newdate = month +'-'+day+'-'+year
                        print(newdate)
                        newitem.append(newdate)
                getdate()
                itemask = str.lower(input('Enter item name. \n'))
                newitem.append(itemask)
                try:
                        priceask = int(input('Enter item price. \n'))
                        newitem.append(priceask)
                except:
                        print('Invalid price entered. \n')
        print(newitem)
        importList.append(newitem)
        refreshPantry()
        updatedoc()
def addUsedate():
        def updater():
                for item in importList:
                        print(item[1])
                whichUpd = str.lower(input('Please choose one item above to update with a final usedate.\n'))
                for item in importList:
                        for attribute in item:
                                if whichUpd == attribute:
                                        if len(item)>3:
                                                print('Item already has usedate: ' + item[3]) #future project: remove items with usedate to add fresh item, and/or add multiple of item to compare usedates (more advanced database stuff?)
                                                updater()
                                        else:
                                                dateget = str.lower(input('Was use date today? \n'))
                                                if dateget == 'y' or dateget == 'yes':
                                                        item.append(today)
                                                        print(item)
                                                else:                              
                                                        getmonth()
                                                        getday()
                                                        getyear()
                                                        usedate = month +'-'+day+'-'+year
                                                        print(usedate)
                                                        item.append(usedate)
                                                        print(item)
        updater()
        updatedoc()
        refreshPantry()                                                                                                          
def daysLasted():
        def runIt():
                for item in pantryList:
                        if item.usedate != None:
                                print(item.name)
                        else:
                                pass
                itemSel = str.lower(input('Select an item.\n'))
                for item in pantryList:
                        if itemSel == item.name:
                                initdate = datetime.strptime(item.buydate,'%m-%d-%y')
                                usedate = datetime.strptime(item.usedate,'%m-%d-%y')
                                dayslength = str((usedate - initdate)).strip(' days,0:00:00')
                                if dayslength =='':
                                        dayslength='1'
                                print('Item lasted ' + dayslength + ' days.')
                        else:
                                pass
                def rerun():
                        doAgain = str.lower(input("Investigate another item? Y/N \n"))
                        if doAgain == 'yes' or doAgain == 'y':
                                runIt()
                        else:
                                print('bye')
                rerun()
        runIt()
def itemValue():
        def runIt():
                for item in pantryList:
                        if item.usedate != None:
                                print(item.name)
                        else:
                                pass
                itemSel = str.lower(input('Select an item from the list above.\n'))
                for item in pantryList:
                        if itemSel == item.name:
                                initdate = datetime.strptime(item.buydate,'%m-%d-%y')
                                usedate = datetime.strptime(item.usedate,'%m-%d-%y')
                                dayslength = str((usedate - initdate)).strip(' days,0:00:00')
                                if dayslength == '':
                                        dayslength='1'
                                value = int(item.price / int(dayslength))
                                print('Item lasted ' + dayslength + ' days and cost $'+ str(value) + ' per day.')
                        else:
                                pass
                def rerun():
                        doAgain = str.lower(input("See value of another item? Y/N \n"))
                        if doAgain == 'yes' or doAgain == 'y':
                                runIt()
                        else:
                                print('bye')
                rerun()
        runIt()
def runAll():
        def rerun():
                doAgain = str.lower(input('Perform another function? Y/N\n'))
                if doAgain == 'yes' or doAgain =='y':
                        runAll()
                else:
                        print('bye')
        whichdo = str.lower(input('Select a function to run: [Add New Item (A)] [Add Use Date(U)] [View Item Use Length (L)] [View Item Value(V)] [Exit(E)]\n'))
        if whichdo == 'a':
                addItem()
                rerun()
        elif whichdo == 'u':
                addUsedate()
                rerun()
        elif whichdo == 'l':
                daysLasted()
                rerun()
        elif whichdo == 'v':
                itemValue()
                rerun()
        elif whichdo == 'e':
                print('bye')
        else:
                print('Invalid input')
                rerun()
runAll()
