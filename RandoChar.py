import random

align1 = ['Lawful', 'Neutral', 'Chaotic']
align2 = ['Good', 'Evil','True']
race = ['Human', 'Half-elf', 'Elven', 'Dwarf', 'Gnome', 'Halfling', 'Half-orc', 'Dragonborn', 'Tiefling']
job = ['Bard', 'Barbarian', 'Cleric', 'Druid', 'Fighter', 'Ranger', 'Rogue', 'Paladin', 'Monk', 'Sorcerer', 'Warlock', 'Wizard']
randLang = ['Halfling', 'Elvish', 'Dwarvish', 'Gnomish', 'Orc', 'Draconic', 'Infernal', 'Giant', 'Abyssal', 'Celestial', 'Deep Speech', 'Primordial', 'Sylvan', 'Undercommon']
dAncestry = ['Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White']
breathTypeList = ['Acid', 'Lightning', 'Fire', 'Lightning', 'Acid', 'Fire', 'Poison', 'Fire', 'Cold', 'Cold']
breathWeapList = ['5x30ft line (DEX save)', '5x30ft line (DEX save)', '5x30ft line (DEX save)', '5x30ft line (DEX save)', '5x30ft line (DEX save)', '15ft cone (DEX save)', '15ft cone (DEX save)', '15ft cone (DEX save)', '15ft cone (DEX save)', '15ft cone (DEX save)']
randSkill = ['Athletics', 'Acrobatics', 'Sleight of Hand', 'Stealth', 'Arcana', 'History', 'Investigation', 'Nature', 'Religion', 'Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival', 'Deception', 'Intimidation', 'Performance', 'Persuasion']
modifier = [-5,-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,+1,+1,+2,+2,+3,+3,+4,+4,+5,+5,+6,+6,+7,+7,+8,+8,+9,+9,+10,+10]
languages = ['common']
dRand = 0
instruments = []
racials = []
wepProf = []
skills = []
toolsProf = []
randTools = []
randToolsProf = []
randSubRace = []
cFeatures = []
armProf = []
spellList = []
cantrips = ['']
randCant = ''
cantList = []
rmHolder = []
age = 0

spellList1Bard = ['']
cantListBard = ['']

spellList1Cler = ['']
cantListCler = ['']

strength1 = random.randint(1,6)
strength2 = random.randint(1,6)
strength3 = random.randint(1,6)
strength4 = random.randint(1,6)
strength = strength1 + strength2 + strength3 + strength4
strMod = modifier[strength]

dex1 = random.randint(1,6)
dex2 = random.randint(1,6)
dex3 = random.randint(1,6)
dex4 = random.randint(1,6)
dex = dex1 + dex2 + dex3 + dex4
dexMod = modifier[dex]

con1 = random.randint(1,6)
con2 = random.randint(1,6)
con3 = random.randint(1,6)
con4 = random.randint(1,6)
con = con1 + con2 + con3 + con4
conMod = modifier[con]

int1 = random.randint(1,6)
int2 = random.randint(1,6)
int3 = random.randint(1,6)
int4 = random.randint(1,6)
intel = int1 + int2 + int3 + int4
intMod = modifier[intel]

wis1 = random.randint(1,6)
wis2 = random.randint(1,6)
wis3 = random.randint(1,6)
wis4 = random.randint(1,6)
wis = wis1 + wis2 + wis3 + wis4
wisMod = modifier[wis]

cha1 = random.randint(1,6)
cha2 = random.randint(1,6)
cha3 = random.randint(1,6)
cha4 = random.randint(1,6)
cha = cha1 + cha2 + cha3 + cha4
chaMod = modifier[cha]

speed = 0
size = "Medium"
hp = 0
hd = ''
classProfBonus = 0
cantripsKnown = 0
spellsKnown = 0
counter = 0

randAlign1 = align1[random.randint(0,2)]
if randAlign1 == 'Neutral':
    randAlign2 = align2[random.randint(0,2)]
    if randAlign2 == 'True':
        print('Alignment: ' + randAlign2 + ' ' + randAlign1)
    else:
        print('Alignment: ' + randAlign1 + ' ' + randAlign2)
