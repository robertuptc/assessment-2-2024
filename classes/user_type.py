from classes.user import User
import csv


class UserType(User):
    all_customers = []

    @classmethod
    def load_customers(cls):
        with open('data/customers.csv', newline='') as csvfile:
            file_reader = csv.DictReader(csvfile)
            for row in file_reader:
                customer = cls(**row)
                cls.all_customers.append(customer)
        return cls.all_customers


    @classmethod
    def new_customer(cls, customer_id, account_type, f_name, l_name):
        with open('data/customers.csv', 'a', newline='') as csvfile:
            fieldnames = ['id', 'account_type', 'first_name', 'last_name', 'current_video_rentals']
            dict_info = {'id': customer_id, 'account_type': account_type, 'first_name':f_name, 'last_name': l_name, 'current_video_rentals':''}
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict_info)


    @classmethod
    def rent_video(cls, user_id, rental, rating):
        validation = False
        rental = rental.title()
        for customer in cls.all_customers:
            if customer.id == user_id:
                customer_rentals = customer.current_video_rentals.split('/')
                if customer.account_type == 'sx':
                    if len(customer_rentals) == 1 and customer_rentals[0] != '':
                        print('You currently have 1 movie rented. Your sx account only allows 1 rental at the time.')
                        print(">>>>>>HERE-1")
                        validation = False
                    else:
                        customer.current_video_rentals = rental
                elif customer.account_type == 'px':
                    if len(customer_rentals) == 3:
                        print('You currently have 3 movies rented. Your px account only allows 3 rentals at the time.')
                        validation = False
                        print(">>>>>>HERE-2")
                    else:
                        if customer_rentals[0] == '':
                            customer.current_video_rentals += f"{rental}"
                            validation = True
                            print(">>>>>>HERE-3")
                        else: 
                            customer.current_video_rentals += f"/{rental}"
                            validation = True
                            print(">>>>>>HERE-4")
                elif customer.account_type == 'sf':
                    if len(customer_rentals) == 1 and customer_rentals[0] != '':
                        print('You currently have 1 movie rented. Your px account only allows 1 rental at the time.')
                        validation = False
                        print(">>>>>>HERE-5")
                    else:
                        print(rating)
                        if rating == 'R':
                            print("R rated movies not allowed for rental in your sf account")
                            validation = False
                            print(">>>>>>HERE-6")
                        else:
                            customer.current_video_rentals = rental
                            validation = True
                            print(">>>>>>HERE-7")
                elif customer.account_type == 'pf':
                    if len(customer_rentals) == 3:
                        print('You currently have 3 movies rented. Your pf account only allows 3 rentals at the time.')
                        validation = False
                        print(">>>>>>HERE-8")
                    else:
                        if rating == 'R':
                            print("R rated movies not allowd for rental in your sf account")
                            validation = False
                            print(">>>>>>HERE-9")
                        else:
                            if customer_rentals[0] == '':
                                customer.current_video_rentals += f"{rental}"
                                validation = True
                            else: 
                                customer.current_video_rentals += f"/{rental}"
                                validation = True
                                print(">>>>>>HERE-11")
            else:
                validation = True
        with open('data/customers.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'account_type', 'first_name', 'last_name', 'current_video_rentals']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for customer in cls.all_customers:
                writer.writerow({
                    'id': customer.id, 
                    'account_type': customer.account_type, 
                    'first_name': customer.first_name, 
                    'last_name': customer.last_name, 
                    'current_video_rentals': customer.current_video_rentals
                })
        return validation

    @classmethod
    def return_video(cls):
        with open('data/customers.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'account_type', 'first_name', 'last_name', 'current_video_rentals']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for customer in cls.all_customers:
                writer.writerow({
                    'id': customer.id, 
                    'account_type': customer.account_type, 
                    'first_name': customer.first_name, 
                    'last_name': customer.last_name, 
                    'current_video_rentals': customer.current_video_rentals
                })


    def __init__(self, id, first_name, last_name, account_type, current_video_rentals=''):
        super().__init__(id, first_name, last_name, current_video_rentals)
        self.account_type = account_type


    def __repr__(self):
        return f"{self.id} | {self.first_name} | {self.last_name} | {self.account_type} | {self.current_video_rentals}"        




