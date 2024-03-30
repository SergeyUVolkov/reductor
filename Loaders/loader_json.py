# -*- coding: utf-8 -*-

import json
from Product.brand import Brand
from Product.model import Model
from Product.product import Product
from Product.device_type import DeviceType
from Product.group_type import GroupType

brand = Brand()
model = Model()
product = Product()
device_type = DeviceType()
group_type = GroupType()


def loader_file():
    """
    Загрузка данных из json файла
    """
    with open('файл.json', 'r', encoding='utf-8') as product_file:
        product_data = json.load(product_file)

    product_flag = {'device_type': {'prom': ['Сплит-системы полупромышленные', 'Сплит-система напольно-потолочная',
                                             'сплит-система кассетного типа'],
                                    'home': ['Бытовые сплит-системы', 'Сплит-система'],
                                    'invertor': ['Бытовые инверторные сплит-системы', 'Сплит-система инверторная'],
                                    'multi': ['Мульти сплит-системы с инверторным управлением',
                                              'инверторной мульти сплит-системы']},
                    'brand': ['ballu', 'zanussi', 'royal clima', 'royal thermo', 'newtek', 'ac electric',
                              'electrolux'],
                    'zanussi': ['barocco', 'perfecto', 'siena', 'barocco dc inverter 2.0', 'milano dc',
                                'siena dc inverter', 'multi combo'],
                    'ballu': ['lagoon', 'free match'],
                    'royal thermo': ['barocco', 'barocco dc white', 'siena dc'],
                    'newtek': ['beige glass', 'black glass'],
                    'royal clima': ['vela nuova', 'gloria inverter'],
                    'ac electric': ['pro']
                    }
    print('Началась загрузка данных из json файла.')

    for item in product_data['ВаловаяПрибыль']:
        # print(item['Организация'])
        # print(item['Склад'])
        # print(item['Родитель'])  # тип оборудования
        # print(item['Номенклатура'])  # Brand / model / вид оборуд / тип оборудования
        # print(item['Количество'])
        # print(item['Цена'])
        # print('--------------------------')

        model_id = 0
        brand_id = 0
        brand.insert(brand_name='no_Brand')
        group_type.insert(group_devices_type_name='no_group_type')
        device_type.insert(device_type_name='no_type')
        full_name_product = ''

        for item_brand in product_flag['brand']:
            brand_id = brand.select_id(brand_name='no_Brand')[0]

            model.insert(model_name='no_Model', brand_id=brand_id)
            model_id = model.select_id(model_name='no_Model', brand_id=brand_id)[0][0]

            item_brand = item_brand.lower()
            full_name_product = item['Номенклатура']
            if item_brand in item['Номенклатура'].lower():  # В названии найден Бренд
                brand.insert(brand_name=item_brand)
                brand_id = brand.select_id(brand_name=item_brand)[0]
                item['Номенклатура'] = drop_template(original_string=item['Номенклатура'],
                                                     template=item_brand)

                # Проверить существование индекса по бренду в product_flag
                if item_brand in product_flag:
                    for item_model in product_flag[item_brand]:
                        if item_model.lower() in item['Номенклатура'].lower():
                            model.insert(model_name=item_model, brand_id=brand_id)
                            model_id = model.select_id(model_name=item_model, brand_id=brand_id)[0][0]
                            item['Номенклатура'] = drop_template(original_string=item['Номенклатура'],
                                                                 template=item_model)

                    break  # Прерываем FOR для Бренда

        group_devices_type = group_type.select_id(group_devices_type_name='no_group_type')[0]
        device_type_id = device_type.select_id(device_type_name='no_type')[0]

        for item_group_type in product_flag['device_type']:
            for group_type_name in product_flag['device_type'][item_group_type]:
                group_type_name = group_type_name.lower()
                if group_type_name in item['Родитель'].lower():
                    group_type.insert(group_devices_type_name=group_type_name)
                    group_devices_type = group_type.select_id(group_devices_type_name=group_type_name)[0]

                    device_type_id = device_type.select_id(device_type_name='no_type')[0]

                    for device_type_name in product_flag['device_type'][item_group_type]:
                        if device_type_name.lower() in item['Номенклатура']:
                            item['Номенклатура'] = drop_template(original_string=item['Номенклатура'],
                                                                 template=device_type_name)
                            device_type.insert(device_type_name=device_type_name)
                            device_type_id = device_type.select_id(device_type_name=device_type_name)[0]
                            break
                    break

        # Сохраняем продукт
        if brand_id != 0 and model_id != 0 and group_devices_type != 0 and device_type_id != 0:
            product.insert(product_name=item['Номенклатура'],
                           full_name=full_name_product,
                           brand_id=brand_id,
                           model_id=model_id,
                           device_type_id=device_type_id,
                           group_devices_type_id=group_devices_type)
            product_id = product.select_product(
                product_name=item['Номенклатура'],
                brand_id=brand_id,
                model_id=model_id,
                device_type_id=device_type_id,
                group_devices_type_id=group_devices_type)[0][0]
            if item['Количество'] == '':
                item['Количество'] = '0'
            if item['Цена'] == '':
                item['Цена'] = '0.0'
            product.update_stock(product_id=product_id, stock=int(item['Количество']),
                                 price=float(item['Цена'].replace(',', '.')))

    print('Закончилась загрузка.')


def drop_template(original_string: str, template: str):
    """
    Удаление из исходной строки образец
    :param original_string:
    :param template:
    :return: Строка после очистки.
    """
    # S.strip([chars]) удаление пробелов в начале и конце строки
    original_string = original_string.strip()

    # S.lower() преобразование к нижнему регистру
    original_string = original_string.lower()
    template = template.replace('  ', ' ')
    template = template.strip()
    template = template.lower()

    # S.replace(шаблон, замена[, maxcount]) Замена шаблона в исходной строке.
    # Заменяем все пробелы на один пробел.
    original_string = original_string.replace('  ', ' ')

    # len(S) Длина строки
    # S.find(str, [start], [end]) поиск подстроки
    if original_string.find(template) != -1:
        # S.replace(шаблон, замена[, maxcount]) Замена шаблона в исходной строке
        original_string = original_string.replace(template, '')
        original_string = original_string.replace('  ', ' ')
        original_string = original_string.strip()
    return original_string


if __name__ == '__main__':
    loader_file()
    # in_str1 = 'Блок внешний BALLU BA2OI-FM/out-18HN8/EU инверторной мульти сплит-системы Free Match'
    # in_str2 = 'Мульти сплит-системы с инверторным управлением'
    # print(drop_template(original_string=in_str1, template='Ballu'))
