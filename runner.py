from classes.user_type import UserType
from classes.video_inventory import VideoInventory
from classes.store import Store
import csv

triton = Store('TRITON')
# print(triton)
# triton.view_inventory()
# triton.view_customers()

triton.view_customer(4)

# triton.new_customer()
# triton.rent_video('toy story', 1)
