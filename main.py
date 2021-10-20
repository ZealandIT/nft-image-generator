from PIL import Image 
import random
import json
import os.path

METADATA_FILE_NAME = './metadata/all-traits.json'

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Blue", "Cyan", "Green", "Pink", "Purple", "Solana"]
background_file_names = ["bg blue","bg cyan","bg green","bg pink","bg purple", "bg solana"]
background_weights = [0.25, 0.35, 0.18, 0.197, 0.02,0.003]

base = ["Black caramel", "Blonde", "Cyborg", "Delta", "Gamma","Regular", "Steampunk"]
base_file_names = ["black caramel","blonde","cyborg","delta","gamma","regular","steampunk"]
base_weights = [0.12,0.17,0.1,0.095,0.005,0.3,0.1]

eyes = ["Blue","Brown","Pink","Purple","Yellow","Laser","Crosshair","Robot","Terminator"] 
eyes_file_names = ["regular blue","regular brown","regular pink","regular purple","regular yellow","laser eyes","crosshair","robot","terminator"]
eyes_weights = [0.4,0.3,0.025,0.05,0.05,0.025,0.11,0.02,0.02]

mouth = ["Default","Blunt","Grills","Grin","Metal growl","Growl","Muzzle","Metal open","Open","Tongue"]
mouth_file_names = ["default","blunt","grills","grinning","growl metal teeth","growl","muzzled","open mouth metal","open mouth","tongue out"]
mouth_weights = [0.35,0.0625,0.0625,0.1125,0.0625,0.0825,0.0625,0.0925,0.1125,0.0625]

eyewear = ["None","Deal with it","Goggles","Monocle","Nerd","Nightvision","Ovals","Pit vipers","Soldoge","Startrek"]
eyewear_file_names = ["none","deal with it","goggles","monocle","nerdy glasses","night vision","oval glasses","pit vipers","soldoge glasses","star trek"]
eyewear_weights = [0.3, 0.07,0.1,0.15,0.15,0.02,0.075,0.075,0.03,0.03]

hair = ["None","Afro","Liberty black","Liberty blue","Liberty green","Liberty pink","Liberty purple","Liberty white","Matrix dreads","Mohawk 1 black","Mohawk 1 blue","Mohawk 1 green","Mohawk 1 pink","Mohawk 1 purple","Mohawk 1 white","Mohawk 2 black", "Mohawk 2 blue", "Mohawk 2 green", "Mohawk 2 pink", "Mohawk 2 purple", "Mohawk 2 white"]
hair_file_names = ["none","afro","liberty spike black","liberty spike blue","liberty spike green","liberty spike pink","liberty spike purple","liberty spike white","matrix dreads","mohawk 1 black","mohawk 1 blue","mohawk 1 green","mohawk 1 pink","mohawk 1 purple","mohawk 1 white", "mohawk 2 black", "mohawk 2 blue", "mohawk 2 green", "mohawk 2 pink", "mohawk 2 purple", "mohawk 2 white"]
hair_weights = [0.33,0.0004995,0.09,0.09,0.09,0.09,0.09,0.09,0.0095005,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]

clothes = ["None","Astronaut","Camo","Armor","Leather spikes","Solana tank","Tron"]
clothes_file_names = ["none","astronaut","camou","futuristic armor","futuristic leather jacket","solana tank top","tron"]
clothes_weights = [0.5,0.05,0.07,0.08,0.11,0.09,0.1]

collar = ["None","Chain","Bow-tie black","Bow-tie blue","Bow-tie green","Bow-tie pink","Bow-tie purple","Bow-tie white","Heart","Mr T","SolDoge","Piano tie","Solana tie","Black tie","Blue tie","Green tie","Pink tie","Purple tie","White tie","Spikes"]
collar_file_names = ["none","big chain","bow tie black","bow tie blue","bow tie green","bow tie pink","bow tie purple","bow tie white","heart","mr t","normal","piano tie","short solana tie","short tie black","short tie blue","short tie green","short tie pink","short tie purple","short tie white","spikes"]
collar_weights = [0.2,0.075,0.075,0.075,0.075,0.03,0.075,0.075,0.075,0.075,0.005,0.01,0.005,0.009,0.009,0.009,0.009,0.009,0.005,0.1]

backpack = ["None","Gun","Jetpack","Rocket","SolDoge backpack"]
backpack_file_names = ["none","futuristic gun","jetpack","rocket","soldoge backpack"]
backpack_weights = [0.75,0.10,0.05,0.09,0.06]

