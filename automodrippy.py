# miscellaneous
import os, re, discord, json, os, os.path, threading, logging, random

# thefuzz search
from thefuzz import process as fuzz

DEFAULT = "not_found.mp3"

# import best shitpost update ever
from cool_things import ads

# basic json-"db" "manager" for storing data
class JsonDB:
    data: dict = None
    __last_data: dict = None
    __filename: str = None
    __autosave_interval: int = None

    def save(self, force = True):
        if self.data == self.__last_data and not force:
            return

        with open(self.__filename, "w") as file:
            self.__last_data = self.data
            json.dump(self.__last_data, file)
    
    def __save(self):
        self.save(force = False)
        threading.Timer(interval = self.__autosave_interval, function = self.__save)

    def __init__(self, filename, autosave_interval = 300):
        self.__filename = filename
        self.__autosave_interval = autosave_interval

        with open(self.__filename) as file:
            self.__last_data = json.load(file)
            self.data = self.__last_data

        if self.__autosave_interval != None:
            self.__save()

# very clever index search
def vcis(what: object, where: list, gate: int = 75):
    found, accuracy = fuzz.extract(what, where, limit = 50)[0]

    if accuracy < gate:
        return None
    else:
        return {
            "index": where.index(found),
            "accuracy": accuracy
        }

# car finder helper function
def find_car(query: str, gate = None):
    if gate:
        search_result = vcis(query, cars, gate)
    else:
        search_result = vcis(query, cars)

    if not search_result:
        return None
    
    index = search_result["index"]
    accuracy = search_result["accuracy"]

    return {
        "name": original_cars[index],
        "url": f"https://awesomecars.neocities.org/ver2/{index + 1}.mp4",
        "accuracy": accuracy
    }

# simple embed generator
def create_embed(title, description):
    return discord.Embed(title = title, description = description)

# number to ordinal function
def to_ordinal(number):
    last_digit = number % 10
    suffix = ["st", "nd", "rd"][last_digit - 1] if last_digit in [1, 2, 3] else "th"
    return f"{number}{suffix}"

# duplicate finder
def find_duplicates(where: list):
    seen = set()
    buffer = []

    for element in where:
        if element in seen:
            buffer.append(element)
        else:
            seen.add(element)

    return buffer



# load cars info
with open("cars.txt") as lines:
    cars = [line.strip().lower() for line in lines]

# deletes "car" suffix from every element because it seems like it really messes up fuzzy search algorithm
original_cars = cars.copy()
cars = [re.sub(r"(.+) +?car", "\\1", car, 1) for car in cars]

duplicates = find_duplicates(cars)
if len(duplicates) > 0:
    print("Duplicate cars are found!")

    reverse_cars = cars[::-1]
    cars_count = len(cars)

    for element in duplicates:
        where = cars_count - reverse_cars.index(element) - 1
        print(f"\"{cars[where]}\" at line {where + 1}")

    print("Note: currently only last duplicates are shown, if there is >2 cars with same name this screen wouldn't tell you all of them immediately.")
    print("Exiting.")

    exit(1)

# open databases
name_db = JsonDB(".automodrippy/name_data.json")
user_db = JsonDB(".automodrippy/user_data.json")
frequency_db = JsonDB(".automodrippy/frequency_data.json")

# create instance of discord.Client
intents = discord.Intents().default()
intents.message_content = True
automodrippy = discord.Client(intents = intents)

async def post_leaderboards(message: discord.Message):
    total_posted = 0
    for car in frequency_db.data.keys():
        total_posted += frequency_db.data[car]

    people = []
    for name in user_db.data.keys():
        people.append((name_db.data[name], len(user_db.data[name])))

    people.sort(key = lambda element: element[1])
    
    if len(people) > 5:
        people = people[-5:]

    people.reverse()

    description = ""

    for index in range(len(people)):
        person = people[index]
        max_format = "**" if person[1] == len(cars) else ""
        separator = "🚗🚙" if index % 2 == 0 else "🚙🚗"
        description += f"{index + 1}. {separator[0]} **{person[0]}** with {max_format}{person[1]}/{len(cars)}{max_format} cars {separator[1]}\n"

    await message.reply(embed = create_embed(f"car of fame (posted {total_posted} cars in total)", description))

