# Goolkeeper-Training-Robot
In order to obtain the Engineering diploma in Automation field at the National Polytechnic School (Algeria) and in collaboration with the Central school of Electronics (France), I present to you my final thesis project, entitled **“Goalkeeper Training Robot”**.

![11](https://user-images.githubusercontent.com/46269667/63205455-41a0d000-c09c-11e9-8066-b8d3816b6de4.PNG)

## Summary
The project consists on the modeling and the realization of an autonomous robot that shoots
and evaluates the performances of a soccer goalkeeper based on his reactions.
Using a camera and a 3D human pose estimator, the system can detect and modelize the
goalkeeper’s physical gestures.
Finally, it proposes using artificial intelligence the suitable decision for the future exercises,
which maximizes the player’s performances.

## Folder structure
+ **README** 
  
+ **software/**
     - README
          - § Tool (Requirements , etc)
          - § Architecture (State-machine)
     - launch-train-goalkeeper.py 
     - launch-simulation.sh  
     - utils/ 
          - compute_pose.py
          - analyze_pose.py
          - send_navigation_mav.py
          - etc
+ **hardware/**
     - README
          - § List of components (existent and missing ones) 
     - mechanics/ 
          - cad_files/
          - images/
     - electronics/
          - cad-files/
          - images/
+ **articles/**
     - english
          - summary.docx 
          - summary.pdf
     - french
          - Mémoire_STIHI_Maha_ENP.pdf
