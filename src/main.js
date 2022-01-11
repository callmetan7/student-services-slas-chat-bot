function messageProb(userInput, potentialWords, requiredWords) {
    var messageCertainty = 0.0;
    var hasPotentialWords = false;
    var hasRequiredWords = false;
    for (var index = 0; index < userInput.length; index++) {
        var userWord = userInput[index];
        for (var potentialIndex = 0; potentialIndex < potentialWords.length; potentialIndex++) {
            if (userWord === potentialWords[potentialIndex]) {
                hasPotentialWords = true;
                messageCertainty = messageCertainty + 0.01;
            }
        }
        for (var requiredIndex = 0; requiredIndex < requiredWords.length; requiredIndex++) {
            if (userWord === requiredWords[requiredIndex]) {
                hasRequiredWords = true;
                messageCertainty = messageCertainty + 0.5;
            }
        }
    }
    if (hasPotentialWords || hasRequiredWords) {
        return messageCertainty * 100;
    }
    else {
        return 0;
    }
}
function findBestMatch(dict) {
    var max = 0;
    var maxkey = "";
    var keys = Object.keys(dict);
    var values = Object.values(dict);
    for (var keyi = 0; keyi < Object.keys(dict).length; keyi++) {
        var value = values[keyi];
        var key = keys[keyi];
        if (value > max) {
            max = value;
            maxkey = key;
        }
    }
    if (15 > max) {
        return "I do not understand that";
    }
    else {
        return maxkey;
    }
}
function checkAllMessages(userMessage) {
    var highestProbList = {};
    function response(botResponse, potentialWords, requiredWords) {
        highestProbList[botResponse] = messageProb(userMessage, potentialWords, requiredWords);
    }
    response("Hello!", ["hi", "hello", "hey"], ["hi", "hello", "hey"]);
    response("See you", ["bye", "cya", "goodbye"], ["bye", "cya", "goodbye"]);
    response("The cafeteria is beside the multipurpose room", ["where", "is", "the", "cafeteria"], ["where", "cafeteria"]);
    response("My name is Madison. How may I help you.", ["what", "is", "your", "name"], ["your", "name"]);
    response("The lost and found room is beside the kids playground outside", ["where", "is", "the", "lost", "found", "and"], ["lost"]);
    response("I'm doing fine, and you?", ["how", "are", "you", "doing"], ["how", "are", "you"]);
    response("You're welcome!", ["thank", "thanks", "thx"], ["thank", "thanks", "thx"]);
    response("You can borrow a computer from room 315", ["how", "do", "i", "borrow", "a", "computer", "checkout"], ["borrow", "computer"]);
    response("The guidance office is on the third floor", ["is", "the", "guidance", "office"], ["guidance", "office", "where"]);
    response("You can apply for the ID in room 310", ["how", "can", "get", "new", "id"], ["id", "get"]);
    response("A student ID costs 25 RMB, and it has to be in cash", ["how", "much", "does", "a", "new", "id", "cost"], ["id", "cost"]);
    response("The secondary computer classroom is on the fifth floor, and is number 521", ["is", "the", "secondary", "computer", "classroom"], ["secondary", "computer"]);
    response("The head of school is Ms.Faustina, and the principle is Mr.Jamal", ["who", "is", "the", "principle"], ["principle"]);
    response("Don't worry about it.", ["sorry", "sry"], ["sorry", "sry"]);
    response("To find out about the school's contact info you can visit this https://www.laschina.org/contact", ["how", "can", "i", "contact", "the", "school"], ["contact", "school"]);
    response("The school wifi's password is iloveslas", ["what", "is", "the", "school", "wifis", "password"], ["wifis", "password"]);
    response("You can get your schedule at room 301 or the guidance office", ["where", "can", "i", "get", "my", "schedule"], ["schedule", "my"]);
    // Ignored Responses
    response("", ["slas", "is", "a", "bad", "school"], ["slas", "bad"]);
    response("Good to hear", ["i", "doing", "good", "fine", "ok"], ["i", "good"]);
    response("I advise you to talk to your parents, teachers, or friends about the sitation", ["give", "advice"], ["advice"]);
    response("I do not eat since I'm a bot obviously", ["what", "you", "eat"], ["you", "eat"]);
    response("Please do not swear here", ["fuck", "shit", "wtf", "tf", "bitch"], ["fuck", "shit", "wtf", "tf", "bitch"]);
    response("Don't worry about it.", ["sorry", "sry"], ["sorry", "sry"]);
    response("", ["yea", "yah", "yee", "ok", "yep", "yes"], ["yea", "yah", "yee", "ok", "yep", "yes"]);
    return findBestMatch(highestProbList);
}
function getResponse(userInput) {
    userInput = userInput.toLowerCase();
    var splitMessage = userInput.split(" ");
    for (var index = 0; index < splitMessage.length; index++) {
        splitMessage[index] = splitMessage[index]
            .replace(/[.,/#!$%^&*;:{}=-_`~()]/g, "")
            .replace(/s{2,}/g, " ");
    }
}