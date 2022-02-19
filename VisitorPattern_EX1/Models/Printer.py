class Printer:

    def visit_sum(self, custom_sum):
        print('(', end='')
        custom_sum.left_expression.accept_visitor(self)
        print('+', end='')
        custom_sum.right_expression.accept_visitor(self)
        print(')', end='')

    def visit_subtraction(self, custom_subtraction):
        print('(', end='')
        custom_subtraction.left_expression.accept_visitor(self)
        print('-', end='')
        custom_subtraction.right_expression.accept_visitor(self)
        print(')', end='')

    def visit_number(self, custom_number):
        print(custom_number.calculate(), end='')
