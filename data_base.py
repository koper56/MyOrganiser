from sqlalchemy import Table, Column, Integer, String, MetaData,\
    create_engine, select, update

# Connect with data base, Echo = True returns commands in SQL language
engine = create_engine('sqlite:///test_sqlalchemy.db', echo=False)
connection = engine.connect()


def create_table():
    metadata = MetaData()

    # set name of table, names of columns, kind of data in columns
    clothes_data = Table('clothes_data', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String(10)),
                         Column('color_1', String(10)),
                         Column('color_2', String(10)),
                         Column('color_3', String(10)),
                         Column('photo_source', String),
                         Column('description', String),
                         Column('exclusion', String),
                         Column('kind', String), )

    # commit changes in data base
    metadata.create_all(engine)

    return clothes_data


def insert_new_data():

    # Insert data to new item in clothes_data table
    input_name = input('Name: ')
    # TODO: add color_palette.py
    input_color_1 = input('Color code: ')
    input_color_2 = input('Color code: ')
    input_color_3 = input('Color code: ')
    input_description = input('Description: ')
    input_exclusion = input('Exclusions: ')
    input_kind = input('Kind: ')

    insert_data = create_table().insert()
    # TODO: set new ID = last ID in table + 1
    connection.execute(insert_data, id=" ",
                       name='{}'.format(input_name),
                       color_1='{}'.format(input_color_1),
                       color_2='{}'.format(input_color_2),
                       color_3='{}'.format(input_color_3),
                       # TODO: add ID number after source
                       photo_source='/photos' + 'id_num' + '.jpg',
                       description='{}'.format(
                           input_description),
                       exclusion='{}'.format(
                           input_exclusion),
                       kind='{}'.format(input_kind))
    str(insert_data)


def print_all_data_from_all():
    select_data = select([create_table()])
    result = connection.execute(select_data)
    for row in result:
        print('ID:', row[0], 'Name:', row[1], 'Colors:', row[2], row[3],
              row[4],
              'Photo source:', row[5], 'Description:', row[6],
              'Exclusions:', row[7], 'Kind:', row[8])


def print_all_name_id_from_all():
    select_data = select([create_table()])
    result = connection.execute(select_data)
    for row in result:
        print('ID:', row[0], 'Name:', row[1])


def print_all_data_from_kind():
    input_kind = input('Select kind of clothes: ')
    # From SQL language * = all
    select_data = select(['*']).where(
        create_table().c.kind == input_kind)
    for row in connection.execute(select_data):
        print('ID:', row[0], 'Name:', row[1], 'Colors:', row[2], row[3],
              row[4],
              'Photo source:', row[5], 'Description:', row[6],
              'Exclusions:', row[7], 'Kind:', row[8])


def print_one_data_from_id():
    input_id = int(input('Select ID: '))
    # From SQL language * = all
    select_data = select(['*']).where(
        create_table().c.id == input_id)
    for row in connection.execute(select_data):
        print('ID:', row[0], 'Name:', row[1], 'Colors:', row[2], row[3],
              row[4],
              'Photo source:', row[5], 'Description:', row[6],
              'Exclusions:', row[7], 'Kind:', row[8])


def update_item():
    input_id = int(input('Select ID number of item to change: '))

    # Get data from rows with selected ID number
    select_data = select(['*']).where(
        create_table().c.id == input_id)
    for row in connection.execute(select_data):
        input_name = input('New name for name: {}: '.format(row[1]))
        input_description = input(
            'New description for description: {}: '.format(row[6]))
        input_exclusion = input(
            'New exclusions for exclusion: {}: '.format(row[7]))
        # TODO: OperationalError
        update_data = update(create_table()).where(
            input_id == create_table().c.id).values(
            name='{}'.format(input_name),
            description='{}'.format(input_description),
            exclusion='{}'.format(input_exclusion))

        # Commit change
        connection.execute(update_data)


def delete_item():
    input_id = int(input('Select ID number of item to delete: '))

    delete = create_table().delete().where(create_table().c.id == input_id)

    # Commit delete
    connection.execute(delete)
