# NgCarRestAPI
 Recruitment task


## Technologies
 * Python
 * Django
 * Docker 
 * Bootstrap

## Frameworks
 * Django-Rest-Framework
## Installation

Pull application from github 
Open application folder with powershell and run command below :

```shell
docker-compose build 
```

```shell
docker-compose run 
```
or start docker image from docker-desktop application 

After that open your browser and go to http://localhost:8000/

## Usage

* POST /cars

If we introduce corret data in both fields, application will return success response about existing car in this API https://vpic.nhtsa.dot.gov/api/ and about adding car to our data base. If We introduce wrong data, We will have wrong response returned and that means the data are wrong or in our database car with same mark and model exists.
Example of data input : 
{
  "make" : "Volkswagen",
  "model" : "Golf"
}

* DELETE /cars/{id}
We are able to delete car by id
Example of data input : https://ngapplication.herokuapp.com/cars/6/ <- remember LAST SLASH !

* POST /rate

We can rate each car in our data base.
Example of data input :
{
  "car_id" : 1,
  "grade" : 5
}

* GET /cars

Due to DRF view, each car is shown in response with mark, model and with their current average rate.


* GET /popular

Due to DRF view we see data with each object in our database with field called rates_number which means how many votes each car has.



## HEROKU

Project is deployed on Heroku 
[link](https://ngapplication.herokuapp.com/)


## Authors 

https://github.com/LikeaBoooM
