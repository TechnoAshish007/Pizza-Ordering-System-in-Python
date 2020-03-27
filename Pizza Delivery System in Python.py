


pizza_type_dict ={} # dictionary for storing pizza type data ## eg: pizza_type_dict[P1]= [Margarita, 3.0]
base_type_dict ={}  # dictionary for storing base type data
toppings_type_dict ={} # dictionary to store toppings data
cust_data ={}          # dictionary to store customer data


# Load the data into the dictionaries
def load_data(data_path, type):
    data_file = open(data_path,"r")
    for line in data_file:
        splitedLine = line.split(";")
        if type =="pizza":
            pizza_type_dict[splitedLine[0]]=[splitedLine[1],float(splitedLine[2])]
        elif type == "base":
                base_type_dict[splitedLine[0]]=[splitedLine[1],float(splitedLine[2])]
        elif type == "toppings":
                toppings_type_dict[splitedLine[0]]=[splitedLine[1],float(splitedLine[2])]
    data_file.close()


if __name__ == "__main__":
    load_data(r"F:\MS Data Science - IIIT B Upgrad\Python Crash Course-Rajan Chettri\Types_of_Pizza.txt", "pizza")
    load_data(r"F:\MS Data Science - IIIT B Upgrad\Python Crash Course-Rajan Chettri\Types_of_Base.txt", "base")
    load_data(r"F:\MS Data Science - IIIT B Upgrad\Python Crash Course-Rajan Chettri\Types_of_Toppings.txt", "toppings")


## Generate unique order number for the given number
def generate_order_num(name):
    if name in cust_data.keys():# check if the customer allready exists in the cust data dictionary
        ord_num = cust_data[name]["num_of_orders"]
        ord_num += 1
        return ord_num
    else:
        ord_num =0 # new customer 
        cust_data[name] = {}
        cust_data[name]["num_of_orders"] = ord_num
        ord_num += 1
        return ord_num



 # common function for printing dictionaries to make menu available for customers
def print_dict(dictionary):
    print("Code, Type, Price")
    for key in dictionary.keys():
        print(""+ key + ", " + str(dictionary[key][0]) + ", " + str(dictionary[key][1]))

# calculate the total bill of a customer given the order
def calculate_bill(ord_tup):
    bill = 0
    piza_type = ord_tup[0]
    base_type = ord_tup[1]
    top_list = ord_tup[2]
    qty = ord_tup[3]
    bill += pizza_type_dict[piza_type][1]
    bill += base_type_dict[base_type][1]
    bill += len(top_list)*0.5
    bill = bill * qty
    return bill



# add orders to the cust_data dictionary
def add_cust_data (order_tup, name, order_num):
    cust_data[name]["num_of_orders"]= order_num
    if order_num in cust_data[name].keys():
        l = cust_data[name][order_num]
        l.append(order_tup)
    else:
        l =[]
        l.append(order_tup)
        cust_data[name][order_num]=1

# print the final order
def print_complete_order(name, ord_num):
    order_list = cust_data[name][ord_num]
    print("Piza_type"+"-->"+"Base_type"+ "-->"+ "Toppings" + "-->" + "-->" + "qty"+ "-->"+ "price")
    print("-------------------------------------------")
    for order in order_list:
        bill = calculate_bill(order)
        print(order[0]+ "-->"+ order[1]+"-->" +str(order[2])+ "-->" + str(order[3])+ "-->"+ str(bill)+"$")

# Function to order data
def order():
    print("Welcome to the pizza takeaway")
    name = input("Please enter your name ")
    total_bill = 0
    ord_num = generate_order_num(name)
    print("Hello " + name + ", What kind of pizza would you like to have:")
    print_dict(pizza_type_dict)
    piza_type = input("Please select from above options:")
    piza_type = piza_type.upper() #converted into a upper case
    while piza_type != "x":
        if piza_type in pizza_type_dict.keys():
            print(" Here is the base options available")
            print_dict(base_type_dict)
            base_type = input("Please enter your option:")
            base_type = base_type.upper() #converted into a upper case
            # check if the base type option is valid
            base_flag = 0
            while base_flag ==0:
                base_flag = 1
                if base_type not in base_type_dict.keys():
                    base_flag = 0
                    print(" It is an invalid option")
                    print_dict(base_type_dict)
                    base_type =  input(" please enter the valid option")
                    base_type = base_type.upper()
            
            print("\n")
            print(" Please enter the toppings you would like to have from following list")
            print_dict(toppings_type_dict)
            toppings = input("Enter the toppings in comma separated form, e.g, if you want to add T1 and t2, enter T1, T2")
            split_toppings = toppings.split(", ")
            split_toppings=[x.upper() for x in split_toppings] #onverting the list into upper case
            
            # checl if topping are valid
            top_flag = 0
            while top_flag ==0:
                top_flag = 1
                for item in split_toppings:
                    if item not in toppings_type_dict.keys():
                        top_flag = 0
                        toppings = input("" + item + " is invalid, please reenter the toppings")
                        split_toppings= toppings.split(",")
                        split_toppings= [x.upper() for x in split_toppings]
                        break
            
            qty = 2000
            while qty > 1000:
                qty = input("Please enter the number of pizzas to order")
                qty = int(qty)
                if qty > 1000:
                    print("You cannot order more than 1000 pizzas")
                
            print("\n")
            print("Here is your order till now")
            print("Pizza Type: ", pizza_type_dict[piza_type][0])
            print("Pizza Base: ", base_type_dict[base_type][0])
            print("Toppings: ", str(split_toppings))
            print("Number of pizzas", qty)
            
          
            cnf = input("Press y to confirm, else press c to cancel")
            if cnf == "y":
                ord_tup =  (piza_type, base_type, split_toppings, qty)
                total_bill = calculate_bill(ord_tup)
                print(" Your total bill till now is", total_bill)
                add_cust_data(ord_tup, name, ord_num)
                piza_type = input("Press x  to complete your order or to continue, select pizza type")
                piza_type = piza_type.upper()
                
            elif cnf == "c":
                print_dict(pizza_type_dict)
                piza_type = input("Please enter a valid option")
                piza_type = piza_type.upper()
                
         
        
        else:
            print_dict(pizza_type_dict)
            piza_type = input(" Please enter a valid option")
            piza_type = piza_type.upper()
    
    
    print(" Thank you for your order, here is your final order")
    print_complete_order(name, ord_num)
    print("Total amount to be paid",str(total_bill))
    
    return none


 if __name__ == "__main__":
    load_data(r"F:\MS Data Science - IIIT B Upgrad\Python Crash Course-Rajan Chettri\Types_of_Pizza.txt", "pizza")
    load_data(r"F:\MS Data Science - IIIT B Upgrad\Python Crash Course-Rajan Chettri\Types_of_Base.txt", "base")
    load_data(r"F:\MS Data Science - IIIT B Upgrad\Python Crash Course-Rajan Chettri\Types_of_Toppings.txt", "toppings")
    order()