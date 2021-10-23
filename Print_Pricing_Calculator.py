import json
import decimal



try:
    document_sizes = json.load(open("document_sizes.json"))
    paper_stocks = json.load(open("paper_stocks.json"))
    printer_specs = json.load(open("printer_specs.json"))
    print_suppliers = json.load(open("print_suppliers.json"))
except Exception as e: 
    print("There was a problem loading the configuration files.\n")

def int_input(message):
    print(message)
    while True:
        ans=input()
        try:
            return int(ans)
        except ValueError:
            print("This is not a whole number. Try again.\n")

def yes_no_input(message):
    while True:
        reply = str(input(message+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def numbered_dict_menu(dictionary) :
    i = 1
    for e in dictionary:
        print (i, ". ", e['identifier'], sep='')
        i += 1
    
    while(True):
        ans=int_input("\nType your selection.")
        if int(ans) <= len(dictionary):
            return list(dictionary)[int(ans)-1]
        else:
            print ("Selection does not exist. Try again.\n")


print ("_______________________________\n")            
print ("Please select the document size\n")
doc_size_sel = numbered_dict_menu(document_sizes)
print ("Document Type: ", doc_size_sel["identifier"])

print ("_______________________________\n")            
print ("Please select the paper type\n")
paper_type_sel = numbered_dict_menu(paper_stocks)
print ("Paper Stock: ", paper_type_sel["identifier"])

print ("_______________________________\n")
dbl_sided = yes_no_input("Is it printed on both sides?")
print(dbl_sided)

print ("_______________________________\n")
input_quantity = int_input("Please input the quantity needed")

print ("_______________________________\n")
print ("In-House Print Breakdown:")

sheets_printed = int(input_quantity/doc_size_sel["multiprint"])
click_cost = printer_specs["click_rate"] * sheets_printed
if(dbl_sided):
    click_cost = click_cost * 2
paper_cost = paper_type_sel["unit_price"] * sheets_printed

decimal.getcontext().prec = 2

print ("Sheets Printed:", sheets_printed)
print ("Paper Cost:", paper_cost)
print ("Print Cost:", click_cost)
print ("\nTotal:   ", decimal.Decimal(paper_cost + click_cost))
print ("_______________________________\n")

print("Distribution Cost:", input_quantity * 0.12)

