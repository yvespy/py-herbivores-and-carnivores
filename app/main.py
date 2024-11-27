class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden:
                 bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore):
            if not prey.hidden:
                prey.health -= 50

            if prey.health <= 0:
                Animal.alive.remove(prey)
