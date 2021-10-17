from PIL import Image 
from IPython.display import display 
import random
import json


# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Blue", "Cyan", "Green", "Pink", "Purple"]
background_file_names = ["bg blue","bg cyan","bg green","bg pink","bg purple"]
background_weights = [30, 40, 15, 10, 5]

base = ["Black caramel", "Blonde", "Cyborg", "Delta", "Gamma","Regular", "Steampunk"]
base_file_names = ["black caramel","blonde","cyborg","delta","gamma","regular","steampunk"]
base_weights = [20,22,5,5,5,35,8]

eyes = ["Blue","Brown","Pink","Purple","Yellow","Laser","Crosshair","Robot","Terminator"] 
eyes_file_names = ["regular blue","regular brown","regular pink","regular purple","regular yellow","laser eyes","crosshair","robot","terminator"]
eyes_weights = [15,13,7,10,10,3,5,5,3]

mouth = ["Default","Blunt","Grills","Grin","Metal growl","Growl","Muzzle","Metal open","Open","Tongue"]
mouth_file_names = ["default","blunt","grills","grinning","growl metal teeth","growl","muzzled","open mouth metal","open mouth","tongue out"]
mouth_weights = [40,3,6,9,4,6,6,4,6,10]

eyewear = ["None","Deal with it","Goggles","Monocle","Nerd","Nightvision","Ovals","Pit vipers","Soldoge","Startrek"]
eyewear_file_names = ["none","deal with it","goggles","monocle","nerdy glasses","night vision","oval glasses","pit vipers","soldoge glasses","star trek"]
eyewear_weights = [33,8,6,6,4,6,6,3,6,6]

hair = ["None","Afro","Liberty black","Liberty blue","Liberty green","Liberty pink","Liberty purple","Liberty white","Matrix dreads","Mohawk 1 black","Mohawk 1 blue","Mohawk 1 green","Mohawk 1 pink","Mohawk 1 purple","Mohawk 1 white","Mohawk 2 black", "Mohawk 2 blue", "Mohawk 2 green", "Mohawk 2 pink", "Mohawk 2 purple", "Mohawk 2 white"]
hair_file_names = ["none","afro","liberty spike black","liberty spike blue","liberty spike green","liberty spike pink","liberty spike purple","liberty spike white","matrix dreads","mohawk 1 black","mohawk 1 blue","mohawk 1 green","mohawk 1 pink","mohawk 1 purple","mohawk 1 white", "mohawk 2 black", "mohawk 2 blue", "mohawk 2 green", "mohawk 2 pink", "mohawk 2 purple", "mohawk 2 white"]
hair_weights = [30,3,13,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

clothes = ["None","Astronaut","Camo","Armor","Leather spikes","Solana tank","Tron"]
clothes_file_names = ["none","astronaut","camou","futuristic armor","futuristic leather jacket","solana tank top","tron"]
clothes_weights = [60,7,10,10,5,5,3]

collar = ["None","Chain","Bow-tie black","Bow-tie blue","Bow-tie green","Bow-tie pink","Bow-tie purple","Bow-tie white","Heart","Mr T","SolDoge","Piano tie","Solana tie","Black tie","Blue tie","Green tie","Pink tie","Purple tie","White tie","Spikes"]
collar_file_names = ["none","big chain","bow tie black","bow tie blue","bow tie green","bow tie pink","bow tie purple","bow tie white","heart","mr t","normal","piano tie","short solana tie","short tie black","short tie blue","short tie green","short tie pink","short tie purple","short tie white","spikes"]
collar_weights = [20,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

backpack = ["None","Gun","Jetpack","Rocket","SolDoge backpack"]
backpack_file_names = ["none","futuristic gun","jetpack","rocket","soldoge backpack"]
backpack_weights = [70,15,5,8,3]

headwear = ["None","Astronaut","FTX hat","Cowboy","Jason X","Kitty","Predator","Radar dish","SolDoge","Solana","Steampunk","Tin foil","Top hat","TV"]
headwear_file_names = ["none","astronaut helmet","ftx hat","howboy hat","jason x mask","kitty hat","predator mask","radar dish hat","sdoge hat","solana hat","steampunk hat","tin foil hat","top hat","tv head"]
headwear_weights = [50,4,4,4,4,4,4,4,4,4,4,4,4,4]

## Generate Traits

TOTAL_IMAGES = 30 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 

    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Base"] = random.choices(base, base_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["EyeWear"] = random.choices(eyewear, eyewear_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Clothes"] = random.choices(clothes, clothes_weights)[0]
    new_image ["Collar"] = random.choices(collar, collar_weights)[0]
    new_image ["Backpack"] = random.choices(backpack, background_weights)[0]
    new_image ["Headwear"] = random.choices(headwear, headwear_weights)[0]

    if new_image["Hair"] not in ("None","Matrix dreads") or new_image["Eyes"]=="Laser":
        # can't have headwear
        new_image ["Headwear"] = "None"

    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)
    

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

all_unique = all_images_unique(all_images)
print("Are all images unique?", all_unique)

