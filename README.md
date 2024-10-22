# Control System Task

This repository contains the code and documentation for a control system task involving a system that processes commands related to a drive system and arm components using WebSockets. The task involves parsing specific command structures to manage different parts of a robotic system.

## Screencapture

## Project Structure

The repository contains all project files inside the control-system-task folder. The key components include:

### WebSocket Command Parsing: 
The system receives and processes real-time commands via WebSockets to control drive and arm components.

### Drive System Commands: 
Commands starting with D_ manage the drive system of the robot.

### Arm System Commands: 
Commands starting with A_ manage arm components such as the elbow, wrist, claw, gantry, and shoulder.

### Part-1-task (Python Program): 
A Python program that connects to a PS4 controller using pygame, processes controller inputs, and outputs them in the required command structure (D_ or A_) using sockets and WebSockets.

### Part-2-option-A (React Web App): 
A React-based web app that receives WebSocket data from the part-1-task and visualizes the commands using Chart.js.

## Command Structure

The commands follow a structured format:

### Drive Commands:
D_128_128_128_128_128_128
Each segment represents a specific part of the drive system.

### Arm Commands:
A_128_128_128_128_128_128
Each segment represents a specific component of the arm.

The numbers represent different control values for each component. The system parses these commands in real-time to perform actions on the respective components.

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/Allenreinoso28/control-system-task.git
Navigate to the project directory:
bash
Copy code
cd control-system-task
Running the Python Program (Part-1-task)
Navigate to the part-1-task folder:

bash
Copy code
cd part-1-task
Install pygame if not already installed:

bash
Copy code
pip install pygame
Run the Python program:

bash
Copy code
python controller.py
The program will detect inputs from the PS4 controller, process them, and output the corresponding command structure through sockets and WebSockets.

Running the React Web App (Part-2-option-A)
Navigate to the part-2-option-A folder:

bash
Copy code
cd part-2-option-A
Install the necessary dependencies:

bash
Copy code
npm install
Run the React app:

bash
Copy code
npm start
The web app will receive WebSocket data from the part-1-task and visualize the commands using Chart.js.

Features
Real-time WebSocket Integration: The project receives and handles commands in real-time.
PS4 Controller Input Processing: The Python program captures controller inputs and converts them to command structures.
Command Visualization: The React web app visualizes the received commands using Chart.js.
Modular Command Parsing: The system parses both drive and arm commands based on their respective structures.
Technologies
JavaScript
React
WebSockets
Python
Pygame
Chart.js
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, feel free to contact Allen Reinoso at allenreinoso28@gmail.com.