else:
    randAlign2 = align2[random.randint(0,1)]
    print('Alignment: ' + randAlign1 + ' ' + randAlign2)

randRace = race[random.randint(0,6)]
print('Race: ' + randRace)
randJob = job[random.randint(0,7)]
print('Class: ' + randJob)



if randRace == 'Human':
    strength += 1
    dex += 1
    con += 1
    intel += 1
    wis += 1
    cha += 1
    size = 'Medium'
    speed = 30
    languages = languages + [randLang[random.randint(0,len(randLang)-1)]]
    age = random.randint(18, 60)
elif randRace == 'Half-elf':
    cha += 2
    size = 30
    languages = languages + ['Elvish'] + [randLang[random.randint(0,len(randLang))]]
    racial = racials + ['Darkvision'] + ['Fey Ancestry: advantage on saving throws vs being charmed and magic can\'t put you to sleep']
    abList = ['strength' + 'dex' + 'con' + 'intel' + 'wis' + 'cha']
    skills = skills + [randSkill[random.randint(0,len(randSkill))] + randSkill[random.randint(0,len(randSkill))]]
    age = random.randint(20,180)
    randAb = abList[random.randint(0,len(abList)-1)]
    if randAb == 'strength':
        strength += 1
    elif randAb == 'dex':
        dex += 1
    elif randAb == 'con':
        con += 1
    elif randAb == 'intel':
        intel += 1
    elif randAb == 'wis':
        wis += 1
    elif randAb == 'cha':
        cha += 1
    randAb = abList[random.randint(0,len(ablist)-1)]
    if randAb == 'strength':
        strength += 1
    elif randAb == 'dex':
        dex += 1
    elif randAb == 'con':
        con += 1
    elif randAb == 'intel':
        intel += 1
    elif randAb == 'wis':
        wis += 1
    elif randAb == 'cha':
        cha += 1
elif randRace == 'elf':
    dex += 2
    speed = 30
    languages = languages + ['Elvish']
    racials = racials + ['Darkvision'] + ['Keen Senses'] + ['Fey Ancestry: advantage on saving throws vs being charmed and magic can\'t put you to sleep'] + ['Trance: Instead of sleeping elves meditate deeply, remaining semiconscious, for 4 hours a day. Gains same benefit as a human with 8 hours of sleep']
    skills = skills + ['Perception']
    randSubRace = random.randint(1,20)
    age = random.randint(100, 700)
    if randSubRace <=9:
        randRace == 'High Elf'
        int += 1
        wepProf = wepProf + ['Longsword'] + ['Shortsword'] + ['Shortbow'] + ['Longbow']
        racials = racials + ['Cantrip: You know one cantrip from the wizard spell list. Int is your spellcasting ability for it. ' + randCant]
        randCant = [cantList(random.randint(0,len(cantList)))]
        languages = languages + [randLang(random.randint(0,len(randLang)))]
        cantrips = cantrips + randCant
    elif randSubRace >=10 and randSubRace <= 19:
        randRace == 'Wood Elf'
        wis += 1
        wepProf = wepProf + ['Longsword'] + ['Shortsword'] + ['Shortbow'] + ['Longbow']
        speed = 35
        racials = racials + ['Mask of the Wild: You can attempt to hide even when only lightly obscured by foliage, heavy raid, falling snow, mist, and other natural phenomena']
    elif randSubRace == 20:
        randRace == 'Drow'
        cha += 1
        racials = racials + ['Superior darkvision: Darkvision has a radius of 120ft.'] + ['Drow Magic: You know the dancing lights cantrip. At 3rd lvl you can cast the faerie fire spell once per day. At 5th level you can also cast the darkness spell once per day. CHA is the spellcasting ability for these spells.']
        wepProf = wepProf + ['Rapier'] + ['Shortsword'] + ['Hand Crossbow']
        cantrips = cantrips + ['Dancing Lights']
