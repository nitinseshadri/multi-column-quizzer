#!/usr/bin/env python3

import random
import numpy as np
import pandas as pd

print("Multi-Column Quizzer")
print("by Nitin Seshadri")
print("Film Identification Quiz version")

df = pd.read_excel("./questions.xlsx")
df = df.sample(frac=1).reset_index(drop=True)

print("\nLoaded questions\n")

total_questions_asked = 0
correct_answer_count = 0

while True:
        row = df.sample()
        
        film_name = row["Name"].values[0]
        
        film_question_column_name = random.choice(["Filmmaker", "Release Year", "Country of Origin"])
        
        print(film_question_column_name, "of", film_name + "?")
        
        user_answer = input("> ")
        
        user_answer = str(user_answer)
        
        correct_answer = str(row[film_question_column_name].values[0])
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answer_count += 1
        else:
            print("Incorrect, the correct answer is", correct_answer)

        total_questions_asked += 1

        print("Score:", str(correct_answer_count)+"/"+str(total_questions_asked), "("+str(int((correct_answer_count/total_questions_asked)*100))+"%)")

        print("\n")
