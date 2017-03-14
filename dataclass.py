import gc


class Clothes:
    # Define all categories of clothes
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 description, exclusion, kind):

        self.id = id
        self.name = name
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.photo = photo
        self.description = description
        self.exclusion = exclusion
        self.kind = kind

    # Return basic clothes data id number and name
    def id_and_name(self):
        return 'ID: {} \tName: {}'.format(self.id, self.name)

        # How to use:
        # print(Clothes.id_and_name(red_ts))
        # or
        # print(red_ts.id_and_name())

    # Format of data when call 'repr(name)'
    def __repr__(self):
        return 'Full description: \n' \
               'ID: {}\n' \
               'Name: {}\n' \
               'Colors: {}, {}, {}\n' \
               'Photo: {}\n' \
               'Description: {}\n' \
               'Exclusion: {}\n' \
               'Kind: {}\n'.format(self.id, self.name, self.color_1,
                                   self.color_2, self.color_3, self.photo,
                                   self.description, self.exclusion, self.kind)

    # Change clear
    def change_clear(self):
        if not self.clear:
            self.clear = True
        else:
            self.clear = False

            # How to use:
            # print(red_ts.clear)
            # red_ts.change_clear()
            # print(red_ts.clear)

    # Change data in color_1, color_2, color_3, source, description, exclusion
    # and kind by input text
    def apply_color_1(self):
        new_color_1 = input('Set new color 1: ')
        self.color_1 = new_color_1

    def apply_color2(self):
        new_color_2 = input('Set new color 2: ')
        self.color_2 = new_color_2

    def apply_color3(self):
        new_color_3 = input('Set new color 3: ')
        self.color_3 = new_color_3

    def apply_photo(self):
        new_photo = input('Set new photo source: ')
        self.photo = new_photo

    def apply_description(self):
        new_description = input('Set new description: ')
        self.description = new_description

    def apply_exclusion(self):
        new_exclusion = input('Set new exclusion: ')
        self.exclusion = new_exclusion

    def apply_kind(self):
        new_kind = input('Set new kind: ')
        self.kind = new_kind

    # TODO: Get data from clothesdata.txt
    @classmethod
    def get_data(cls, data):

        # In clothesdata.txt are clothes, ex. of one data item:
        # name = category(1, 'name', 'HEX1', 'HEX2', 'HEX3', 'source',
        #                'True', '', '', 'category')

        with open('clothesdata.txt', 'r') as clothes_data:
            clothes_data_from_file = eval(clothes_data.read())
            cls.clothes_data_from_file = data
        return data


class t_shirts(Clothes):
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 clear, description, exclusion, kind):
        super().__init__(id, name, color_1, color_2, color_3, photo,
                         description, exclusion, kind)
        self.clear = clear


class tank_tops(Clothes):
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 clear, description, exclusion, kind):
        super().__init__(id, name, color_1, color_2, color_3, photo,
                         description, exclusion, kind)
        self.clear = clear


class hoodies(Clothes):
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 clear, description, exclusion, kind):
        super().__init__(id, name, color_1, color_2, color_3, photo,
                         description, exclusion, kind)
        self.clear = clear


class shirts(Clothes):
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 clear, description, exclusion, kind):
        super().__init__(id, name, color_1, color_2, color_3, photo,
                         description, exclusion, kind)
        self.clear = clear


class trousers(Clothes):
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 clear, description, exclusion, kind):
        super().__init__(id, name, color_1, color_2, color_3, photo,
                         description, exclusion, kind)
        self.clear = clear


class shorts(Clothes):
    def __init__(self, id, name, color_1, color_2, color_3, photo,
                 clear, description, exclusion, kind):
        super().__init__(id, name, color_1, color_2, color_3, photo,
                         description, exclusion, kind)
        self.clear = clear


class shoes(Clothes):
    pass


class hats(Clothes):
    pass


class jackets(Clothes):
    pass


class sunglasses(Clothes):
    pass


class necklaces(Clothes):
    pass


class piercing(Clothes):
    pass


