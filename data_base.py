from sqlalchemy import Column, Integer, String, create_engine, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

data_base = declarative_base()


class ClothesData(data_base):
    __tablename__ = 'ClothesData'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    color_1 = Column(String(20), nullable=False)
    color_2 = Column(String(20), nullable=False)
    color_3 = Column(String(20), nullable=False)
    photo_source = Column(String(20), nullable=False)
    description = Column(String(100), nullable=False)
    exclusion = Column(String(250), nullable=False)
    clear = Column(String(5), nullable=False)
    rate = Column(Integer, nullable=False)
    kind = Column(String(20), nullable=False)


# Connect with data base, Echo = True returns commands in SQL language
engine = create_engine('sqlite:///test_sqlalchemy.db', echo=False)
data_base.metadata.create_all(engine)
data_base_session = sessionmaker(bind=engine)
session = data_base_session()
connection = engine.connect()


# Return last value of id number + 1
def next_id_value():
    max_id = session.query(func.max(ClothesData.id).label("max_id_data"))
    select_max = max_id.one()
    try:
        next_id = select_max.max_id_data + 1
    # Except error when id = 0, set next id value equal 1
    except TypeError:
        print('First data in data base')
        next_id = 1
    return next_id


def insert_new_data():
    # TODO reformat id number to '001.jpg', '010.jpg', '100.jpg'
    # Insert data to new item in ClothesData table
    # Default ID = last ID + 1, for first item ID = 1
    # Default photo source photo/'ID NUMBER'.jpg
    # Default clear = True
    # Default rate = 0

    input_name = input('Name: ')
    # Run code with color palette
    import color_palette as color
    input_color_1 = color.get_color()
    import color_palette as color
    input_color_2 = color.get_color()
    import color_palette as color
    input_color_3 = color.get_color()
    input_description = input('Description: ')
    input_exclusion = input('Exclusions: ')
    input_kind = input('Kind: ')

    new_data = ClothesData(id=next_id_value(),
                           name='{}'.format(input_name),
                           color_1='{}'.format(input_color_1),
                           color_2='{}'.format(input_color_2),
                           color_3='{}'.format(input_color_3),
                           photo_source='photo/{}.jpg'.format(
                               str(next_id_value())),
                           description='{}'.format(
                               input_description),
                           exclusion='{}'.format(
                               input_exclusion),
                           clear='True',
                           rate='0',
                           kind='{}'.format(input_kind))

    # Commit new data
    session.add(new_data)
    session.commit()


def get_names_clothes_data_row():
    select_data = select([ClothesData.name])
    return [row[0] for row in connection.execute(select_data)]


def get_kinds_clothes_data_row():
    select_data = select([ClothesData.kind])
    return [row[0] for row in connection.execute(select_data)]

print(get_kinds_clothes_data_row())

def print_all_name_from_all():
    select_data = select([ClothesData])
    result = connection.execute(select_data)
    for row in result:
        print('ID:', row[0], 'Name:', row[1])


def print_all_data_by_kind():
    input_kind = input('Select kind of clothes: ')
    select_data = select([ClothesData]).where(
        ClothesData.kind == input_kind)
    for row in connection.execute(select_data):
        print('ID:', row[0], 'Name:', row[1], 'Colors:', row[2], row[3],
              row[4],
              'Photo source:', row[5], 'Description:', row[6],
              'Exclusions:', row[7], 'Kind:', row[10])


def print_one_data_by_name(input_name):
    select_data = select([ClothesData]).where(
        ClothesData.name == input_name)
    for row in connection.execute(select_data):
        return row


def update_item():
    input_id = int(input('Select ID number of item to change: '))
    select_data = select([ClothesData]).where(ClothesData.id == input_id)
    for row in connection.execute(select_data):
        input_name = input('New name for name: {}: '.format(row[1]))
        input_description = input(
            'New description for description: {}: '.format(row[6]))
        input_exclusion = input(
            'New exclusions for exclusion: {}: '.format(row[7]))
        # CREATE ONCE
        table = ClothesData
        update_data = update(table).where(table.id == input_id).values(
            name='{}'.format(input_name),
            description='{}'.format(input_description),
            exclusion='{}'.format(input_exclusion))
        # Commits changes, IF autocommit is in use
        connection.execute(update_data)


def delete_item():
    input_id = int(input('Select ID number of item to delete: '))
    selected_item = session.query(ClothesData).get(input_id)

    session.delete(selected_item)
    # Commit delete
    session.commit()


# TODO: Don't work
def change_clear():
    input_id = int(input('Select ID number of item to change clear: '))
    if select([ClothesData]).where(ClothesData.id == input_id,
                                   ClothesData.clear == 'True'):

        update_data = update(ClothesData).where(
            ClothesData.id == input_id).values(clear='False')

    elif select([ClothesData]).where(ClothesData.id == input_id,
                                     ClothesData.clear == 'False'):

        update_data = update(ClothesData).where(
            ClothesData.id == input_id).values(clear='True')

        # Commits changes
        connection.execute(update_data)


def set_rate():
    input_id = int(input('Select ID number of item to change: '))
    select_data = select([ClothesData]).where(ClothesData.id == input_id)
    for row in connection.execute(select_data):
        input_rate = input('New rate(1 - 5) for name: {}: '.format(row[1]))
        # CREATE ONCE
        table = ClothesData
        update_data = update(table).where(table.id == input_id).values(
            rate='{}'.format(input_rate))
        # Commits changes, IF autocommit is in use
        connection.execute(update_data)