if not all_unique:
    print("Not all images are unique.")
    exit(1)


# Add token Id to each image
i = 1
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)


# Get Trait Counts

background_count = {}
for item in background:
    background_count[item] = 0
    
base_count = {}
for item in base:
    base_count[item] = 0

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0

mouth_count = {}
for item in mouth:
    mouth_count[item] = 0

eyewear_count = {}
for item in eyewear:
    eyewear_count[item] = 0

hair_count = {}
for item in hair:
    hair_count[item] = 0

clothes_count = {}
for item in clothes:
    clothes_count[item] = 0

collar_count = {}
for item in collar:
    collar_count[item] = 0

backpack_count = {}
for item in backpack:
    backpack_count[item] = 0

headwear_count = {}
for item in headwear:
    headwear_count[item] = 0


for image in all_images:
    background_count[image["Background"]] += 1
    base_count[image["Base"]] += 1
    eyes_count[image["Eyes"]] += 1
    mouth_count[image["Mouth"]] += 1
    eyewear_count[image["EyeWear"]] += 1
    hair_count[image["Hair"]] += 1
    clothes_count[image["Clothes"]] += 1
    collar_count[image["Collar"]] += 1
    backpack_count[image["Backpack"]] += 1
    headwear_count[image["Headwear"]] += 1
    
    
print(background_count)
print(base_count)
print(eyes_count)
print(mouth_count)
print(eyewear_count)
print(hair_count)
print(clothes_count)
print(collar_count)
print(backpack_count)
print(headwear_count)


#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


      
    
#### Generate Images    
for item in all_images:


    bg = Image.open(f'./trait-layers/background/{background_file_names[background.index(item["Background"])]}.png').convert('RGBA')
    base_img = Image.open(f'./trait-layers/base/{base_file_names[base.index(item["Base"])]}.png').convert('RGBA')
    eyes_img = Image.open(f'./trait-layers/eyes/{eyes_file_names[eyes.index(item["Eyes"])]}.png').convert('RGBA')
    
    if item["Mouth"]!="Default":
        mouth_img = Image.open(f'./trait-layers/mouth/{mouth_file_names[mouth.index(item["Mouth"])]}.png').convert('RGBA')

    if item["EyeWear"]!="None":
        eyewear_img = Image.open(f'./trait-layers/eyewear/{eyewear_file_names[eyewear.index(item["EyeWear"])]}.png').convert('RGBA')

    if item["Hair"]!="None":
        hair_img = Image.open(f'./trait-layers/hair/{hair_file_names[hair.index(item["Hair"])]}.png').convert('RGBA')
    
    if item["Clothes"]!="None" and item["Base"] in ("Black caramel","Blonde","Gamma","Regular"):
        clothes_img = Image.open(f'./trait-layers/clothes/{clothes_file_names[clothes.index(item["Clothes"])]}.png').convert('RGBA')
    else:
      item["Clothes"]="None"

    if item["Collar"]!="None":
        collar_img = Image.open(f'./trait-layers/collar/{collar_file_names[collar.index(item["Collar"])]}.png').convert('RGBA')

    if item["Backpack"]!="None":
        backpack_img = Image.open(f'./trait-layers/backpack/{backpack_file_names[backpack.index(item["Backpack"])]}.png').convert('RGBA')

    if item["Headwear"]!="None":
        headwear_img = Image.open(f'./trait-layers/headwear/{headwear_file_names[headwear.index(item["Headwear"])]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(bg, base_img)
    com1 = Image.alpha_composite(com1, eyes_img)

    if item["Mouth"]!="Default":
        com1 = Image.alpha_composite(com1, mouth_img)
    
    if item["EyeWear"]!="None":
        com1 = Image.alpha_composite(com1, eyewear_img)

    if item["Hair"]!="None":
        com1 = Image.alpha_composite(com1, hair_img)

    if item["Clothes"]!="None":
        com1 = Image.alpha_composite(com1, clothes_img)

    if item["Collar"]!="None":
        com1 = Image.alpha_composite(com1, collar_img)

    if item["Backpack"]!="None":
        com1 = Image.alpha_composite(com1, backpack_img)

    if item["Headwear"]!="None":
        com1 = Image.alpha_composite(com1, headwear_img)

    #Convert to RGB
    rgb_im = com1.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)


#### Generate Metadata for each Image    

f = open('./metadata/all-traits.json',) 
data = json.load(f)


IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Base", i["Base"]))
    token["attributes"].append(getAttribute("Eyes", i["Eyes"]))
    token["attributes"].append(getAttribute("Mouth", i["Mouth"]))
    token["attributes"].append(getAttribute("EyeWear", i["EyeWear"]))
    token["attributes"].append(getAttribute("Hair", i["Hair"]))
    token["attributes"].append(getAttribute("Clothes", i["Clothes"]))
    token["attributes"].append(getAttribute("Collar", i["Collar"]))
    token["attributes"].append(getAttribute("Backpack", i["Backpack"]))
    token["attributes"].append(getAttribute("Headwear", i["Headwear"]))
    

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()

