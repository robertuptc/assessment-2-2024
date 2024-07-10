from classes.video_inventory import VideoInventory
from classes.user_type import UserType


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = VideoInventory.load_inventory()
        self.customers = UserType.load_customers()

    def __repr__(self):
        return f"""***********************
*** {self.store_name}'S MOVIES ***
***********************"""

    def view_inventory(self):
        print("--------------------------------")
        print("--- CURRENT MOVIES INVENTORY ---")
        print("--------------------------------")
        for movie in self.inventory:
            print(f"{movie.id}. {movie.title} | {movie.copies_available}")

    def view_customers(self):
        print("-------------------------------")
        print("------- STORE CUSTOMERS -------")
        print("-------------------------------")
        for customer in self.customers:
            print(f"{customer.id}. {customer.first_name} {customer.last_name}")


    def view_customer(self, customer_id):
        for customer in self.customers:
            if int(customer.id) == int(customer_id):
                if len(customer.current_video_rentals) != 0:
                    rentals = customer.current_video_rentals.split('/')
                    print(
                        f"{customer.first_name} {customer.last_name} has rented the following movies:\n")
                    for rental in rentals:
                        print(f"- {rental}")
                    print('')
                else:
                    print(
                        f"{customer.first_name} {customer.last_name} has NO movies rented\n")


    def new_customer(self):
        customers_id_list = []
        customer_id = input("Type customer ID: ")
        if customer_id:
                try:
                    int(customer_id)
                except:
                    print("Only numbers are allowed")
                    return 1
        
        for customer in self.customers:
            customers_id_list.append(customer.id)
        if str(customer_id) in customers_id_list:
            print(f"Customer ID {customer_id} already taken. ID must be greater than {len(self.customers)}")
        else: 
            customer_f_name = input("Type your first name: ")
            customer_l_name = input("Type your lastname: ")
            account_type = input("""What type of accound would you like?
    1. sx
    2. px
    3. sf
    4. pf
Enter a number: """)
            if account_type:
                try:
                    account_type = int(account_type)
                    if account_type < 0 or account_type > 4:
                        print("Number choice must be between 1 and 4")
                    else:
                        if account_type == 1:
                            account_type = 'sx'
                        elif account_type == 2:
                            account_type = 'px'
                        elif account_type == 3:
                            account_type = 'sf'
                        else:
                            account_type = 'pf'
                except:
                    print("Only numbers are allowed")
            UserType.new_customer(customer_id, account_type, customer_f_name, customer_l_name)


    def rent_video(self, title, customer_id):
        print(title, customer_id)
        pass