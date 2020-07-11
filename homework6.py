class Animals:            # общий класс животных
    feed = 'голодный'
    voices = 'Какой звук?'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # грамм

    def food(self):
        self.feed = 'накормлен'

    def animal_sound(self, sound):
        self.voices = sound


class CowAndGoat(Animals):  # класс коровы и козы
    milk = 'молоко недоено'

    def dairy_cattle(self):
        self.milk = 'молоко надоено'


class Sheep(Animals):   # класс овцы
    cut = 'не стриженный'

    def cut_sheep(self):
        self.cut = 'стриженный'


class Birds(Animals):   # класс птицы
    eggs = 'яйца не собраны'

    def collect_eggs(self):
        self.eggs = 'яйца собраны'

# гусь "Серый"
goose1 = Birds('"Серый"', 3100)
goose1.food()
goose1.animal_sound('Га-га-га')
goose1.collect_eggs()
print('Гусь:', goose1.name)
print('Вес:', goose1.weight, 'г.')
print('Звук:', goose1.voices)
print(goose1.feed)
print(goose1.eggs)
print()

# гусь "Белый"
goose2 = Birds('"Белый"', 2900)
goose2.food()
goose2.animal_sound('Га-га-га')
goose2.collect_eggs()
print('Гусь:', goose2.name)
print('Вес:', goose2.weight, 'г.')
print('Звук:', goose2.voices)
print(goose2.feed)
print(goose2.eggs)
print()

# корова "Манька"
cow = CowAndGoat('"Манька"', 700000)
cow.food()
cow.animal_sound('Му-му')
cow.dairy_cattle()
print('Корова:', cow.name)
print('Вес:', cow.weight, 'г.')
print('Звук:', cow.voices)
print(cow.feed)
print(cow.milk)
print()

# овца "Барашек"
sheep1 = Sheep('"Барашек"', 50000)
sheep1.food()
sheep1.animal_sound('Бе-бе')
sheep1.cut_sheep()
print('Овца:', sheep1.name)
print('Вес:', sheep1.weight, 'г.')
print('Звук:', sheep1.voices)
print(sheep1.feed)
print(sheep1.cut)
print()

# овца "Кудрявый"
sheep2 = Sheep('"Кудрявый"', 60000)
sheep2.food()
sheep2.animal_sound('Бе-бе')
sheep2.cut_sheep()
print('Овца:', sheep2.name)
print('Вес:', sheep2.weight, 'г.')
print('Звук:', sheep2.voices)
print(sheep2.feed)
print(sheep2.cut)
print()

# курица "Ко-Ко"
chicken1 = Birds('"Ко-Ко"', 800)
chicken1.food()
chicken1.animal_sound('Ку-ка-ре-ку')
chicken1.collect_eggs()
print('Курица:', chicken1.name)
print('Вес:', chicken1.weight, 'г.')
print('Звук:', chicken1.voices)
print(chicken1.feed)
print(chicken1.eggs)
print()

# курица "Кукареку"
chicken2 = Birds('"Кукареку"', 700)
chicken2.food()
chicken2.animal_sound('Ку-ка-ре-ку')
chicken2.collect_eggs()
print('Курица:', chicken2.name)
print('Вес:', chicken2.weight, 'г.')
print('Звук:', chicken2.voices)
print(chicken2.feed)
print(chicken2.eggs)
print()

# коза "Рога"
goat1 = CowAndGoat('"Рога"', 40000)
goat1.food()
goat1.animal_sound('Ме-е-е-е')
goat1.dairy_cattle()
print('Коза:', goat1.name)
print('Вес:', goat1.weight, 'г.')
print('Звук:', goat1.voices)
print(goat1.feed)
print(goat1.milk)
print()

# коза "Копыта"
goat2 = CowAndGoat('"Копыта"', 60000)
goat2.food()
goat2.animal_sound('Ме-е-е-е')
goat2.dairy_cattle()
print('Коза:', goat2.name)
print('Вес:', goat2.weight, 'г.')
print('Звук:', goat2.voices)
print(goat2.feed)
print(goat2.milk)
print()

# утка "Кряква"
duck = Birds('"Кряква"', 2500)
duck.food()
duck.animal_sound('Кря-кря-кря')
duck.collect_eggs()
print('Коза:', duck.name)
print('Вес:', duck.weight, 'г.')
print('Звук:', duck.voices)
print(duck.feed)
print(duck.eggs)
print()

all_animal_weight = [goose1.weight, goose2.weight, cow.weight, sheep1.weight, sheep2.weight, chicken1.weight, chicken2.weight, goat1.weight, goat2.weight, duck.weight]
print(f'Общий вес всех животных: {sum(all_animal_weight)} грамм')
print(f'Вес самого тяжелого животного: {max(all_animal_weight)} грамм')

