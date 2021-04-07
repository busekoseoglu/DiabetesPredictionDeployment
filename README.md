# Diabetes Prediction Deployment with Flask and Heroku

PIMA Indian Diabetes dataset is used in this project. Features are;

1. Pregnancies: Number of times pregnant
2. Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3. BloodPressure: Diastolic blood pressure (mm Hg)
4. SkinThickness: Triceps skin fold thickness (mm)
5. Insulin: 2-Hour serum insulin (mu U/ml)
6. BMI: Body mass index (weight in kg/(height in m)^2)
7. DiabetesPedigreeFunction: Diabetes pedigree function
8. Age: Age (years)
9. Outcome: Class variable (0 or 1)

## model.py
Created and tuned a model with random forest. This model is saved as a pickle file (model.pkl).

## app.py
index.html file opens with using flask. According to user inputs makes a prediction. For prediction process pickle file opens as model. 
If user do not enter anything in form return a warning.

## index.html
Created a form for take the inputs from user.

## Heroku
Procfile, runtime.txt and requirements.txt ara necessary for heroku.

## You can find the project here : [Diabetes Prediction Heroku](https://diabetes-prediction-pro.herokuapp.com) 

![Ekran görüntüsü 2021-04-07 114744](https://user-images.githubusercontent.com/44964158/113838308-52351b00-9797-11eb-9aad-8f941d1bbf03.png)
