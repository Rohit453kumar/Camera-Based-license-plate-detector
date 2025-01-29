import os
import xml.etree.ElementTree as ET

def voc_to_yolo(voc_dir, yolo_dir, class_name="number_plate"):
    os.makedirs(yolo_dir, exist_ok=True)

    for file in os.listdir(voc_dir):
        if file.endswith(".xml"):
            print(f"Processing: {file}")
            xml_file = os.path.join(voc_dir, file)

            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()

                # Image dimensions
                size = root.find("size")
                if size is None:
                    print(f"Skipping {file}: Missing size information.")
                    continue

                width = int(size.find("width").text)
                height = int(size.find("height").text)

                # YOLO annotations
                yolo_lines = []
                for obj in root.findall("object"):
                    name = obj.find("name").text  # This is the actual plate number
                    print(f"Found plate: {name}")  # Debugging to see plate number

                    # Bounding box
                    bbox = obj.find("bndbox")
                    if bbox is None:
                        print(f"Skipping object in {file}: Missing bounding box.")
                        print('----------------------------------------------------')
                        continue

                    xmin = int(bbox.find("xmin").text)
                    ymin = int(bbox.find("ymin").text)
                    xmax = int(bbox.find("xmax").text)
                    ymax = int(bbox.find("ymax").text)

                    # Convert to YOLO format
                    x_center = ((xmin + xmax) / 2) / width
                    y_center = ((ymin + ymax) / 2) / height
                    box_width = (xmax - xmin) / width
                    box_height = (ymax - ymin) / height

                    # Since all plates belong to the same class, assign ID 0
                    yolo_lines.append(f"0 {x_center} {y_center} {box_width} {box_height}\n")

                # Write YOLO annotations
                if yolo_lines:
                    yolo_file = os.path.join(yolo_dir, file.replace(".xml", ".txt"))
                    with open(yolo_file, "w") as f:
                        f.writelines(yolo_lines)
                else:
                    print(f"No valid annotations for {file}.")
            except Exception as e:
                print(f"Error processing {file}: {e}")
                print('```````````````````````````````````````````````')

# Define your Pascal VOC directory and class name
voc_dir = "D:\\project2\\number plate 1\\images\\video_"  # Replace with your actual VOC folder path
yolo_dir = "D:\\project2\\number plate 1\\images\\yolo_video_images"  # Replace with your desired output folder
voc_to_yolo(voc_dir, yolo_dir, class_name="number_plate")
