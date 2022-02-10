class Category:
    def __init__(self, name) :
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = "") : 
        self.ledger.append({"amount":amount, "description":description})
    def withdraw(self, amount, description = ""):
        x = 0
        for i in self.ledger :
            x+=i["amount"]
        if x - amount <= 0 :
            return False
        else :
            self.ledger.append({"amount":-amount, "description":description})
            return True
    def get_balance(self) : 
        x = 0
        for i in self.ledger :
            x+=i["amount"]
        return x 
    def transfer(self, amount, other) :
        if self.withdraw(amount, 'Transfer to ' + other.name) :
            other.deposit(amount, 'Transfer from ' + self.name )
            return True
        else : 
            return False
    def check_funds(self, amount) : 
        if self.get_balance() < amount :
            return False
        else :
            return True 
    def __str__(self) :
        header = self.name.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.get_balance())
        return header + ledger + total
def create_spend_chart(listOfCategories) :
    x = ""
    listOfDeposits = []
    x += "Percentage spent by category\n"
    for i in listOfCategories : 
        s = 0
        for j in i.ledger :
            if j["amount"] < 0 : s += -j["amount"]
        listOfDeposits.append(round(s, 2))
    percentOfDeposits = []
    for i in listOfCategories : 
        s = 0
        for j in i.ledger :
            if j["amount"] < 0 : s += -j["amount"]
        percentOfDeposits.append(int((10*s/round(sum(listOfDeposits), 2))//1)*10)
    chart= ""
    for v in range(100, -10, -10) :
        chart += str(v).rjust(3) + '|'
        for percent in percentOfDeposits :
            if percent >= v:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    x += chart + "    " + "-"*(len(listOfCategories)*3 + 1) + "\n"
    m = max([len(i.name) for i in listOfCategories])
    h = [""]*m
    for i in range(m) :
        for j in listOfCategories :
            if i + 1 > len(j.name) : 
                h[i] += " "
            else :
                h[i] += j.name[i]
    for i in range(len(h)-1) :
        x += "     " + "  ".join(list(h[i])) + "  \n"    
    x += "     " + "  ".join(list(h[-1])) + "  " 
    return x

