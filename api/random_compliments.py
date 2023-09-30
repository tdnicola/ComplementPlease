from wonderwords import RandomWord
import random

def generate_random_compliment_handler(req, res):
    r = RandomWord()
    adjective = r.word(include_parts_of_speech=["adjectives"])
    noun = r.word(include_parts_of_speech=["nouns"])
    
    sentence_options = [
        f"You are truly {adjective}! You are a {noun} and a delight to be around.",
        f"You are absolutely {adjective}! Your {noun} qualities shine brightly.",
        f"I must say, you're incredibly {adjective}! You're a true {noun}.",
        f"Your {noun} nature is {adjective}! You bring joy to everyone you meet.",
        f"Being around you is like experiencing pure {adjective}! You're an amazing {noun}.",
        f"You possess such {adjective} qualities! Your {noun} spirit is inspiring.",
        f"Your {noun} is truly {adjective}! You make the world a better place.",
        f"I can't help but admire your {adjective} {noun} nature! You're a gem.",
        f"Your {noun} is as {adjective} as it gets! You're a remarkable individual.",
        f"Your {noun} is filled with {adjective} goodness! You brighten everyone's day.",
        f"Your {noun} radiates {adjective} positivity! You're an absolute joy.",
        f"In every way, you're exceptionally {adjective}! Your {noun} is a treasure.",
        f"You are the epitome of {adjective}! Your {noun} is pure perfection.",
        f"I am constantly amazed by your {adjective} {noun}! You're one of a kind.",
        f"Your {noun} is a beacon of {adjective} light! You lift spirits wherever you go.",
        f"Your {noun} is an inspiration to all! You embody {adjective} goodness.",
        f"You bring {adjective} vibes with you everywhere! Your {noun} is legendary.",
        f"Your {noun} is an oasis of {adjective}! You make the world a better place.",
        f"Your {noun} is a fountain of {adjective}! You're a true inspiration.",
        f"I'm convinced your {noun} is made of {adjective} dreams! You're phenomenal.",
    ]

    compliment = random.choice(sentence_options)
    return res.json({compliment})
