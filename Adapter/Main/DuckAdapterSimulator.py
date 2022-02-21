from Adapter.Models.MallardDuck import MallardDuck
from Adapter.Models.WildTurkey import WildTurkey
from Adapter.Models.SuperDrone import SuperDrone
from Adapter.Models.TurkeyAdapter import TurkeyAdapter
from Adapter.Models.DroneAdapter import DroneAdapter


def main():
    print("--- Duck ---")
    duck = MallardDuck()
    test_duck(duck)

    print("--- Turkey ---")
    turkey_adapter = TurkeyAdapter(WildTurkey())
    test_duck(turkey_adapter)

    print("--- Drone ---")
    drone_adapter = DroneAdapter(SuperDrone())
    test_duck(drone_adapter)


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    main()
