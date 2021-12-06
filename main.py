import re
import long_responses as long
import check as checkAllMessages

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = checkAllMessages.checkAllMesages(split_message)
    if user_input == "quit":
        quit()
    return response


# TODO: Implement this to send the bots response to the webapp 
while True:
    print('Bot: ' + get_response(input('You: ')))
