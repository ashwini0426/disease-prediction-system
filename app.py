from flask import Flask, render_template, request, url_for
import pandas as pd

# Create Flask App
app = Flask(__name__)

# All symptoms
symptoms_list = [

    'fever',
    'cough',
    'chest_pain',
    'shortness_of_breath',
    'blurred_vision',
    'eye_redness',
    'tooth_pain',
    'gum_swelling',
    'irregular_periods',
    'weight_gain',
    'acne',
    'frequent_urination',
    'increased_thirst',
    'weight_loss',
    'body_pain',
    'skin_rash',
    'sore_throat',
    'loss_of_smell',
    'high_fever',
    'joint_pain',
    'abdominal_pain',
    'vomiting',
    'swelling_legs',
    'wheezing'
]

# Natural solutions
solutions = {

    "Flu":
    "Drink warm water, take steam and proper rest.",

    "Heart Disease":
    "Avoid oily foods and do exercise daily.",

    "Eye Disease":
    "Reduce screen time and eat green vegetables.",

    "Teeth Disease":
    "Brush teeth twice daily and avoid sugar foods.",

    "PCOD":
    "Exercise daily and avoid junk food.",

    "Diabetes":
    "Avoid sugar and maintain healthy diet.",

    "Dengue":
    "Drink more fluids and take proper rest.",

    "Kidney Disease":
    "Drink enough water and avoid salty foods.",

    "Skin Disease":
    "Keep skin clean and avoid chemicals.",

    "Asthma":
    "Avoid smoke and dust.",

    "Typhoid":
    "Drink boiled water and eat light food."
}

# Home Page
@app.route('/')
def home():

    return render_template('home.html')

# Login Page
@app.route('/login')
def login():

    return render_template('login.html')

# Symptoms Page
@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():

    if request.method == 'POST':

        selected = request.form.getlist('symptoms')

        # If only one symptom selected
        if len(selected) <= 1:

            return render_template(
                'result.html',
                disease="No Disease Predicted",
                matched=[]
            )

        # Disease symptom mapping
        disease_data = {

            "Flu": [
                "fever",
                "cough",
                "body_pain",
                "sore_throat",
                "loss_of_smell"
            ],

            "Heart Disease": [
                "chest_pain",
                "shortness_of_breath",
                "joint_pain"
            ],

            "Eye Disease": [
                "blurred_vision",
                "eye_redness"
            ],

            "Teeth Disease": [
                "tooth_pain",
                "gum_swelling"
            ],

            "PCOD": [
                "irregular_periods",
                "weight_gain",
                "acne"
            ],

            "Diabetes": [
                "frequent_urination",
                "increased_thirst",
                "weight_loss"
            ],

            "Dengue": [
                "high_fever",
                "joint_pain",
                "body_pain",
                "vomiting"
            ],

            "Kidney Disease": [
                "swelling_legs",
                "frequent_urination",
                "abdominal_pain"
            ],

            "Skin Disease": [
                "skin_rash"
            ],

            "Asthma": [
                "cough",
                "wheezing",
                "shortness_of_breath"
            ],

            "Typhoid": [
                "high_fever",
                "abdominal_pain",
                "vomiting",
                "body_pain"
            ]
        }

        best_disease = "No Disease Predicted"

        max_match = 0

        matched_symptoms = []

        # Find best matching disease
        for disease, symptoms in disease_data.items():

            current_match = []

            for symptom in symptoms:

                if symptom in selected:

                    current_match.append(symptom)

            if len(current_match) > max_match:

                max_match = len(current_match)

                best_disease = disease

                matched_symptoms = current_match

        # Minimum 2 symptoms required
        if max_match < 2:

            best_disease = "No Disease Predicted"

            matched_symptoms = []

        return render_template(
            'result.html',
            disease=best_disease,
            matched=matched_symptoms
        )

    return render_template(
        'symptoms.html',
        symptoms=symptoms_list
    )

# Solution Page
@app.route('/solution')
def solution():

    from flask import request

    disease = request.args.get('disease')

    solution_text = solutions.get(
        disease,
        'No solution available'
    )

    return render_template(
        'solution.html',
        disease=disease,
        solution=solution_text
    )

# Run App
if __name__ == '__main__':

    app.run(debug=True)