from datetime import date
from MementoPattern_EX1.Models.Contract import Contract
from MementoPattern_EX1.Models.ContractHistory import ContractHistory


def main():
    history = ContractHistory()
    contract = Contract(contract_date=date.today(), client='John Doe')

    history.add_state(contract.save_state())

    contract.next()
    contract.client = 'Maria Doe'
    history.add_state(contract.save_state())

    print(f'First state {history.get_state(0).contract}')
    print(f'Second state {history.get_state(1).contract}')

    contract.restore_state(history.get_state(0))
    print('\nContract restored to the first state')
    print(contract)

if __name__ == '__main__':
    main()
