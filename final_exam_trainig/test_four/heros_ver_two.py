def cast_spell(name, mana, spell):
    if heroes[name][1] >= mana:
        heroes[name][1] -= mana
        print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")


def take_damage(name, health, enemy):
    heroes[name][0] -= health
    if heroes[name][0] > 0:
        print(f"{name} was hit for {health} HP by {enemy} and now has {heroes[name][0]} HP left!")
    else:
        del heroes[name]
        print(f"{name} has been killed by {enemy}!")


def recharge(name, mana_points):
    charge = heroes[name][1] + mana_points
    if charge > MAX_MANA:
        recharged = MAX_MANA - heroes[name][1]
        heroes[name][1] = MAX_MANA
        print(f"{name} recharged for {recharged} MP!")
    else:
        print(f"{name} recharged for {mana_points} MP!")
        heroes[name][1] += mana_points


def heal(name, health):
    charge = heroes[name][0] + health
    if charge > MAX_HP:
        recharged = MAX_HP - heroes[name][0]
        heroes[name][0] = MAX_HP
        print(f"{name} healed for {recharged} HP!")
    else:
        print(f"{name} healed for {health} HP!")
        heroes[name][0] += health


MAX_HP = 100
MAX_MANA = 200

number = int(input())

heroes = {}
for _ in range(number):
    hero, hp, mp = input().split()
    if hero not in heroes:
        heroes[hero] = []
    heroes[hero].append(int(hp))
    heroes[hero].append(int(mp))

command = input()

while command != "End":
    command = command.split(" - ")
    hero_name = command[1]

    if command[0] == "CastSpell":
        mp_req = int(command[2])
        spell_name = command[3]
        cast_spell(hero_name, mp_req, spell_name)

    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        take_damage(hero_name, damage, attacker)

    elif command[0] == "Recharge":
        mana = int(command[2])
        recharge(hero_name, mana)

    elif command[0] == "Heal":
        health = int(command[2])
        heal(hero_name, health)

    command = input()

for hero, values in heroes.items():
    hp = values[0]
    mp = values[1]
    print(hero)
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")
