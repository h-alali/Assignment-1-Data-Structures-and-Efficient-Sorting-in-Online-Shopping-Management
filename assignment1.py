

from calendar import c
from cgi import print_directory
from gettext import install
from html.entities import codepoint2name
from itertools import count
import time
import subprocess

#This command creating the array array
products = []


#appends the txt file to the array 
#--------------------------------------------------------------------------------------------------------------------
# This command will open a txt file called product_data.txt and it will read from it
with open('product_data.txt','r') as f:
    # This command reads the lines in the file   
    lines = f.readlines()
    # This command starts a loop over each line in the file
    for i in range(len(lines)):
        # This command this command removed extra spaces from the start of the line and end of the line
        line = lines[i].strip()
        # This command checks of the line is empty then it will skip it
        if not line:
            continue
        # This command will split the lines into parts when there is a comma
        items = line.split(',')
        # This command makes a new list with 4 zeros
        row =[0 for _ in range(4)]
        # This command starts a loop over each part of the line
        for j in range(len(items)):
            # This command checks if thier are more than four parts, then it will stop looking 
            if j >= 4: 
                break
            # This command reokaces the zero at position j with the part form the line
            row[j] = items[j]
        # This command adds the information to the array
        products.append(row)
#--------------------------------------------------------------------------------------------------------------------          
            

        
                  

        

#Bubble sorting 
#-------------------------------------------------------------
#this command starts a function called bubbleSort
def bubbleSort(arr):
    #this command counts how many items are in the list arr 
    n = len(arr)
    #this command starts a loop that will go through each item in the list
    for i in range(n):
        #this command makes a note that no itms have been swapped
        swapped = False
        #this command starts another loop
        for j in range(0, n-i-1):
            try:
               #this command will check if one item is bigger than the next one
               if float(arr[j][2]) > float(arr[j+1][2]):
                   #this command will check if they are then it will get swapped
                   arr[j], arr[j+1] = arr[j+1], arr[j]
                   swapped = True
            #this command  will check if their is a problem turning the item into a number, then it will skip it
            except ValueError:
                continue
        if not swapped:
            break
#-------------------------------------------------------------

#Bubble sorting in reverse 
#-------------------------------------------------------------
#this command starts a function called bubbleSort
def Reverse_bubbleSort(arr):
    #this command counts how many items are in the list arr 
    n = len(arr)
    #this command starts a loop that will go through each item in the list
    for i in range(n):
        #this command makes a note that no itms have been swapped
        swapped = False
        #this command starts another loop
        for j in range(0, n-i-1):
            try:
               #this command will check if one item is bigger than the next one
               if float(arr[j][2]) < float(arr[j+1][2]):
                   #this command will check if they are then it will get swapped
                   arr[j], arr[j+1] = arr[j+1], arr[j]
                   swapped = True
            #this command  will check if their is a problem turning the item into a number, then it will skip it
            except ValueError:
                continue
        if not swapped:
            break
#-------------------------------------------------------------






while True:
    print("Select an option:\n1. View array\n2. Insert value\n3. Update value\n4. Remove product\n5. Search for product\n6. Exit")
    insert = int(input("\nPlease select one of the values at the top:  "))
    
    #the command that lets the user see whats inside the array, without sorting it and  # to check the time complexity in the array with the list of the things inside the array
    if insert == 1:
        print("Select one of the following options:\n1. View the list without sorting\n2. View the list in bubble sort\n3. View the list in reverse bubble sort")
        array_edits = int(input("enter value here: "))
        if array_edits == 1:
            start_Time = time.perf_counter()
            end_time = time.perf_counter()
            print(f"Time taken to sort the data: :{end_time-start_Time} seconds")
            for product in products:
                print(product) 
            print("\nThe array has not been sorted in any way")
        # this will sort the list in bubble sort and  # to check the time complexity in the array with the list of the things inside the array
        elif array_edits == 2:
            start_Time = time.perf_counter()
            bubbleSort(products)
            end_time = time.perf_counter()
            print(f"Time taken to sort the data: :{end_time-start_Time} seconds")
            for product in products:
                print(product) 
            print("\nThe array has been sorted using the bubble sort algorithm.")
                    # this will sort the list in bubble sort and  # to check the time complexity in the array with the list of the things inside the array
        elif array_edits == 3:
            start_Time = time.perf_counter()
            Reverse_bubbleSort(products)
            end_time = time.perf_counter()
            print("\nThe array has been sorted using the reverse bubble sort algorithm.")
            print(f"Time taken to sort the data: :{end_time-start_Time} seconds")
            for product in products:
                print(product) 
       
    #the command that lets the user insert a product to input a new line
    elif insert == 2:
       
            productId = input("please enter the product id: ")
            productName = input("please enter the product name: ")
            productCost = input("please enter the product Cost: ")
            productCategory = input("yplease enter the product Category: ")
    
            combined = [productId,productName,productCost,productCategory]
    
            ValuePrint = print("\nHere is what you have entered:" ,combined)
    
            confirmValue = input("\nIs the value you entered correct? Please select Y for Yes and N for No:")
            if confirmValue.lower() == 'y':
                 products.append(combined)
                 print("\nthe value has been added to the array")
                 continue
            elif confirmValue.lower() == 'n':
                 continue
            else:
                print("Invalid selection")
    #the command that lets the user update a product            
    elif insert == 3:
        productId = input("\n please enter the product id of the product you want to updated: ")
        for i, product in enumerate(products):
             if product[0] == productId:        
                 productId = input("\nplease enter the new product id: ")
                 productName = input("\nplease enter the new product name: ")
                 productCost = input("\nplease enter the new product Cost: ")
                 productCategory = input("\nplease enter new the product Category: ")
                 products[i] = productId, productName,productCost,productCategory
                 print("\nsuscessfuly updated", products[i])
                 break
        else:
           print("\nProduct not found") 
    #the command that lets the user delete a product 
    elif insert == 4:   
           productId = input("\n please enter the product id of the product you want to delete: ")
           for i,product in enumerate(products):
                if product[0] == productId:
                    del products[i]
                    print("\nproduct deleted successfully") 
                    break
           else:    
              print("\nProduct not found") 
    
    #the command that lets the user usearch for a product, this command was eddited form https://stackoverflow.com/questions/64486153/how-to-search-array-and-find-item-that-user-input-in-python
    elif insert == 5:
        searching = input("please enter the what you are shearching for:  ")
        found = False
        for product in products:
            for detail in product:
                if searching.lower() in detail.lower():
                    print(f"Found it! product details: {product}")
                    found = True
        if not found:
            print("not found")
    #the command that lets the  user exit the program
    elif insert == 6:
        break
    
    
    
    else:
        print("invalid value you have selected: " , insert)
        
