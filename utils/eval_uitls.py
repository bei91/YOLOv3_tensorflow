import numpy as np

def label_extractor( scale ):
    boxes_label = []
    for box in scale:
        box_labels = []
        for i in range( 3 ):
            pretect_x = box[i * 25]
            pretect_y = box[i * 25 + 1]
            pretect_width = box[i * 25 + 2]
            pretect_height = box[i * 25 + 3]
            pretect_objectness = box[i * 25 + 4]
            pretect_class = box[i * 25 + 5: i * 25 + 5 + 20]

            box_label = ( pretect_x, pretect_y, pretect_width, pretect_height, pretect_objectness, pretect_class )
            box_labels.append( box_label )

        boxes_label.append( box_labels )

    return boxes_label

def get_bdboxes( boxes_labels ):
    bdboxes = []
    index = 0
    for box_labels in boxes_labels:
        max = 0
        for i in range( 3 ):
            if box_labels[i][4] > max:
                index = i

        if box_labels[i][4] >= 0.5:
            x = boxes_labels[i][0]
            y = boxes_labels[i][1]
            width = boxes_labels[i][2]
            height = boxes_labels[i][3]
            object_class = get_object_class( boxes_labels[i][5] )

            bdbox = ( x, y, width, height, object_class )

        bdboxes.append( bdbox )

    return bdboxes

def get_object_class( input ):
    max = 0
    index = 0
    for i in range( len( input ) ):
        if input[i] > max:
            index = i

    class_map = {
        5 : 'person',
        6 : 'bird',
        7 : 'cat',
        8 : 'cow',
        9 : 'dog',
        10 : 'horse',
        11 : 'sheep',
        12 : 'aeroplane',
        13 : 'bicycle',
        14 : 'boat',
        15 : 'bus',
        16 : 'car',
        17 : 'motorbike',
        18 : 'train',
        19 : 'bottle',
        20 : 'chair',
        21 : 'diningtable',
        22 : 'pottedplant',
        23 : 'sofa',
        24 : 'tvmonitor'
    }

    class_name = class_map[index]
    return class_name
