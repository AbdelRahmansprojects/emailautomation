const http = require('http')
const express = require('express');
const path = require('path')
const app = express()

const server = app.listen(process.env.PORT || 3000, ()=> console.log("listening port 3000"))
////It's also important to preprocess the data before training the AI, to make sure it's in the appropriate format and to remove any irrelevant information. This can include tokenizing the text, removing stop words, stemming or lemmatizing the words, and removing special characters.

app.get('/', (req, res) => {
    res.sendFile(path.resolve(process.cwd(), 'public/twitchai.html'))
})






// To build a Twitch moderator self-learning AI that can detect and filter out unwanted messages, you can follow these steps:

// Collect a dataset of unwanted messages by scraping Twitch chat logs or by manually collecting examples. This dataset will be used to train the AI.

// Preprocess the text data by cleaning it, tokenizing it, and creating a numerical representation of the text, such as word embeddings.

// Train a text classification model, such as a neural network or a pre-trained model like BERT, on the dataset of unwanted messages.

// Implement the trained model into your Twitch bot using a library like TMI.js which allows you to connect to Twitch's chat service and listen for new messages.

// Once the bot receives a new message, it will use the trained model to classify the message as unwanted or acceptable. If the message is classified as unwanted, the bot can take an action, such as sending a warning message or banning the user.

// As the bot receives more messages, you can use the active learning approach where the model can actively request human annotation of the most informative examples from a pool of unlabeled messages. This way the model can focus on the examples that are more informative and will help improve the performance of the model.

// Continuously monitor and evaluate the performance of the model and update it as needed.

//Connect the front-end to the back-end: Use JavaScript to send requests to the Flask endpoint and display the results on the website. You can use a library like axios or fetch to make the request and display the response.