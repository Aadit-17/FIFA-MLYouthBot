import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive
import requests
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor

model = joblib.load("xgboost_model.joblib")
label_encoders = {}
categorical_columns = ['Team', 'Position', 'Continent']
for col in categorical_columns:
    filename = f'label_encoder_{col}.joblib'
    label_encoder = joblib.load(filename)
    label_encoders[col] = label_encoder
requests.get('https://tender-marred-packet.glitch.me/')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user} '.format(bot))


@bot.command()
async def retire(ctx, threshold: int):
    x = random.randint(1, 100)
    embed = discord.Embed(
        title="Verdict",
        color=discord.Color.green()
    )
    if x <= threshold:
        retired = True
    else:
        retired = False
    embed.add_field(name="Value", value=x, inline=True)
    embed.add_field(name="Retired?", value=retired, inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def youth(ctx, command):
    buckets_poor = [
        (0, 50, 74, 65, 88),
        (5, 50, 55, 65, 70),
        (9, 55, 60, 70, 74),
        (16, 60, 63, 74, 77),
        (19, 63, 67, 77, 82),
        (20, 68, 72, 80, 85)
    ]
    buckets_basic = [
        (0, 50, 74, 65, 88),
        (4, 50, 55, 65, 70),
        (10, 55, 60, 70, 74),
        (15, 60, 63, 74, 77),
        (18, 63, 67, 77, 82),
        (19, 68, 72, 80, 85),
        (20, 70, 74, 84, 88)
    ]
    buckets_decent = [
        (0, 50, 74, 65, 88),
        (5, 50, 55, 65, 70),
        (9, 55, 60, 70, 74),
        (14, 60, 63, 74, 77),
        (17, 63, 67, 77, 82),
        (19, 68, 72, 80, 85),
        (20, 70, 74, 84, 88)
    ]
    buckets_good = [
        (0, 50, 74, 65, 88),
        (5, 50, 55, 65, 70),
        (9, 55, 60, 70, 74),
        (13, 60, 63, 74, 77),
        (17, 63, 69, 77, 82),
        (19, 68, 72, 80, 85),
        (20, 72, 74, 84, 88)
    ]
    buckets_great = [
        (0, 50, 74, 65, 88),
        (4, 50, 55, 65, 70),
        (8, 55, 60, 70, 74),
        (12, 60, 63, 74, 77),
        (16, 63, 69, 77, 82),
        (18, 70, 72, 80, 85),
        (20, 72, 74, 84, 88)
    ]
    buckets_elite = [
        (0, 50, 74, 65, 88),
        (4, 50, 55, 65, 70),
        (8, 55, 60, 70, 74),
        (12, 60, 68, 74, 77),
        (15, 68, 70, 77, 82),
        (18, 70, 72, 82, 86),
        (20, 72, 74, 84, 88)
    ]
    bucket_levels = {
        'poor': buckets_poor,
        'basic': buckets_basic,
        'decent': buckets_decent,
        'good': buckets_good,
        'great': buckets_great,
        'elite': buckets_elite
    }
    if command in bucket_levels:
        buckets = bucket_levels[command]
    else:
        await ctx.send("Invalid bucket, default to poor")
        buckets = buckets_poor
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
        "Versatile", "Quick Learner", "Leadership", "Teachers Pet", "Consistent", "Second Nation"
    ]
    Player_Position = random.choice(positions)
    if Player_Position == "GK":
        traits.remove("Versatile")
    Player_Trait = random.choice(traits)

    versatile_traits = {
        "CB": ["Complete Defender (DM, WB, FB, CB)", "DLP (CM, DM, WB, FB)"],
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

    PositionP = Player_Position
    AgeP = str(Age)
    RatingP = str(Rating) + "/" + str(Potential)
    TraitP = Player_Trait
    VersatileP = VerTrait

    conditions = {
        (Age == 17 and Player_Position == "CM" and Rating <= 53): ("you got gavi", 'gavi.png'),
        ((Age == 23 or Age == 22) and Rating == 70 and Potential == 84): (
        "Congrats on finding the next messi", 'messi.png'),
        (Rating >= 68 and Player_Position == "WM/W"): ("Project mbappe is here", 'mbappe.png'),
        (Rating >= 68 and Player_Position == "CF/ST"): ("The next robot?", 'haaland.png'),
        (Growth >= 20): (
        "damn that's a lot of growth, hope he doesn't turn out like this forgotten wonderkid", 'mastour.png'),
        (VerTrait == "BTB (CM, DM, WB, FB)" and Rating >= 65): ("this is fede the b2b god", 'fede.png'),
        (Player_Position == "FB/WB" and Rating >= 67): ("MARCELO REGEN???", 'marcelo.png'),
        (Player_Position == "GK" and Rating >= 68): (
        "looks cute hopefully he won't lie about his time with puyol", 'iker.png')
    }

    embed = discord.Embed(
        title="Youth Player",
        color=discord.Color.green()
    )

    embed.add_field(name="Position", value=PositionP, inline=True)
    embed.add_field(name="Age", value=AgeP, inline=True)
    embed.add_field(name="Rating", value=RatingP, inline=True)
    embed.add_field(name="Trait", value=TraitP, inline=True)
    embed.add_field(name="VersatileP", value=VersatileP, inline=True)

    for condition, (message_text, image_file) in conditions.items():
        if condition:
            embed.set_image(url=image_file)

    await ctx.send(embed=embed)


@bot.command()
async def scout(ctx, team: str, position: str, continent: str):
    team = team.lower()
    age = random.randint(18, 29)
    input_features = {
        "Team": team,
        "Position": position,
        "Continent": continent,
        "Age": age,
        "S11": 1
    }
    inputdf = pd.DataFrame(input_features, index=[0])
    for col, le in label_encoders.items():
        if col in inputdf:
            inputdf[col] = inputdf[col].str.lower()
            inputdf[col] = le.transform(inputdf[col])

    rating = model.predict(inputdf)
    age_ranges = {
        (18, 20): (10, 16),
        (21, 23): (7, 12),
        (24, 25): (3, 5),
        (26, 27): (1, 2),
        (28, 29): (0, 1)
    }
    for (min_age, max_age), (min_growth, max_growth) in age_ranges.items():
        if min_age <= age <= max_age:
            growth = random.randint(min_growth, max_growth)
            break
    potential = rating + growth
    rating_str = str(rating)

    embed = discord.Embed(
        title="Scouted Player",
        color=discord.Color.green()
    )
    embed.add_field(name="Team", value=team, inline=True)
    embed.add_field(name="Position", value=position, inline=True)
    embed.add_field(name="Continent", value=continent, inline=True)
    embed.add_field(name="Age", value=age, inline=True)
    embed.add_field(name="Rating", value=rating_str, inline=True)
    embed.add_field(name="Potential", value=potential, inline=True)
    await ctx.send(embed=embed)


keep_alive()
bot.run(os.getenv("TOKEN"))