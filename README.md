
# Blog-NewsBot

Blog-NewsBot is a chatbot that uses Rasa and large language models to deliver the latest news with human-like responses. It can answer questions about current events, provide summaries of articles, and recommend news sources based on the user's preferences.

## Features

- **Natural language understanding**: Blog-NewsBot uses Rasa NLU to parse the user's messages and extract their intents and entities.
- **Dialogue management**: Blog-NewsBot uses Rasa Core to handle the conversation flow and execute actions based on the user's inputs and the bot's policies.
- **Large language models**: NewsBot leverages large pre-trained language models such as GPT-3 or GPT-Neo to generate natural and engaging responses. It also uses these models to perform tasks such as summarization, paraphrasing, and sentiment analysis.
- **News API**: Blog-NewsBot uses the News API to fetch the latest news articles from various sources and categories. It also uses the API to filter and rank the articles based on the user's queries and preferences.

## Installation

To install Blog-NewsBot, you need to have Python 3.7 or higher and pip installed on your system. Then, you can clone this repository and install the required dependencies using the following commands:

```bash
gh repo clone sahibpreetsingh12/Blog-newsbot
cd NewsBot
pip install -r requirements.txt
```

## Usage

To run Blog-NewsBot, you need to start the Rasa server and the action server using the following commands:

```bash
rasa run --enable-api --cors "*"
rasa run actions
```

Then, you can interact with Blog-NewsBot using either the Rasa shell interface. To use the Rasa shell, run:

```bash
rasa shell
```


You can also use other channels such as Telegram, Slack, or Facebook Messenger to connect with NewsBot. For more details, please refer to the [Rasa documentation](https://rasa.com/docs/rasa/connectors/your-own-website/).



I hope this helps you with your project. 😊