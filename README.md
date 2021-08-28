# NLP-Model-Deployment
### This project is forked from https://github.com/krishnaik06/NLP-Deployment-Heroku.
#### I have added more comments and have updated the below Readme to make the files more readable & the overall process more understandable. I have also added a separate file (model.py) for the model training

In this demonstration, we show how we can leverage Heroku PaaS for our ML model deployment using a Flask WebAPI.

We are creating Spam-Ham SMS Filtering model using CountVectorizer based approach, and then used MultinomialNB for classification purposes.

Here we needed to create 2 .pkl files, as we needed to save the CountVectorizer model (for transformation of incoming data during run-time), as well as the actual MultinomialNB classification model.

This entire architecture is then deployed on Heroku using a Flask web-service, and a html page is provided to capture the i/p features and display the predicted salary.

Using Flask, we can also execute the model locally and provide the i/p features either using the webpage hosted on our local m/c or by passing the features via a URL request.

The web-app is hosted at:
https://deb-nlpspamdetection-demo.herokuapp.com
##
#### I had faced issues in direct deployment from krishnaik06/Heroku-Demo due to joblib import from sklearn.externals having been deprecated. I commented the import statement in app.py
### In addition, I also changed the sklearn version from 0.18 to 0.23.2, as I had faced issues with this earlier & build the model .pkl files locally. The rest of the model deployment & hosting on Heorku was successful.
#### The deployment logs were available in Heroku CLI & I used the command:$ heroku logs --app deb-nlpspamdetection-demo to check the deployment logs. Here deb-nlpspamdetection-demo is my Heroku app name ####
