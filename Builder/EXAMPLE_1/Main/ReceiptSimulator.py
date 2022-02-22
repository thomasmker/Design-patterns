from Builder.EXAMPLE_1.Models.ReceiptBuilder import ReceiptBuilder
from Builder.EXAMPLE_1.Models.Receipt import Receipt


def main():
    receipt = Receipt(customer='John doe', item='Book', details='Lorem ipsum')
    print(receipt)

    receipt_builder = ReceiptBuilder()
    from_receipt_builder = (receipt_builder
                            .with_customer('John doe')
                            .with_item('Book')
                            .with_details('Lorem ipsum')
                            .build())

    print(from_receipt_builder)


if __name__ == '__main__':
    main()
