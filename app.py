from flask import Flask, render_template, request, url_for

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

# Disease Solutions
solutions = {

    "Flu": {
        "medicines": "Paracetamol, Cough Syrup",
        "precautions": "Take rest, Drink warm water",
        "diet": "Soup, Fruits, Warm liquids",
        "home_remedies": "Ginger tea, Steam inhalation",
        "doctor": "General Physician"
    },

    "Heart Disease": {
        "medicines": "Aspirin, Blood Pressure Tablets",
        "precautions": "Avoid stress and oily food",
        "diet": "Low-fat diet, Green vegetables",
        "home_remedies": "Regular walking, Meditation",
        "doctor": "Cardiologist"
    },

    "Eye Disease": {
        "medicines": "Eye Drops, Vitamin A tablets",
        "precautions": "Avoid screen time",
        "diet": "Carrot, Green vegetables",
        "home_remedies": "Cold water wash",
        "doctor": "Eye Specialist"
    },

    "Teeth Disease": {
        "medicines": "Painkillers, Mouth Gel",
        "precautions": "Brush twice daily",
        "diet": "Avoid sweets",
        "home_remedies": "Salt water rinse",
        "doctor": "Dentist"
    },

    "PCOD": {
        "medicines": "Hormonal tablets",
        "precautions": "Exercise regularly",
        "diet": "Healthy protein diet",
        "home_remedies": "Yoga and hydration",
        "doctor": "Gynecologist"
    },

    "Diabetes": {
        "medicines": "Insulin, Metformin",
        "precautions": "Avoid sugar",
        "diet": "Low sugar diet",
        "home_remedies": "Fenugreek seeds",
        "doctor": "Diabetologist"
    },

    "Dengue": {
        "medicines": "Paracetamol",
        "precautions": "Avoid mosquito exposure",
        "diet": "Papaya leaf juice, Fluids",
        "home_remedies": "Drink plenty of water",
        "doctor": "General Physician"
    },

    "Kidney Disease": {
        "medicines": "Blood pressure medicines",
        "precautions": "Reduce salt intake",
        "diet": "Low sodium diet",
        "home_remedies": "Stay hydrated",
        "doctor": "Nephrologist"
    },

    "Skin Disease": {
        "medicines": "Antifungal cream",
        "precautions": "Maintain hygiene",
        "diet": "Vitamin-rich foods",
        "home_remedies": "Aloe vera gel",
        "doctor": "Dermatologist"
    },

    "Asthma": {
        "medicines": "Inhaler",
        "precautions": "Avoid dust and smoke",
        "diet": "Healthy fruits",
        "home_remedies": "Steam therapy",
        "doctor": "Pulmonologist"
    },

    "Typhoid": {
        "medicines": "Antibiotics",
        "precautions": "Drink clean water",
        "diet": "Boiled food, Fruits",
        "home_remedies": "ORS and rest",
        "doctor": "General Physician"
    }
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
                'solution.html',
                disease="No Disease Predicted",
                solution={
                    "medicines": "No medicines available",
                    "precautions": "No precautions available",
                    "diet": "No diet available",
                    "home_remedies": "No home remedies available",
                    "doctor": "No doctor recommendation"
                }
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

        # Get Solution Data
        solution_data = solutions.get(
            best_disease,
            {
                "medicines": "No medicines available",
                "precautions": "No precautions available",
                "diet": "No diet available",
                "home_remedies": "No home remedies available",
                "doctor": "No doctor recommendation"
            }
        )

        return render_template(
            'solution.html',
            disease=best_disease,
            solution=solution_data
        )

    return render_template(
        'symptoms.html',
        symptoms=symptoms_list
    )

# Run App
if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)