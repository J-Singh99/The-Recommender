![alt text](https://github.com/J-Singh99/The-Recommender/blob/master/ReadMe%20Images/RecommendationEngine.webp)
    
# THE RECOMMENDER  
An app made **for** students, **by** students

### Mentor: Prof. Rajesh Bhatia
#### Group ID : 4
**Atul Jawa** 18103122  
**Jaspreet Singh** 18103107  
**Parizat Garg** 18103097  
**Malvika Jindal**  18103040
  
  
  
### Aim
The primary motive of this project is to provide a common platform for productivity and entertainment.

Often, the leap from work to play is large, and switching modes, whether mental or physical, is difficult. Hence, our idea was to bring both sides of the coin to a common plane.

The main idea behind this application, targetted specifically for college students, is that you manage your usual college work flow, including assignments, tests, events, etc. along with intuitive entertainment like personalised movie and song recomendations, mood sensing interactions, etc.   
  
  
### Overview
This is an application primarily to integrate entertainment with college activities.
Activities like maintaining a schedule, organizing events, submitting assignments, etc. would be done side-by-side with an ML model that recommends movies and songs, a chatbot that senses your mood (as a scalable idea), recomendations for activities, etc. All this is done parallely, so the user can seamlesly submit an assignment, watch a personally recommended movie, manage college events, chat with a group, etc. all in the same application.
  
  
  
### Goals
- Create an ML supported recommendation system for songs, videos, activities, etc.
- Build a discussion forum to connect students to organize events
- Build a supporting notification system to notify the user of the same
- A system for managing assignments and schedules, such as a to-do list
- Build a chat system with group chat functionality 
  
  
### Technologies Used:
- Django
- Python 
- Sklearn for ML
- Numpy & Pandas
- Django channels
- Html Css Bootstrap


![alt text](https://github.com/J-Singh99/The-Recommender/blob/master/ReadMe%20Images/Photo2.webp)


## HOW TO RUN
Please run the following commands to run the project:
- `pip install requirment.txt`
- `python manage.py makemigration`
- `python manage.py migrate`
- `python populate_movies_link.py`
- Train model
  - Download and extract [this file](https://drive.google.com/file/d/1rQdmWz3u9G1V_d0R8NbPYvuhcYls7RgB/view?usp=sharing) to **movieRecom/mlModel/**  
  OR
  - `python movieRecom/mlModels/Svdtuning.py`
- Start Redis services  
- `python manage.py runserver`


## Use Case Diagram  
![Use Case Diagram](https://github.com/J-Singh99/The-Recommender/blob/master/UML%20diagrams/Use%20case%20diagram.pdf)

## Class Diagram  
![Class Diagram](https://github.com/J-Singh99/The-Recommender/blob/master/UML%20diagrams/class_diagram_SE.pdf)

#### The link to the project write up PDF can be found [here](https://docs.google.com/document/d/1e4s_ns_DGjKBgFjUaxnllk0Nj08A2Vivo7f9j8acFW4/edit?usp=sharing).  
#### The link to the UML Diagrams can be found [here](https://drive.google.com/drive/folders/1B_514GvPcEAeFQ03XSfG496SJAam8VPp?usp=sharing).
