from src.Users.controllers.UserManager import UserManager
from src.Utils.Tools import *
from src.Movements.Controllers.MovementManager import MovementManager
from threading import *
import time


def generate_users(quantity: int, um: UserManager) -> None:
    for i in range(0, quantity):
        try:
            um.add(user_generator())
            print(f"{i} of {quantity} users generated.")
        except Exception as err:
            print(err)


def generate_items(quantity: int, im) -> None:
    for i in range(0, quantity):
        try:
            im.add_item(generate_random_item())
            print(f"{i} of {quantity} items generated.")
        except Exception as err:
            print(err)


def generate_movement(quantity: int, im, um, mm) -> None:
    for i in range(0, quantity):
        try:
            mm.add(movement_generator(im, um))
            print(f"{i} of {quantity} movements generated.")
        except Exception as err:
            print(err)


def delete_all_previous():
    db = DatabaseManager()
    db.query("DELETE FROM users;")
    db.query("DELETE FROM items;")
    db.query("DELETE FROM movements;")
    db.query("DELETE FROM items_genres;")
    db.query("DELETE FROM items_inner_states;")
    db.query("DELETE FROM items_external_states;")


def test_thread():
    for i in range(0,100):
        print("test")

if __name__ == "__main__":
    im = ItemManager()
    um = UserManager()
    mm = MovementManager()

    gu1 = Thread(target=test_thread)
    gu1.start()

    gu1.join()

    #generate_users(10000, um)
    #generate_items(50000, im)
    generate_movement(100000, im, um, mm)


    # _thread.start_new_thread(generate_items, (25000,))
    # _thread.start_new_thread(generate_items, (25000,))
    #
    # _thread.start_new_thread(generate_movement, (33000,))
    # _thread.start_new_thread(generate_movement, (33000,))
    # _thread.start_new_thread(generate_movement, (34000,))
