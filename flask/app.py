from flask import Flask, request, render_template
import matlab.engine
app = Flask(__name__)
eng = matlab.engine.start_matlab()
matlab_drive_path = ""  # Change path as needed
eng.addpath(matlab_drive_path)
@app.route("/")
def survey_form():
    return render_template("landing_page.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit_survey():
    # Collect form data
    survey_data = {
        "checking_account": request.form.get("checkingAccount"),
        "loan_duration": int(request.form.get("loanDuration")),
        "credit_history": request.form.get("creditHistory"),
        "loan_purpose": request.form.get("loanPurpose"),
        "credit_amount": int(request.form.get("creditAmount")),
        "savings": request.form.get("savings"),
        "employment_status": request.form.get("employmentStatus"),
        "installment_rate": int(request.form.get("installmentRate")),
        "personal_status": request.form.get("personalStatus"),
        "other_debtors": request.form.get("debtors"),
        "residence_length": int(request.form.get("residenceSince")),
        "property": request.form.get("property"),
        "age": int(request.form.get("age")),
        "other_loans": request.form.get("installmentPlans"),
        "housing": request.form.get("housing"),
        "current_loans": int(request.form.get("currentLoans")),
        "job": request.form.get("job"),
        "dependents": int(request.form.get("dependents")),
        "telephone": request.form.get("telephone"),
        "foreign_worker": request.form.get("foreignWorker"),
    }

    # Convert strings to categorical by passing them directly as strings and using eng.categorical().
    checking_account = eng.categorical([survey_data["checking_account"]])
    credit_history = eng.categorical([survey_data["credit_history"]])
    loan_purpose = eng.categorical([survey_data["loan_purpose"]])
    savings = eng.categorical([survey_data["savings"]])
    employment_status = eng.categorical([survey_data["employment_status"]])
    personal_status = eng.categorical([survey_data["personal_status"]])
    other_debtors = eng.categorical([survey_data["other_debtors"]])
    property_val = eng.categorical([survey_data["property"]])
    other_loans = eng.categorical([survey_data["other_loans"]])
    housing = eng.categorical([survey_data["housing"]])
    job = eng.categorical([survey_data["job"]])
    telephone = eng.categorical([survey_data["telephone"]])
    foreign_worker = eng.categorical([survey_data["foreign_worker"]])

    # Convert numeric fields as matlab.double 
    loan_duration = matlab.double([survey_data["loan_duration"]])
    credit_amount = matlab.double([survey_data["credit_amount"]])
    installment_rate = matlab.double([survey_data["installment_rate"]])
    residence_length = matlab.double([survey_data["residence_length"]])
    age = matlab.double([survey_data["age"]])
    current_loans = matlab.double([survey_data["current_loans"]])
    dependents = matlab.double([survey_data["dependents"]])

    # Create a table in MATLAB
    inputTable = eng.table(
        checking_account,
        loan_duration,
        credit_history,
        loan_purpose,
        credit_amount,
        savings,
        employment_status,
        installment_rate,
        personal_status,
        other_debtors,
        residence_length,
        property_val,
        age,
        other_loans,
        housing,
        current_loans,
        job,
        dependents,
        telephone,
        foreign_worker,
        'VariableNames', ['Var1', 'Var2', 'Var3', 'Var4', 'Var5', 'Var6', 'Var7', 'Var8', 'Var9', 'Var10',
                      'Var11', 'Var12', 'Var13', 'Var14', 'Var15', 'Var16', 'Var17', 'Var18', 'Var19', 'Var20']

    )

    # Call the MATLAB prediction function
    predictions = eng.predictModel(inputTable)
    prediction_class = int(predictions[0])
    return render_template("submit.html", prediction=prediction_class, data=survey_data)


if __name__ == "__main__":
    app.run(debug=True)
