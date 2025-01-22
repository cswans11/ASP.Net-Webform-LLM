# ASP.Net-Webform-LLM

## LLM Folder
This contains the source code for the ASP.NET application built using Visual Studio 2022. The application creates a web app which utilizes Webforms to connect to the python LLM background. 

To use this you simply start the project in Visual Studio. A page with a basic text box and button should appear. 

## llm_socket.py 

This file downloads the given model to the local computer. For repeated use, the model is stored and is accessed through checkpoints. The script opens up a port for listening and when a message is received, it runs it through the llm. The answer is then sent back through the port to the listening ASP.NET application and displayed on the screen. 

##### Warning: The model is meant to be run with access to multiple GPU's so the response time can be varied and lengthy. For my Dell XPS, the average response time was 5 minutes. 

