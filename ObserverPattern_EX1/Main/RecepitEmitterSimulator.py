from ObserverPattern_EX1.Models.Receipt import Receipt
from ObserverPattern_EX1.Models.Observers import send_by_email, save_on_database, push_notification_on_slack


def main():
    observers = [send_by_email, save_on_database, push_notification_on_slack]
    receipt = Receipt(customer='John doe', item='Book', observers=observers)
    receipt.notify_observers()


if __name__ == '__main__':
    main()
