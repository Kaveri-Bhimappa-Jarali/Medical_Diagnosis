# =====================================================
#      MEDICAL DIAGNOSIS EXPERT SYSTEM
# =====================================================

print("========================================")
print("      MEDICAL DIAGNOSIS SYSTEM")
print("========================================")

# -----------------------------------------------------
# Taking Personal Details
# -----------------------------------------------------

name = input("Enter Patient Name : ")
age = int(input("Enter Age : "))
gender = input("Enter Gender : ")

print("\nWelcome", name)
print("Please answer the following symptoms with yes or no.\n")

# -----------------------------------------------------
# Function to Ask Symptoms
# -----------------------------------------------------

def ask(symptom):
    answer = input(f"Do you have {symptom}? (yes/no): ")

    if answer.lower() == "yes":
        return True
    else:
        return False


# -----------------------------------------------------
# Asking Symptoms
# -----------------------------------------------------

fever = ask("fever")
cough = ask("cough")
headache = ask("headache")
body_pain = ask("body pain")
loss_of_taste = ask("loss of taste")
breathing_problem = ask("breathing problem")
chest_pain = ask("chest pain")
frequent_urination = ask("frequent urination")
excessive_thirst = ask("excessive thirst")
weight_loss = ask("weight loss")
chills = ask("chills")
sweating = ask("sweating")

# -----------------------------------------------------
# Disease Prediction Rules
# -----------------------------------------------------

disease = "Unknown Disease"
precaution = "Please consult a doctor."

# Flu
if fever and cough and headache and body_pain:
    disease = "Flu"
    precaution = "Take rest, drink warm fluids, and take proper medication."

# COVID-19
elif fever and cough and loss_of_taste and breathing_problem:
    disease = "COVID-19"
    precaution = "Isolate yourself and consult a doctor immediately."

# Pneumonia
elif fever and cough and chest_pain and breathing_problem:
    disease = "Pneumonia"
    precaution = "Seek medical attention and take proper treatment."

# Diabetes
elif frequent_urination and excessive_thirst and weight_loss:
    disease = "Diabetes"
    precaution = "Maintain healthy diet and check blood sugar regularly."

# Malaria
elif fever and chills and sweating and headache:
    disease = "Malaria"
    precaution = "Take proper medication and avoid mosquito exposure."

# -----------------------------------------------------
# Displaying Result
# -----------------------------------------------------

print("\n========================================")
print("          DIAGNOSIS REPORT")
print("========================================")

print("Patient Name       :", name)
print("Age                :", age)
print("Gender             :", gender)

print("\nPredicted Disease  :", disease)

print("\nSuggested Precaution:")
print(precaution)

print("\nThank You for Using Medical Diagnosis System")
print("========================================")