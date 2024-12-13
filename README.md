# MadlibKivy

Mad Libs Game
Overview

This is a simple Mad Libs game application built using Kivy, a Python framework for developing multitouch applications. The game allows users to input words (nouns, verbs, adjectives) and select a mood to generate a fun and random story based on predefined templates.

Features

Input fields for nouns, verbs, and adjectives.
A dropdown menu (Spinner) to select a mood.
Buttons to generate a story, reset inputs, and show help.
A scrollable area to display the generated story.
Random selection of words and moods if the input fields are left empty.

Installation

To run this application, ensure you have Python and Kivy installed. You can install Kivy using pip:

pip install kivy

Clone the repository or download the code, then run the application:

python mad_libs.py

Usage

Enter a noun, verb, and adjective in the respective fields.
Choose a mood from the dropdown menu.
Click the "Generate Story!" button to create a fun story.
Use the "Reset" button to clear the inputs and start over.
Click "Help" for instructions on how to use the application.

Answers to Questions

What is the purpose of this application? The purpose of this application is to provide a fun and interactive way to create silly stories using user-provided words.

How does the story generation work? The application randomly selects a story template and fills in the placeholders with the user inputs or randomly chosen words if the inputs are empty.

What are the predefined lists used in the application? The application includes predefined lists of nouns, verbs, adjectives, and moods to enhance the story generation process.

Known Issues

The application may not handle very long words or phrases well, which could affect the layout of the story display.
The random selection of words may lead to repetitive stories if the user does not provide their own inputs.
