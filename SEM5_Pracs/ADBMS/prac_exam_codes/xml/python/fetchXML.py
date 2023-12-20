import xml.etree.ElementTree as ET

tree = ET.parse("../foodie.xml")
root = tree.getroot()

for food in root.findall("food"):
    print(f"---------------- menu item-----------------")
    print(food.find("name").text)
    print(food.find("calorie").text)
    print(food.find("description").text)

new_food = ET.Element("food")
name = ET.SubElement(new_food,"name")
name.text = "a"

calorie = ET.SubElement(new_food,'calorie')
calorie.text = "1"

description = ET.SubElement(new_food,"description")
description.text = "a1"

root.append(new_food)
tree.write("../foodie.xml")