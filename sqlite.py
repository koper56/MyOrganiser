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

    def check():
        # Check data
        print('Name:{}, Color_1:{}, Color_2:{}, Color_3:{}, Source:{}, '
              'Description:{}. Exclusions:{}. Kind:{}\n\n'
              'Correct?'.format(input_name, input_color_1, input_color_2, input_color_3, input_source, input_description, input_exclusion, input_kind))

        check_input_data = input('(Y/N)')

        if check_input_data == 'Y':

            # Send data to table
            db_cursor.execute(
                "INSERT INTO clothes_data VALUES('ID', '{}', '{}', '{}', "
                "'{}', '{}', '{}', '{}', '{}')".format(input_name, input_color_1, input_color_2, input_color_3, input_source, input_description, input_exclusion, input_kind))
            # Add data to table
            connection.commit()

            # Close function
            db_cursor.close()
            connection.close()
        elif check_input_data == 'N':
            add_data_from_input()
        else:
            print("'Y' or 'N'!")
            check()
    inputs()
    check()


