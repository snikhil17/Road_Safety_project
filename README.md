# Deploying App on Cloud

We have deployed the app on cloud using Streamlit & Docker successfully.


# Streamlit Application:

## Note: 
- **Sign Up** in [Streamlit](https://share.streamlit.io/) using your personal credentials
- Link your project github repository to visualize your application on Streamlit

Demo Link : https://share.streamlit.io/prathimacode-hub/ai-for-road-safety/main/main.py


# Docker Steps:

## Note: 
- **snikhil17** : login ID of Dockerhub (use own when deploying)
- **omdena_road_safety**: name of the image created (you may use something else)

## To Push the image and run in your PC
## Create the image
- **docker build -t snikhil17/omdena_road_safety .**
## Run the image in  local PC
- **docker run -it -p 8501:8501 snikhil17/omdena_road_safety**
- **To run streamlit: once docker image is run. Open a new browser and run http://localhost:8501/**

## To Push image in docker-hub
- **docker login**
- **docker push snikhil17/omdena_road_safety** 

## To  pull the image and run in your PC
- **docker pull snikhil17/customer_intention_1:latest**
- **docker run -it -p 8501:8501  snikhil17/omdena_road_safety**
- To run streamlit: once docker image is run. Open a new browser and run **http://localhost:8501/**


# Tasks Involved:

## Natural Language Processing

Label & Sentiment Generator - Check out this application through Streamlit Demo App Link provided.

## Computer Vision

Eye Gaze Estimation + Drowsiness Detection + Yawn Detection

This application doesn't support Streamlit, hence it can compiled directly on Local System using generated [driver_distraction_eyegaze_drowsiness_yawn.exe](https://drive.google.com/file/d/18GMcLeY4d0U1LTraKtCRMNTv4yho91al/view) file in the drive.
