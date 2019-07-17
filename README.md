# Music recommendation service
This project is intended to help users to find new interesting music bands based on their vk.com profile.

It's simple: send your user_id and get recommendation of 5 music bands which will likely meet your taste. 

Adjust settings and try again.

## Under the hood system has 7 main parts:
- UI:
Django based web server.
- Telegram bot:
just start chat with @Muzender_bot
- recommendation model:
We use Word2Vec, it supports online recommendation without recalculation, it takes about 25ms for to generate 
recomendations for new user. It also have tiny memory footprint which allows to host whole system on 1 CPU, 
1GB RAM server.
- vk.com user page parser:
We use vk_api implementation to parse all user music data. We run multiple parsers at the same time to work with several users simultaneously.
- Redis to cache parser results for fast recommendation recalculation when user changes settings.
- message queue:
RabbitMQ as queue manager. Really easy to work with and functional.
- vk.com crawler: it runs through user's friends and friends of friends, send their pages to parser to collect dataset. 

All services run in Docker containers and we use docker compose for orchestration. This allows to deploy and run all 
services with a single command, test different solutions in parallel and balance loads. 

## Super quick start:
- download [model_w2v.pkl](https://drive.google.com/open?id=1Jkvhuo5ULFl8L4jkwc_1XjtFkEaosyHm) (290MB) to /data/

- setup vk account for parser:
create dictionary with 'login' and 'password' keys and enter your values and dump it to pickle version 3 
to parser/secret.pkl and crawler/secret.pkl

- setup telegram bot token:
pickle string with bot token and dump it to tg_bot/token.pkl 

- start service:
cd to root folder of the project and run: `docker-compose up --build .`

- get your recommendation:
just open http://localhost:8000 in your browser and enter vk.com user id

## Build dataset and train model from scratch:
- get data:
You can use Million Song Dataset and Echo Nest user-music rating dataset. 
Download these tables /data/ (you will find links in dataset_sources.txt file of this folder).

Alternatively you can use our own dataset which includes 950K of music playlists (links also in dataset_sources.txt file of this folder)

- preprocess data:
Run /model_creation/dataset_assembly.ipynb to reformat data to apropriate format.

- train model:
Run /model_creation/w2v_recommender.ipynb to generate model and band popularity index.

## Dataset
During project development we collected huge dataset of user music playlists, we believe it's one of the biggest 
(950K unique users, 92M interactions) open datasets with user-item interactions with real item names available.

You can find dataset on [Kaggle](https://www.kaggle.com/usasha/million-music-playlists).