elif randRace == 'Dwarf':
    con += 2
    speed = 25
    languages = languages + ['Dwarvish']
    racials = racials + ['Darkvision'] + ['Dwarven Resilience: advantage on saving throws vs. poison and resistance vs. poison'] + ['Dwarven combat training'] + ['Tool proficiency'] + ['Stonecunning']
    wepProf = wepProf + ['battleaxe'] + ['handaxe'] + ['throwing hammer'] + ['warhammer']
    skills = skills + ['History(Stonework origin)']
    randTools = ['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools']
    randToolsProf = randTools[random.randint(0,len(randTools))]
    toolsProf = toolsProf + [randToolsProf]
    age = random.randint(50,300)
    randSubRace = random.randint(1,20)
    if randSubRace <= 10:
        randRace == 'Hill Dwarf'
        wis += 1
        hp += 1
        hd = hd + '+ 1/level'
    if randSubRace >= 11:
        randRace == 'Mountain Dwarf'
        strength +=2
        armProf = armProf + ['light armor'] + ['medium armor']
elif randRace == 'Gnome':
    intel += 2
    size = 'Small'
    speed = 25
    languages = languages + ['Gnomish']
    racials = racials + ['Darkvision'] + ['Gnome Cunning: advantage on all INT/WIS/CHA saving throws vs magic']
    randSubRace = random.randint(1,20)
    age = random.randint(40,400)
    if randSubRace <= 10:
        randRace == 'Forest Gnome'
        racials = racials + ['Natural illusionist: You know the minor illusion cantrip. INT is your spellcasting ability for it.'] + ['Speak with small beasts: Through sounds and gestures you can communicate simple ideas with small or smaller beasts.']
        cantList = cantList + ['Minor Illusion']
    if randSubRace >= 11:
        randRace == 'Rock Gnome'
        con += 1
        racials = racials + ['Artificer\'s Lore: Whenever you make an INT(History) check related to magic items, alchemical objects or technological devices, you can add twice your proficiency bonus instead of any proficiency bonus you normally apply'] + ['Tinker: You have proficiency with artisan\'s tools (tinker\'s tools). Using those tools you can spend one hour and 10GP worth of materials to contruct a tiny Clockwork device (AC 5, 1 hp). The device ceases to functon after 24 hours unless you spend 1 hour repairing it to keep the device functioning or when you use your action to dismantle it. At that time you can reclaim the materials used to create it. You can have up to three such devices active at a time.'] + ['Device options: \n \t Clockwork toy. The toy is a clockwork animal monster or person. When placed on the ground the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents. \n \t FireStarter. The device produces a miniature flame which you can use to light a candle torch or campfire. Using the device requires your action. \n \tMusic box. When opened this music box plays a single song at a moderate volume. The box stops playing when it reaches the song\'s end or when closed.']
elif randRace == 'Halfling':
    dex += 2
    speed = 25
    size = 'Small'
    languages = languages + ['Halfling']
    racials = racials + ['Lucky: can re-roll a 1 on an attack roll, ability check, or saving throw'] + ['Brave: advantage on saving throws vs being frightened'] + ['Halfling Nibleness: move through the space of any creature that is a size or more larger than yours']
    age = random.randint(20, 200)
    randSubRace = random.randint(1,20)
    if randSubRace <= 10:
        randRace = 'Lightfoot Halfling'
        cha += 1
        racials = racials + ['Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you']
    if randSubRace >= 11:
        randRace = 'Stout Halfling'
        con += 1
        racials = racials + ['You have advantage on saving throws vs. poison and you have resistance against poison damage.']
elif randRace == 'Dragonborn':
    strength += 2
    cha += 1
    size = 'Medium'
    speed = 30
    languages = languages + ['Draconic']
    dRand = random.randint(0,len(dAncestry))
    dAncestry = dAncestry(dRand)
    breathTypeList = breathTypeList(dRand)
    breathWeapList = breathWeapList(dRand)
    dracAncestry = str(dAncestry + 'Ancestry ( ' + breathType + ' ' + breathWeap + ') DC Saving throw: ' + str(8 + con + classProfBonus) + ' A creature takes 2d6 on a failed save and half on successful one. Increase to 3d6 at 6th level and 5d6 at 16th. Cannot be used again until completing a short or long rest.')
    racials = racials + [str(dracAncestry)] + ['Damage resistance: Damage resistance to the damage type associated with your draconic ancestry.']
    age = random.randint(15, 75)
