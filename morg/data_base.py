import time
import logging

from sqlalchemy import Column, Integer, String, create_engine, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

# Create tables in data base
data_base = declarative_base()

# Take time and store in format day_month_year - 09_05_2017
time_format = time.strftime("%Y_%m_%d")

# Create specific logger different than Kivy logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.INFO)

# Logging info format f.ex.
# "[2017-05-09 15:33:58,217]	data_base_test_log.py	message"
format_of_logger = logging.Formatter('[%(asctime)s]\t%(pathname)s\t%(message)s')

# Create file with logging info f.ex. "morg_09_05_2017.log"
file_handler = logging.FileHandler('logs/morg_{}.log'.format(time_format))
file_handler.setFormatter(format_of_logger)
logger.addHandler(file_handler)


# Create table with clothes data
class ClothesData(data_base):
    __tablename__ = 'ClothesData'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    color_1 = Column(String(8), nullable=False)
    color_2 = Column(String(8), nullable=False)
    color_3 = Column(String(8), nullable=False)
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


# Connect with database file, Echo = True returns commands in SQL language
engine = create_engine('sqlite:///data_base_file.db', echo=False)
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
        logger.info('First data in data base - ClothesData')
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
    logger.info(
        'New Data: ID: {}, Name: {}, Color 1: {}, Color 2: {}, Color 3: {}, '
        'Photo Source: photo/{}.png, Description: {}, Exclusion: {}, '
        'Clear: True, '
        'Rate: 0, Kind: {}'.format(next_id_value() - 1,
                                   input_name,
                                   input_color_1, input_color_2,
                                   input_color_3, next_id_value(),
                                   input_description, input_exclusion,
                                   input_kind))


def get_names_clothes_data_row():
    select_data = select([ClothesData.name])
    return [row[0] for row in connection.execute(select_data)]


def get_id_clothes_data_row():
    select_data = select([ClothesData.id])
    return [row[0] for row in connection.execute(select_data)]


def get_colors_names_clothes_data_row():
    select_data = select([ClothesData])
    return [row[1:5] for row in connection.execute(select_data)]


def get_color1_clothes_data_row():
    select_data = select([ClothesData.color_1])
    return [row[0] for row in connection.execute(select_data)]


def get_color2_clothes_data_row():
    select_data = select([ClothesData.color_2])
    return [row[0] for row in connection.execute(select_data)]


def get_color3_clothes_data_row():
    select_data = select([ClothesData.color_3])
    return [row[0] for row in connection.execute(select_data)]


def get_kinds_clothes_data_row():
    select_data = select([ClothesData.kind])
    return [row[0] for row in connection.execute(select_data)]


def get_names_clothes_by_kind(input_kind):
    # Return all names with input name of kind
    select_data = select([ClothesData]).where(
        ClothesData.kind == input_kind)
    return [row[1] for row in connection.execute(select_data)]


def get_names_clothes_by_rate(input_rate):
    # Return all names with input value of rate
    select_data = select([ClothesData]).where(
        ClothesData.rate == input_rate)
    return [row[1] for row in connection.execute(select_data)]


def print_one_data_by_name(input_name):
    select_data = select([ClothesData]).where(
        ClothesData.name == input_name)
    for row in connection.execute(select_data):
        return row


def print_one_data_by_id(input_id):
    select_data = select([ClothesData]).where(
        ClothesData.id == input_id)
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
    logger.info(
        'Changes commited in {} -> {}'.format(input_name,
                                              input_new_name))


def delete_item(input_id):
    selected_item = session.query(ClothesData).get(input_id)

    session.delete(selected_item)
    # Commit delete
    session.commit()
    logger.info(
        'Cloth id {} deleted'.format(input_id))


def update_clear(input_name, input_clear):
    update_data = update(ClothesData).where(
        ClothesData.name == input_name).values(
        clear='{}'.format(input_clear))
    # Commits changes in ClothesData table
    connection.execute(update_data)
    logger.info('Changes commited in {}'.format(
        input_name))


def update_rate(input_name, input_rate):
    update_data = update(ClothesData).where(
        ClothesData.name == input_name).values(
        rate='{}'.format(input_rate))
    # Commits changes in ClothesData table
    connection.execute(update_data)
    logger.info('Changes commited in {}'.format(
        input_name))


# Return last value of id number + 1
def next_id_history():
    max_id = session.query(func.max(HistoryData.id).label("max_id_data"))
    select_max = max_id.one()
    try:
        next_id = select_max.max_id_data + 1
    # Except error when id = 0, set next id value equal 1
    except TypeError:
        logger.info(
            'First data in data base - HistoryData')
        next_id = 1
    return next_id


def insert_new_history_data(input_date, input_description, input_rate):
    # Insert new history to HistoryData table
    # Default ID = last ID + 1, for first item ID = 1
    # Default photo source 'sets/Set_from_d_m_y.png'


    new_data = HistoryData(id=next_id_history(),
                           date='{}'.format(input_date),
                           photo_source='sets/Set_from_{}.png'.format(
                               input_date),
                           description='{}'.format(
                               input_description),
                           rate='{}'.format(input_rate))

    # Commit new data
    session.add(new_data)
    session.commit()
    logger.info(
        'New Data: ID: {}, Date: {}, Photo: sets/Set_from_{}.png, '
        'Description: {}, Set rate: {}'.format(
            next_id_history() - 1,
            time_format,
            time_format,
            input_description,
            input_rate))


def update_description_and_rate_history(input_date, input_description,
                                        input_rate):
    # Function change description and rate by typed date of set
    update_data = update(HistoryData).where(
        HistoryData.date == input_date).values(
        description='{}'.format(input_description),
        rate='{}'.format(input_rate))
    # Commits changes in HistoryData table
    connection.execute(update_data)
    logger.info('Changes commited in {}'.format(
        input_date))


def print_one_data_by_date(input_date):
    # Function return all columns for typed date of set from HistoryData
    select_data = select([HistoryData]).where(
        HistoryData.date == input_date)
    for row in connection.execute(select_data):
        return row


def get_date_sets_by_rate(input_rate):
    # Return all date of sets with input value of rate
    select_data = select([HistoryData]).where(
        HistoryData.rate == input_rate)
    return [row[1] for row in connection.execute(select_data)]


def get_date_sets_data_row():
    # Return all dates with data in HistoryData table
    select_data = select([HistoryData.date])
    return [row[0] for row in connection.execute(select_data)]
