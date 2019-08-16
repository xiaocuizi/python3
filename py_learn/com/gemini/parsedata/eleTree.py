import xml.etree.cElementTree as et

tree = et.parse("pom.xml")

root = tree.getroot()

# print(root,root.get("xmlns"))

for ele in root.findall("dependencies"):
    print(ele.text)
