# SellCar

The site is listing your cars for sale. So the user is able to list cars that they want to sell and are also able to view listing incase they want buy a car. You can upload images, vehicle build, and description of the vehicle. 


### wireframe

[img]https://i.imgur.com/3muDkfT.png
[img2]https://i.imgur.com/X6xajym.png
[img3]https://i.imgur.com/pYiVJfv.png


### Prerequisites/Installing

What things you need to install the software and how to install them
npm i to install dependencies

Need python installed
Need pipenv installed
Need postgres installed
pipenv install django



## Deployment
Used Herohu added some depencises in the django files in order to diploy 


## Built With
Html
css
python
django
bulma
psql

## Code Example
 Is a for loop that goes through cars and displays all of them (frontend). 
 
 {% for car in cars %}
          <a href="{% url 'car_detail' car.pk %}">
            <div class="card">
              <div class="card-image">
                <figure class="image is-square">
                  <img src="{{car.img}}" alt="{{car.make}}" />
                </figure>
              </div>
              <div class="card-header">
                <p class="card-header-title">{{car.year}} {{car.make}} {{car.model}} </p>
                <p class="card-header-title">{{car.price}} </p>
                </div>
            </div>
          </a>
          {% endfor %}

## Testing
App has full crud and user auth. So if all works then app is funcational.



## Acknowledgments/Documents resources
https://git.generalassemb.ly/seir-ten3/django-installation#setting-up-a-new-django-application---tunr_django
https://git.generalassemb.ly/seir-ten3/django-rest-framework
https://www.django-rest-framework.org/
https://www.django-rest-framework.org/api-guide/serializers/#customizing-field-mappings
https://www.django-rest-framework.org/api-guide/views/
https://www.django-rest-framework.org/api-guide/generic-views/
https://www.django-rest-framework.org/api-guide/authentication/
https://git.generalassemb.ly/seir-ten3/django-auth
https://git.generalassemb.ly/seir-ten3/django-models
https://bulma.io/documentation/layout/level/
https://bulma.io/documentation/columns/basics/
https://bulma.io/documentation/components/card/
https://bulma.io/documentation/components/navbar/
https://bulma.io/documentation/form/general/
https://bulma.io/documentation/layout/footer/
https://bulma.io/documentation/layout/level/

