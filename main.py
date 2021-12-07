import re
import long_responses as long
import check as check

# Used to get the response


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    if split_message == ["quit"]:
        quit()
    for word in split_message:
        currentIndex = 0
        if word == "im":
            split_message[currentIndex] = "i"
        currentIndex += 1
    response = check.checkAllMesages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
