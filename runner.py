from classes.user_type import UserType
from classes.video_inventory import VideoInventory
from classes.store import Store


triton = Store('Triton')

main_ui_message = f"""
{triton}

1. View store video inventory
2. View store customers
3. View customer rented videos
4. Add new customer
5. Rent video
6. Return video
7. Exit

"""

# command line program
is_active = True
while is_active:
    cmd = input(main_ui_message)
    if cmd == '1':
        triton.view_inventory()
    elif cmd == '2':
        triton.view_customers()
    elif cmd == '3':
        user_id = input("Enter user ID: ")
        triton.view_customer(user_id)
    elif cmd == '4':
        triton.new_customer()
    elif cmd == '5':
        triton.rent_video()
    elif cmd == '6':
        triton.return_video()
    elif cmd == '7':
        is_active = False

# print(triton)
# triton.view_inventory()
# triton.view_customers()

# triton.view_customer(2)

# triton.new_customer()
# triton.rent_video()
# triton.view_inventory()
