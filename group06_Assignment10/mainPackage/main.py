# Name: Aditya Achar, Riley McCullough
# email: acharay@mail.uc.edu, mccullrw@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: API Assignment
# Citations: https://api.collegefootballdata.com/api/docs/?url=/api-docs.json#/
# Anything else that's relevant:

import json
import requests # Web requests
import cfbd # College football database

configuration = cfbd.Configuration()

# API Key
configuration.api_key['Authorization'] = '3nVVw1xOAHEuUjZ4qzyr0m5THv+pMRPDg1hKQTK8McLzxvj2n1wtoMGtNpOUvnV9'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# Ohio State vs. Michigan 2014 data
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
games = api_instance.get_games(year = 2014, team = 'Ohio State', week = 14)

print(games)