async def reply_to_query(message: discord.Message, query: str):
    # update display name of author
    name_db.data[str(message.author.id)] = message.author.display_name
    name_db.save(force = False)

    # deletes car suffix, copypaste of some code above
    query = re.sub(r"(.+) +?car", "\\1", query, 1)
    result = find_car(query, 1)

    # reply accordingly and save data if car was found
    if result:
        name = result["name"]
        url = result["url"]
        accuracy = result["accuracy"]

        times_format = "time"
        if name not in frequency_db.data.keys():
            times_format = "EVER SEEN"
            frequency_db.data[name] = 1
            times_seen = 1
        else:
            frequency_db.data[name] += 1
            times_seen = frequency_db.data[name]

        description = "already seen"
        title = ""
        if message.author.id not in user_db.data.keys():
            user_db.data[str(message.author.id)] = []

        if name not in user_db.data[str(message.author.id)]:
            description = "**+1**"
            title = "NEW "
            user_db.data[str(message.author.id)].append(name)

        random_tlds = [
            ".com",
            ".xxx",
            ".xyz",
            ".love",
            ".io",
            ".roblox",
            ".volvo",
            ".kia",
            ".mercedes",
            ".bmw",
            ".cars",
            ".dripcar"
        ]

        random_links = [
            "download-more-cars",
            "i-love-my-car",
            "hot-cars-watch-for-free",
            "dripcar-my-beloved",
            "i-have-car-videos",
            "car-share"
        ]

        # please DO NOT OPEN ANY OF THESE LINKS I HAVE THESE ARE RANDOMLY GENERATED AND MAY AND MAY NOT EXIST
        # CONTENT ON THESE PAGES IS NOT CONTROLLED SO FOR YOUR SAFETY DO NOT VISIT THESE URLS, PERIOD.

        lol = random_links[random.randint(0, len(random_links) - 1)] + random_tlds[random.randint(0, len(random_tlds) - 1)]

        await message.reply(f"## Sponsored: [{ads[random.randint(0, len(ads) - 1)]}]\n{lol}: {url}")
        await message.channel.send(embed = create_embed(f"{title}[{name}] ({to_ordinal(times_seen)} {times_format})", f"🚗 {accuracy}% accuracy, {description} 🚙"))

        # save data
        frequency_db.save()
        user_db.save()

        return
    
    # ...or reply with error message
    await message.reply(embed = create_embed("no car found", "🚗 choot choot 🚙 (0% accuracy)"), file = discord.File(DEFAULT))

@automodrippy.event
async def on_message(message: discord.Message):
    # ignore bot messages
    if message.author == automodrippy.user:
        return
    
    # ignore messages from non-text channels
    if message.channel.type != discord.channel.ChannelType.text:
        return

    # --- nc group: ignore spaces in the beginning
    # --- nc group: bot prefixes
    # --- nc group: ignore spaces after bot prefix
    # 1st ct group: user query
    regex = r"(?: *)(?:🚗|🚙|:DripCar:)(?: *)(.*)"

    # parse user message
    match = re.search(regex, message.content)

    # ignore if regex doesn't match
    if not match:
        return
    
    # get data from query
    query = match.group(1)

    # send leaderboards if query is empty
    if query == "":
        await post_leaderboards(message)
        return
    
    # ...or else reply to query
    await reply_to_query(message, query)

@automodrippy.event
async def on_ready():
    logging.info(f"Add bot via this link: https://discord.com/api/oauth2/authorize?client_id={automodrippy.user.id}&permissions=52224&scope=bot")
    await automodrippy.change_presence(activity = discord.Game("videos of drip cars"))

automodrippy.run(os.getenv("AUTOMODRIPPY_TOKEN"))