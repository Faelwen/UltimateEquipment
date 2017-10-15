import zipfile
import shutil
import csv
from lxml import etree
import html

# Filenames / paths
csv_files = ("Clothing.csv", "Lodging and Services.csv", "Food and Drink.csv",
"Entertainment and Trade Goods.csv", "Alchemical Tools.csv",
"Alchemical Remedies.csv", "Alchemical Weapons.csv",
"Animals and Transports.csv", "Tools and Skill Kits.csv", "Adventuring Gear.csv",
"Intelligent Items.csv", "Cursed Items.csv", "Artifacts.csv", "Gems.csv",
"Potions.csv", "Poisons.csv", "Rings.csv", "Rods.csv", "Wands.csv", "Staves.csv",
"Scrolls.csv", "Armor.csv", "Art objects.csv", "Weapons.csv", "Belts Slot.csv",
"Body Slot.csv","Chest Slot.csv",
"Eyes Slot.csv","Feet Slot.csv", "Hands Slot.csv", "Head Slot.csv",
"Headband Slot.csv", "Neck Slot.csv", "Shoulders Slot.csv",  "Slotless.csv",
"Wrists Slot.csv", "Specific Magic Armor.csv", "Specific Magic Weapons.csv",)
module_file_name = "UltimateEqupiment.mod"
xml_definition_file = "definition.xml"
xml_database_file = "db.xml"
license_file = "license.html"
FG_module_directory = "E:\\Fantasy Grounds\\DataDir\\modules"

