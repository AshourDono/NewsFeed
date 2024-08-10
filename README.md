
# Newsfeed - CROCOSOFT backend task

A **Python** microservice implemented using **Flask** microframework that should connect to **MySQL DB** with no ORM used.

**Note:**

As **Flask** is a microframework, I needed a directory structure, so I created the **flask_boilerplate.sh** file



## Acknowledgements

 - [Chatgpt](https://chatgpt.com/share/83f6184f-3840-48b7-83e0-33b4c7922986)
 - [Flask Docs](https://flask.palletsprojects.com/en/3.0.x/)
 - [Readme Editor](https://readme.so/editor)


## Environment Variables

To run this project, you will need to edit the following environment variables to your .env file

`DB_HOST`

`DB_PORT`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`


## Installation
1- Environment initiation:
```bash
 python -m venv .venv
 .venv\Scripts\activate
```
2- Package installation:
```bash
 cd NewsFeed
 pip install -r requirements.txt
```
3- DB creation:
 - get the sql scripts located in **Attachments** directory.
 - run its contents in any db app: like phpmyadmin
4- DB population:
```bash
 cd NewsFeed
 py seeder.py
```
5- Project Run:
```bash
 run_flask.bat
```
    
## API Reference

### Posts Endpoints: Done

#### Get a post

```http
  GET /api/posts/${post_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `post_id` | `int`    | **Required**. post_id      |

#### Update a post

```http
  PATCH /api/posts/${post_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `post_id` | `int`    | **Required**. post_id             |

Response Body
| Parameter | Type     | Description             |
| :-------- | :------- | :-----------------------|
| `content` | `string` | **Required**. content   |

#### Delete a post

```http
  DELETE /api/posts/${post_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `post_id` | `int`    | **Required**. post_id             |

#### Create a post

```http
  POST /api/posts
```
Response Body
| Parameter | Type     | Description             |
| :-------- | :------- | :-----------------------|
| `user_id` | `int`    | **Required**. user_id   |
| `content` | `string` | **Required**. content   |

### On Progress: User, Comment, Like, Share, Follow endpoints.


## Screenshots
ERD

![ERD](https://github.com/AshourDono/NewsFeed/blob/main/Attachments/news_feed_ERD.png)

