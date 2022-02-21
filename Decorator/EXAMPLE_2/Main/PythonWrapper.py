def show_highlight_message(function):
    def wrapper(phrase):
        print("****")
        function(phrase)
        print("****")
    return wrapper


@show_highlight_message
def show_message(phrase):
    print(phrase)


if __name__ == '__main__':
    show_message('Hello')