#Globals
module_name = "Ultimate Equipment"
module_author = "Faelwen"
module_ruleset = "PFRPG"
library_tag_name = "UltimateEquipment"
library_name = "Ultimate Equipment"
library_category = "PFRPG Essentials"
library_entries =   [{"Entry name":"---Legal Notice---",
                    "Entry tag":"AA.License",
                    "Link type":"librarylink",
                    "Window class":"referencetext",
                    "Record name": "License"},
                    {"Entry name":"Armor",
                    "Entry tag":"AB.Armors",
                    "Link type":"librarylink",
                    "Window class":"reference_armortablelist",
                    "Record name": "lists.Armor@"+module_name},
                    {"Entry name":"Armor - Specific Magic",
                    "Entry tag":"AC.Armors",
                    "Link type":"librarylink",
                    "Window class":"reference_armortablelist",
                    "Record name": "lists.SpecificMagicArmor@"+module_name},
                    {"Entry name":"Artifacts",
                    "Entry tag":"AD.Artifacts",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Artifact@"+module_name},
                    {"Entry name":"Art objects",
                    "Entry tag":"AE.Art",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Art@"+module_name},
                    {"Entry name":"Cursed items",
                    "Entry tag":"CA.Cursed",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Cursed@"+module_name},
                    {"Entry name":"Gear - Adventuring Gear",
                    "Entry tag":"GA.AdventuringGear",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.AdventuringGear@"+module_name},
                    {"Entry name":"Gear - Tools and Skill Kits",
                    "Entry tag":"GB.Tools",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Tool@"+module_name},
                    {"Entry name":"Gear - Animals, Mounts, and Related Gear",
                    "Entry tag":"GC.Animals",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Animals@"+module_name},
                    {"Entry name":"Gear - Clothing",
                    "Entry tag":"GD.Clothings",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Clothing@"+module_name},
                    {"Entry name":"Gear - Entertainment and Trade Goods",
                    "Entry tag":"GE.Entertainment",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Entertainment@"+module_name},
                    {"Entry name":"Gear - Food and Drink",
                    "Entry tag":"GF.Food",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Food@"+module_name},
                    {"Entry name":"Gear - Lodging and Services",
                    "Entry tag":"GG.Lodging",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Lodging@"+module_name},
                    {"Entry name":"Gear - Alchemical Remedies",
                    "Entry tag":"GH.AlcRemedies",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.AlcRem@"+module_name},
                    {"Entry name":"Gear - Alchemical Tools",
                    "Entry tag":"GI.AlcTools",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.AlcTool@"+module_name},
                    {"Entry name":"Gear - Alchemical Weapons",
                    "Entry tag":"GJ.AlcWeapons",
                    "Link type":"librarylink",
                    "Window class":"reference_weapontablelist",
                    "Record name": "lists.AlcWeapon@"+module_name},
                     {"Entry name":"Gear - Poisons",
                    "Entry tag":"GK.Poisons",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Poison@"+module_name},
                     {"Entry name":"Gems",
                    "Entry tag":"GL.Gems",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Gem@"+module_name},
                     {"Entry name":"Intelligent Items",
                    "Entry tag":"IA.Intel",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Intel@"+module_name},
                    {"Entry name":"Oils and Potions",
                    "Entry tag":"OA.Potions",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Potion@"+module_name},
                    {"Entry name":"Rings",
                    "Entry tag":"RA.Rings",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Ring@"+module_name},
                    {"Entry name":"Rods",
                    "Entry tag":"RB.Rods",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Rod@"+module_name},
                     {"Entry name":"Scrolls",
                    "Entry tag":"SA.Scrolls",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Scroll@"+module_name},
                     {"Entry name":"Staves",
                    "Entry tag":"SB.Staves",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Staff@"+module_name},
                     {"Entry name":"Wands",
                    "Entry tag":"WA.Wands",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Wand@"+module_name},
                    {"Entry name":"Weapons",
                    "Entry tag":"WB.Weapons",
                    "Link type":"librarylink",
                    "Window class":"reference_weapontablelist",
                    "Record name": "lists.Weapons@"+module_name},
                    {"Entry name":"Weapons - Specific Magic Weapons",
                    "Entry tag":"WC.WeaponsSpecific",
                    "Link type":"librarylink",
                    "Window class":"reference_weapontablelist",
                    "Record name": "lists.SpecificMagicWeapons@"+module_name},
                    {"Entry name":"Wondrous Items - Belts",
                    "Entry tag":"WD.Belts",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Belt@"+module_name},
                    {"Entry name":"Wondrous Items - Body",
                    "Entry tag":"WE.Body",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Body@"+module_name},
                    {"Entry name":"Wondrous Items - Chest",
                    "Entry tag":"WF.Chest",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Chest@"+module_name},
                    {"Entry name":"Wondrous Items - Eyes",
                    "Entry tag":"WG.Eyes",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Eyes@"+module_name},
                    {"Entry name":"Wondrous Items - Feet",
                    "Entry tag":"WH.Feet",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Feet@"+module_name},
                    {"Entry name":"Wondrous Items - Hands",
                    "Entry tag":"WI.Hands",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Hands@"+module_name},
                    {"Entry name":"Wondrous Items - Head",
                    "Entry tag":"WI.Head",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Head@"+module_name},
                    {"Entry name":"Wondrous Items - Headband",
                    "Entry tag":"WI.Headband",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Headband@"+module_name},
                    {"Entry name":"Wondrous Items - Neck",
                    "Entry tag":"WI.Neck",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Neck@"+module_name},
                    {"Entry name":"Wondrous Items - Shoulders",
                    "Entry tag":"WI.Shoulders",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Shoulders@"+module_name},
                    {"Entry name":"Wondrous Items - Wrists",
                    "Entry tag":"WI.Wrists",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Wrists@"+module_name},
                    {"Entry name":"Wondrous Items - Slotless",
                    "Entry tag":"WI.Slotless",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Slotless@"+module_name},]

def populate_library_entries(xml_library_entries):
    for entry in library_entries:
        xml_library_entry =  etree.SubElement(xml_library_entries, entry["Entry tag"])
        xml_library_entry_linktype = etree.SubElement(xml_library_entry, entry["Link type"], type="windowreference")
        xml_library_entry_linktype_class = etree.SubElement(xml_library_entry_linktype, "class")
        xml_library_entry_linktype_class.text = entry["Window class"]
        xml_library_entry_linktype_recordname = etree.SubElement(xml_library_entry_linktype, "recordname")
        xml_library_entry_linktype_recordname.text = entry["Record name"]
        xml_library_entry_name = etree.SubElement(xml_library_entry, "name", type="string")
        xml_library_entry_name.text = entry["Entry name"]

def populate_license(xml_root):
    xml_license = etree.SubElement(xml_root, "License", static="true")
    xml_license_link = etree.SubElement(xml_license,"librarylink", type="windowreference")
    xml_license_link_class = etree.SubElement(xml_license_link, "class")
    xml_license_link_class.text = "referencetext"
    xml_license_link_recordname = etree.SubElement(xml_license_link, "recordname")
    xml_license_link_recordname.text = ".."
    xml_license_name = etree.SubElement(xml_license,"name", type="string")
    xml_license_name.text = "License"
    xml_license_text = etree.SubElement(xml_license,"text", type="formattedtext")
    with open(license_file, 'r') as file:
        license_test = file.read()
    xml_license_text.text = license_test


def generate_xml_deffile():
    xml_def_root = etree.Element('root')
    xml_def_name = etree.SubElement(xml_def_root, "name")
    xml_def_name.text = module_name
    xml_def_author = etree.SubElement(xml_def_root, "author")
    xml_def_author.text = module_author
    xml_def_ruleset = etree.SubElement(xml_def_root, "ruleset")
    xml_def_ruleset.text = module_ruleset
    with open(xml_definition_file, 'w') as file:
        file.write(etree.tostring(xml_def_root,pretty_print=True,encoding="iso-8859-1",xml_declaration=True).decode("iso-8859-1"))

def generate_xml_dbfile(xml_root):
    with open(xml_database_file, 'w', encoding="iso-8859-1") as file:
        xmldoc = html.unescape(etree.tostring(xml_root,pretty_print=True,encoding="iso-8859-1",xml_declaration=True).decode("iso-8859-1"))
        file.write(xmldoc)

def generate_module():
    with zipfile.ZipFile(module_file_name, 'w', zipfile.ZIP_DEFLATED) as file:
        file.write('db.xml')
        file.write('definition.xml')
        #myzip.write('thumbnail.png')

def copy_to_Fantasy_Grounds():
    shutil.copy(module_file_name, FG_module_directory)


def populate_items(xml_lists, xml_ref_equipment, xml_ref_armor, xml_ref_weapons):
    for file in csv_files:
        print(file)
        with open(file, 'r',encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
            row = next(csvreader)
            list_name = row[0]
            item_prefix = row[1]
            list_header = row[2]

            xml_list = etree.SubElement(xml_lists, list_name.strip())
            xml_list_description = etree.SubElement(xml_list, "description", type="string")
            xml_list_description.text = list_header.strip()
            xml_list_group = etree.SubElement(xml_list, "groups")

            lib_type = lib_subtype = item_type = item_subtype = item_name = item_cost = item_armor_bonus = item_max_dex = item_armor_penalty = item_spell_fail = item_speed30 = item_speed20 = item_weight = item_description = item_bonus = item_cl = item_reqs = item_aura = item_subtype2 = item_damage_s = item_damage_m = item_critical = item_range = item_damage_type = item_properties = None
            section_number = 0
            item_number = 0
            previous_lib_type = None
            previous_lib_subtype = None

            for row in csvreader:
                item_type = row[2]
                item_is_armor = (item_type == "Armor")
                item_is_weapon = (item_type == "Weapon")

                if item_is_armor:
                    [lib_type, lib_subtype, item_type, item_subtype, item_name, item_cost, item_armor_bonus, item_max_dex, item_armor_penalty, item_spell_fail, item_speed30, item_speed20, item_weight, item_description, item_bonus, item_cl, item_reqs, item_aura] = row
                    ref_prefix = "armor"
                    ref_group = "armor"
                elif item_is_weapon:
                    [lib_type, lib_subtype, item_type, item_subtype, item_subtype2, item_name, item_cost, item_damage_s, item_damage_m, item_critical, item_range, item_weight, item_damage_type, item_properties, item_description, item_bonus, item_cl, item_reqs, item_aura] = row
                    ref_prefix = "weapon"
                    ref_group = "weapons"
                else:
                    [lib_type, lib_subtype, item_type, item_subtype, item_name, item_cost, item_cl, item_weight, item_description, item_reqs, item_aura] = row
                    ref_prefix = "equipment"
                    ref_group = "equipment"
                new_type = (lib_type != previous_lib_type)
                new_subtype = (lib_subtype != previous_lib_subtype)
                item_number += 1

                if new_type or new_subtype:
                    previous_lib_type = lib_type
                    previous_lib_subtype = lib_subtype
                    section_number += 1

                    xml_section = etree.SubElement(xml_list_group, "section"+'{:03d}'.format(section_number))
                    xml_section_description = etree.SubElement(xml_section, "description", type="string")
                    xml_section_description.text = lib_type
                    if lib_subtype != "":
                        xml_section_subdescription = etree.SubElement(xml_section, "subdescription", type="string")
                        xml_section_subdescription.text = lib_subtype
                    xml_section_items = etree.SubElement(xml_section, ref_group)

                # Ref to lib lists
                item_ref = item_prefix + "{:04d}".format(item_number)
                xml_item = etree.SubElement(xml_section_items, item_ref)
                xml_item_link = etree.SubElement(xml_item, "link", type="windowreference")
                xml_item_link_class = etree.SubElement(xml_item_link, "class")
                xml_item_link_recordname = etree.SubElement(xml_item_link, "recordname")
                xml_item_name = etree.SubElement(xml_item, "name", type="string")
                xml_item_cost = etree.SubElement(xml_item, "cost", type="string")
                xml_item_weight = etree.SubElement(xml_item, "weight", type="string")

                if item_is_armor or item_is_weapon:
                    xml_item_link_class.text = "item"
                else:
                    if (item_aura != "") or (item_cl != "") or (item_reqs != ""):
                        xml_item_link_class.text = "item"
                    else:
                        xml_item_link_class.text = "referenceequipment"
                xml_item_link_recordname.text = "reference." + ref_prefix + "." + item_ref + "@" + module_name
                xml_item_name.text = item_name
                xml_item_cost.text = item_cost if item_cost !="" else "-"
                xml_item_weight.text = item_weight + " lb." if (item_weight not in ["", "0"]) else "-"

                if item_is_armor:
                    xml_item_ac = etree.SubElement(xml_item, "ac", type="string")
                    xml_item_maxdex = etree.SubElement(xml_item, "maxstatbonus", type="string")
                    xml_item_penalty = etree.SubElement(xml_item, "checkpenalty", type="string")
                    xml_item_fail = etree.SubElement(xml_item, "spellfailure", type="string")
                    xml_speed30 = etree.SubElement(xml_item, "speed30", type="string")
                    xml_speed20 = etree.SubElement(xml_item, "speed20", type="string")

                    xml_item_ac.text = item_armor_bonus if item_armor_bonus != "" else "-"
                    xml_item_maxdex.text = item_max_dex if item_max_dex != "" else "-"
                    xml_item_penalty.text = item_armor_penalty if item_armor_penalty != "" else "-"
                    xml_item_fail.text = item_spell_fail + "%" if item_spell_fail != "" else "-"
                    xml_speed30.text = item_speed30 + " ft." if item_speed30 != "" else "-"
                    xml_speed20.text = item_speed20 + " ft." if item_speed20 != "" else "-"

                if item_is_weapon:
                    xml_item_damage = etree.SubElement(xml_item, "damage", type="string")
                    xml_item_critical = etree.SubElement(xml_item, "critical", type="string")
                    xml_item_range = etree.SubElement(xml_item, "range", type="string")
                    xml_item_prop = etree.SubElement(xml_item, "properties", type="string")
                    xml_item_type = etree.SubElement(xml_item, "damagetype", type="string")

                    xml_item_damage.text = item_damage_m if item_damage_m != "" else "-"
                    xml_item_critical.text = item_critical if item_critical != "" else "-"
                    xml_item_range.text = item_range if item_range != "" else "-"
                    xml_item_prop.text = item_properties if item_properties != "" else "-"
                    xml_item_type.text = item_damage_type if item_damage_type != "" else "-"

                # Link to item stats
                if item_is_armor:
                    xml_ref = etree.SubElement(xml_ref_armor, item_ref)
                elif item_is_weapon:
                    xml_ref = etree.SubElement(xml_ref_weapons, item_ref)
                else:
                    xml_ref = etree.SubElement(xml_ref_equipment, item_ref)
                xml_ref_name = etree.SubElement(xml_ref, "name", type="string")
                xml_ref_name.text = item_name.strip()

                xml_ref_type = etree.SubElement(xml_ref, "type", type="string")
                if item_is_armor:
                    xml_ref_type.text = "Armor"
                    if item_subtype != "":
                        xml_ref_subtype = etree.SubElement(xml_ref, "subtype", type="string")
                        xml_ref_subtype.text = item_subtype
                    if item_armor_bonus != "":
                        xml_ref_ac = etree.SubElement(xml_ref, "ac", type="number")
                        xml_ref_ac.text = item_armor_bonus.strip()
                    if item_max_dex != "":
                        xml_ref_maxdex = etree.SubElement(xml_ref, "maxstatbonus", type="number")
                        xml_ref_maxdex.text = item_max_dex.strip()
                    if item_armor_penalty != "":
                        xml_ref_penalty = etree.SubElement(xml_ref, "checkpenalty", type="number")
                        xml_ref_penalty.text = item_armor_penalty.strip()
                    if item_spell_fail != "":
                        xml_ref_fail = etree.SubElement(xml_ref, "spellfailure", type="number")
                        xml_ref_fail.text = item_spell_fail.strip()
                    if item_speed20 != "":
                        xml_ref_speed20 = etree.SubElement(xml_ref, "speed20", type="number")
                        xml_ref_speed20.text = item_speed20.strip()
                    if item_speed30 != "":
                        xml_ref_speed30 = etree.SubElement(xml_ref, "speed30", type="number")
                        xml_ref_speed30.text = item_speed30.strip()
                    if item_bonus != "":
                        if int(item_bonus) > 0:
                            xml_ref_bonus = etree.SubElement(xml_ref, "bonus", type="number")
                            xml_ref_bonus.text = item_bonus.strip()
                elif item_is_weapon:
                    xml_ref_type.text = "Weapon"
                    if lib_type != "":
                         xml_ref_subtype = etree.SubElement(xml_ref, "subtype", type="string")
                         xml_ref_subtype.text = lib_type
                         if lib_subtype != "":
                            xml_ref_subtype.text += ";" + lib_subtype
                    if item_damage_m != "":
                        xml_ref_damage = etree.SubElement(xml_ref, "damage", type="string")
                        xml_ref_damage.text = item_damage_m.strip()
                    if item_critical != "":
                        xml_ref_crit = etree.SubElement(xml_ref, "critical", type="string")
                        xml_ref_crit.text = item_critical.strip()
                    if item_range not in ["", "0"]:
                        xml_ref_range = etree.SubElement(xml_ref, "range", type="number")
                        xml_ref_range.text = item_range.strip()
                    if item_damage_type != "":
                        xml_ref_damagetype = etree.SubElement(xml_ref, "damagetype", type="string")
                        xml_ref_damagetype.text = item_damage_type.strip()
                    if item_properties != "":
                        xml_ref_prop = etree.SubElement(xml_ref, "properties", type="string")
                        xml_ref_prop.text = item_properties.strip()
                    if item_bonus != "":
                        if int(item_bonus) > 0:
                            xml_ref_bonus = etree.SubElement(xml_ref, "bonus", type="number")
                            xml_ref_bonus.text = item_bonus.strip()
                else:
                    xml_ref_type.text = lib_type
                    if lib_subtype != "":
                        xml_ref_subtype = etree.SubElement(xml_ref, "subtype", type="string")
                        xml_ref_subtype.text = lib_subtype

                if item_cost not in ["", "0"]:
                    xml_ref_cost = etree.SubElement(xml_ref, "cost", type="string")
                    xml_ref_cost.text = item_cost.strip()
                if item_weight not in ["", "0"]:
                    xml_ref_weight = etree.SubElement(xml_ref, "weight", type="number")
                    xml_ref_weight.text = item_weight.strip()
                if item_aura != "":
                    xml_ref_aura = etree.SubElement(xml_ref, "aura", type="string")
                    xml_ref_aura.text = item_aura.strip()
                if item_cl not in ["", "0"]:
                    xml_ref_cl = etree.SubElement(xml_ref, "cl", type="number")
                    xml_ref_cl.text = item_cl.strip()
                if item_reqs != "":
                    xml_ref_reqs = etree.SubElement(xml_ref, "prerequisites", type="string")
                    xml_ref_reqs.text = item_reqs.strip()
                if item_description != "":
                    xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
                    xml_ref_desc.text = item_description.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')



def main():
    xml_root = etree.Element('root', version="2.0")
    xml_libraries = etree.SubElement(xml_root, "library", static="true")
    xml_library = etree.SubElement(xml_libraries, library_tag_name)
    xml_library_name = etree.SubElement(xml_library, "name", type="string")
    xml_library_name.text = library_name
    xml_library_categoryname = etree.SubElement(xml_library, "categoryname", type="string")
    xml_library_categoryname.text = library_category
    xml_library_entries = etree.SubElement(xml_library, "entries")
    xml_reference = etree.SubElement(xml_root, "reference", static="true")
    xml_ref_weapons = etree.SubElement(xml_reference,"weapon")
    xml_ref_armor = etree.SubElement(xml_reference,"armor")
    xml_ref_equipment = etree.SubElement(xml_reference,"equipment")
    xml_lists = etree.SubElement(xml_root, "lists", static="true")

    populate_library_entries(xml_library_entries)
    populate_license(xml_root)

    populate_items(xml_lists, xml_ref_equipment, xml_ref_armor, xml_ref_weapons)

    #populate_weapons(xml_lists, xml_ref_weapons)
    #populate_specific_weapons(xml_lists, xml_ref_weapons)
    #populate_armor(xml_lists, xml_ref_armor)
    #populate_specific_armor(xml_lists, xml_ref_armor)
    #populate_adventuring_gear(xml_lists, xml_ref_equipment)

    generate_xml_deffile()
    generate_xml_dbfile(xml_root)
    generate_module()
    copy_to_Fantasy_Grounds()

if __name__ == '__main__':
    main()