def emoji_convertor(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = " "
    for x in words:
        output += emojis.get(x, x) + " "
    return output


message = input(">")
print(emoji_convertor(message))

