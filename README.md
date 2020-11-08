![alt text](https://github.com/J-Singh99/The-Recommender/blob/master/ReadMe%20Images/RecommendationEngine.webp)
    
# The Recommender  
An app made for students, by students

### Mentor: Prof. Rajesh Bhatia
#### Group ID : 4
**Jaspreet Singh** 18103107  
**Parizat Garg** 18103097  
**Atul Jawa** 18103122  
**Malvika Jindal**  18103040
  
  
  
### Aim
The primary motive of this project is to provide a common platform for productivity and entertainment.

Often, the leap from work to play is large, and switching modes, whether mental or physical, is difficult. Hence, our idea was to bring both the sides of the coin to a common plane.

The main idea behind this application, targetted specifically for college students, is that you manage your usual college work flow, including assignments, tests, events, etc. along with intuitive entertainment like personalised movie and song recomendations, mood sensing chatbots, etc.   
  
  
### Overview
This is an app to integrate entertainment with college activities like maintaining a schedule, organize events, and get notifications for all.  This app will feature a chatbot, which analyzes the mood of the user, and recommends activities like exercise, watch a movie, study, etc. All this is done parallely, so the user can seamlesly submit an assignment, watch a personally recommended movie in the same application, manage college events, chat with a chatbot, etc all in the same application.
  
  
  
### Goals:
- Create recommendation systems for songs, news, videos, and activities.
- Create a chatbot to chat with the user and to analyze the mood of the user
- Build a discussion form to connect students to organize events and a notification system to notify the user of the same.
- A system for managing assignments and schedules. 
- Feature to use different systems at once like listening to songs and reading news at once.
  
  
### Technologies Used:
- Python, for different ML models
- Flask, as a web framework
- React for frontend.  
- Flutter, to create a mobile application.

![alt text](https://github.com/J-Singh99/The-Recommender/blob/master/ReadMe%20Images/Photo2.webp)


## How to run
Please run the following commands to run the project:
- `pip install requirment.txt`
- `python manage.py makemigration`
- `python manage.py migrate`
- `python manage.py createsuperuser`
  - Follow the on screen commands to set up the superuser
- `python populate_movies_link.py`
- `python user_sample.py`
- `python populate_song_user.py`
  - Download and extract [this file](https://drive.google.com/file/d/1rQdmWz3u9G1V_d0R8NbPYvuhcYls7RgB/view?usp=sharing) to **movieRecom/mlModel/**
- Start Redis services  
- `python manage.py runserver`


## Use Case Diagram  
![Use Case Diagram](https://github.com/J-Singh99/The-Recommender/blob/master/UML%20diagrams/Use%20case%20diagram.pdf)

## Class Diagram  
![Class Diagram](https://github.com/J-Singh99/The-Recommender/blob/master/UML%20diagrams/class_diagram_SE.pdf)

#### The link to the project write up PDF can be found [here](https://docs.google.com/document/d/1e4s_ns_DGjKBgFjUaxnllk0Nj08A2Vivo7f9j8acFW4/edit?usp=sharing).  
#### The link to the UML Diagrams can be found [here](https://drive.google.com/drive/folders/1B_514GvPcEAeFQ03XSfG496SJAam8VPp?usp=sharing).
