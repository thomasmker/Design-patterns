from abc import ABCMeta, abstractmethod


class BudgetState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_extra_discount(self, budget):
        pass

    @abstractmethod
    def approve(self, budget):
        pass

    @abstractmethod
    def deny(self, budget):
        pass

    @abstractmethod
    def close(self, budget):
        pass


class InProgress(BudgetState):
    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.01)

    def approve(self, budget):
        budget.current_state = Approved()

    def deny(self, budget):
        budget.current_state = Denied()

    def close(self, budget):
        raise Exception("In progress budgets cannot be closed")


class Approved(BudgetState):
    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.02)

    def approve(self, budget):
        raise Exception("Budgets already approved")

    def deny(self, budget):
        raise Exception("Approved budgets cannot be denied")

    def close(self, budget):
        budget.current_state = Closed()


class Denied(BudgetState):
    def apply_extra_discount(self, budget):
        raise Exception("Denied budgets do not get extra discount")

    def approve(self, budget):
        raise Exception("Denied budgets cannot be approved")

    def deny(self, budget):
        raise Exception("Budgets already denied")

    def close(self, budget):
        budget.current_state = Closed()


class Closed(BudgetState):
    def apply_extra_discount(self, budget):
        raise Exception("Closed budgets do not get extra discount")

    def approve(self, budget):
        raise Exception("Closed budgets cannot be approved")

    def deny(self, budget):
        raise Exception("Closed budgets cannot be denied")

    def close(self, budget):
        raise Exception("Budgets already closed")
