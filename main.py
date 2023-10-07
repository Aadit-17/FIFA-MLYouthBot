import discord
import os
import random
from keep_alive import keep_alive
import requests

requests.get('https://tender-marred-packet.glitch.me/')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)


@client.event
async def on_ready():
  print('We have logged in as {0.user} '.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$retire'):
    x = random.randint(1, 100)
    await message.channel.send(x)

  if message.content.startswith('$youth'):
    command = message.content.split('$youth')[1].strip().lower()

    bucketsPoor = [
        (0, 50, 72, 65, 88),
        (5, 50, 55, 65, 70),
        (9, 55, 60, 70, 74),
        (16, 60, 63, 74, 77),
        (19, 63, 67, 77, 82),
        (20, 68, 70, 80, 85)
    ]
    bucketsBasic = [
        (0, 50, 72, 65, 88),
        (4, 50, 55, 65, 70),
        (10, 55, 60, 70, 74),
        (15, 60, 63, 74, 77),
        (18, 63, 67, 77, 82),
        (19, 68, 70, 80, 85),
        (20, 70, 72, 84, 88)
    ]
    bucketsAverage = [
        (0, 50, 72, 65, 88),
        (5, 50, 55, 65, 70),
        (9, 55, 60, 70, 74),
        (14, 60, 63, 74, 77),
        (17, 63, 67, 77, 82),
        (19, 68, 70, 80, 85),
        (20, 70, 72, 84, 88)
    ]
    bucketsGood = [
        (0, 50, 72, 65, 88),
        (5, 50, 55, 65, 70),
        (9, 55, 60, 70, 74),
        (13, 60, 63, 74, 77),
        (17, 63, 67, 77, 82),
        (19, 68, 70, 80, 85),
        (20, 70, 72, 84, 88)
    ]
    bucketsGreat = [
        (0, 50, 72, 65, 88),
        (4, 50, 55, 65, 70),
        (8, 55, 60, 70, 74),
        (12, 60, 63, 74, 77),
        (16, 63, 67, 77, 82),
        (18, 68, 70, 80, 85),
        (20, 70, 72, 84, 88)
    ]
    bucketsElite = [
        (0, 50, 72, 65, 88),
        (4, 50, 55, 65, 70),
        (8, 55, 60, 70, 74),
        (12, 60, 63, 74, 77),
        (15, 63, 67, 77, 82),
        (18, 68, 70, 80, 85),
        (20, 70, 72, 84, 88)
    ]
    bucket_levels = {
        'poor': bucketsPoor,
        'basic': bucketsBasic,
        'average': bucketsAverage,
        'good': bucketsGood,
        'great': bucketsGreat,
        'elite': bucketsElite
    }
    if command in bucket_levels:
        buckets = bucket_levels[command]
    else:
        await message.channel.send("Invalid bucket, default to poor")
        buckets = bucketsPoor
    random_num = random.randint(0, 20)
    selected_bucket = None
    for bucket in buckets:
        if random_num <= bucket[0]:
            selected_bucket = bucket
            break
    Rating = random.randint(selected_bucket[1], selected_bucket[2])
    Potential = random.randint(selected_bucket[3], selected_bucket[4])

    positions = ["GK", "CB", "FB/WB", "CDM", "CM", "CAM", "WM/W", "CF/ST"]
    traits = [
        "Quick Learner", "Leadership", "Teachers Pet", "Consistent", "Second Nation"
    ]
    Player_Position = random.choice(positions)
    if Player_Position == "GK":
        traits.remove("Versatile")
    Player_Trait = random.choice(traits)

    versatile_traits = {
        "CB": ["Complete Defender (DM, WB, FB, CB)", "DLP (CM, DM, CB)"],
        "FB/WB": ["Complete Defender (DM, WB, FB, CB)", "Wideman (FB, WB, WM, W)", "BTB (CM, DM, WB, FB)"],
        "CDM": ["Complete Defender (DM, WB, FB, CB)", "Complete Midfielder (AM, CM, WM, DM)", "BTB (CM, DM, WB, FB)",
                "DLP (CM, DM, CB)"],
        "CM": ["Complete Midfielder (AM, CM, WM, DM)", "BTB (CM, DM, WB, FB)", "DLP (CM, DM, CB)"],
        "CAM": ["Complete Attacker (AM, W, F, ST)", "Complete Midfielder (AM, CM, WM, DM)"],
        "WM/W": ["Complete Attacker (AM, W, F, ST)", "Complete Midfielder (AM, CM, WM, DM)", "Wideman (FB, WB, WM, W)"],
        "CF/ST": ["Complete Attacker (AM, W, F, ST)"]
    }

    if Player_Trait == "Versatile":
        VerTrait = random.choice(versatile_traits.get(Player_Position, ["no.", "not versatile"]))
    else:
        VerTrait = random.choice(["no.", "not versatile"])

    Growth = Potential - Rating
    age_ranges = {
        (3, 5): (21, 23),
        (6, 8): (19, 21),
        (9, 11): (18, 19),
        (12, 15): (17, 18),
        (16, float('inf')): (16, 17)
    }

    for growth_range, age_range in age_ranges.items():
        if growth_range[0] <= Growth <= growth_range[1]:
            Age = random.randint(age_range[0], age_range[1])
            break

    PositionP = "Position = " + Player_Position
    AgeP = "Age = " + str(Age)
    RatingP = "Rating/Potential = " + str(Rating) + "/" + str(Potential)
    TraitP = "Trait = " + Player_Trait
    VersatileP = "Versatile Trait = " + VerTrait
    await message.channel.send(PositionP)
    await message.channel.send(AgeP)
    await message.channel.send(RatingP)
    await message.channel.send(TraitP)
    await message.channel.send(VersatileP)

    conditions = {
    (Age == 17 and Player_Position == "CM" and Rating <= 53): ("you got gavi", 'gavi.png'),
    ((Age == 23 or Age == 22) and Rating == 70 and Potential == 84): ("Congrats on finding the next messi", 'messi.png'),
    (Rating >= 68 and Player_Position == "WM/W"): ("Project mbappe is here", 'mbappe.png'),
    (Rating >= 68 and Player_Position == "CF/ST"): ("The next robot?", 'haaland.png'),
    (Growth >= 20): ("damn that's a lot of growth, hope he doesn't turn out like this forgotten wonderkid", 'mastour.png'),
    (VerTrait == "BTB (CM, DM, WB, FB)" and Rating >= 65): ("this is fede the b2b god", 'fede.png'),
    (Player_Position == "FB/WB" and Rating >= 67): ("MARCELO REGEN???", 'marcelo.png'),
    (Player_Position == "GK" and Rating >= 68): ("looks cute hopefully he won't lie about his time with puyol", 'iker.png')
}

    for condition, (message_text, image_file) in conditions.items():
      if condition:
        await message.channel.send(message_text, file=discord.File(image_file))


keep_alive()

client.run(os.getenv("TOKEN"))
