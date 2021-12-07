import long_responses as long

# Returns the probability of a message matching the responses that we have


def messageProb(userMessage, recognizedWords, isSingleResponse=False, requiredWords=[]):
    messageCertainty = 0
    hasRequiredWords = True

    # Counts how many words are present in each predefined message
    for word in userMessage:
        if word in recognizedWords:
            messageCertainty += 1

    # Calculates the percent of recognized words in a user message
    percentage = float(messageCertainty) / float(len(recognizedWords))

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

# Checks all the responses using the probability of the messages


def checkAllMesages(message):
    highest_prob_list = {}
    ignore_list = {}

    def ignoreResponse(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal ignore_list
        ignore_list[bot_response] = messageProb(
            message, list_of_words, single_response, required_words)
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
             'how', 'are', 'you', 'doing'], required_words=['how', "you"])

    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    response("You can borrow a computer from room 315", ["how", "do", "i", "borrow", "a", "computer"], required_words=["borrow", "computer"])
    response("You can apply for a new locker key in room 310", ["how", "can", "i", "apply", "for", "a", "new", "locker", "key"], ["new", "locker", "key"])

    response("The guidance office is on the third floor", [
             "where", "is", "the", "guidance", "office"], required_words=["guidance", "office"])

    response("You can apply for the ID in room 310", [
             "how", "can", "i", "get", "new", "id"], ["new", "id"])

    response("A student ID costs 25 RMB, and it has to be in cash", [
             "how", "much", "does", "a", "new", "id", "cost"], ["id", "cost"])

    response("The secondary computer classroom is on the fifth floor, and is number 521", [
             "where", "is", "the", "secondary", "computer", "classroom"], ["secondary", "computer"])

    response("Don't worry about it.", ["sorry", "sry"], ["sorry", "sry"])

    # Ignored Responses
    ignoreResponse("Good to hear", [
                   "i", "doing", "good", "fine", "ok"], required_words=["i", "good"])
    best_ignore_match = max(ignore_list, key=ignore_list.get)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'],
             required_words=['you', 'eat'])
    response(long.R_SWEARING, [
             "fuck", "shit", "motherfucker", "fuck", "you"])
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # DEBUGGING TOOLS IF NEEDED
    print(highest_prob_list)
    print("")
    print(
        f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    if highest_prob_list[best_match] < ignore_list[best_ignore_match]:
        return best_ignore_match
    elif highest_prob_list[best_match] < 1:
        return long.unknown()
    else:
        return best_match
