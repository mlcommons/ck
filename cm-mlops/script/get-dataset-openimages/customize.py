from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    print ("")
    print ("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")
    print ("")

    if os_info['platform'] == 'windows':
        MLPERF_CLASSES=['Airplane','Antelope','Apple','Backpack','Balloon','Banana',
        'Barrel','Baseball bat','Baseball glove','Bee','Beer','Bench','Bicycle',
        'Bicycle helmet','Bicycle wheel','Billboard','Book','Bookcase','Boot',
        'Bottle','Bowl','Bowling equipment','Box','Boy','Brassiere','Bread',
        'Broccoli','Bronze sculpture','Bull','Bus','Bust','Butterfly','Cabinetry',
        'Cake','Camel','Camera','Candle','Candy','Cannon','Canoe','Carrot','Cart',
        'Castle','Cat','Cattle','Cello','Chair','Cheese','Chest of drawers','Chicken',
        'Christmas tree','Coat','Cocktail','Coffee','Coffee cup','Coffee table','Coin',
        'Common sunflower','Computer keyboard','Computer monitor','Convenience store',
        'Cookie','Countertop','Cowboy hat','Crab','Crocodile','Cucumber','Cupboard',
        'Curtain','Deer','Desk','Dinosaur','Dog','Doll','Dolphin','Door','Dragonfly',
        'Drawer','Dress','Drum','Duck','Eagle','Earrings','Egg (Food)','Elephant',
        'Falcon','Fedora','Flag','Flowerpot','Football','Football helmet','Fork',
        'Fountain','French fries','French horn','Frog','Giraffe','Girl','Glasses',
        'Goat','Goggles','Goldfish','Gondola','Goose','Grape','Grapefruit','Guitar',
        'Hamburger','Handbag','Harbor seal','Headphones','Helicopter','High heels',
        'Hiking equipment','Horse','House','Houseplant','Human arm','Human beard',
        'Human body','Human ear','Human eye','Human face','Human foot','Human hair',
        'Human hand','Human head','Human leg','Human mouth','Human nose','Ice cream',
        'Jacket','Jeans','Jellyfish','Juice','Kitchen & dining room table','Kite',
        'Lamp','Lantern','Laptop','Lavender (Plant)','Lemon','Light bulb','Lighthouse',
        'Lily','Lion','Lipstick','Lizard','Man','Maple','Microphone','Mirror',
        'Mixing bowl','Mobile phone','Monkey','Motorcycle','Muffin','Mug','Mule',
        'Mushroom','Musical keyboard','Necklace','Nightstand','Office building',
        'Orange','Owl','Oyster','Paddle','Palm tree','Parachute','Parrot','Pen',
        'Penguin','Personal flotation device','Piano','Picture frame','Pig','Pillow',
        'Pizza','Plate','Platter','Porch','Poster','Pumpkin','Rabbit','Rifle',
        'Roller skates','Rose','Salad','Sandal','Saucer','Saxophone','Scarf','Sea lion',
        'Sea turtle','Sheep','Shelf','Shirt','Shorts','Shrimp','Sink','Skateboard',
        'Ski','Skull','Skyscraper','Snake','Sock','Sofa bed','Sparrow','Spider','Spoon',
        'Sports uniform','Squirrel','Stairs','Stool','Strawberry','Street light',
        'Studio couch','Suit','Sun hat','Sunglasses','Surfboard','Sushi','Swan',
        'Swimming pool','Swimwear','Tank','Tap','Taxi','Tea','Teddy bear','Television',
        'Tent','Tie','Tiger','Tin can','Tire','Toilet','Tomato','Tortoise','Tower',
        'Traffic light','Train','Tripod','Truck','Trumpet','Umbrella','Van','Vase',
        'Vehicle registration plate','Violin','Wall clock','Waste container','Watch',
        'Whale','Wheel','Wheelchair','Whiteboard','Window','Wine','Wine glass','Woman',
        'Zebra','Zucchini']

        x = ''
        for v in MLPERF_CLASSES:
            if x!='': x+=' '
            x+='"'+v+'"'
        env['CM_DATASET_OPENIMAGES_CLASSES']=x

    return {'return': 0}

def postprocess(i):
    env = i['env']

    env['CM_DATASET_ANNOTATIONS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'annotations')

    if env.get('CM_DATASET_CALIBRATION','') == "no":
        env['CM_DATASET_PATH_ROOT'] = os.path.join(os.getcwd(), 'install')
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'validation', 'data')
        annotations_file_path = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-mlperf.json")
        env['CM_DATASET_VALIDATION_ANNOTATIONS_FILE_PATH'] = annotations_file_path
        env['CM_DATASET_ANNOTATIONS_FILE_PATH'] = annotations_file_path
        if env.get("CM_DATASET_OPENIMAGES_CUSTOM_ANNOTATIONS",'') == "yes":
            annotations_file_src = env['CM_DATASET_OPENIMAGES_ANNOTATIONS_FILE_PATH']
            shutil.copy(annotations_file_src, env['CM_DATASET_ANNOTATIONS_DIR_PATH'])
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')
        annotations_file_path = os.path.join(env['CM_DATASET_ANNOTATIONS_DIR_PATH'], "openimages-calibration-mlperf.json")
        env['CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH'] = annotations_file_path


    return {'return': 0}
