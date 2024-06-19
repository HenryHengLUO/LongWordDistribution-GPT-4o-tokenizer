# GPT-4o Tokenizer: Exploring the Long Word Distribution 🚀

Welcome to this exciting project where we dive deep into the world of long word distribution using the [GPT-4o](https://openai.com/index/hello-gpt-4o/) tokenizer [o200k_base](https://community.openai.com/t/whats-the-new-tokenization-algorithm-for-gpt-4o/746708)! 😄🔍

## Project Overview

The main objective of this project is to uncover the top 100 long token sub-words for 11 different languages. These languages include:

1. English 🇺🇸
2. Japanese 🇯🇵
3. Korean 🇰🇷
4. Chinese 🇨🇳🇨
5. Russian 🇷🇺
6. German 🇩🇪
7. French 🇫🇷
8. Italian 🇮🇹
9. Spanish 🇪🇸
10. Portuguese 🇵🇹
11. Turkish 🇹🇷

To achieve this, we utilized the [tiktoken](https://github.com/openai/tiktoken?tab=readme-ov-file#-tiktoken) library, a lightning-fast open-source tokenizer developed by OpenAI that makes [encoding and decoding](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb) a breeze. 🌪️📚

Determining the language of these tokens was no small feat! We employed advanced methods like [langid](https://github.com/saffsd/langid.py) and [langdetect](https://pypi.org/project/langdetect/), using a probability threshold set at 0.5. 🕵️‍♀️🔍

## Project Structure

The project is organized into three folders, each containing a Python file and data CSV files. Let's take a closer look at them:

1. `tokenizer_o200k_base_langid`: This folder contains the Python file and data CSV files for language identification using the langid method.

2. `tokenizer_o200k_base_langdetect`: Here, you'll find the Python file and data CSV files for language identification using the langdetect method.

3. `tokenizer_o200k_base_langid&langdetect`: In this folder, we combine the powers of both langid and langdetect methods for language identification. You'll find the respective Python file and data CSV files here.

## GPT-4o: The New Frontier 🌌

GPT-4o, developed by OpenAI, is the latest flagship model that has revolutionized the world of AI. It can reason across audio, vision, and text in real time, opening up endless possibilities! 🌟💡

One of the key innovations in GPT-4o is the introduction of a brand new tokenizer called o200k_base. This tokenizer plays a crucial role in preparing text materials for large language models like GPT-4o. It breaks down the text into smaller units called tokens, optimizing computation resources and improving semantic coherence. 🧩✂️

Tokens are like puzzle pieces that come together to form the bigger picture of language understanding. By analyzing the distribution of these tokens, we gain valuable insights into how language is structured and used. 📊🔍

## Conclusion

With this project, we've embarked on a thrilling journey through the depths of long word distribution using the GPT-4o tokenizer o200k_base. We've explored multiple languages and harnessed the power of advanced language identification methods.

Remember, language is a beautiful tapestry woven with tokens. By understanding its intricacies, we unlock new possibilities for human-machine interaction and communication.

So, let's dive in and uncover the fascinating world of long word distribution together! Happy exploring! 🎉🔬😄
