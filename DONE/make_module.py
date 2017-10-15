import zipfile
import shutil
import csv
from lxml import etree
import html

# Filenames / paths
module_file_name = "UltimateEqupiment.mod"
xml_definition_file = "definition.xml"
xml_database_file = "db.xml"
license_file = "license.html"
FG_module_directory = "E:\\Fantasy Grounds\\DataDir\\modules"
weapons_file = "weapons.csv"
specific_weapons_file = "Specific Magic Weapons.csv"
armor_file = "armor.csv"
specific_armor_file = "Specific Magic Armor.csv"
adventure_gear_file = "Adventuring Gear.csv"

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
                    "Record name": "lists.Artifacts@"+module_name},
                    {"Entry name":"Art objects",
                    "Entry tag":"AE.Art",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Art@"+module_name},
                    {"Entry name":"Gear - Adventuring Gear",
                    "Entry tag":"GA.AdventuringGear",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.AdventuringGear@"+module_name},
                    {"Entry name":"Gear - Tools and Skill Kits",
                    "Entry tag":"GB.Tools",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Tools@"+module_name},
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
                    "Record name": "lists.AlcRemedies@"+module_name},
                    {"Entry name":"Gear - Alchemical Tools",
                    "Entry tag":"GI.AlcTools",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.AlcTools@"+module_name},
                    {"Entry name":"Gear - Alchemical Weapons",
                    "Entry tag":"GJ.AlcWeapons",
                    "Link type":"librarylink",
                    "Window class":"reference_weapontablelist",
                    "Record name": "lists.AlcWeapons@"+module_name},
                     {"Entry name":"Gear - Poisons",
                    "Entry tag":"GK.Poisons",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Poisons@"+module_name},
                     {"Entry name":"Gems",
                    "Entry tag":"GK.Gems",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Gems@"+module_name},
                     {"Entry name":"Intelligent Items",
                    "Entry tag":"IA.Intel",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Intel@"+module_name},
                    {"Entry name":"Oils and Potions",
                    "Entry tag":"OA.Potions",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Potions@"+module_name},
                    {"Entry name":"Rings",
                    "Entry tag":"RA.Rings",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Rings@"+module_name},
                    {"Entry name":"Rods",
                    "Entry tag":"RB.Rods",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Rods@"+module_name},
                     {"Entry name":"Scrolls",
                    "Entry tag":"SA.Scrolls",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Scrolls@"+module_name},
                     {"Entry name":"Staves",
                    "Entry tag":"SB.Staves",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Staves@"+module_name},
                     {"Entry name":"Wands",
                    "Entry tag":"WA.Wands",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Wands@"+module_name},
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
                    "Record name": "lists.Belts@"+module_name},
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

def populate_weapons(xml_lists, xml_reference):
    xml_list_weapons = etree.SubElement(xml_lists,"Weapons")
    xml_list_weapons_description = etree.SubElement(xml_list_weapons, "description", type="string")
    xml_list_weapons_description.text = "Weapons"
    xml_list_weapons_groups = etree.SubElement(xml_list_weapons, "groups")
    with open(weapons_file, 'r',encoding="utf-8") as file:
        csvreader = csv.reader(file, delimiter="\t", quotechar='"')
        csvreader.__next__()
        previous_type = "AAAA"
        previous_subtype = "AAAA"
        section_number = 0
        weapon_number = 0
        for row in csvreader:
            (weapon_type, weapon_subtype, weapon_name, weapon_cost,
            weapon_damage_s, weapon_damage_m, weapon_critical, weapon_range,
            weapon_weight, weapon_damage_type, weapon_prop, weapon_desc)  = row
            weapon_number += 1
            if (weapon_type != previous_type) or (weapon_subtype != previous_subtype):
                previous_type = weapon_type
                previous_subtype = weapon_subtype
                section_number += 1
                xml_weapon_section = etree.SubElement(xml_list_weapons_groups, "section"+'{:03d}'.format(section_number))
                xml_weapon_section_desc = etree.SubElement(xml_weapon_section, "description", type="string")
                xml_weapon_section_desc.text = weapon_type
                xml_weapon_section_subdesc = etree.SubElement(xml_weapon_section, "subdescription", type ="string")
                xml_weapon_section_subdesc.text = weapon_subtype
                xml_weapon_section_weapons = etree.SubElement(xml_weapon_section, "weapons")
            weapon_ref = "weapon" + "{:04d}".format(weapon_number)
            xml_weapon = etree.SubElement(xml_weapon_section_weapons, weapon_ref)
            xml_weapon_link = etree.SubElement(xml_weapon, "link", type="windowreference")
            xml_weapon_link_class = etree.SubElement(xml_weapon_link, "class")
            xml_weapon_link_class.text = "referenceweapon"
            xml_weapon_link_recordname = etree.SubElement(xml_weapon_link, "recordname")
            xml_weapon_link_recordname.text = weapon_name
            xml_weapon_link_recordname.text = "reference.weapon." + weapon_ref + "@" + module_name
            xml_weapon_name = etree.SubElement(xml_weapon, "name", type="string")
            xml_weapon_name.text = weapon_name
            xml_weapon_cost = etree.SubElement(xml_weapon, "cost", type="string")
            xml_weapon_cost.text = weapon_cost if weapon_cost != "" else "-"
            xml_weapon_weight = etree.SubElement(xml_weapon, "weight", type="string")
            xml_weapon_weight.text = weapon_weight + " lb." if weapon_weight != "" else "-"
            xml_weapon_damage = etree.SubElement(xml_weapon, "damage", type="string")
            xml_weapon_damage.text = weapon_damage_m if weapon_damage_m != "" else "-"
            xml_weapon_critical = etree.SubElement(xml_weapon, "critical", type="string")
            xml_weapon_critical.text = weapon_critical if weapon_critical != "" else "-"
            xml_weapon_range = etree.SubElement(xml_weapon, "range", type="string")
            xml_weapon_range.text = weapon_range if weapon_range != "" else "-"
            xml_weapon_damagetype = etree.SubElement(xml_weapon, "damagetype", type="string")
            xml_weapon_damagetype.text = weapon_damage_type if weapon_damage_type != "" else "-"
            xml_weapon_properties = etree.SubElement(xml_weapon, "properties", type="string")
            xml_weapon_properties.text = weapon_prop if weapon_prop != "" else "-"

            xml_ref_weapon_reftag = etree.SubElement(xml_reference, weapon_ref)
            xml_ref_weapon_ref_name = etree.SubElement(xml_ref_weapon_reftag, "name", type="string")
            xml_ref_weapon_ref_cost = etree.SubElement(xml_ref_weapon_reftag, "cost", type="string")
            xml_ref_weapon_ref_weight = etree.SubElement(xml_ref_weapon_reftag, "weight", type="number")
            xml_ref_weapon_ref_damage = etree.SubElement(xml_ref_weapon_reftag, "damage", type="string")
            xml_ref_weapon_ref_crit = etree.SubElement(xml_ref_weapon_reftag, "critical", type="string")
            xml_ref_weapon_ref_range = etree.SubElement(xml_ref_weapon_reftag, "range", type="number")
            xml_ref_weapon_ref_damtype = etree.SubElement(xml_ref_weapon_reftag, "damagetype", type="string")
            xml_ref_weapon_ref_prop = etree.SubElement(xml_ref_weapon_reftag, "properties", type="string")
            xml_ref_weapon_ref_type = etree.SubElement(xml_ref_weapon_reftag, "type", type="string")
            xml_ref_weapon_ref_subtype = etree.SubElement(xml_ref_weapon_reftag, "subtype", type="string")
            xml_ref_weapon_ref_desc = etree.SubElement(xml_ref_weapon_reftag, "description", type="formattedtext")
            xml_ref_weapon_ref_name.text = weapon_name
            xml_ref_weapon_ref_cost.text = weapon_cost if weapon_cost != "" else "0 gp"
            xml_ref_weapon_ref_weight.text = weapon_weight if weapon_weight != "" else "0"
            xml_ref_weapon_ref_damage.text = weapon_damage_m
            xml_ref_weapon_ref_crit.text = weapon_critical
            xml_ref_weapon_ref_range.text = weapon_range if weapon_range != "" else "0"
            xml_ref_weapon_ref_damtype.text = weapon_damage_type
            xml_ref_weapon_ref_prop.text = weapon_prop
            xml_ref_weapon_ref_type.text = "Weapon"
            xml_ref_weapon_ref_subtype.text = weapon_type + (";" + weapon_subtype if weapon_subtype != "" else "")
            xml_ref_weapon_ref_desc.text = weapon_desc.replace('–','-').replace('—','-')


def populate_specific_weapons(xml_lists, xml_reference):
    xml_list_weapons = etree.SubElement(xml_lists,"SpecificMagicWeapons")
    xml_list_weapons_description = etree.SubElement(xml_list_weapons, "description", type="string")
    xml_list_weapons_description.text = "Specific Magic Weapons"
    xml_list_weapons_groups = etree.SubElement(xml_list_weapons, "groups")
    with open(specific_weapons_file, 'r',encoding="utf-8") as file:
        csvreader = csv.reader(file, delimiter="\t", quotechar='"')
        csvreader.__next__()
        previous_type = "AAAA"
        previous_subtype = "AAAA"
        section_number = 0
        weapon_number = 0
        for row in csvreader:
            (weapon_type, weapon_subtype, weapon_name, weapon_cost,
            weapon_damage_s, weapon_damage_m, weapon_critical, weapon_range,
            weapon_weight, weapon_damage_type, weapon_prop, weapon_desc,
            weapon_bonus, weapon_cl, weapon_req, weapon_aura)  = row
            weapon_number += 1
            if (weapon_type != previous_type) or (weapon_subtype != previous_subtype):
                previous_type = weapon_type
                previous_subtype = weapon_subtype
                section_number += 1
                xml_weapon_section = etree.SubElement(xml_list_weapons_groups, "section"+'{:03d}'.format(section_number))
                xml_weapon_section_desc = etree.SubElement(xml_weapon_section, "description", type="string")
                xml_weapon_section_desc.text = weapon_type
                xml_weapon_section_subdesc = etree.SubElement(xml_weapon_section, "subdescription", type ="string")
                xml_weapon_section_subdesc.text = weapon_subtype
                xml_weapon_section_weapons = etree.SubElement(xml_weapon_section, "weapons")
            weapon_ref = "SpecificWeapon" + "{:04d}".format(weapon_number)
            xml_weapon = etree.SubElement(xml_weapon_section_weapons, weapon_ref)
            xml_weapon_link = etree.SubElement(xml_weapon, "link", type="windowreference")
            xml_weapon_link_class = etree.SubElement(xml_weapon_link, "class")
            xml_weapon_link_class.text = "item"
            xml_weapon_link_recordname = etree.SubElement(xml_weapon_link, "recordname")
            xml_weapon_link_recordname.text = weapon_name
            xml_weapon_link_recordname.text = "reference.weapon." + weapon_ref + "@" + module_name
            xml_weapon_name = etree.SubElement(xml_weapon, "name", type="string")
            xml_weapon_name.text = weapon_name
            xml_weapon_cost = etree.SubElement(xml_weapon, "cost", type="string")
            xml_weapon_cost.text = weapon_cost if weapon_cost != "" else "-"
            xml_weapon_weight = etree.SubElement(xml_weapon, "weight", type="string")
            xml_weapon_weight.text = weapon_weight + " lb." if weapon_weight != "" else "-"
            xml_weapon_damage = etree.SubElement(xml_weapon, "damage", type="string")
            xml_weapon_damage.text = weapon_damage_m if weapon_damage_m != "" else "-"
            xml_weapon_critical = etree.SubElement(xml_weapon, "critical", type="string")
            xml_weapon_critical.text = weapon_critical if weapon_critical != "" else "-"
            xml_weapon_range = etree.SubElement(xml_weapon, "range", type="string")
            xml_weapon_range.text = weapon_range if weapon_range != "" else "-"
            xml_weapon_damagetype = etree.SubElement(xml_weapon, "damagetype", type="string")
            xml_weapon_damagetype.text = weapon_damage_type if weapon_damage_type != "" else "-"
            xml_weapon_properties = etree.SubElement(xml_weapon, "properties", type="string")
            xml_weapon_properties.text = weapon_prop if weapon_prop != "" else "-"

            xml_ref_weapon_reftag = etree.SubElement(xml_reference, weapon_ref)
            xml_ref_weapon_ref_name = etree.SubElement(xml_ref_weapon_reftag, "name", type="string")
            xml_ref_weapon_ref_cost = etree.SubElement(xml_ref_weapon_reftag, "cost", type="string")
            xml_ref_weapon_ref_weight = etree.SubElement(xml_ref_weapon_reftag, "weight", type="number")
            xml_ref_weapon_ref_damage = etree.SubElement(xml_ref_weapon_reftag, "damage", type="string")
            xml_ref_weapon_ref_crit = etree.SubElement(xml_ref_weapon_reftag, "critical", type="string")
            xml_ref_weapon_ref_range = etree.SubElement(xml_ref_weapon_reftag, "range", type="number")
            xml_ref_weapon_ref_damtype = etree.SubElement(xml_ref_weapon_reftag, "damagetype", type="string")
            xml_ref_weapon_ref_prop = etree.SubElement(xml_ref_weapon_reftag, "properties", type="string")
            xml_ref_weapon_ref_type = etree.SubElement(xml_ref_weapon_reftag, "type", type="string")
            xml_ref_weapon_ref_subtype = etree.SubElement(xml_ref_weapon_reftag, "subtype", type="string")
            xml_ref_weapon_ref_desc = etree.SubElement(xml_ref_weapon_reftag, "description", type="formattedtext")
            xml_ref_weapon_ref_name.text = weapon_name
            xml_ref_weapon_ref_cost.text = weapon_cost if weapon_cost != "" else "0 gp"
            xml_ref_weapon_ref_weight.text = weapon_weight if weapon_weight != "" else "0"
            xml_ref_weapon_ref_damage.text = weapon_damage_m
            xml_ref_weapon_ref_crit.text = weapon_critical
            xml_ref_weapon_ref_range.text = weapon_range if weapon_range != "" else "0"
            xml_ref_weapon_ref_damtype.text = weapon_damage_type
            xml_ref_weapon_ref_prop.text = weapon_prop
            xml_ref_weapon_ref_type.text = "Weapon"
            xml_ref_weapon_ref_subtype.text = weapon_type + (";" + weapon_subtype if weapon_subtype != "" else "")
            xml_ref_weapon_ref_desc.text = weapon_desc.replace('–','-').replace('—','-')

            if int(weapon_bonus) > 0:
                xml_ref_weapon_ref_aura = etree.SubElement(xml_ref_weapon_reftag, "aura", type="string")
                xml_ref_weapon_ref_cl = etree.SubElement(xml_ref_weapon_reftag, "cl", type="number")
                xml_ref_weapon_ref_req = etree.SubElement(xml_ref_weapon_reftag, "prerequisites", type="string")
                xml_ref_weapon_ref_bonus = etree.SubElement(xml_ref_weapon_reftag, "bonus", type="number")
                xml_ref_weapon_ref_aura.text = weapon_aura
                xml_ref_weapon_ref_cl.text = weapon_cl
                xml_ref_weapon_ref_req.text = weapon_req
                xml_ref_weapon_ref_bonus.text = weapon_bonus


def populate_armor(xml_lists, xml_reference):
    xml_list_armors = etree.SubElement(xml_lists,"Armor")
    xml_list_armors_description = etree.SubElement(xml_list_armors, "description", type="string")
    xml_list_armors_description.text = "Armor"
    xml_list_armors_groups = etree.SubElement(xml_list_armors, "groups")
    with open(armor_file, 'r',encoding="utf-8") as file:
        csvreader = csv.reader(file, delimiter="\t", quotechar='"')
        csvreader.__next__()
        previous_type = "AAAA"
        section_number = 0
        armor_number = 0
        for row in csvreader:
            (armor_type, armor_name, armor_cost, armor_bonus,
            armor_maxdex, armor_penalty, armor_spellfail,
            armor_sp30, armor_sp20, armor_weight, armor_desc) = row
            armor_number += 1
            armor_ref = "Armor" + "{:04d}".format(armor_number)
            if armor_type != previous_type:
                previous_type = armor_type
                section_number += 1
                xml_armor_section = etree.SubElement(xml_list_armors_groups, "section"+'{:03d}'.format(section_number))
                xml_armor_section_desc = etree.SubElement(xml_armor_section, "description", type="string")
                xml_armor_section_armor = etree.SubElement(xml_armor_section, "armor")
            xml_armor_section_armor_node = etree.SubElement(xml_armor_section_armor, armor_ref)
            xml_armor_section_armor_node_link = etree.SubElement(xml_armor_section_armor_node, "link", type="windowreference")
            xml_armor_section_armor_node_link_class = etree.SubElement(xml_armor_section_armor_node_link, "class")
            xml_armor_section_armor_node_link_recordname = etree.SubElement(xml_armor_section_armor_node_link, "recordname")
            xml_armor_section_armor_node_name = etree.SubElement(xml_armor_section_armor_node, "name", type="string")
            xml_armor_section_armor_node_cost = etree.SubElement(xml_armor_section_armor_node, "cost", type="string")
            xml_armor_section_armor_node_weight = etree.SubElement(xml_armor_section_armor_node, "weight", type="string")
            xml_armor_section_armor_node_ac = etree.SubElement(xml_armor_section_armor_node, "ac", type="string")
            xml_armor_section_armor_node_maxstatbonus = etree.SubElement(xml_armor_section_armor_node, "maxstatbonus", type="string")
            xml_armor_section_armor_node_checkpenalty = etree.SubElement(xml_armor_section_armor_node, "checkpenalty", type="string")
            xml_armor_section_armor_node_spellfailure = etree.SubElement(xml_armor_section_armor_node, "spellfailure", type="string")
            xml_armor_section_armor_node_speed30 = etree.SubElement(xml_armor_section_armor_node, "speed30", type="string")
            xml_armor_section_armor_node_speed20 = etree.SubElement(xml_armor_section_armor_node, "speed20", type="string")
            #xml_armor_section_armor_node_properties = etree.SubElement(xml_armor_section_armor_node, "properties", type="string")
            xml_armor_section_desc.text = armor_type
            xml_armor_section_armor_node_link_class.text = "referencearmor"
            xml_armor_section_armor_node_link_recordname.text = "reference.armor."+armor_ref+"@"+module_name
            xml_armor_section_armor_node_name.text = armor_name
            xml_armor_section_armor_node_cost.text = armor_cost
            xml_armor_section_armor_node_weight.text = armor_weight + "lb." if armor_weight != "" else "-"
            xml_armor_section_armor_node_ac.text = armor_bonus if armor_bonus != "" else "-"
            xml_armor_section_armor_node_maxstatbonus.text =  armor_maxdex if armor_maxdex != "" else "-"
            xml_armor_section_armor_node_checkpenalty.text =  armor_penalty if armor_penalty != "" else "-"
            xml_armor_section_armor_node_spellfailure.text = armor_spellfail + "%" if armor_spellfail != "" else "-"
            xml_armor_section_armor_node_speed30.text = armor_sp30 + " ft."  if armor_sp30 != "" else "-"
            xml_armor_section_armor_node_speed20.text = armor_sp20 + " ft."  if armor_sp20 != "" else "-"
            #xml_armor_section_armor_node_properties.text = ""

            xml_ref_armor_ref = etree.SubElement(xml_reference, armor_ref)
            xml_ref_armor_name = etree.SubElement(xml_ref_armor_ref, "name", type="string")
            xml_ref_armor_cost = etree.SubElement(xml_ref_armor_ref, "cost", type="string")
            xml_ref_armor_weight = etree.SubElement(xml_ref_armor_ref, "weight", type="number")
            xml_ref_armor_ac = etree.SubElement(xml_ref_armor_ref, "ac", type="number")
            xml_ref_armor_maxstatbonus = etree.SubElement(xml_ref_armor_ref, "maxstatbonus", type="number")
            xml_ref_armor_checkpenalty = etree.SubElement(xml_ref_armor_ref, "checkpenalty", type="number")
            xml_ref_armor_spellfailure = etree.SubElement(xml_ref_armor_ref, "spellfailure", type="number")
            xml_ref_armor_speed30 = etree.SubElement(xml_ref_armor_ref, "speed30", type="number")
            xml_ref_armor_speed20 = etree.SubElement(xml_ref_armor_ref, "speed20", type="number")
            #xml_ref_armor_properties = etree.SubElement(xml_ref_armor_ref, "properties", type="string")
            xml_ref_armor_type = etree.SubElement(xml_ref_armor_ref, "type", type="string")
            xml_ref_armor_subtype = etree.SubElement(xml_ref_armor_ref, "subtype", type="string")
            xml_ref_armor_description = etree.SubElement(xml_ref_armor_ref, "description", type="formattedtext")
            xml_ref_armor_name.text = armor_name
            xml_ref_armor_cost.text = armor_cost
            xml_ref_armor_weight.text = armor_weight
            xml_ref_armor_ac.text = armor_bonus if armor_bonus != "" else "0"
            xml_ref_armor_maxstatbonus.text = armor_maxdex if armor_maxdex != "" else "0"
            xml_ref_armor_checkpenalty.text = armor_penalty if armor_penalty != "" else "0"
            xml_ref_armor_spellfailure.text = armor_spellfail + "%" if armor_spellfail != "" else "0"
            xml_ref_armor_speed30.text = armor_sp30 + " ft."  if armor_sp30 != "" else "0"
            xml_ref_armor_speed20.text = armor_sp30 + " ft."  if armor_sp30 != "" else "0"
            #xml_ref_armor_properties.text =
            xml_ref_armor_type.text = "Armor"
            xml_ref_armor_subtype.text = armor_type
            xml_ref_armor_description.text = armor_desc.replace('–','-').replace('—','-')


def populate_specific_armor(xml_lists, xml_reference):
    xml_list_armors = etree.SubElement(xml_lists,"SpecificMagicArmor")
    xml_list_armors_description = etree.SubElement(xml_list_armors, "description", type="string")
    xml_list_armors_description.text = "Specific Magic Armor"
    xml_list_armors_groups = etree.SubElement(xml_list_armors, "groups")
    with open(specific_armor_file, 'r',encoding="utf-8") as file:
        csvreader = csv.reader(file, delimiter="\t", quotechar='"')
        csvreader.__next__()
        previous_type = "AAAA"
        section_number = 0
        armor_number = 0
        for row in csvreader:
            (armor_type, armor_name, armor_cost, armor_bonus,
            armor_maxdex, armor_penalty, armor_spellfail,
            armor_sp30, armor_sp20, armor_weight, armor_desc,
            armor_bonus, armor_cl, armor_aura, armor_req) = row
            armor_number += 1
            armor_ref = "SpecificArmor" + "{:04d}".format(armor_number)
            if armor_type != previous_type:
                previous_type = armor_type
                section_number += 1
                xml_armor_section = etree.SubElement(xml_list_armors_groups, "section"+'{:03d}'.format(section_number))
                xml_armor_section_desc = etree.SubElement(xml_armor_section, "description", type="string")
                xml_armor_section_armor = etree.SubElement(xml_armor_section, "armor")
            xml_armor_section_armor_node = etree.SubElement(xml_armor_section_armor, armor_ref)
            xml_armor_section_armor_node_link = etree.SubElement(xml_armor_section_armor_node, "link", type="windowreference")
            xml_armor_section_armor_node_link_class = etree.SubElement(xml_armor_section_armor_node_link, "class")
            xml_armor_section_armor_node_link_recordname = etree.SubElement(xml_armor_section_armor_node_link, "recordname")
            xml_armor_section_armor_node_name = etree.SubElement(xml_armor_section_armor_node, "name", type="string")
            xml_armor_section_armor_node_cost = etree.SubElement(xml_armor_section_armor_node, "cost", type="string")
            xml_armor_section_armor_node_weight = etree.SubElement(xml_armor_section_armor_node, "weight", type="string")
            xml_armor_section_armor_node_ac = etree.SubElement(xml_armor_section_armor_node, "ac", type="string")
            xml_armor_section_armor_node_maxstatbonus = etree.SubElement(xml_armor_section_armor_node, "maxstatbonus", type="string")
            xml_armor_section_armor_node_checkpenalty = etree.SubElement(xml_armor_section_armor_node, "checkpenalty", type="string")
            xml_armor_section_armor_node_spellfailure = etree.SubElement(xml_armor_section_armor_node, "spellfailure", type="string")
            xml_armor_section_armor_node_speed30 = etree.SubElement(xml_armor_section_armor_node, "speed30", type="string")
            xml_armor_section_armor_node_speed20 = etree.SubElement(xml_armor_section_armor_node, "speed20", type="string")
            #xml_armor_section_armor_node_properties = etree.SubElement(xml_armor_section_armor_node, "properties", type="string")
            xml_armor_section_desc.text = armor_type
            xml_armor_section_armor_node_link_class.text = "item"
            xml_armor_section_armor_node_link_recordname.text = "reference.armor."+armor_ref+"@"+module_name
            xml_armor_section_armor_node_name.text = armor_name
            xml_armor_section_armor_node_cost.text = armor_cost
            xml_armor_section_armor_node_weight.text = armor_weight + "lb." if armor_weight != "" else "-"
            xml_armor_section_armor_node_ac.text = armor_bonus if armor_bonus != "" else "-"
            xml_armor_section_armor_node_maxstatbonus.text =  armor_maxdex if armor_maxdex != "" else "-"
            xml_armor_section_armor_node_checkpenalty.text =  armor_penalty if armor_penalty != "" else "-"
            xml_armor_section_armor_node_spellfailure.text = armor_spellfail + "%" if armor_spellfail != "" else "-"
            xml_armor_section_armor_node_speed30.text = armor_sp30 + " ft."  if armor_sp30 != "" else "-"
            xml_armor_section_armor_node_speed20.text = armor_sp20 + " ft."  if armor_sp20 != "" else "-"
            #xml_armor_section_armor_node_properties.text = ""

            xml_ref_armor_ref = etree.SubElement(xml_reference, armor_ref)
            xml_ref_armor_name = etree.SubElement(xml_ref_armor_ref, "name", type="string")
            xml_ref_armor_cost = etree.SubElement(xml_ref_armor_ref, "cost", type="string")
            xml_ref_armor_weight = etree.SubElement(xml_ref_armor_ref, "weight", type="number")
            xml_ref_armor_ac = etree.SubElement(xml_ref_armor_ref, "ac", type="number")
            xml_ref_armor_maxstatbonus = etree.SubElement(xml_ref_armor_ref, "maxstatbonus", type="number")
            xml_ref_armor_checkpenalty = etree.SubElement(xml_ref_armor_ref, "checkpenalty", type="number")
            xml_ref_armor_spellfailure = etree.SubElement(xml_ref_armor_ref, "spellfailure", type="number")
            xml_ref_armor_speed30 = etree.SubElement(xml_ref_armor_ref, "speed30", type="number")
            xml_ref_armor_speed20 = etree.SubElement(xml_ref_armor_ref, "speed20", type="number")
            #xml_ref_armor_properties = etree.SubElement(xml_ref_armor_ref, "properties", type="string")
            xml_ref_armor_type = etree.SubElement(xml_ref_armor_ref, "type", type="string")
            xml_ref_armor_subtype = etree.SubElement(xml_ref_armor_ref, "subtype", type="string")
            xml_ref_armor_description = etree.SubElement(xml_ref_armor_ref, "description", type="formattedtext")
            xml_ref_armor_name.text = armor_name
            xml_ref_armor_cost.text = armor_cost
            xml_ref_armor_weight.text = armor_weight
            xml_ref_armor_ac.text = armor_bonus if armor_bonus != "" else "0"
            xml_ref_armor_maxstatbonus.text = armor_maxdex if armor_maxdex != "" else "0"
            xml_ref_armor_checkpenalty.text = armor_penalty if armor_penalty != "" else "0"
            xml_ref_armor_spellfailure.text = armor_spellfail + "%" if armor_spellfail != "" else "0"
            xml_ref_armor_speed30.text = armor_sp30 + " ft."  if armor_sp30 != "" else "0"
            xml_ref_armor_speed20.text = armor_sp30 + " ft."  if armor_sp30 != "" else "0"
            #xml_ref_armor_properties.text = "masterwork"
            xml_ref_armor_type.text = "Armor"
            xml_ref_armor_subtype.text = armor_type
            xml_ref_armor_description.text = armor_desc.replace('–','-').replace('—','-')

            if int(armor_bonus) > 0:
                xml_ref_armor_ref_aura = etree.SubElement(xml_ref_armor_ref, "aura", type="string")
                xml_ref_armor_ref_cl = etree.SubElement(xml_ref_armor_ref, "cl", type="number")
                xml_ref_armor_ref_req = etree.SubElement(xml_ref_armor_ref, "prerequisites", type="string")
                xml_ref_armor_ref_bonus = etree.SubElement(xml_ref_armor_ref, "bonus", type="number")
                xml_ref_armor_ref_aura.text = armor_aura
                xml_ref_armor_ref_cl.text = armor_cl
                xml_ref_armor_ref_req.text = armor_req
                xml_ref_armor_ref_bonus.text = armor_bonus


def populate_adventuring_gear(xml_lists, xml_reference):
    xml_list_gear = etree.SubElement(xml_lists,"AdventuringGear")
    xml_list_gear_description = etree.SubElement(xml_list_gear, "description", type="string")
    xml_list_gear_description.text = "Adventuring Gear"
    xml_list_gear_groups = etree.SubElement(xml_list_gear, "groups")
    xml_list_gear_section = etree.SubElement(xml_list_gear_groups, "section001")
    xml_list_gear_sec_description = etree.SubElement(xml_list_gear_section, "description", type="string")
    xml_list_gear_sec_description.text = "Adventuring Gear"
    xml_list_gear_sec_equipment = etree.SubElement(xml_list_gear_section, "equipment")
    item_number = 0
    with open(adventure_gear_file, 'r',encoding="utf-8") as file:
        csvreader = csv.reader(file, delimiter="\t", quotechar='"')
        for row in csvreader:
            (gear_name, gear_cost, gear_weight, gear_desc) = row
            item_number += 1
            item_ref = "AdvGear" + "{:04d}".format(item_number)
            xml_list_gear_sec_eq_ref = etree.SubElement(xml_list_gear_sec_equipment, item_ref)
            xml_list_gear_sec_eq_ref_link = etree.SubElement(xml_list_gear_sec_eq_ref, "link", type="windowreference")
            xml_list_gear_sec_eq_ref_link_class = etree.SubElement(xml_list_gear_sec_eq_ref_link, "class")
            xml_list_gear_sec_eq_ref_link_recname = etree.SubElement(xml_list_gear_sec_eq_ref_link, "recordname")
            xml_list_gear_sec_eq_ref_name = etree.SubElement(xml_list_gear_sec_eq_ref, "name", type="string")
            xml_list_gear_sec_eq_ref_cost = etree.SubElement(xml_list_gear_sec_eq_ref, "cost", type="string")
            xml_list_gear_sec_eq_ref_weight = etree.SubElement(xml_list_gear_sec_eq_ref, "weight", type="string")
            xml_list_gear_sec_eq_ref_link_class.text = "referenceequipment"
            xml_list_gear_sec_eq_ref_link_recname.text = "reference.equipment." + item_ref + "@" + module_name
            xml_list_gear_sec_eq_ref_name.text = gear_name
            xml_list_gear_sec_eq_ref_cost.text = gear_cost
            xml_list_gear_sec_eq_ref_weight.text = gear_weight + " lb."

            xml_ref_gear_ref = etree.SubElement(xml_reference, item_ref)
            xml_ref_gear_name = etree.SubElement(xml_ref_gear_ref, "name", type="string")
            xml_ref_gear_cost = etree.SubElement(xml_ref_gear_ref, "cost", type="string")
            xml_ref_gear_weight = etree.SubElement(xml_ref_gear_ref, "weight", type="number")
            xml_ref_gear_type = etree.SubElement(xml_ref_gear_ref, "type", type="string")
            xml_ref_gear_subtype = etree.SubElement(xml_ref_gear_ref, "subtype", type="string")
            xml_ref_gear_desc = etree.SubElement(xml_ref_gear_ref, "description", type="formattedtext")
            xml_ref_gear_name.text = gear_name
            xml_ref_gear_cost.text = gear_cost
            xml_ref_gear_weight.text = gear_weight
            xml_ref_gear_type.text = "Gear"
            xml_ref_gear_subtype.text = "Adventuring Gear"
            xml_ref_gear_desc.text = gear_desc.replace('–','-').replace('—','-').replace('\ufffd','×')



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

def main():
    xml_root = etree.Element('root', version="2.0")
    xml_libraries = etree.SubElement(xml_root, "library", static="true")
    xml_library = etree.SubElement(xml_libraries, library_tag_name)
    xml_library_name = etree.SubElement(xml_library, "name", type="string")
    xml_library_name.text = library_name
    xml_library_categoryname = etree.SubElement(xml_library, "categoryname", type="string")
    xml_library_categoryname.text = library_category
    xml_library_entries = etree.SubElement(xml_library, "entries")

    populate_library_entries(xml_library_entries)
    populate_license(xml_root)
    xml_reference = etree.SubElement(xml_root, "reference", static="true")
    xml_ref_weapons = etree.SubElement(xml_reference,"weapon")
    xml_ref_armor = etree.SubElement(xml_reference,"armor")
    xml_ref_equipment = etree.SubElement(xml_reference,"equipment")
    xml_lists = etree.SubElement(xml_root, "lists", static="true")

    populate_weapons(xml_lists, xml_ref_weapons)
    populate_specific_weapons(xml_lists, xml_ref_weapons)
    populate_armor(xml_lists, xml_ref_armor)
    populate_specific_armor(xml_lists, xml_ref_armor)
    populate_adventuring_gear(xml_lists, xml_ref_equipment)

    generate_xml_deffile()
    generate_xml_dbfile(xml_root)
    generate_module()
    copy_to_Fantasy_Grounds()

if __name__ == '__main__':
    main()