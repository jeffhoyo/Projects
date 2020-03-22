import os

def thing():
    int = []
    int = os.system('ifconfig | grep "en[0-9{1}]:" | cut -d ":" -f 1 | head -n1')
    print("The selected int is: %s" % int)
thing()
