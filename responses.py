import re
blacklist = ["nigga","nigger","bitch","fuck","shit","stfu","wtf"]

def contains_blacklisted_words(message):
    message_content = message.content.lower()
    return any(re.search(r'\b' + re.escape(word) + r'\b', message_content) for word in blacklist)

def generate_warning_message(user):
    return f"{user.mention}, your message was removed due to inappropriate language. Please adhere to the community guidelines."


def get_response(user_input):
    lower_user_input=user_input.lower()

    if lower_user_input=="":
        return '''bruh you're silent are you dumb?'''
    elif 'hello' in lower_user_input:
        return "sup?"
