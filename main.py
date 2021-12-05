import re
import long_responses as long


def messageProb(userMessage, recognisedWords, isSingleResponse=False, requiredWords=[]):
    messageCertainty = 0
    hasRequiredWords = True

    # Counts how many words are present in each predefined message
    for word in userMessage:
        if word in recognisedWords:
            messageCertainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(messageCertainty) / float(len(recognisedWords))

    # Checks that the required words are in the string
    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break

    # Must either have the required words, or be a single response
    if hasRequiredWords or isSingleResponse:
        return int(percentage * 100)
    else:
        return 0


def checkAllMesages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = messageProb(
            message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey',
             'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', [
             'how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response("Please do not swear or cuss at me, swearing is bad", [
             "fuck", "shit", "motherfucker", "fuck", "you"], single_response=True)
    response("You can borrow a computer from room 315", [
             "how", "do", "i", "borrow", "a", "computer"], ["borrow", "computer"])
    response("The guidance office is on the third floor", ["where", "is", "the", "guidance", "office"], ["guidance", "office"])
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'],
             required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(
    #     f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
    # DEBUGGING TOOLS IF NEEDED 


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = checkAllMesages(split_message)
    if user_input == "quit":
        quit()
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
