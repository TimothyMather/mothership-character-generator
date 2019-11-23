import os
import csv
import random
from character import Character


def fill_csv(writer, character):
    # 0 name
    writer.writerow(['1', 'Level', character.level])
    # 2 rank/title
    # 3 stress
    # 4 resolve
    writer.writerow(['5', 'Max Health', character.max_health])
    writer.writerow(['6', 'Strength Score', character.strength])
    writer.writerow(['7', 'Speed Score', character.speed])
    writer.writerow(['8', 'Intellect Score', character.intellect])
    writer.writerow(['9', 'Combat Score', character.combat])
    # 10 is image
    writer.writerow(['11', 'Biology Skill', character.skills['biology']])
    writer.writerow(['12', 'First Aid Skill', character.skills['first_aid']])
    writer.writerow(['13', 'Hydroponics Skill',
                     character.skills['hydroponics']])
    writer.writerow(['14', 'Geology Skill', character.skills['geology']])
    writer.writerow(['15', 'Zero-G Skill', character.skills['zero_g']])
    writer.writerow(['16', 'Scavenging Skill', character.skills['scavenging']])
    writer.writerow(['17', 'Heavy Machinery Skill',
                     character.skills['heavy_machinery']])
    writer.writerow(['18', 'Computers Skill', character.skills['computers']])
    writer.writerow(['19', 'Mechanical Repair Skill',
                     character.skills['mechanical_repair']])
    writer.writerow(['20', 'Driving Skill', character.skills['driving']])
    writer.writerow(['21', 'Theology Skill', character.skills['theology']])
    writer.writerow(['22', 'Archaeology Skill',
                     character.skills['archeology']])
    writer.writerow(['23', 'Art Skill', character.skills['art']])
    writer.writerow(['24', 'Mathematics Skill',
                     character.skills['mathematics']])
    writer.writerow(['25', 'Piloting Skill', character.skills['piloting']])
    writer.writerow(['26', 'Chemistry Skill', character.skills['chemistry']])
    writer.writerow(['27', 'Athletics Skill', character.skills['athletics']])
    writer.writerow(['28', 'Rimwise Skill', character.skills['rimwise']])
    writer.writerow(['29', 'Military Training Skill',
                     character.skills['military_training']])
    writer.writerow(['30', 'Psychology Skill', character.skills['psychology']])
    writer.writerow(['31', 'Genetics Skill', character.skills['genetics']])
    writer.writerow(['32', 'Pathology Skill', character.skills['pathology']])
    writer.writerow(['33', 'Botany Skill', character.skills['botany']])
    writer.writerow(['34', 'Planetology Skill',
                     character.skills['planetology']])
    writer.writerow(['35', 'Asteroid Mining Skill',
                     character.skills['asteroid_mining']])
    writer.writerow(['36', 'Jury Rigging Skill',
                     character.skills['jury_rigging']])
    writer.writerow(['37', 'Engineering Skill',
                     character.skills['engineering']])
    writer.writerow(['38', 'Hacking Skill', character.skills['hacking']])
    writer.writerow(['39', 'Vehicle Specialization Skill',
                     character.skills['vehicle_specialization']])
    writer.writerow(['40', 'Tactics Skill', character.skills['tactics']])
    writer.writerow(['41', 'Mysticism Skill', character.skills['mysticism']])
    writer.writerow(['42', 'Physics Skill', character.skills['physics']])
    writer.writerow(['43', 'Astrogation Skill',
                     character.skills['astrogation']])
    writer.writerow(['44', 'Gunnery Skill', character.skills['gunnery']])
    writer.writerow(['45', 'Firearms Skill', character.skills['firearms']])
    writer.writerow(
        ['46', 'Close-Quarters Combat Skill', character.skills['cqc']])
    writer.writerow(['47', 'Explosives Skill', character.skills['explosives']])
    writer.writerow(['48', 'Sophontology Skill',
                     character.skills['sophontology']])
    writer.writerow(['49', 'Xenobiology Skill',
                     character.skills['xenobiology']])
    writer.writerow(['50', 'Command Skill', character.skills['command']])
    writer.writerow(
        ['51', 'Artificial Intelligence Skill', character.skills['ai']])
    writer.writerow(['52', 'Robotics Skill', character.skills['robotics']])
    writer.writerow(['53', 'Cybernetics Skill',
                     character.skills['cybernetics']])
    writer.writerow(['54', 'Hyperspace Skill', character.skills['hyperspace']])
    writer.writerow(['55', 'Xenoesotericism Skill',
                     character.skills['xenoesotericism']])
    writer.writerow(['56', 'Linguistics Skill',
                     character.skills['linguistics']])
    writer.writerow(['57', 'Weapon Specialization Skill',
                     character.skills['weapon_specialization']])
    # 58 player notes
    # 59 equipment
    writer.writerow(['60', 'Credits', character.starting_credits])
    writer.writerow(['61', 'XP', character.xp])
    if character.character_class == 'Teamster':
        writer.writerow(['62', 'Armor', character.armor])
        writer.writerow(['63', 'Sanity', character.sanity])
        writer.writerow(['64', 'Fear', character.fear])
        writer.writerow(['65', 'Body', character.body])
    elif character.character_class == 'Android':
        writer.writerow(['66', 'Sanity', character.sanity])
        writer.writerow(['67', 'Fear', character.fear])
        writer.writerow(['68', 'Body', character.body])
        writer.writerow(['75', 'Armor', character.armor])
    elif character.character_class == 'Scientist':
        writer.writerow(['69', 'Body', character.body])
        writer.writerow(['70', 'Fear', character.fear])
        writer.writerow(['71', 'Sanity', character.sanity])
        writer.writerow(['76', 'Armor', character.armor])
    elif character.character_class == 'Marine':
        writer.writerow(['72', 'Sanity', character.sanity])
        writer.writerow(['73', 'Body', character.body])
        writer.writerow(['74', 'Fear', character.fear])
        writer.writerow(['77', 'Armor', character.armor])
    writer.writerow(['78', 'Class', character.character_class])
    writer.writerow(['79', 'Loadout', character.loadout])


def create_character(character_class=None, level=0):
    if character_class is None:
        character_class = random.choice(
            ['Teamster', 'Marine', 'Android', 'Scientist'])
    character_fields = Character(character_class, level)
    csvfile = open('fields.csv', 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['mothership_character_sheet.pdf', 'Name', 'Value'])
    fill_csv(writer, character_fields)
    csvfile.close()
    os.system('pdfforms fill fields.csv')