class rings(Clothes):
    pass


class bracelets(Clothes):
    pass


class bags(Clothes):
    pass


class gloves(Clothes):
    pass


class scarfs(Clothes):
    pass


# Printing all from class in __repr__ format
def print_all_objects_from_class(class_name):
    for objects in gc.get_objects():
        if isinstance(objects, class_name):
            print(objects)


# Printing all subclasses of Clothes class
def print_all_subclasses():
    list_of_subclasses = ([cls.__name__ for cls in vars()['Clothes'].__subclasses__()])
    print('\n'.join(list_of_subclasses))


# Data
red_ts = t_shirts(1, 'red_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True', '',
                  '', 't_shirts')
dark_red_ts = t_shirts(2, 'dark_red_ts', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 't_shirts')
white_ts = t_shirts(3, 'white_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True',
                    '', '', 't_shirts')
long_white_ts = t_shirts(4, 'long_white_ts', 'HEX1', 'HEX2', 'HEX3', 'source',
                         'True', '', '', 't_shirts')
gray_ts = t_shirts(5, 'gray_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True', '',
                   '', 't_shirts')
neck_gray_ts = t_shirts(6, 'neck_gray_ts', 'HEX1', 'HEX2', 'HEX3', 'source',
                        'True', '', '', 't_shirts')
deer_ts = t_shirts(7, 'deer_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True', '',
                   '', 't_shirts')
mygf_ts = t_shirts(8, 'mygf_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True', '',
                   '', 't_shirts')
gorilla_ts = t_shirts(9, 'gorilla_ts', 'HEX1', 'HEX2', 'HEX3', 'source',
                      'True', '', '', 't_shirts')
astronaut_ts = t_shirts(10, ' astronaut_ts ', 'HEX1', 'HEX2', 'HEX3', 'source',
                        'True', '', '', 't_shirts')
puma_ts = t_shirts(11, 'puma_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True', '',
                   '', 't_shirts')
tiger_ts = t_shirts(12, 'tiger_ts', 'HEX1', 'HEX2', 'HEX3', 'source', 'True',
                    '', '', 't_shirts')
teddy_bear_ts = t_shirts(13, 'teddy_bear_ts', 'HEX1', 'HEX2', 'HEX3', 'source',
                         'True', '', '', 't_shirts')
pitbull_tt = tank_tops(14, 'pitbull_tt', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'tank_tops')
charizard_tt = tank_tops(15, 'charizard_tt', 'HEX1', 'HEX2', 'HEX3', 'source',
                         'True', '', '', 'tank_tops')
light_gray_longsleeve = hoodies(16, 'light_gray_longsleeve', 'HEX1', 'HEX2',
                                'HEX3', 'source', 'True', '', '', 'hoodies')
black_white_longsleeve = hoodies(17, 'black_white_longsleeve', 'HEX1', 'HEX2',
                                 'HEX3', 'source', 'True', '', '', 'hoodies')
gray_longsleeve = hoodies(18, 'gray_longsleeve', 'HEX1', 'HEX2', 'HEX3',
                          'source', 'True', '', '', 'hoodies')
black_monk = hoodies(19, 'black_monk', 'HEX1', 'HEX2', 'HEX3', 'source',
                     'True', '', '', 'hoodies')
gray_hoodie = hoodies(20, 'gray_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source',
                      'True', '', '', 'hoodies')
white_longsleeve = hoodies(21, 'white_longsleeve', 'HEX1', 'HEX2', 'HEX3',
                           'source', 'True', '', '', 'hoodies')
black_longsleeve = hoodies(22, 'black_longsleeve', 'HEX1', 'HEX2', 'HEX3',
                           'source', 'True', '', '', 'hoodies')
