print ("Hello Everyone")

print ("Welcome to Wolf of Wall Street")

print ("We can predict your Company's rating or else you can view our data for 800 Companies")

Option = input("Would you like to check your company's data? Y/N: ")

if Option == 'Y':
    Name = input("What is the name of your Company: ")
    Revenue = int(input("Please input your Revenue (in $ million, upto $100,000): "))
    PPE = int(input("Please input your Net Plant, Property & Equipments (in $ million, upto $80,000): "))
    EBITDA = int(input("Please input your Earning before Interest, Taxes, Depreciation & Amortization (in $ million): "))
    Debt = int(input ("Please input the amount of Debt (in $ million): "))
    TotalAssets = int(input("Please provide Total No. of Assets (in $ million): "))
    Interest = int(input("Please provide all the Interest Expenses (in $ million): "))
    RCF = int(input("Please provide your Retained Cash Flow (in $ million): "))
    BusinessAnalysis = int(input("Rate your Company's Business profile from 1-100, where 100 being the highest: "))
    FinancialAnalysis = int(input("Rate your Company's Financial Analysis from 1-100, where 100 being the highest: "))
    A = (Revenue//100000)*100
    B = (PPE//80000)*100
    C = (EBITDA/Revenue)*100
    print("Your EBITDA Margin is: ", C)
    D = EBITDA/TotalAssets
    print("Your Return on Average Assets is: ", D)
    E = Debt/EBITDA
    print("Your Debt/EBITDA ratio is: ", E)
    F = (RCF/Debt)*100
    print("Your RCF/Debt ratio is: ", F)
    G = (EBITDA/Interest)
    print("Your EBITDA/Interest Expense ratio is: ", G)
    A = (A*7.5)//100
    B = (B*7.5)//100
    BusinessAnalysis = (BusinessAnalysis*25)//100
    C = (C*5)//100
    D = (D*5)//100
    E = (E*10)//100
    F = (F*10)//100
    G = (G*10)//100
    FinancialAnalysis = (FinancialAnalysis*20)//100
    Total = (A + B + C + D + E + F + G + BusinessAnalysis + FinancialAnalysis)
    i = int(Total)
    print(Total)
    if i > 89:
        print("Your company,", Name, "can be predicted to have a credit rating as Aaa")
    elif 90 > i > 79:
        print("Your company,", Name, "can be predicted to have a credit rating as Aa")
    elif 80 > i > 69:
        print("Your company,", Name, "can be predicted to have a credit rating as A")
    elif 70 > i > 59:
        print("Your company,", Name, "can be predicted to have a credit rating as Baa")
    elif 60 > i > 49:
        print("Your company,", Name, "can be predicted to have a credit rating as Ba")
    elif 50 > i > 39:
        print("Your company,", Name, "can be predicted to have a credit rating as B")
    elif 40 > i > 29:
        print("Your company,", Name, "can be predicted to have a credit rating as Caa")
    elif 30 > i > 19:
        print("Your company,", Name, "can be predicted to have a credit rating as Ca")
    elif 20 > i > 1:
        print("Your company,", Name, "can be predicted to have a credit rating as C")
    else:
        print("Your company,", Name, "cannot be predicted to have a credit rating as it is having a below credit grade Business in the market")
elif Option == 'N':
    print("We have a Data of 800 Companies")

    import csv
    List = []
    with open('DATA PYTHON FINALS.csv', 'rt') as f:
          data = csv.reader(f)
          for row in data:
              List.append(row)
    import csv
  
    X = int(input("Which company's data would you like to pull up, let us know by typing the number from 1 to 800 = "))

    List1 = []
    for i in List[X]:
          List1.append(i)
    print("The Name of the the Company is: ", List1[0])
    print("Revenue: $", List1[1])
    print("Net Plant, Property & Equipment: $", List1[2])
    print("Business Profile: ", List1[3], "%")
    print("EBITDA: $", List1[5])
    print("EBITDA Margin (EBITDA/Revenue): ", List1[6], "%")
    print("Total Assets: $", List1[7])
    print("Return on Average Assets: ", List1[8], "%")
    print("Company's Debt: $", List1[9])
    print("Debt/EBITDA: ", List1[10], "%")
    print("Retained Cash Flow: $", List1[11])
    print("Retained Cash Flow/Debt: ", List1[12], "%")
    print("Interest Expenses: $", List1[13])
    print("EBITDA/Interest Expenses: ", List1[14], "%")
    print("Financial Poliy: ", List1[15], "%")

    A = int(List1[1])
    A = ((A/99999)*7.5)
    B = int(List1[2])
    B = ((B/80000)*7.5)
    C = int(List1[3])
    C = ((C*25)//100)
    E = int(List1[6])
    E = (E*5)//100
    G = int(List1[8])
    G = (G*5)//100
    I = int(List1[10])
    I = (I*10//100)
    K = int(List1[12])
    K = (K*10)//100
    M = int(List1[14])
    M = (M*10)//100
    N = int(List1[15])
    N = (N*20)//100

    Total = (A + B + C + E + G + I + K + M + N)
    i = int(Total)
    if i > 89:
          print("The Company,", List1[0], "can be predicted to have a credit rating as Aaa")
    elif 90 > i > 79:
          print("The Company,", List1[0], "can be predicted to have a credit rating as Aa")
    elif 80 > i > 69:
          print("The Company,", List1[0], "can be predicted to have a credit rating as A")
    elif 70 > i > 59:
          print("The Company,", List1[0], "can be predicted to have a credit rating as Baa")
    elif 60 > i > 49:
          print("The Company,", List1[0], "can be predicted to have a credit rating as Ba")
    elif 50 > i > 39:
          print("The Company,", List1[0], "can be predicted to have a credit rating as B")
    elif 40 > i > 29:
          print("The Company,", List1[0], "can be predicted to have a credit rating as Caa")
    elif 30 > i > 19:
          print("The Company,", List1[0], "can be predicted to have a credit rating as Ca")
    elif 20 > i > 1:
          print("The Company,", List1[0], "can be predicted to have a credit rating as C")
    else:
          print("The Company,", List1[0], "cannot be predicted to have a credit rating")


    with open('WriteData.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Company Name', 'Rating in Percentage'])
        writer.writerow([List1[0], Total])

Plot = input("Would you like to see the first 25 companies rating plotted in a graph? (Y/N) ")

if Plot == 'Y':
    import matplotlib.pyplot as plt
    import csv
    x = []
    y = []

    with open('Matplotlib Analysis Data Set Random.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x.append(row[0])
            y.append(row[1])
            
        plt.plot(x,y, 'r:', label='Loaded from file!')
        plt.xlabel('Name of the Company')
        plt.ylabel('Credit Ratings of the company')
        plt.title('Interesting Graph\nCheck it out')
        plt.show()

else:
    print("Have a Good Day")



