# Django Chat App

Django Chat App is a real-time chat application built using Python, Django, Tailwind CSS, Django-channels, WebSocket, and Redis as the channels layer. This app allows users to create public and private chat rooms, and communicate with other users in real-time.

## What I Learned

During the development of this project, I learned how to:

- Integrate Websocket and Django to build real-time chat applications.
- Use Django Channels and Redis as the channels layer to handle WebSocket - requests and push messages to the clients in real-time.
- Build responsive and modern user interfaces using Tailwind CSS. (Yay! I know that not good. not a Frontend guy.)
- Implement user authentication and authorization using Django's built-in - authentication system.
- Use Django ORM to implement CRUD operations for the chat rooms.
- Build a feature to create public and private chat rooms.

## Features
- Sign-up, sign-in, and sign-out functionality
- Create and join public and private chat rooms
- Real-time communication using Websocket and Redis
- Edit and delete rooms
- View a list of all public and private rooms
- Responsive design using Tailwind CSS

## Requirements
- Python 3.x (I used 3.10.9)
- Django 3.x (I used 3.2.18)
- Channels(I used 3.0.5) 
- Tweak(I used 1.4.12)

## :exclamation:  This is very important

NOTE: Before running the app, please ensure the following steps:

If you are running the app on a development server, please comment out the Postgres database 
setting and Redis channel layer in the settings.py file and uncomment the In-Memory Channel 
Layer and SQLite3 database settings.

If you are using a .env file, please ensure that you provide important environment variables 
such as SECRET_KEY, DEBUG, and ALLOWED_HOSTS. If you want to use the environment variables 
directly, please comment out all the os.environ.get functions in the settings.py file and 
provide all the environment variables directly.

By following these steps, you will be able to run the app smoothly without any errors related 
to database or environment variables. 

## Support
If you need any help or have any questions, please feel free to contact me.

## Conclusion
In conclusion, the chat application is a useful tool for facilitating communication between users in real-time. The application makes use of various technologies such as Django, Channels, and Redis to provide a seamless experience for users. The different components of the application, such as the URL patterns and HTML templates, work together to create a functional and aesthetically pleasing user interface. However, before running the application, it is important to ensure that the necessary environment variables are properly configured, especially if using a .env file. By following the instructions and best practices provided, developers can create a reliable and secure chat application that meets the needs of their users.

## Fun Section
The demo web site is up and running at [here](https://jethliyabalaji-chat.up.railway.app/) but it may be temporarily down because the developer needs a coffee break. If you find the app helpful, feel free to buy the developer a coffee! [here]()

## Authors
Balaji Jethliya - Initial work - [GitHub](https://github.com/jethliya-balaji), [Twitter](https://twitter.com/jethliyabalaji)
