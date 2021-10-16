# Plathanus Python Test

This project aims to set up an interview with the <a href="https://tabas.com.br/">Tabas Project</a>. The challenge is to make an application that can save properties registers. In the register model we need an `name` and for each property we need at least 3 and a maximum of 5 photos. This photos should be stored locally.


## About the Backend Architecture

It uses an the DDD design pattern, being: domain, Infrastructure, services and presentation layers. Each layer has its own responsability and dependecies specified as follows:

* Domain - Does not depend on anybody, the main business rule of the application;
* Infrastructure - Any communication, storage, database that its outside of the application;
* Services - The use case of the application;
* Presentation - Data transformation and API / FrontEnd layers.
  

## About the Technology

It uses python 3.9.1.
For the presentation layer we are using:
* FastAPI for the API / FrontEnd server-side HTML render with Jinja Templates.
For the Infrastructure layer we are using:
* PostgreSQL for the Database
* SQLAlchemy as the ORM;
* Local Storage for saving the image files.
  
The infrastructure layer has factories in case the Database, Storage or ORM type changes.


## Running the project

On an terminal:
`python -m pip install requirements.txt`

And then:
`cd backend`

Lastly:
`uvicorn presentation.http.app:app`
