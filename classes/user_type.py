from classes.user import User
import csv


class UserType(User):
    @classmethod
    def load_customers(cls):
        all_customers = []
        with open('data/customers.csv', newline='') as csvfile:
            file_reader = csv.DictReader(csvfile)
            for row in file_reader:
                customer = cls(**row)
                all_customers.append(customer)
        return all_customers

    @classmethod
    def new_customer(cls, customer_id, account_type, f_name, l_name):
        with open('data/customers.csv', 'a', newline='') as csvfile:
            fieldnames = ['id', 'account_type', 'first_name', 'last_name', 'current_video_rentals']
            dict_info = {'id': customer_id, 'account_type': account_type, 'first_name':f_name, 'last_name': l_name, 'current_video_rentals':''}
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(dict_info)
        pass


    def __init__(self, id, first_name, last_name, account_type, current_video_rentals):
        super().__init__(id, first_name, last_name, current_video_rentals)
        self.account_type = account_type


    def __repr__(self):
        return f"{self.id} | {self.first_name} | {self.last_name} | {self.account_type} | {self.current_video_rentals}"        




