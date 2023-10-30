def do_stuff(num):
    try:
        if num:
            return int(num) + 5

        elif num == 0:
            return 'please enter a number other than 0'
        else:
            return "please enter number"
    except ValueError as err:
        return err