brown_hoodie = hoodies(23, 'brown_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'hoodies')
black_ninja_hoodie = hoodies(24, 'black_ninja_hoodie', 'HEX1', 'HEX2', 'HEX3',
                             'source', 'True', '', '', 'hoodies')
black_admirable_hoodie = hoodies(25, 'black_admirable_hoodie', 'HEX1', 'HEX2',
                                 'HEX3', 'source', 'True', '', '', 'hoodies')
black_cropp_hoodie = hoodies(26, 'black_cropp_hoodie', 'HEX1', 'HEX2', 'HEX3',
                             'source', 'True', '', '', 'hoodies')
black_adidas_hoodie = hoodies(27, 'black_adidas_hoodie', 'HEX1', 'HEX2',
                              'HEX3', 'source', 'True', '', '', 'hoodies')
black_long_sweater = hoodies(28, 'black_long_sweater', 'HEX1', 'HEX2', 'HEX3',
                             'source', 'True', '', '', 'hoodies')
light_gray_hoodie = hoodies(29, 'light_gray_hoodie', 'HEX1', 'HEX2', 'HEX3',
                            'source', 'True', '', '', 'hoodies')
gray_sweater = hoodies(30, 'gray_sweater', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'hoodies')
green_long_sweater = hoodies(31, 'green_long_sweater', 'HEX1', 'HEX2', 'HEX3',
                             'source', 'True', '', '', 'hoodies')
raven_hoodie = hoodies(32, 'raven_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'hoodies')
pitbull_hoodie = hoodies(33, 'pitbull_hoodie', 'HEX1', 'HEX2', 'HEX3',
                         'source', 'True', '', '', 'hoodies')
skull_hoodie = hoodies(34, 'skull_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'hoodies')
bear_hoodie = hoodies(35, 'bear_hoodie', 'HEX1', 'HEX2', 'HEX3', 'source',
                      'True', '', '', 'hoodies')
moro = hoodies(36, 'moro', 'HEX1', 'HEX2', 'HEX3', 'source', 'True', '', '',
               'hoodies')
revolution_cat_hoodie = hoodies(37, 'revolution_cat_hoodie', 'HEX1', 'HEX2',
                                'HEX3', 'source', 'True', '', '', 'hoodies')
mountains_baseball = hoodies(38, 'mountains_baseball', 'HEX1', 'HEX2', 'HEX3',
                             'source', 'True', '', '', 'hoodies')
gray_casual_shirt = shirts(39, 'gray_casual_shirt', 'HEX1', 'HEX2', 'HEX3',
                           'source', 'True', '', '', 'shirts')
green_casual_shirt = shirts(40, 'green_casual_shirt', 'HEX1', 'HEX2', 'HEX3',
                            'source', 'True', '', '', 'shirts')
gray_shirt = shirts(41, 'gray_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', 'True',
                    '', '', 'shirts')
blue_shirt = shirts(42, 'blue_shirt', 'HEX1', 'HEX2', 'HEX3', 'source', 'True',
                    '', '', 'shirts')
black_shirt = shirts(43, 'black_shirt', 'HEX1', 'HEX2', 'HEX3', 'source',
                     'True', '', '', 'shirts')
white_shirt = shirts(44, 'white_shirt', 'HEX1', 'HEX2', 'HEX3', 'source',
                     'True', '', '', 'shirts')
black_pants_holes = trousers(45, 'black_pants_holes', 'HEX1', 'HEX2', 'HEX3',
                             'source', 'True', '', '', 'trousers')
blue_pants = trousers(46, 'blue_pants', 'HEX1', 'HEX2', 'HEX3', 'source',
                      'True', '', '', 'trousers')
white_pants = trousers(47, 'white_pants', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'trousers')
gray_loose_pants = trousers(48, 'gray_loose_pants', 'HEX1', 'HEX2', 'HEX3',
                            'source', 'True', '', '', 'trousers')
gray_zip_pants = trousers(49, 'gray_zip_pants', 'HEX1', 'HEX2', 'HEX3',
                          'source', 'True', '', '', 'trousers')
black_pants = trousers(50, 'black_pants', 'HEX1', 'HEX2', 'HEX3', 'source',
                       'True', '', '', 'trousers')
gray_slim_pants = trousers(51, 'gray_slim_pants', 'HEX1', 'HEX2', 'HEX3',
                           'source', 'True', '', '', 'trousers')
red_pants = trousers(52, 'red_pants', 'HEX1', 'HEX2', 'HEX3', 'source', 'True',
                     '', '', 'trousers')
skull_joggers = trousers(53, 'skull_joggers', 'HEX1', 'HEX2', 'HEX3', 'source',
                         'True', '', '', 'trousers')
strokes_joggers = trousers(54, 'strokes_joggers', 'HEX1', 'HEX2', 'HEX3',
                           'source', 'True', '', '', 'trousers')
black_vans = shoes(55, 'black_vans', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                   'shoes')
black_flips = shoes(56, 'black_flips', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                    '', 'shoes')
strokes_sneakers = shoes(57, 'strokes_sneakers', 'HEX1', 'HEX2', 'HEX3',
                         'source', '', '', 'shoes')
brown_shoes = shoes(58, 'brown_shoes', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                    '', 'shoes')
jackboots = shoes(59, 'jackboots', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                  'shoes')
black_airmax = shoes(60, 'black_airmax', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                     '', 'shoes')
black_elastic_sides = shoes(61, 'black_elastic_sides', 'HEX1', 'HEX2', 'HEX3',
                            'source', '', '', 'shoes')
black_snapback = hats(62, 'black_snapback', 'HEX1', 'HEX2', 'HEX3', 'source',
                      '', '', 'hats')
gray_hat = hats(63, 'gray_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                'hats')
city_hat = hats(64, 'city_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                'hats')
panda_hat = hats(65, 'panda_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                 'hats')
strokes_hat = hats(66, 'strokes_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                   'hats')
black_hat = hats(67, 'black_hat', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                 'hats')
black_jacket = jackets(68, 'black_jacket', 'HEX1', 'HEX2', 'HEX3', 'source',
                       '', '', 'jackets')
green_coat = jackets(69, 'green_coat', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                     '', 'jackets')
moro_jacket = jackets(70, 'moro_jacket', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                      '', 'jackets')
silver_sg = sunglasses(71, 'silver_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                       '', 'sunglasses')
gold_sg = sunglasses(72, 'gold_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                     'sunglasses')
black_green_sg = sunglasses(73, 'black_green_sg', 'HEX1', 'HEX2', 'HEX3',
                            'source', '', '', 'sunglasses')
gray_sg = sunglasses(74, 'gray_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                     'sunglasses')
black_sg = sunglasses(75, 'black_sg', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                      'sunglasses')
black_neck = necklaces(76, 'black_neck', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                       '', 'necklaces')
gray_neck = necklaces(77, 'gray_neck', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                      '', 'necklaces')
silver_black_tunnels = piercing(78, 'silver_black_tunnels', 'HEX1', 'HEX2',
                                'HEX3', 'source', '', '', 'piercing')
eye_ring = rings(79, 'eye_ring', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                 'rings')
silver1_ring = rings(80, 'silver1_ring', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                     '', 'rings')
silver2_ring = rings(81, 'silver2_ring', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                     '', 'rings')
brown_bracelet = bags(82, 'bracelets', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                      '', 'bracelets')
black_bag = bags(83, 'black_bag', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                 'bags')
black_backpack = bags(84, 'black_backpack', 'HEX1', 'HEX2', 'HEX3', 'source',
                      '', '', 'bags')
panda_backpack = bags(85, 'panda_backpack', 'HEX1', 'HEX2', 'HEX3', 'source',
                      '', '', 'bags')
strokes_gloves = gloves(86, 'strokes_gloves', 'HEX1', 'HEX2', 'HEX3', 'source',
                        '', '', 'gloves')
black_scarf = scarfs(87, 'black_scarf', 'HEX1', 'HEX2', 'HEX3', 'source', '',
                     '', 'scarfs')
red_scarf = scarfs(88, 'red_scarf', 'HEX1', 'HEX2', 'HEX3', 'source', '', '',
                   'scarfs')

