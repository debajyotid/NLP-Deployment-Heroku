# NLP-Model-Deployment
### This project is forked from https://github.com/krishnaik06/NLP-Deployment-Heroku.
#### I have added more comments and have updated the below Readme to make the files more readable & the overall process more understandable. I have also added a separate file (model.py) for the model training

In this demonstration, we show how we can leverage Heroku PaaS for our ML model deployment using a Flask WebAPI.

Our ML model is a simple salary predictor and takes the below 3 i/p as features, along with the salary drawn as the target:
1. experience
2. test_score
3. interview_score

This data is availabe in a csv file called 'hiring.csv'.

We then perform a simple LinearRegression to predict salaries for employees for whom we have only the above features, but not the actual salary. Thus, this is a Supervised Learning problem.

Once the model is trained, we save it as a .pkl file using pickle. This model is then deployed on Heroku using a Flask web-service, and a html page is provided to capture the i/p features and display the predicted salary.

Using Flask, we can also execute the model locally and provide the i/p features either using the webpage hosted on our local m/c or by passing the features via a URL request.

The web-app is hosted at:
https://deb-nlpspamdetection-demo.herokuapp.com
##
#### I had faced issues in direct deployment from krishnaik06/Heroku-Demo due to joblib import from sklearn.externals having been deprecated. I commented the import statement in app.py & the rest of the model deployment & hosting on Heorku was successful.
#### The deployment logs were available in Heroku CLI & I used the command:$ heroku logs --app deb-nlpspamdetection-demo to check the deployment logs. Here deb-nlpspamdetection-demo is my Heroku app name ####
