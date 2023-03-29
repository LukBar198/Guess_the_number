def exception_handler(func):
    """Error handling decorator

    :param func: function passed to decorator
    :return:     function with added exception handling
    """

    def inner_function(*args, **kwargs):
        """Exception handling function

        :param args:    positional arguments
        :param kwargs:  key arguments
        :return:        exception handling
        """
        try:
            func(*args, **kwargs)
        except (TypeError, ValueError):
            print("It's not a number!")

    return inner_function
