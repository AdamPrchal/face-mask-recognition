import xml.etree.ElementTree as ET
import uuid
import os

annotations = os.listdir('dataset/annotations')

for annotation in annotations:
    tree = ET.parse(f'dataset/annotations/{annotation}')
    root = tree.getroot()
    folder = root.findall("./folder")[0].text
    filename = root.findall("./filename")[0].text
    file_path = f'dataset/{folder}/{filename}'
    im = Image.open(file_path)

    for object in root.findall("./object"):
        category = object.find("name").text
        boundary = object.find('bndbox')
        x_min = int(boundary.find('xmin').text)
        y_min = int(boundary.find('ymin').text)
        x_max = int(boundary.find('xmax').text)
        y_max = int(boundary.find('ymax').text)

        box = (x_min, y_min, x_max, y_max)
        region = im.crop(box).convert('RGB')
        new_name = uuid.uuid4().hex

        region.save(f'faces/{category}/{new_name}.jpg')
