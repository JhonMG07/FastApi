edad: int = 0
name: str = "Jhon"
surname: str = "Meza"
age: int = 21

# example format
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Una tupla no es editable y una lista si
# Un set no es una estructura ordenada, no tiene posiciones
# y tampoco no admiten repetidos

# en los diccionarios se busca por clave, no por valor "key": value

# condicionales
my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")


my_string = ""  # esto equivale a falso -> ya que no tiene caracteres
if not my_string:  # pregunta si mi cadena es vacia
    print("Mi cadena de texto es vacía")
else:
    print("Tiene caracteres")

# bucles/ciclos


# clases
class Person:
    # constructor
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname


my_person = Person("Jhon", "Meza")

print(f"Mi nombre es: {my_person.get_name()}")
print(f"Mi apellido es: {my_person.get_surname()}")

my_person.set_name("new name")
print(f"Mi nombre es: {my_person.get_name()}")
