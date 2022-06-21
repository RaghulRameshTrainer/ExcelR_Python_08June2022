import sys

if len(sys.argv) != 3:
    print("USAGE: {} {} {}".format(sys.argv[0],"cust name" ,"acct num"))
    sys.exit(0)
    
cust_name = sys.argv[1]
acct_num = sys.argv[2]

print("Program Name:",sys.argv[0])
print("Customer Name:",cust_name)
print("Account Number:",acct_num)

