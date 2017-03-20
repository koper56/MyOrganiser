import sqlite3

# Create new data base
connection = sqlite3.connect('clothes_data.db')

# Create cursor
db_cursor = connection.cursor()


# Create new table for data
def create_table():
    db_cursor.execute('CREATE TABLE IF NOT EXISTS clothes_data(id INTEGER, '
                      'name TEXT, color_1 TEXT, color_2 TEXT, color_3 TEXT, '
                      'photo TEXT, description TEXT, '
                      'exclusion TEXT, kind TEXT)')


# Value of last ID number + 1
def next_id():
    last_id_num = db_cursor.execute('SELECT max(id) FROM clothes_data')
    global next_id
    next_id = last_id_num.fetchone()[0] + 1


# Add new data to table
def add_data_from_input():
    # Type data
    def inputs():
        global input_name
        global input_color_1
        global input_color_2
        global input_color_3
        global input_source
        global input_description
        global input_exclusion
        global input_kind
        input_name = input('Name: ')
        input_color_1 = input('Color code: ')
        input_color_2 = input('Color code: ')
        input_color_3 = input('Color code: ')
        input_source = input('Photo source: ')
        input_description = input('Description: ')
        input_exclusion = input('Exclusions: ')
        input_kind = input('Kind: ')
        return inputs

    # Check typed data
    def check():
        print('Name: {}, Color_1: {}, Color_2: {}, Color_3: {}, Source: {}, '
              'Description: {}. Exclusions: {}. Kind: {}\n\n'
              'Correct?'.format(input_name, input_color_1, input_color_2,
                                input_color_3, input_source, input_description,
                                input_exclusion, input_kind))

        check_input_data = input("'Y', 'N' or 'quit'\n")

        if check_input_data == 'Y':

            # Create new ID number
            next_id()

            # Send data to table with new ID number
            db_cursor.execute(
                "INSERT INTO clothes_data VALUES({}, '{}', '{}', '{}', "
                "'{}', '{}', '{}', '{}', '{}')"
                    .format(next_id, input_name, input_color_1, input_color_2,
                            input_color_3, input_source, input_description,
                            input_exclusion, input_kind))

            # Add data to table
            connection.commit()

            # Close function
            db_cursor.close()
            connection.close()

        elif check_input_data == 'N':
            add_data_from_input()

        elif check_input_data == 'quit':
            pass

        else:
            print("'Y' or 'N'!")
            check()

    inputs()
    check()


def print_all_data():
    db_cursor.execute('SELECT * FROM clothes_data')
    for row in db_cursor.fetchall():
        print(row)


def print_selected_data():
    search_category = input('Select category of search in data base\nid, '
                            'name, kind\n-->: ')
    search_data = input('Data to search in data base: ')
    db_cursor.execute('SELECT * FROM clothes_data WHERE {}={}'
                      .format(search_category, search_data))

    for row in db_cursor.fetchall():
        print(row)


def update_data_base():
    category = input('Choose category to update: ')
    old_value = input('Choose value from {} to update: '.format(category))
    new_value = input('Set new value for {} in {}'.format(old_value, category))

    db_cursor.execute('UPDATE clothes_data SET {} = {} WHERE {} = {}'
                      .format(category, new_value, category, old_value))
    # Add data to table
    connection.commit()

    # Close function
    db_cursor.close()
    connection.close()


def delete_data():
    value = input('Choose data ID number to delete: ')
    db_cursor.execute('DELETE FROM clothes_data WHERE ID = {}'.format(value))
    # Add data to table
    connection.commit()

    # Close function
    db_cursor.close()
    connection.close()
