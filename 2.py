import math
from datetime import date


class House:
    street = 'Ленина'

    def __init__(self, address=0, id=0, number=0, floor=0, number_of_rooms=0, type_of_building=None):
        super().__init__()
        self.address = address
        self.__id = id
        self.__number = number
        self.__floor = floor
        self.__number_of_rooms = number_of_rooms
        self.square = 55.36
        self.service_life = 50
        self.service_life_industrial_buildings = 1.5
        self.type_of_building = type_of_building

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_number(self, number):
        try:
            self.__number = int(number)
        except ValueError:
            print('Неправильно указан номер квартиры')
            exit(0)

    def get_number(self):
        return self.__number

    def set_floor(self, floor):
        try:
            self.__floor = int(floor)
        except ValueError:
            print('Неправильно указан номер этажа')
            exit(0)

    def get_floor(self):
        return self.__floor

    def set_number_of_rooms(self, number_of_rooms):
        try:
            self.__number_of_rooms = int(number_of_rooms)
        except ValueError:
            print('Неправильно указано количество комнат в квартире')
            exit(0)

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    table_flats_with_rooms = []

    def add_flats_with_rooms(self, flats_with_rooms):
        self.table_flats_with_rooms.append(flats_with_rooms)

        print('-------------------------------------------------------------------------------------------')
        specified_number_of_rooms = int(input('Список квартир с каким числом комнат вы бы хотели посмотреть?'))

        print('Список квартир, имеющих заданное число комнат:')
        print('-------------------------------------------------------------------------------------------')
        print('ID квартиры', ' Номер квартиры')

        for flat_with_room in flats_with_rooms:
            if flat_with_room['Число комнат'] == specified_number_of_rooms:
                print(flat_with_room['ID квартиры'], '\t\t\t', flat_with_room['Номер квартиры'])

    table_flats_on_floors = []

    def add_flats_on_floors(self, flat_on_floors):
        self.table_flats_on_floors.append(flat_on_floors)

        print('-------------------------------------------------------------------------------------------')
        print(
            'Введите  параметры список квартира, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке:')
        number_of_rooms_on_floor = int(input('Число комнат:'))
        first_floor = int(input('номер этажа с которого начинается список:'))
        last_floor = int(input('Номер этажа с которого заканвается список:'))

        print('Список квартир, имеющих', number_of_rooms_on_floor, 'комнату(ы) и расположенные на этaжах c',
              first_floor, 'по', last_floor)
        print('-------------------------------------------------------------------------------------------')
        print('ID квартиры', ' Номер квартиры')

        for flat_on_floor in flat_on_floors:
            if number_of_rooms_on_floor == flat_on_floor['Число комнат'] and first_floor <= flat_on_floor[
                'Этаж'] <= last_floor:
                print(flat_on_floor['ID квартиры'], '\t\t\t', flat_on_floor['Номер квартиры'])

    # Увеличиваем срок эксплуатации промышленных зданий до кап. ремонта с 50  до 75 лет:

    def __getattribute__(self, item):
        if item == "service_life":
            sr = super().__getattribute__('service_life')
            srib = super().__getattribute__('service_life_industrial_buildings')
            return sr * srib
        return super().__getattribute__(item)

   #Округляем полщадь до целого чила:

    def __ceil__(self):
        square_value = int(self.square)
        if square_value < self.square:
            return square_value + 1
        return square_value


    # Проверяем корректность ввода номера дома:

    def __setattr__(self, key, value):
        if key == 'address':
            try:
                int(value)
            except ValueError:
                print('Неправильно указан номер дома')
                exit(0)
        return super().__setattr__(key, value)

    # Указываем сколько лет можно эксплуатировать промышленные или гражданские здания:

    def __str__(self):
        return f'Срок эксплуатации {self.service_life} лет для промышленных зданий, а для гражданских - 50'


    # Сигнализируем об истекшем сроке эксплуатации здания:

    def __getattr__(self, name):
        return 'Истекший срок эксплуатации здания!!!'


    @staticmethod
    def calculate_age_of_builder(service_life, age_of_building_for_repair):
        return age_of_building_for_repair - service_life

    @classmethod
    def determine_age_building(cls):
        age_house = int(input('Введите год постройки задания(дома):'))
        print('Введите тип здания, если промышленное (p - латинская), если  гражданское (g)')
        houses.type_of_building = input()
        count_years = date.today().year - age_house

        if houses.type_of_building == 'p' or houses.type_of_building == 'P':
            result = cls.calculate_age_of_builder(count_years, houses.service_life)
            return result
        elif houses.type_of_building == 'g' or houses.type_of_building == 'G':
            result = cls.calculate_age_of_builder(count_years, 50)
            houses.type_of_building = 'гражданское'
            return result
        else:
            print('Нет токого типа здания')
            exit(0)


houses = House(1, 2, 3, 4, 5, 6)

print('Введите номер дома на улице', House.street, ': ')
houses.address = input()

print('Введите количество квартир в доме №', houses.address, ', на улице', House.street, ': ')
n = int(input())

houses.house_list = []
for i in range(0, n):
    houses.set_id(i + 1)
    id_flat = houses.get_id()

    print('Введите номер', (i + 1), 'квартиры из', n, 'квартир')
    houses.set_number(input())
    number_flat = houses.get_number()

    print('Введите этаж, где находится квартира №', number_flat)
    houses.set_floor(input())
    floor_of_flat = int(houses.get_floor())

    print('Введите количество комнат в квартире №', number_flat)
    houses.set_number_of_rooms(input())
    number_of_rooms_in_flat = houses.get_number_of_rooms()

    houses.house_list.append({'ID квартиры': id_flat,
                              'Номер квартиры': number_flat,
                              'Площадь квартиры': math.ceil(houses.square),
                              'Этаж': floor_of_flat,
                              'Число комнат': number_of_rooms_in_flat
                              })
    if id_flat == n:
        print('-------------------------------------------------------------------------------------------')
        print(str(houses))
        print('-------------------------------------------------------------------------------------------')

        age = House.determine_age_building()

        print('-------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------')

        if age > 1:
            print('До кап. ремонта дома №', houses.address, ', по улице', House.street, ' осталась', age, 'лет(года)')
        elif age == 1:
            print('До кап. ремонта дома №', houses.address, ', по улице', House.street, ' остался', age, 'год')
        elif age < 0:
            print(houses.expired_service_life)
            print('Кап. ремонт дома №', houses.address, ', по улице', House.street, 'нужно уже делать')

        print('-------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------')

        print('Дом №', houses.address, ', по улеце', House.street, '. Тип здания', houses.type_of_building, '.')
        for flat in houses.house_list:
            print('ID квартиры', ' Номер квартиры', ' Площадь квартиры  ', ' Номер этажа  ', '  Число комнат')
            print(flat['ID квартиры'], '\t\t\t', flat['Номер квартиры'], '\t\t\t\t', flat['Площадь квартиры'],
                  '\t\t\t\t', flat['Этаж'], '\t\t\t\t', flat['Число комнат'])
            print('-------------------------------------------------------------------------------------------')
        houses.add_flats_with_rooms(houses.house_list)
        houses.add_flats_on_floors(houses.house_list)
