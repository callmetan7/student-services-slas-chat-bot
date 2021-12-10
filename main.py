import re
import check as check
import colors as colors 

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    if split_message == ["quit"]:
        quit()
    for word in split_message:
        currentIndex = 0
        if word == "im":
            split_message[currentIndex] = "i"
        elif word == "laptop":
            split_message[currentIndex] = "computer"
        currentIndex += 1
    # print(split_message)
    response = check.checkAllMesages(split_message)
    return response

def main():
    while True:
        print(f'{colors.RESET}Bot: {colors.HEADER} ' + get_response(input(f'{colors.RESET}You: {colors.OKBLUE} ')))
main()