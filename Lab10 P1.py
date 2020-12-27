def get_time():

    # getting the time for the user

    time = input('Enter time [hh:mm:ss]: ')

    time = time.split(':')

    # checking if it;s colon separated only

    if len(time) != 3:

        print('Must separate hour, minute and second with colons.')

        return

    hh, mm, ss = time

    # Hour must be a 2 digit number

    if len(hh) != 2 or not hh.isdigit():

        print('Hour must be a 2-digit number.')

        return

    # Minute must be a 2 digit number

    if len(mm) != 2 or not mm.isdigit():

        print('Minute must be a 2-digit number.')

        return

    # Second must be a 2 digit number

    if len(ss) != 2 or not ss.isdigit():

        print('Second must be a 2-digit number.')

        return

    # Hour must be within 0 - 23

    if not 0 <= int(hh) <= 23:

        print('Hour must be a 2-digit number between 0 and 23.')

        return

    # Minute must be within 0 - 59

    if not 0 <= int(mm) <= 59:

        print('Minute must be a 2-digit number between 0 and 59.')

        return

    # Second must be within 0 - 59

    if not 0 <= int(ss) <= 59:

        print('Second must be a 2-digit number between 0 and 59.')

        return

    print('Time with colons removed: ', ''.join(time))

# calling the method

get_time()