headwear = ["None","Astronaut","FTX hat","Cowboy","Jason X","Kitty","Predator","Radar dish","SolDoge","Solana","Steampunk","Tin foil","Top hat","TV","Solana earphones","Cone of shame","SDoge helmet","Wizard"]
headwear_file_names = ["none","astronaut helmet","ftx hat","howboy hat","jason x mask","kitty hat","predator mask","radar dish hat","sdoge hat","solana hat","steampunk hat","tin foil hat","top hat","tv head","big earphones","cone of shame","sdoge army helmet","wizard hat"]
headwear_weights = [0.33,0.009995,0.045,0.09,0.09,0.09,0.09,0.09,0.0095005,0.01,0.01,0.01,0.013,0.01,0.085,0.01,0.01,0.01]
headwear_weights_subset = [0.33,0,0.045,0.09,0,0.09,0,0.09,0.0095005,0.01,0.01,0.01,0.01,0,0.085,0.01,0.01,0.01]


if not os.path.isfile(METADATA_FILE_NAME):
    ## Generate Traits

    TOTAL_IMAGES = 1000 # Number of random unique images we want to generate

    all_images = [] 

    # A recursive function to generate unique image combinations
    def create_new_image():
        
        new_image = {} #

        # For each trait category, select a random trait based on the weightings 

        new_image ["Background"] = random.choices(background, background_weights)[0]
        new_image ["Base"] = random.choices(base, base_weights)[0]
        new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
        new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]

        if new_image["Mouth"]=="Muzzle":
            new_image["EyeWear"] = "None"
        else:
            new_image ["EyeWear"] = random.choices(eyewear, eyewear_weights)[0]

        if new_image["Base"] in ("Cyborg","Steampunk"):
            new_image["Hair"] = "None"
        else:
            new_image ["Hair"] = random.choices(hair, hair_weights)[0]

        if not new_image["Base"] in ("Black caramel","Blonde","Gamma","Regular"):
            new_image["Clothes"] = "None"
        else:
            new_image ["Clothes"] = random.choices(clothes, clothes_weights)[0]

        new_image ["Collar"] = random.choices(collar, collar_weights)[0]
        new_image ["Backpack"] = random.choices(backpack, backpack_weights)[0]
        if new_image["Mouth"] in ("Blunt","Tongue") or new_image["EyeWear"]!="None" or new_image["Eyes"]=="Laser":
            new_image["Headwear"] = random.choices(headwear, headwear_weights_subset)[0]
        else:
            new_image["Headwear"] = random.choices(headwear, headwear_weights)[0]

        if new_image["Hair"] not in ("None","Matrix dreads"):
            # can't have headwear
            new_image ["Headwear"] = "None"

        if new_image["Eyes"]=="Laser":
            # can't have eyewear
            new_image ["EyeWear"] = "None"

        if new_image["Headwear"]=="Astronaut":
            # can't have collar or hair
            new_image["Collar"] = "None"
            new_image["Hair"] = "None"
        
        if new_image in all_images:
            return create_new_image()
        else:
            return new_image
        
        
    # Generate the unique combinations based on trait weightings
    for i in range(TOTAL_IMAGES): 
        
        new_trait_image = create_new_image()
        
        all_images.append(new_trait_image)

    all_unique = all_images_unique(all_images)
    print("Are all images unique?", all_unique)

    if not all_unique:
        print("Error: Not all images are unique.")
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

    print("Background:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in background_count.items()])

    print("Base:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in base_count.items()])

    print("Eyes:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in eyes_count.items()])

    print("Mouth:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in mouth_count.items()])

    print("Eye wear:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in eyewear_count.items()])

    print("Hair:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in hair_count.items()])

    print("Clothes")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in clothes_count.items()])

    print("Collar:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in collar_count.items()])

    print("Backpack:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in backpack_count.items()])

    print("Head wear:")
    print([key+f": {value} ({(value/TOTAL_IMAGES):.2%})" for key,value in headwear_count.items()])




    #### Generate Metadata for all Traits 
    with open(METADATA_FILE_NAME, 'w') as outfile:
        json.dump(all_images, outfile, indent=4)

else:

    #### Generate Metadata for each Image    

    f = open(METADATA_FILE_NAME,) 
    data = json.load(f)


    #IMAGES_BASE_URI = "https://www.arweave.net/"
    PROJECT_NAME = "SolDoge NFT"
    COMMUNITY_WALLET = "COMBLAHBLAH"

    def getAttribute(key, value):
        return {
            "trait_type": key,
            "value": value
        }
    for i in data:
        token_id = i['tokenId']
        token = {
            "tokenId": token_id,
            "name": PROJECT_NAME + ' ' + str(token_id),
            "description": "SolDoge NFT - official genesis NFT for SDOGE token",
            "symbol": 'SDOGE',
            "seller_fee_basis_points": 1000,
            "external_url": "https://www.soldoge.io",
            "attributes": [],
            "properties":
            {  "creators": [
                {
                    "address": COMMUNITY_WALLET,
                    "share": 100
                }
                ]
            }
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


    f = open(METADATA_FILE_NAME,) 
    image_metadata = json.load(f)

    if not all_images_unique(image_metadata):
        print("Error: Not all images are unique.")
        exit(1)


    #### Generate Images    
    for item in image_metadata:


        bg = Image.open(f'./trait-layers/background/{background_file_names[background.index(item["Background"])]}.png').convert('RGBA')
        base_img = Image.open(f'./trait-layers/base/{base_file_names[base.index(item["Base"])]}.png').convert('RGBA')
        eyes_img = Image.open(f'./trait-layers/eyes/{eyes_file_names[eyes.index(item["Eyes"])]}.png').convert('RGBA')
        
        if item["Mouth"]!="Default":
            mouth_img = Image.open(f'./trait-layers/mouth/{mouth_file_names[mouth.index(item["Mouth"])]}.png').convert('RGBA')

        if item["EyeWear"]!="None":
            eyewear_img = Image.open(f'./trait-layers/eyewear/{eyewear_file_names[eyewear.index(item["EyeWear"])]}.png').convert('RGBA')

        if item["Hair"]!="None":
            hair_img = Image.open(f'./trait-layers/hair/{hair_file_names[hair.index(item["Hair"])]}.png').convert('RGBA')
        
        if item["Clothes"]!="None":
            clothes_img = Image.open(f'./trait-layers/clothes/{clothes_file_names[clothes.index(item["Clothes"])]}.png').convert('RGBA')

        if item["Collar"]!="None":
            collar_img = Image.open(f'./trait-layers/collar/{collar_file_names[collar.index(item["Collar"])]}.png').convert('RGBA')

        if item["Headwear"]!="None":
            if item["Headwear"] in ("Solana earphones","Cone of shame","SDoge helmet","Wizard"):
                headwear_fg_img = Image.open(f'./trait-layers/headwear foreground/{headwear_file_names[headwear.index(item["Headwear"])]}.png').convert('RGBA')
                headwear_bg_img = Image.open(f'./trait-layers/headwear background/{headwear_file_names[headwear.index(item["Headwear"])]}.png').convert('RGBA')
            else:
                headwear_img = Image.open(f'./trait-layers/headwear/{headwear_file_names[headwear.index(item["Headwear"])]}.png').convert('RGBA')

        if item["Backpack"]!="None":
            backpack_img = Image.open(f'./trait-layers/backpack/{backpack_file_names[backpack.index(item["Backpack"])]}.png').convert('RGBA')
        

        #Create each composite
        com1 = Image.alpha_composite(bg, base_img)
    
        if item["Backpack"]!="None":
            com1 = Image.alpha_composite(com1, backpack_img)

        if item["Hair"]!="None":
            com1 = Image.alpha_composite(com1, hair_img)

        if item["Clothes"]!="None":
            com1 = Image.alpha_composite(com1, clothes_img)

        if item["Collar"]!="None":
            com1 = Image.alpha_composite(com1, collar_img)

        if item["Headwear"] in ("Solana earphones","Cone of shame","SDoge helmet","Wizard"):
            com1 = Image.alpha_composite(com1, headwear_bg_img)

        if item["Eyes"]!="Laser":
            com1 = Image.alpha_composite(com1, eyes_img)

        if item["Mouth"]!="Default":
            com1 = Image.alpha_composite(com1, mouth_img)

        if item["EyeWear"]!="None":
            com1 = Image.alpha_composite(com1, eyewear_img)

        if item["Eyes"]=="Laser":
            com1 = Image.alpha_composite(com1, eyes_img)

        if item["Headwear"]!="None":
            if item["Headwear"] in ("Solana earphones","Cone of shame","SDoge helmet","Wizard"):
                com1 = Image.alpha_composite(com1, headwear_fg_img)
            else:
                com1 = Image.alpha_composite(com1, headwear_img)

        #Convert to RGB
        rgb_im = com1.convert('RGB')
        file_name = str(item["tokenId"]) + ".png"
        rgb_im.save("./images/" + file_name)



