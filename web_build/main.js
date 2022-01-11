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
  if (15 >= max) {
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
  response("Hello! How may I help you.", ["hi", "hello", "hey"], ["hi", "hello", "hey"]);
  response("See you", ["bye", "cya", "goodbye"], ["bye", "cya", "goodbye"]);
  response("The cafeteria is beside the multipurpose room", ["where", "is", "the", "cafeteria"], ["where", "cafeteria"]);
  response("My name is Madison. How may I help you.", ["what", "is", "your", "name"], ["your", "name"]);
  response("The lost and found room is beside the kids playground outside", ["where", "is", "the", "lost", "found", "and"], ["lost"]);
  response("I'm doing fine, and you?", ["how", "are", "you", "doing"], ["how", "are", "you"]);
  response("You're welcome!", ["thank", "thanks", "thx"], ["thank", "thanks", "thx"]);
  response("You can borrow a computer from room 315", ["how", "do", "i", "borrow", "a", "computer", "checkout"], ["borrow", "computer"]);
  response("The guidance office is on the third floor", ["is", "the", "guidance", "office"], ["guidance", "office"]);
  response("You can apply for the ID in room 310", ["new", "id"], ["id", "new"]);
  response("A student ID costs 25 RMB, and it has to be in cash", ["how", "much", "does", "a", "new", "id", "cost"], ["id", "cost"]);
  response("The secondary computer classroom is on the fifth floor, and is number 521", ["is", "the", "secondary", "computer", "classroom"], ["secondary", "computer"]);
  response("The head of school is Ms.Faustina, and the principle is Mr.Jamal", ["who", "is", "the", "principle"], ["principle"]);
  response("Don't worry about it.", ["sorry", "sry"], ["sorry", "sry"]);
  response("To find out about the school's contact info you can visit this https://www.laschina.org/contact", ["how", "can", "i", "contact", "the", "school"], ["contact"]);
  response("The school wifi's password is iloveslas", ["what", "is", "the", "school", "wifis", "password"], ["wifis", "password"]);
  response("You can get your schedule at room 301 or the guidance office", ["where", "can", "i", "get", "my", "schedule"], ["schedule", "my"]);
  response("You can learn more about admissions from this link: htts://laschina.org/welcome", ["how", "get", "admission"], ['admission']);
  response("You can learn more about tuition fee's from this link: https://laschina.org/tuition", ['how', 'much', 'fee'], ['fee']);
  response("To find out about lunch you can visit this link https://laschine.org/lunch", ['what', 'is', 'for', 'lunch'], ['lunch']);
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
  return checkAllMessages(splitMessage);
}
class Chatbox {
  constructor() {
    this.args = {
      openButton: document.querySelector(".chatbox__button"),
      chatBox: document.querySelector(".chatbox__support"),
      sendButton: document.querySelector(".send__button"),
    };

    this.state = false;
    this.messages = [];
  }

  display() {
    const { openButton, chatBox, sendButton } = this.args;

    openButton.addEventListener("click", () => this.toggleState(chatBox));

    sendButton.addEventListener("click", () => this.onSendButton(chatBox));

    const node = chatBox.querySelector("input");
    node.addEventListener("keyup", ({ key }) => {
      if (key === "Enter") {
        this.onSendButton(chatBox);
      }
    });
  }

  toggleState(chatbox) {
    this.state = !this.state;

    // show or hides the box
    if (this.state) {
      chatbox.classList.add("chatbox--active");
    } else {
      chatbox.classList.remove("chatbox--active");
    }
  }

  onSendButton(chatbox) {
    var textField = chatbox.querySelector("input");
    let userMessage = textField.value;
    if (userMessage === "") {
      return;
    }

    let usersMessage = { name: "User", message: userMessage };
    this.messages.push(usersMessage);
    const botsResponse = getResponse(userMessage);
    let botResponse = { name: "Madison", message: botsResponse };
    this.messages.push(botResponse);
    this.updateChatText(chatbox);
    textField.value = "";
  }
  updateChatText(chatbox) {
    var html = "";
    this.messages
      .slice()
      .reverse()
      .forEach(function (item) {
        if (item.name === "Madison") {
          html +=
            '<div class="messages__item messages__item--visitor">' +
            item.message +
            "</div>";
        } else {
          html +=
            '<div class="messages__item messages__item--operator">' +
            item.message +
            "</div>";
        }
      });

    const chatmessage = chatbox.querySelector(".chatbox__messages");
    chatmessage.innerHTML = html;
  }
}
// Node Build
// const prompt = require("prompt-sync")({ sigint: true });
// while(true){
//   console.log("Bot: " + getResponse(prompt("You: ")));
// }

// Web build
const chatbox = new Chatbox();
chatbox.display();
