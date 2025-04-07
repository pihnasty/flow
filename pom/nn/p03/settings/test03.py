class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Класс Dog наследует от класса Animal и добавляет новое необязательное поле "breed"
class Dog(Animal):
    def __init__(self, species, breed=None):
        # Вызываем конструктор родительского класса с помощью super()
        super().__init__(species)
        # Добавляем новое необязательное поле с значением по умолчанию None
        self.breed = breed

    # Дополнительный метод для класса Dog
    def bark(self):
        print("Woof!")

# Создаем объекты классов
generic_animal = Animal("Generic")
dog_without_breed = Dog("Canine")
dog_with_breed = Dog("Canine", "Labrador")

# Выводим значения полей
print("Generic Animal - Species:", generic_animal.species)
print("Dog without breed - Species:", dog_without_breed.species, "Breed:", dog_without_breed.breed)
print("Dog with breed - Species:", dog_with_breed.species, "Breed:", dog_with_breed.breed)

# Вызываем методы
dog_with_breed.make_sound()  # Метод унаследован от Animal
dog_with_breed.bark()        # Метод, добавленный в Dog
