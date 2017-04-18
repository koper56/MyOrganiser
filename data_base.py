from sqlalchemy import Column, Integer, String, create_engine, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import time


# Connect with database file, Echo = True returns commands in SQL language
data_base = declarative_base()
engine = create_engine('sqlite:///test_sqlalchemy.db', echo=False)
data_base.metadata.create_all(engine)
data_base_session = sessionmaker(bind=engine)
session = data_base_session()
connection = engine.connect()


# Create table with clothes data
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


# Create table with sets data
class HistoryData(data_base):
    __tablename__ = 'HistoryData'
    id = Column(Integer, primary_key=True)
    date = Column(String(20), nullable=False)
    photo_source = Column(String(20), nullable=False)
    description = Column(String(100), nullable=False)
    rate = Column(Integer, nullable=False)


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


def insert_new_data(input_name, input_color_1, input_color_2, input_color_3,
                    input_description, input_exclusion, input_kind):
    # Insert data to new item in ClothesData table
    # Default ID = last ID + 1, for first item ID = 1
    # Default photo source photo/'ID NUMBER'.png
    # Default clear = True
    # Default rate = 0

    new_data = ClothesData(id=next_id_value(),
                           name='{}'.format(input_name),
                           color_1='{}'.format(input_color_1),
                           color_2='{}'.format(input_color_2),
                           color_3='{}'.format(input_color_3),
                           photo_source='photo/{}.png'.format(
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
    print('New Data: ID: {}, Name: {}, Color 1: {}, Color 2: {}, Color 3: {}, '
          'Photo Source: photo/{}.png, Description: {}, Exclusion: {}, '
          'Clear: True, '
          'Rate: 0, Kind: {}'.format(next_id_value(), input_name,
                                     input_color_1, input_color_2,
                                     input_color_3, next_id_value(),
                                     input_description, input_exclusion,
                                     input_kind))


def get_names_clothes_data_row():
    select_data = select([ClothesData.name])
    return [row[0] for row in connection.execute(select_data)]


def get_kinds_clothes_data_row():
    select_data = select([ClothesData.kind])
    return [row[0] for row in connection.execute(select_data)]


# Return all names with input name of kind
def get_names_clothes_by_kind(input_kind):
    select_data = select([ClothesData]).where(
        ClothesData.kind == input_kind)
    return [row[1] for row in connection.execute(select_data)]


# Return all names with input value of rate
def get_names_clothes_by_rate(input_rate):
    select_data = select([ClothesData]).where(
        ClothesData.rate == input_rate)
    return [row[1] for row in connection.execute(select_data)]


def print_all_name_from_all():
    select_data = select([ClothesData])
    result = connection.execute(select_data)
    for row in result:
        print('ID:', row[0], 'Name:', row[1])


def print_one_data_by_name(input_name):
    select_data = select([ClothesData]).where(
        ClothesData.name == input_name)
    for row in connection.execute(select_data):
        return row


def update_item(input_name, input_new_name, input_description,
                input_exclusion):
    update_data = update(ClothesData).where(
        ClothesData.name == input_name).values(
        name='{}'.format(input_new_name),
        description='{}'.format(input_description),
        exclusion='{}'.format(input_exclusion))
    # Commits changes in ClothesData table
    connection.execute(update_data)


def delete_item(input_id):
    selected_item = session.query(ClothesData).get(input_id)

    session.delete(selected_item)
    # Commit delete
    session.commit()


def update_clear(input_name, input_clear):
    update_data = update(ClothesData).where(
        ClothesData.name == input_name).values(
        clear='{}'.format(input_clear))
    # Commits changes in ClothesData table
    connection.execute(update_data)


def update_rate(input_name, input_rate):
    update_data = update(ClothesData).where(
        ClothesData.name == input_name).values(
        rate='{}'.format(input_rate))
    # Commits changes in ClothesData table
    connection.execute(update_data)


# Return last value of id number + 1
def next_id_history():
    max_id = session.query(func.max(HistoryData.id).label("max_id_data"))
    select_max = max_id.one()
    try:
        next_id = select_max.max_id_data + 1
    # Except error when id = 0, set next id value equal 1
    except TypeError:
        print('First data in data base')
        next_id = 1
    return next_id


def insert_new_history_data(input_description, input_rate):
    # Insert new history to HistoryData table
    # Default ID = last ID + 1, for first item ID = 1
    # Default photo source 'sets/Set_from_d_m_y.png'

    # Take time and store in format day_month_year
    time_format = time.strftime("%d_%m_%Y")

    new_data = HistoryData(id=next_id_history(),
                           date='{}'.format(time_format),
                           photo_source='sets/Set_from_{}.png'.format(
                               time_format),
                           description='{}'.format(
                               input_description),
                           rate='{}'.format(input_rate))

    # Commit new data
    session.add(new_data)
    session.commit()
    print('New Data: ID: {}, Date: {}, Photo: sets/Set_from_{}.png, '
          'Description: {}, Set rate: {}'.format(next_id_history()-1,
                                                 time_format,
                                                 time_format,
                                                 input_description,
                                                 input_rate))
