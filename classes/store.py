from classes.video_inventory import VideoInventory
from classes.user_type import UserType


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = VideoInventory.load_inventory()
        self.customers = UserType.load_customers()
        self._customer = None
        self._movie = None

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


    @property
    def get_movie(self):
        return self._movie
    
    @get_movie.setter
    def set_movie(self, rental):
        for movie in self.inventory:
            if movie.title == rental:
                self._movie = rental

    @property
    def get_customer(self):
        return self._customer


    @get_customer.setter
    def set_customer(self, customer_id):
        for customer in self.customers:
            if int(customer.id) == int(customer_id):
                self._customer = customer
                break


    def view_customer(self, customer_id):
        self.set_customer = customer_id
        customer = self.get_customer
        if len(customer.current_video_rentals) != 0:
            rentals = customer.current_video_rentals.split('/')
            print(
                f"{customer.first_name} {customer.last_name} has rented the following movies:\n")
            for i, rental in enumerate(rentals):
                print(f"{i + 1}. {rental}")
            print('')
        else:
            print(
                f"{customer.first_name} {customer.last_name} has NO movies rented\n")
        return customer


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
            self.customers.append(new_customer)
            new_customer = UserType(customer_id, customer_f_name, customer_l_name, account_type)


    def rent_video(self):
        user = input("Enter user ID: ")
        rental = input("What movie would you like to rent?: ")
        rental = rental.lower()
        user_rental_validation = False
        does_movie_exist = False

        for movie in self.inventory:
            # check if movie exist
            if movie.title.lower() == rental:
                # check if there are enough copies avaliable 
                if int(movie.copies_available) != 0:
                    current_copies = int(movie.copies_available) - 1
                    user_rental_validation = UserType.rent_video(user, rental, movie.rating)
                    if user_rental_validation:
                        VideoInventory.rent_movie(rental, current_copies)
                        does_movie_exist = True
                elif int(movie.copies_available) == 0:
                    print(f"\n{movie.title} is currently rented")
                    does_movie_exist = True
                    return 0
        if does_movie_exist == False:
            print(f"\n{rental} doesn't exist in our inventory")


    def return_video(self):
        user = input("Enter user ID: ")

        customer = self.view_customer(user)
        movie_to_return = input("Type the movie number you would like to return: ")
        movie_to_return = int(movie_to_return) - 1

        current_rentals = customer.current_video_rentals.split('/')
        rental = current_rentals.pop(movie_to_return)
        current_rentals = "".join(current_rentals)
        customer.current_video_rentals = current_rentals
        UserType.return_video()

        # Returning movie to inventory
        for movie in self.inventory:
            if movie.title == rental:
                movie.copies_available = int(movie.copies_available) + 1
        VideoInventory.return_video()


