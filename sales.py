#sales Date Dunder Mifflin Scranton-Branch

employees=["Dwight", "Jim", "Stanley", "Phyllis", "Andrew"] 
sales =[15000, 12000, 9000, 11000, 6000] 


#Michael requires total sales for the entire branch




  

#Function of total sales for the entire branch

def calculate_total_sales(sales_list): 
    total = 0 
    for sale in sales_list: 
        total += sale 
    return total 
     


if __name__ == "__main__":
    for i in range(len(employees)): 
     print(employees[i],":",sales[i],sep="")  

    print(calculate_total_sales(sales)) 