elif randRace == 'Half-orc':
    strength += 2
    con += 1
    size = 'Medium'
    speed = 30
    racials = racials + ['Darkvision'] + ['Relentless Endurance: When you are reduced to 0HP but not killed outright you can drop to 1HP instead. Can\'t be reused until you finish a long rest'] + ['Savage Attacks: when you score a critical hit with a melee weapon attack, you can roll one of the damage dice one additional time and add it to the extra damage of the critical hit']
    skills = skills + ['Intimidation']
    languages = languages + ['Orc']
    age = random.randint(14,70)
elif randRace == 'Tiefling':
    intel += 1
    cha += 2
    size = 'Medium'
    speed = 30
    languages = languages + ['Infernal']
    racials = racials + ['Darkvision'] + ['Hellish Resistance: resistance to fire damage'] + ['Infernal Legacy: You know the thaumaturgy cantrip. When you reach 3rd lvl, you can cast the hellish rebuke spell as a 2nd lvl spell once and regain ability to do so on finishing a long rest. When you reach 5th lvl you can cast the darkness spell once and regain the abilit to do so on ifinishing a long rest. CHA is your spellcasting ability for this.']
    age = random.randint(18,65)
    cantList = cantList + ['Thaumaturgy']


if job == 'Bard':
    hp = 8 + conMod
    hd += '1d8'
    classProfBonus = 2
    armProf = armProf + ['Light Armor']
    wepProf = wepProf + ['Simple Weapons'] + ['Hand Crossbow'] + ['Longsword'] + ['Rapier'] + ['Shortsword']
    toolsProf = toolsProf + [instruments[0,len(instruments)-1]] + [instruments[0,len(instruments)-1]] + [instruments[0,len(instruments)-1]]
    skills = skills + [randSkill[0,len(randSkill)-1]] + [randSkill[0,len(randSkill)-1]] + [randSkill[0,len(randSkill)-1]]
    cFeatures = cFeatures + ['Spellcasting'] + ['Bardic Inspiration: Use a Bonus Action on your turn to choose one creater within 60ft who can hear you. Creature gains one Bardic Inspiration die (d6). Once within 10mins the creature can add the die roll to one ability check, attack roll, or saving throw. Can be used a number of times equal to the CHA mod and is regained on finishing a long rest.']
    cantripsKnown = 2
    spellsKnown = 4
    firstLvlSpells = 2
    secondLvlSpells = 0
    thirdLvlSpells = 0
    fourthLvlSpells = 0
    fifthLvlSpells = 0
    sixLvlSpells = 0
    sevenLvlSpells = 0
    eightLvlSpells = 0
    nineLvlSpells = 0
    spellSaveDC = 8 + classProfBonus + chaMod
    spellAttkMod = classProfBonus + chaMod
    list1Spells = [spellList1Bard(random.randint(0,len(spellList1Bard)))] + [spellList1Bard(random.randint(0,len(spellList1Bard)))] + [spellList1Bard(random.randint(0,len(spellList1Bard)))] + [spellList1Bard(random.randint(0,len(spellList1Bard)))]
    list2Spells = []
    list3Spells = []
    list4Spells = []
    list5Spells = []
    list6Spells = []
    list7Spells = []
    list8Spells = []
    list9Spells = []
    cantList = cantList + [cantListBard(random.randint(0,len(cantListBard)))] +  [cantListBard(random.randint(0,len(cantListBard)))]
