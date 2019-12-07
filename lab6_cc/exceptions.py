def try_expense_type(expense_type):
    """
    Verify the type
    :param expense_type: the type of an expense
    :return: expense type
    """
    if expense_type == 'canal' or expense_type == 'maintenance' or expense_type == 'other':
        return expense_type
    else:
        while expense_type != 'canal' and expense_type != 'maintenance' and expense_type != 'other':
            expense_type = input('Choose only from these three types of expenses: canal, maintenance,other:')
        return expense_type


def try_date(date):
    """
    Verify the date
    :param date: the date of an expense
    :return: the date
    """
    day = -1
    month = -1
    year = -1
    while day == -1 or month == -1 or year == -1:
        while '.' not in date:
            print('Write the date like so: DD/MM/YYYY!')
            date = input('')
        args = date.split('.')
        length = len(args)
        while length != 3:
            print('The . must appear exactly twice!')
            date = input('')
            args = date.split('.')
            length = len(args)
        try:
            day = int(args[0])
        except ValueError:
            print('The day is not a valid number!')
            date = input('')
        else:
            try:
                if day > 32 or day < 1:
                    day = -1
                    raise ValueError
            except ValueError:
                print('The day is not a valid number!')
                date = input('')
            else:
                try:
                    month = int(args[1])
                except ValueError:
                    print('The month is not a number!')
                    date = input('')
                else:
                    try:
                        if month > 12 or month < 1:
                            month = -1
                            raise ValueError
                    except ValueError:
                        print('The month is not a valid number!')
                        date = input('')
                    else:
                        try:
                            year = int(args[2])
                        except ValueError:
                            print('The year is not a number!')
                            date = input('')
                        else:
                            try:
                                if year > 2019 or year < 1999:
                                    year = -1
                                    raise ValueError
                            except ValueError:
                                print('The year is not a valid number!')
                                date = input('')
    return date
