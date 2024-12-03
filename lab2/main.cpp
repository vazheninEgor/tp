#include <iostream>
#include <string>
#include <windows.h>


// Интерфейсы
class Attacker {
public:
    virtual void attack(class Unit* unit) = 0; // Атаковать юнита
    virtual ~Attacker() = default;
};

class Moveable {
public:
    virtual void move(int x, int y) = 0; // Переместить объект
    virtual ~Moveable() = default;
};

// Базовый класс GameObject
class GameObject {
private:
    int id;
    std::string name;
    int x, y;

public:
    GameObject(int id, const std::string& name, int x, int y) : id(id), name(name), x(x), y(y) {}

    int getId() const { return id; }
    std::string getName() const { return name; }
    int getX() const { return x; }
    int getY() const { return y; }

    virtual ~GameObject() = default;
};

// Класс Unit
class Unit : public GameObject {
private:
    float hp;

public:
    Unit(int id, const std::string& name, int x, int y, float hp)
            : GameObject(id, name, x, y), hp(hp) {}

    bool isAlive() const { return hp > 0; }
    float getHp() const { return hp; }

    void receiveDamage(float damage) {
        hp -= damage;
        if (hp < 0) hp = 0;
    }

    virtual ~Unit() = default;
};

// Класс Archer
class Archer : public Unit, public Attacker, public Moveable {
public:
    Archer(int id, const std::string& name, int x, int y, float hp)
            : Unit(id, name, x, y, hp) {}

    void attack(Unit* unit) override {
        if (unit->isAlive()) {
            std::cout << getName() << " атакует " << unit->getName() << " на 10 урона.\n";
            unit->receiveDamage(10);
        }
    }

    void move(int x, int y) override {
        std::cout << getName() << " перемещается в (" << x << ", " << y << ").\n";
    }
};

// Класс Building
class Building : public GameObject {
private:
    bool built;

public:
    Building(int id, const std::string& name, int x, int y, bool built)
            : GameObject(id, name, x, y), built(built) {}

    bool isBuilt() const { return built; }

    virtual ~Building() = default;
};

// Класс Fort
class Fort : public Building, public Attacker {
public:
    Fort(int id, const std::string& name, int x, int y, bool built)
            : Building(id, name, x, y, built) {}

    void attack(Unit* unit) override {
        if (isBuilt() && unit->isAlive()) {
            std::cout << getName() << " атакует " << unit->getName() << " на 20 урона.\n";
            unit->receiveDamage(20);
        }
    }
};

// Класс MobileHome
class MobileHome : public Building, public Moveable {
public:
    MobileHome(int id, const std::string& name, int x, int y, bool built)
            : Building(id, name, x, y, built) {}

    void move(int x, int y) override {
        std::cout << getName() << " перемещается в (" << x << ", " << y << ").\n";
    }
};

// Главная функция
int main() {
    SetConsoleOutputCP(CP_UTF8);

    Archer archer(1, "Лучник", 0, 0, 100);
    Fort fort(2, "Крепость", 5, 5, true);
    MobileHome mobileHome(3, "Дом на колесах", 10, 10, true);

    std::cout << "Здоровье лучника: " << archer.getHp() << "\n";
    archer.move(2, 3);
    fort.attack(&archer);

    std::cout << "Здоровье лучника после атаки крепости: " << archer.getHp() << "\n";
    mobileHome.move(15, 15);

    return 0;
}

