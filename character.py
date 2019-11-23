import random
from roll import roll
import classes
from skills import skills


class Character:
    xp = 0
    strength = 0
    speed = 0
    intellect = 0
    combat = 0
    character_class = ''
    sanity = 0
    fear = 0
    body = 0
    armor = 0
    starting_credits = 0
    level = 0
    max_health = 0
    loadout = ''
    points = 0
    skills = {
        'biology': 'Off',
        'first_aid': 'Off',
        'hydroponics': 'Off',
        'geology': 'Off',
        'zero_g': 'Off',
        'scavenging': 'Off',
        'heavy_machinery': 'Off',
        'computers': 'Off',
        'mechanical_repair': 'Off',
        'driving': 'Off',
        'theology': 'Off',
        'archeology': 'Off',
        'art': 'Off',
        'mathematics': 'Off',
        'piloting': 'Off',
        'chemistry': 'Off',
        'athletics': 'Off',
        'rimwise': 'Off',
        'military_training': 'Off',
        'psychology': 'Off',
        'genetics': 'Off',
        'pathology': 'Off',
        'botany': 'Off',
        'planetology': 'Off',
        'asteroid_mining': 'Off',
        'jury_rigging': 'Off',
        'engineering': 'Off',
        'hacking': 'Off',
        'vehicle_specialization': 'Off',
        'tactics': 'Off',
        'mysticism': 'Off',
        'physics': 'Off',
        'astrogation': 'Off',
        'gunnery': 'Off',
        'firearms': 'Off',
        'cqc': 'Off',
        'explosives': 'Off',
        'sophontology': 'Off',
        'xenobiology': 'Off',
        'command': 'Off',
        'ai': 'Off',
        'robotics': 'Off',
        'cybernetics': 'Off',
        'hyperspace': 'Off',
        'xenoesotericism': 'Off',
        'linguistics': 'Off',
        'weapon_specialization': 'Off',
    }

    loadouts = [
        'Excavation Loadout',
        'Exploration Loadout',
        'Examination Loadout',
        'Extermination Loadout'
    ]

    def __init__(self, character_class, level):
        self.character_class = character_class
        self.level = level
        self.strength = roll(6, 10)
        self.speed = roll(6, 10)
        self.intellect = roll(6, 10)
        self.combat = roll(6, 10)
        self.set_up_character()
        self.get_class_skills()
        self.get_extra_skills()

    def set_up_character(self):
        if (self.character_class == 'Teamster'):
            self.strength += 5
            self.speed += 5
            self.sanity = classes.teamster['sanity']
            self.body = classes.teamster['body']
            self.armor = classes.teamster['armor']
            self.fear = classes.teamster['fear']
            self.points = 4

        elif (self.character_class == 'Android'):
            self.speed += 5
            self.intellect += 5
            self.sanity = classes.android['sanity']
            self.body = classes.android['body']
            self.armor = classes.android['armor']
            self.fear = classes.android['fear']
            self.points = 2

        elif (self.character_class == 'Scientist'):
            self.intellect += 10
            self.sanity = classes.scientist['sanity']
            self.body = classes.scientist['body']
            self.armor = classes.scientist['armor']
            self.fear = classes.scientist['fear']
            self.points = 3

        elif (self.character_class == 'Marine'):
            self.sanity = classes.marine['sanity']
            self.body = classes.marine['body']
            self.armor = classes.marine['armor']
            self.fear = classes.marine['fear']
            self.points = 3

        self.max_health = self.strength*2
        self.starting_credits = roll(5, 10)*10
        self.loadout = random.choice(self.loadouts)

    def get_class_skills(self):
        if (self.character_class == 'Teamster'):
            self.skills['zero_g'] = 'Yes'
            self.skills['mechanical_repair'] = 'Yes'
            skill = random.choice(classes.teamster['skills'])
            self.skills[skill] = 'Yes'
        elif (self.character_class == 'Android'):
            self.skills['computers'] = 'Yes'
            self.skills['mathematics'] = 'Yes'
            self.skills['linguistics'] = 'Yes'
        elif self.character_class == 'Scientist':
            skills = classes.scientist['skills']
            skill = random.choice(skills)
            skills.remove(skill)
            second_skill = random.choice(skills)
            self.skills[skill] = 'Yes'
            self.skills[second_skill] = 'Yes'
        elif (self.character_class == 'Marine'):
            self.skills['military_training'] = 'Yes'

    def get_extra_skills(self):
        while self.points != 0:
            potential_skills = self.get_eligible_skills()
            potential_skill = random.choice(potential_skills)
            if (skills[potential_skill]['cost'] <= self.points):
                self.skills[potential_skill] = 'Yes'
                self.points -= skills[potential_skill]['cost']

    def get_eligible_skills(self):
        current_skills_list = []
        for key, value in self.skills.items():
            if value == 'Yes':
                current_skills_list.append(key)
        potential_skills = []
        for key, value in skills.items():
            if self.skills[key] != 'Yes' and (value['cost'] == 1 or any(elem in current_skills_list for elem in skills[key]['pre_requisites'])):
                potential_skills.append(key)
        return potential_skills
