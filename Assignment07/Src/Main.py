#main.py

# Name: Aanika Garre
# email:garreaa@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date: 2/29/24
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on modifying an existing project from GitHub.

# Brief Description: This module goes over a basic understanding of using GitHub and how to upload and modify existing projects.
# Citations:
# Anything else that's relevant:
'''
Created on Feb 26, 2020

@author: nicomp
'''

from Src.Assignment07 import generate_captcha

result = generate_captcha(7,"captcha.png")
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()
