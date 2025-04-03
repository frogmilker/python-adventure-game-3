import json
import random as rand
rygg_säck = []
class Player:
    def __init__(self, HP, STR, LVL):
        self.HP = HP
        self.STR = STR
        self.LVL = LVL
class Item:
    def __init__(self, name, STR):
        self.name = name
        self.STR = STR
item_1 = Item("yxa", 0)
item_2 = Item("pinne", 0)
item_3 = Item("En riktigt stor sten", 0)
item_4 = Item("Super starkt legendarsikt svärd!!!", 0)
item_5 = Item("Warhammer (40k)", 0)
item_6 = Item("magic wand", 0)
item_7 = Item("Desmos User Guide", 0)
items =[item_1,item_2,  item_3, item_4, item_5, item_6, item_7]

class Monster:
    def __init__(self, name, HP, STR):
        self.name = name
        self.HP = HP
        self.STR = STR
monster_1 = Monster("John the all knowing", 0, 0)
monster_2 = Monster("Nikodemus, manipulator of numbers", 0, 0)
monster_3 = Monster("Alexander, vanguard of vigor", 0, 0)
monster_4 = Monster("Charles the electromagnetic", 0, 0)
monster_5 = Monster("Johanna, brewer of potions", 0, 0)
monster_6 = Monster("Paul the fool", 0, 0)
monster_7 = Monster("Andreas, wielder of gears", 0, 0)
monster_8 = Monster("Maria the genocidal", 0, 0)
monster_9 = Monster("Aitor, speaker of tongues", 0, 0)
monster_10 = Monster("Katarina, imposer of gluttony", 0, 0)
monster_11 = Monster("Walter the goblin", 0, 0)
monster_12 = Monster("Adam the ogre", 0, 0)
monster_13 = Monster("Love, enjoyer of brew", 0, 0)
monsters = [monster_1, monster_2, monster_3, monster_4, monster_5, monster_6, monster_7, monster_8, monster_9, monster_10, monster_11, monster_12, monster_13]

class Trap:
    def __init__(self, name, STR):
        self.name = name
        self.STR = STR
trap_1 = Trap("banana peel", 0)
trap_2 = Trap("", 0)
trap_3 = Trap("", 0)
trap_4 = Trap("", 0)
trap_5 = Trap("", 0)
trap_6 = Trap("", 0)
gamer = Player(10 , 10 , 1)
händelser = ["kista", "monster", "fälla"]
def ägodelar(a):
    for i in range(len(a)):
        print(a[i].name)
def chest():
    print("Du hittade en kista!!! DU FÅR ETT GRATTIS ITEM!!!")
    vinst = rand.choice(items)
    rygg_säck.append(vinst)
    print(f"Du fick en {vinst.name} \ndu har nu")
    print(f"{ägodelar(rygg_säck)}")

def new_hp_trap(a):
    gamer.HP = a-1
def påminelse(lst):
    for i in range(len(lst)):
        print(f"{lst[i].name} har styrka {lst[i].STR}")
        total_strength += lst[i].STR
    print(f"Totalt är det {total_strength}")
def self_reflektion():
    print(f"Du har{gamer.HP} i helath points, du har {gamer.STR} och du är nivå {gamer.LVL}") 
def spel():
    while gamer.HP > 0:
        val = input("Vad vill du göra? \nvill du \nÖppna ryggsäck 1.\nSe dinna egenskaper 2.\nVälja en dörr.3")
        if val.lower == "dörr" or val == 3:
            dörr()
        if val.lower == "egenskaper" or val == 2:
            self_reflektion()
        if val.lower == "ryggsäck" or val.lower =="öpnna ryggsäck" or val == 1:
            påminelse(rygg_säck)
def dörr():
    val = input(f"Du ser tre dörrar framför mig: \nDörr 1: \nDörr 2: \nDörr 3:")
    action = "monster"
    if action == "kista":
        chest()
    if action == "monster":
        new_hp(gamer.HP)
        print(gamer.HP)
    if action == "fälla":
        new_hp_trap(gamer.HP)