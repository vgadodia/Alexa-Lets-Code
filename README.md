

## Inspiration
With the recent COVID-19 pandemic, students worldwide have transitioned to online schooling. For some students, however, the transition has been harder than for others. Near where Veer lives is the oldest school for blind students: Perkins School for the Blind. Veer had always wanted to help them, and, during these times, he decided to help them when they needed it more than ever. Together, our team worked on an online platform dedicated for the blind and targeted for our favourite lesson: programming.<br><br>
According to the National Federation of the Blind, COVID-19 has had a disproportionate impact on the blind, with many facing additional challenges during the pandemic. From an education standpoint, blind students and blind parents face uncertainty about the types of electronic materials they will be expected to use for the remainder of the academic year, making it hard for them to keep up with classes. Lastly, it is difficult for the visually impaired to learn how to code on their computer, a challenge which has been exacerbated by the pandemic.

## What it does
We utilized a complex tech stack incorporating alexa skills, flask endpoints, rest api's, google cloud speech to text, and a python desktop application in order to build a speech-to-text editor which can listen to speech, translate it to Python code, and then display the code in an desktop text editor. The platform is complete with voice enabled git commands which the user can perform using the amazon alexa.<br>
We used natural language processing to:
<ol>
<li>Allow the visually impaired to code in python by simply speaking</li>
<li>Provide a handful of voice enabled git commands and speech recognition features to effectively teach coding and version control</li>
<li>Display the spoken code in an online IDE, where one can run it and get the output</li>
</ol>

## How we built it
We used:
<ul>
<li>Amazon Alexa</li>
<li>Flask</li>
<li>Python</li>
<li>Natural Language Processing</li>
<li>Google Cloud Speech API</li>
</ul>

## Challenges we ran into
At first, we wanted to run everything through Alexa; however, we soon learned that we could not read raw text directly from an Alexa action. Thus we decided to pivot to using Alexa for specific commands and the GCP to intake and process all the commits. We also faced difficulty with time zone differences and staying connected. 

## Accomplishments that we're proud of
We're proud of how we handled the situation once we figured out Alexa couldn't process raw data. We were able to pivot our project nicely and create a product we're proud about. Despite never having met in person, our team as a group was able to be flexible and adapted to the situation. 

## What we learned
We learnt how to use speech recognition and execute the code in string form. We also learned more about linking Alexa skills and git commands with Python, as well as connecting to flask endpoints through desktop applications, especially for real-time work. Overall, three of our four teammates learned about Alexa and its compatibility, and we all tried to learn more by combining different technologies together. 

## What's next for Alexa, Let's Code
We eventually want to push this out for all Alexa users. In addition, we want to connect our application with popular text editors, such as VSC, Repl.it, and Atom. We want to eventually expand our project to more languages and functionalities to ease the life of developers. 