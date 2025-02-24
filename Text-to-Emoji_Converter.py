emojis={ "love": "❤️",
        "pizza": "🍕",
        "cat": "🐱",
        "dog": "🐶",
        "cats": "🐱🐱🐱",
        "dogs": "🐶🐶🐶",
        "happy": "😊",
        "sad": "😢",
        "sun": "☀️",
        "star": "⭐",
        "laugh": "😂",
        "cool": "😎",
        "coffee": "☕",
        "music": "🎵",
        "car": "🚗",
        "book": "📖",
        "fire": "🔥",
        "thumbs up": "👍",
        "heart": "💖",
        "clap": "👏",
        "sleep": "😴",
        "party": "🎉",
        "smile": "😀",
        "rain": "🌧️",
        "cloud": "☁️",
        "gift": "🎁"}
str=input()
list_str=str.lower().split()
for index, i in enumerate(list_str):
    if i in emojis:
        list_str[index]=emojis[i]
print(" ".join(list_str))
