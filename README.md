# FreeSpace: Find Open Study Spaces for Students

## Overview

**FreeSpace** is an innovative app designed to help students find available study spaces in real-time on campus. The app uses the **Area Density Tracker** to monitor room occupancy and identify open spaces for students to study. It was developed as a solution for the **Assurant Hackathon** and is ideal for students who need a quick and reliable way to find an open study area without wasting time walking around.

**FreeSpace** leverages object detection and tracking technologies to analyze video feeds of study areas, providing real-time data on how many people are present in each room. The app helps ensure that students can find quiet, available spaces to focus on their work.

## Key Features

- **Real-Time Tracking**: The app uses video feeds and an **Area Density Tracker** to monitor room occupancy in real time.
- **Live Occupancy Status**: Students can view which study areas have available space based on the current number of people in the room.
- **User-Friendly Interface**: The app is designed with a simple and easy-to-use interface for students to quickly check space availability.
- **Hackathon Solution**: Developed as part of the Assurant Hackathon, FreeSpace showcases the power of computer vision and real-time tracking for practical applications in student life.

## Technologies Used

- **Python**: The core backend of the app is built using Python.
- **OpenCV**: Used for object detection and tracking to analyze video feeds and count people in the rooms.
- **Euclidean Distance Tracker**: A custom tracking algorithm that tracks the movement of objects in real time.
- **Background Subtraction**: Background subtraction is used to detect moving objects and track their occupancy in study spaces.
- **Other Libraries**: `NumPy`, `Matplotlib`, and other OpenCV functionalities for image processing and visualization.

## How It Works

1. **Capture Video Feed**: The app captures video from cameras installed in various study areas.
2. **Track People**: The **Area Density Tracker** algorithm processes the video feed to count and track the number of people in the room.
3. **Analyze Density**: Based on the number of people detected, the app determines whether the study space is full or available.
4. **Display Data**: The availability status of each study area is displayed on the app's interface, so students can choose the best place to study.

## Installation

To get started with **FreeSpace**, clone the repository and install the required dependencies.


## PowerPoint Link
https://kennesawedu-my.sharepoint.com/:p:/g/personal/jbonheur_students_kennesaw_edu/EZH7nu69fwBNi29gFMau7lYBAdxeq0T2tmvhwwDsno1dRA?e=KWtZP8

### Clone the Repository

```bash
git clone https://github.com/Th1sJustIn/FreeSpace.git
cd FreeSpace
