def distribute():
    print('Distribute oranges to the workers!')
    orange = int(input('Please enter the number of oranges:'))
    worker = int(input('Please enter the number of workers on site:'))
    result = orange // worker  # Calculate the number of oranges per person
    remain = orange - result * worker  # Calculate the number of remaining oranges

    if remain > 0:
        print('Each worker got ' + str(result) + ' oranges, with ' + str(remain) + ' oranges remaining.')
    else:
        print('Each worker got ' + str(result) + ' oranges, with 0 oranges remaining.')

if __name__ == '__main__':
    try:
        distribute()
    except ZeroDivisionError:
        print('\nError, oranges cannot be divided by 0 workers!')
    except ValueError as e:
        print('\nError, oranges cannot be divided by 0 workers!',e)
    else:
        print(' divided workers!')
    finally:
        print('\nFinally...')

