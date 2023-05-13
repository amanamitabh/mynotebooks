#COMBAT SYSTEM USING CLASSES AND OBJECTS

import random

# HIa
#CLASS CREATION

class Weapon:
  def __init__(self, name, damage, accuracy):
    self.name = name
    self.damage = damage
    self.accuracy = accuracy
  
  def get_weapon_name(self):
    return self.name

  def get_weapon_damage(self):
    return self.damage

  def get_weapon_accuracy(self):
    return self.accuracy
  
  def user_attack(self):
    rng = random.randint(1,100)
    if rng <= self.accuracy:
      return self.damage

    else:
      return 0
  

class Enemy:
  def __init__(self, name, hp, damage, accuracy):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.accuracy = accuracy

  def get_enemy_name(self):
    return self.name

  def get_enemy_hp(self):
    return self.hp

  def get_enemy_damage(self):
    return self.damage

  def get_enemy_accuracy(self):
    return self.accuracy

  def enemy_attack(self):
    rng = random.randint(1,100)
    if rng <= self.accuracy:
      if rng <= 5:
        dmg = int(self.damage * 1.5 + random.randint(1,5))
      
      else:
        dmg = int(self.damage + random.randint(1,5))

      return dmg

    else:
      return 0


#WEAPONS

longsword = Weapon("Longsword", 90, 95)
mace = Weapon("Mace", 120, 70)
weapons_list = [longsword, mace]


#ENEMIES

babywyvern = Enemy("Baby Wyvern", 350, 15, 90)
ogre = Enemy("Ogre", 400, 50, 60)
enemies_list = [babywyvern, ogre]



#FUNCTIONS

def weapon_picker(weapons_list):
  n = 1
  print("Choose a weapon from the armory - ")
  for i in weapons_list:
    print(f"{n}. {i.get_weapon_name()}")
    n += 1
  weaponnum = int(input("What do you choose? - "))
  pickedweapon = weapons_list[weaponnum - 1]
  print(f"You have picked the {pickedweapon.get_weapon_name()}\n")
  return pickedweapon


def enemy_picker(enemies_list):
  n = 1
  print("Choose an enemy you want to fight - ")
  for i in enemies_list:
    print(f"{n}. {i.get_enemy_name()}")
    n += 1
  enemynum = int(input("What do you choose? - "))
  pickedenemy = enemies_list[enemynum - 1]
  print(f"You will face the {pickedenemy.get_enemy_name()}\n")
  return pickedenemy


def battle_main():

  picked_weapon = weapon_picker(weapons_list)
  weapon_name = picked_weapon.get_weapon_name()


  picked_enemy = enemy_picker(enemies_list)
  enemy_name = picked_enemy.get_enemy_name()
  enemy_hp = picked_enemy.get_enemy_hp()
  player_hp = 100

  battle_status = True
  print("--------------------------FIGHT--------------------------\n")
  print(f"Player HP: {player_hp}")
  while battle_status:
    
    print(f"{enemy_name} HP: {enemy_hp}")
    test = input()
    enemy_attack_damage = picked_enemy.enemy_attack()
    if enemy_attack_damage == 0:
      print(f"The {enemy_name}'s attack missed.\n")
    
    else:
      print(f"The {enemy_name} did {enemy_attack_damage} damage to you.!\n")
    player_hp -= enemy_attack_damage
    if player_hp <= 0:
      player_hp = 0
      print(f"Player HP:{player_hp}")
      print("You died")
      battle_status = False

    else:
      print(f"Player HP: {player_hp}")

  


battle_main()