elif job == 'Barbarian':
    hp = 12 + conMod
    hd += '1d12'
    classProfBonus = 2
    armProf = armProf + ['Light Armor'] + ['Medium Armor'] + ['Shields']
    wepProf = wepProf + ['Simple Weapons'] + ['Martial Weapons']
    barbSkill = ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival']
    skills = skills + [barbSkill(random.randint(0,len(barbSkill)-1))] + [barbSkill(random.randint(0,len(barbSkill)-1))]
    cFeatures = cfeatures + ['Rage: Advantage on STR checks and saving throws. When making a melee weapon attack using STR add Rage Damage to damage roll'] + ['Unarmored Defense: While not wearing any armor your AC=10+Dex Modifier+Con Modifier. You can use a shield and still gain this benefit'] + ['Rage Damage: +2'] + ['Rages: 2']
elif job == 'Cleric':
    hp = 8 + conMod
    hd += '1d8'
    classProfBonus = 2
    armProf = armProf + ['Light Armor'] + ['Medium Armor'] + ['Shields']
    wepProf = wepProf + ['Simple Weapons']
    clericSkill = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
    skills = skills + [clericSkill(random.randint(0,len(clericSkill)-1))] + [clericSkill(random.randint(0,len(clericSkill)-1))]
    divDomain = ['Life', ]
    cFeatures = cFeatures + ['Spellcasting'] + [divDomain]
    cantripsKnown = 3
    firstLvlSpells = 2
    secondLvlSpells = 0
    thirdLvlSpells = 0
    fourthLvlSpells = 0
    fifthLvlSpells = 0
    sixLvlSpells = 0
    sevenLvlSpells = 0
    eightLvlSpells = 0
    nineLvlSpells = 0
    spellSaveDC = 8 + classProfBonus + wisMod
    spellAttkMod = classProfBonus + wisMod
    list1Spells = []
    list2Spells = []
    list3Spells = []
    list4Spells = []
    list5Spells = []
    list6Spells = []
    list7Spells = []
    list8Spells = []
    list9Spells = []
    counter = cantripsKnown
    while counter > 0:
        rmHolder = random.randint(0,len(cantListCler))
        cantList = cantList + [cantListCler(rmHolder)]
        counter -= 1
        del cantListCler[rmHolder]
elif job == 'Druid':
    hp = 8 + conMod
    hd += '1d8'
    classProfBonus = 2
    armProf = armProf + ['Light Armor'] + ['Medium Armor'] + ['Shields'] + ['No armor or shields of metal']
    wepProf = wepProf + ['Club'] + ['Dagger'] + ['Dart'] + ['Javelin'] + ['Mace'] + ['Quarterstaff'] + ['Scimitar'] + ['Sickle'] + ['Sling'] + ['Spear']
    druidSkill = ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival']
    skills = skills + [druidSkill(random.randint(0,len(druidSkill)-1))] + [druidSkill(random.randint(0,len(druidSkill)-1))]
    cFeatures = cFeatures + ['Spellcasting'] + ['Druidic']
    languages = languages + ['Druidic']
    cantripsKnown = 2
    firstLvlSpells = 2
    secondLvlSpells = 0
    thirdLvlSpells = 0
    fourthLvlSpells = 0
    fifthLvlSpells = 0
    sixLvlSpells = 0
    sevenLvlSpells = 0
    eightLvlSpells = 0
    nineLvlSpells = 0
    spellSaveDC = 8 + classProfBonus + wisMod
    spellAttkMod = classProfBonus + wisMod
    list1Spells = []
    list2Spells = []
    list3Spells = []
    list4Spells = []
    list5Spells = []
    list6Spells = []
    list7Spells = []
    list8Spells = []
    list9Spells = []
    cantList = + []
elif job == 'Fighter':
    hp = 10 + conMod
    hd += '1d10'
    classProfBonus = 2
    armProf = ['All Armor'] + ['Shields']
    wepProf = wepProf + ['Simple Weapons'] + ['Martial Weapons']
    fightSkill = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
    skills = skills + [fightSkill(random.randint(0,len(fightSkill)-1))] + [fightSkill(random.randint(0,len(fightSkill)-1))]
    fightStyle = ['Archery', 'Defense', 'Dueling', 'Great Weapon Fighting', 'Protection', 'Two-Weapon Fighting',]
    cFeatures = cFeatures + ['Second Wind'] + [fightStyle(random.randomint(0,len(fightStyle)-1))]
