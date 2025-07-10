monthly_income = input("Enter your monthly income")
monthly_expenses = input("Enter your total monthly expenses")
m_i = int(monthly_income)
m_e = int (monthly_expenses)
monthly_savings = m_i - m_e
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are $", monthly_savings, ".")
print ("Projected savings after one year, with interest, is: $", projected_savings, ".")                     