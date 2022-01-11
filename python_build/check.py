import long_responses as long
import colors as colors
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
# School info, wheres, cafeteria, admins office, mostly wheres
    # Responses       To make a response: response(BOT RESPONSE, LISTOFWORDS, SINGLERESPONSE=TRUE OR FALSE, REQUIREDWORDS)-------------------------------------------------------------------------------------------------------

    response('The cafeteria is beside the multipurpose room', [
             'where', 'is', 'the', 'cafeteria'], required_words=['where', 'cafeteria'])

    response('My name is Madison. How may I help you.', [
             'what', 'is', 'your', 'name'], required_words=['your', 'name'])

    response('The lost and found room is beside the kids playground outside', [
             'where', 'is', 'the', 'lost', 'found', 'and'], required_words=['lost'])

    response('Hello!', ['hello', 'hi', 'hey', ], single_response=True)

    response('See you!', ['bye', 'goodbye'], single_response=True)

    response('I\'m doing fine, and you?', [
             'how', 'are', 'you', 'doing'], required_words=['how', "are", "you"])

    response('You\'re welcome!', [
             'thank', 'thanks', 'thx'], single_response=True)

    response("You can borrow a computer from room 315", [
             "how", "do", "i", "borrow", "a", "computer", "checkout"], required_words=["borrow", "computer"])

    response("The guidance office is on the third floor", [
             "is", "the", "guidance", "office"], required_words=["guidance", "office", "where"])

    response("You can apply for the ID in room 310", [
             "how", "can", "get", "new", "id"], ["id", 'get'])

    response("A student ID costs 25 RMB, and it has to be in cash", [
             "how", "much", "does", "a", "new", "id", "cost"], ["id", "cost"])

    response("The secondary computer classroom is on the fifth floor, and is number 521", [
             "is", "the", "secondary", "computer", "classroom"], ["secondary", "computer"])
    response("The head of school is Ms.Faustina, and the principle is Mr.Jamal", [
             "who", 'is', 'the', 'principle'], required_words=['principle'])
    response("Don't worry about it.", ["sorry", "sry"])
    response(f"To find out about the school's contact info you can visit this {colors.links}https://www.laschina.org/contact{colors.RESET}", [
             'how', 'can', 'i', 'contact', 'the', 'school'], required_words=['contact', 'school'])
    response(f'The school wifi\'s password is {colors.links}iloveslas{colors.RESET}', [
             'what', 'is', 'the', 'school', 'wifis', 'password'], required_words=['wifis', 'password'])
    response('You can get your schedule at room 301 or the guidance office', [
             'where', 'can', 'i', 'get', 'my', 'schedule'], required_words=['schedule', 'my'])
    # Ignored Responses
    ignoreResponse(' ', ['slas,' 'is', 'a', 'bad', 'school'],
                   required_words=['slas', 'bad'])
    ignoreResponse("Good to hear", [
                   "i", "doing", "good", "fine", "ok"], required_words=["i", "good"])

    best_ignore_match = max(ignore_list, key=ignore_list.get)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'],
             required_words=['you', 'eat'])
    response("Please do not swear here",  ["fuck", "shit", "wtf", "tf", "bitch"], required_words=[
             "fuck", "shit", "wtf", "tf", "bitch"], single_response=True)
    response("Don't worry about it.", ["sorry", "sry"])

    # Ignored Responses
    ignoreResponse("Good to hear", [
                   "i", "doing", "good", "fine", "ok"], required_words=["i", "good"])
    ignoreResponse('', [''], required_words=[''])
    ignoreResponse('', ['yea', 'yah', 'yee', 'ok', 'yep', 'yes'], required_words=[
                   'yea', 'yah', 'yee', 'ok', 'yep', 'yes'])

    best_ignore_match = max(ignore_list, key=ignore_list.get)

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'],
             required_words=['you', 'eat'])
    response("Please do not swear here",  ["fuck", "shit", "wtf", "tf", "bitch"], required_words=[
             "fuck", "shit", "wtf", "tf", "bitch"], single_response=True)
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # DEBUGGING TOOLS IF NEEDED
    print(highest_prob_list)
    print("")
    print(
        f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    if highest_prob_list[best_match] < ignore_list[best_ignore_match]:
        return best_ignore_match
    elif highest_prob_list[best_match] <= 15:
        return long.unknown()
    else:
        return best_match