elif job == 'Ranger':
    hp = 10 + conMod
    hd += '1d10'
    classProfBonus = 2
    armProf = armProf + ['Light Armor'] + ['Medium Armor'] + ['Shields']
    wepProf = wepProf + ['Simple Weapons'] + ['Martial Weapons']
    rangerSkill = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
    skills = skills + [rangerSkill(random.randint(0,len(rangerSkill)-1))] + [rangerSkill(random.randint(0,len(rangerSkill)-1))]
    favEnemy = ['Abberations', 'Beasts', 'Celestials', 'Constructs', 'Dragons', 'Elementals', 'Fey', 'Fiends', 'Giants', 'Monstrosities', 'Oozes', 'Plants', 'Undead', 'Gnolls', 'Orcs', 'Humans', 'Elves',
    'Tieflings', 'Dwarves', 'Gnomes', 'Halflings']
    cFeatures = cFeatures + ['Favored Enemy: ' + favEnemy] + ['Natural Explorer']
elif job == 'Rogue':
    hp = 8 + conMod
    hd += '1d8'
    classProfBonus = 2
    armProf = armProf + ['Light Armor']
    wepProf = wepProf + ['Simple weapons'] + ['Hand crossbow'] + ['Longsword'] + ['Rapier'] + ['Shortsword']
    skills = skills
    cFeatures = cFeatures
elif job == 'Paladin':
    hp = 10 + conMod
    hd += '1d10'
    classProfBonus = 2
    armProf = ['All Armor'] + ['Shields']
    wepProf = wepProf + ['Simple Weapons'] + ['Martial weapons']
    skills = skills
    randDom = []
    cFeatures = cFeatures
elif job == 'Monk':
    hp = 8 + conMod
    hd += '1d8'
    classProfBonus = 2
    armProf = armProf
    wepProf = wepProf + ['Simple Weapons'] + ['Short Sword']
    skills = skills
    cFeatures = cFeatures

elif job == 'Sorcerer':
    hp = 6 + conMod
    hd += '1d6'
    classProfBonus = 2
    armProf = armProf
    wepProf = wepProf + ['Dagger'] + ['Dart'] + ['Sling'] + ['Quarterstaff'] + ['Light Crossbow']
    skills = skills
    cFeatures = cFeatures
    cantripsKnown = 4
    firstLvlSpells = 2
    secondLvlSpells = 0
    thirdLvlSpells = 0
    fourthLvlSpells = 0
    fifthLvlSpells = 0
    sixLvlSpells = 0
    sevenLvlSpells = 0
    eightLvlSpells = 0
    nineLvlSpells = 0
    spellSaveDC = 8 + classProfBonus + wisMod
    spellAttkMod = classProfBonus + wisMod
    list1Spells = []
    list2Spells = []
    list3Spells = []
    list4Spells = []
    list5Spells = []
    list6Spells = []
    list7Spells = []
    list8Spells = []
    list9Spells = []
    cantList = cantList + []
elif job == 'Warlock':
    hp = 8 + conMod
    hd += '1d8'
    classProfBonus = 2
    armProf = armProf + ['Light Armor']
    wepProf = wepProf + ['Simple Weapons']
    skills = skills
    cFeatures = cFeatures
    cantripsKnown = 2
    firstLvlSpells = 2
    secondLvlSpells = 0
    thirdLvlSpells = 0
    fourthLvlSpells = 0
    fifthLvlSpells = 0
    sixLvlSpells = 0
    sevenLvlSpells = 0
    eightLvlSpells = 0
    nineLvlSpells = 0
    spellSaveDC = 8 + classProfBonus + wisMod
    spellAttkMod = classProfBonus + wisMod
    list1Spells = []
    list2Spells = []
    list3Spells = []
    list4Spells = []
    list5Spells = []
    list6Spells = []
    list7Spells = []
    list8Spells = []
    list9Spells = []
    listCantrips = []
