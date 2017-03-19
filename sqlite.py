import sqlite3


# Create new data base
connection = sqlite3.connect('clothes_data.db')


# Create cursor
db_cursor = connection.cursor()


# Create new table for data
def create_table():
    db_cursor.execute('CREATE TABLE IF NOT EXISTS clothes_data(id REAL, '
                      'name TEXT, color_1 TEXT, color_2 TEXT, color_3 TEXT, '
                      'photo TEXT, description TEXT, '
                      'exclusion TEXT, kind TEXT)')


# Add new data in table clothes_data
def add_data():
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(1, 'red_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(2, 'dark_red_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(3, 'white_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(4, 'long_white_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(5, 'gray_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(6, 'neck_gray_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(7, 'deer_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(8, 'mygf_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(9, 'gorilla_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(10, ' astronaut_ts ', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(11, 'puma_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(12, 'tiger_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(13, 'teddy_bear_ts', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 't_shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(16, 'light_gray_longsleeve', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(17, 'black_white_longsleeve', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(18, 'gray_longsleeve', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(19, 'black_monk', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(20, 'gray_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(21, 'white_longsleeve', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(22, 'black_longsleeve', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(23, 'brown_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(24, 'black_ninja_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(25, 'black_admirable_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(26, 'black_cropp_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(27, 'black_adidas_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(28, 'black_long_sweater', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(29, 'light_gray_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(30, 'gray_sweater', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(31, 'green_long_sweater', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(32, 'raven_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(33, 'pitbull_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(34, 'skull_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(35, 'bear_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(36, 'moro', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(37, 'revolution_cat_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(38, 'mountains_baseball', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hoodies')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(39, 'gray_casual_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(40, 'green_casual_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(41, 'gray_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(42, 'blue_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(43, 'black_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(44, 'white_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shirts')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(45, 'black_pants_holes', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(46, 'blue_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(47, 'white_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(48, 'gray_loose_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(49, 'gray_zip_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(50, 'black_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(51, 'gray_slim_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(52, 'red_pants', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(53, 'skull_joggers', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(54, 'strokes_joggers', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'trousers')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(55, 'black_vans', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(56, 'black_flips', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(57, 'strokes_sneakers', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(58, 'brown_shoes', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(59, 'jackboots', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(60, 'black_airmax', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(61, 'black_elastic_sides', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'shoes')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(66, 'strokes_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hats')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(67, 'black_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hats')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(62, 'black_snapback', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hats')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(63, 'gray_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hats')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(64, 'city_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hats')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(65, 'panda_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'hats')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(68, 'black_jacket', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'jackets')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(69, 'green_coat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'jackets')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(70, 'moro_jacket', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'jackets')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(71, 'silver_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'sunglasses')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(72, 'gold_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'sunglasses')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(73, 'black_green_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'sunglasses')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(74, 'gray_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'sunglasses')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(75, 'black_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'sunglasses')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(76, 'black_neck', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'necklaces')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(77, 'gray_neck', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'necklaces')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(78, 'silver_black_tunnels', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'piercing')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(79, 'eye_ring', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'rings')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(80, 'silver1_ring', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'rings')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(81, 'silver2_ring', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'rings')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(82, 'bracelets', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'bracelets')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(83, 'black_bag', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'bags')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(84, 'black_backpack', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'bags')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(85, 'panda_backpack', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'bags')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(86, 'strokes_gloves', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'gloves')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(87, 'black_scarf', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'scarfs')")
    db_cursor.execute(
        "INSERT INTO clothes_data VALUES(88, 'red_scarf', 'HEX1', 'HEX2', 'HEX3', 'source', '', '', 'scarfs')")

    # Add data to table
    connection.commit()
    # Close function
    db_cursor.close()
    connection.close()


create_table()
add_data()