elif job == 'Wizard':
    hp = 6 + conMod
    hd += '1d6'
    classProfBonus = 2
    armProf = armProf
    wepProf = wepProf + ['Dagger'] + ['Dart'] + ['Sling'] + ['Quarterstaff'] + ['Light crossbow']
    skills = skills
    cFeatures = cFeatures
    cantripsKnown = 3
    firstLvlSpells = 2
    secondLvlSpells = 0
    thirdLvlSpells = 0
    fourthLvlSpells = 0
    fifthLvlSpells = 0
    sixLvlSpells = 0
    sevenLvlSpells = 0
    eightLvlSpells = 0
    nineLvlSpells = 0
    spellSaveDC = 8 + classProfBonus + wisMod
    spellAttkMod = classProfBonus + wisMod
    list1Spells = []
    list2Spells = []
    list3Spells = []
    list4Spells = []
    list5Spells = []
    list6Spells = []
    list7Spells = []
    list8Spells = []
    list9Spells = []
    listCantrips = []



print('STR: ' + str(strength) + ' (' + str(strength1) + ", " + str(strength2) + ", " + str(strength3) + ", " + str(strength4) +  ')    [' + str(strMod) + ']')
print('DEX: ' + str(dex) + ' (' + str(dex1) + ", " + str(dex2) + ", " + str(dex3) + ", " + str(dex4) + ')    [' + str(dexMod) + ']')
print('CON: ' + str(con) + ' (' + str(con1) + ", " + str(con2) + ", " + str(con3) + ", " + str(con4) + ')    [' + str(conMod) + ']')
print('INT: ' + str(intel) + ' (' + str(int1) + ", " + str(int2) + ", " + str(int3) + ", " + str(int4) + ')    [' + str(intMod) + ']')
print('WIS: ' + str(wis) + ' (' + str(wis1) + ", " + str(wis2) + ", " + str(wis3) + ", " + str(wis4) +  ')    [' + str(wisMod) + ']')
print('CHA: ' + str(cha) + ' (' + str(cha1) + ", " + str(cha2) + ", " + str(cha3) + ", " + str(cha4) +  ')    [' + str(chaMod) + ']')
print()

print('AC: [' + str(10 + dexMod) + '] 10+'+ str(dexMod) + '\tInitiative: ' + str(dexMod) + '\tHP: ' + str(hp) + '\tHD: ' + str(hd))
print('Proficiency Bonus: ' + str(classProfBonus))
print('Speed: ' + str(speed) + '\tSize: ' + str(size))
print('Max Carry: '+ str(strength * 15) + '\tPush/Drag/Lift: ' + str(strength * 30))
print()
print()
print('Languages: ' + ' \n \t '.join(map(str,languages[:])))
print('Racials: ' + ' \n \t '.join(map(str,racials[:])))
print('Class Features: ' + '\n \t '.join(map(str,cFeatures[:])))
print('Skills: ' + ' \n \t '.join(map(str,skills[:])))
print('Weapons proficiencies: ' + ' \n \t '.join(map(str,wepProf[:])))
print('Armor proficiencies: ' + ' \n \t '.join(map(str,armProf[:])))
print('Tool proficiencies: ' + ' \n \t '.join(map(str,toolsProf[:])))

print()
if job == 'Paladin':
    print()
    print(str(randDom))

if cantripsKnown >= 1 or spellsKnown >= 1:
    print()
    print('Cantrips Known: ' + str(cantripsKnown) + '    Spells Known: ]' + str(spellsKnown))
    print('          Spells per Day')
    print('-------------------------------------')
    print('|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|')
    print('|' + str(firstLvlSpells) + '|' + str(secondLvlSpells) + '|' + str(thirdLvlSpells) + '|' + str(fourthLvlSpells) + '|' + str(fifthLvlSpells) +
    '|' + str(sixLvlSpells) + '|' + str(sevenLvlSpells) + '|' + str(eightLvlSpells) + '|' + str(nineLvlSpells) + '|')
    print(spellList)
