from flask import Flask, render_template, request
import random

app = Flask(__name__)

# -------------------- DATA --------------------

teachers = [
    "Dr Swaraj K P", "Gilesh M P", "Dr Vipin Kumar K S",
    "Ali Akbar N", "Rahamathulla K", "Dileesh E D",
    "Bisna N D", "Ezudheen P", "George Mathew",
    "Soni P", "Panchami V U", "Joby N J",
    "Anusree Radhakrishnan", "Nitha C Pankajakshan",
    "Shehin Shams P", "Soumya Rajan", "Jithin Chandran",
    "Premkumar M P", "Bindu K", "Sajeevan K V",
    "Sujith A", "Sabarish C R"
]

phd_scholars = [
    "PhD Scholar 1",
    "PhD Scholar 2",
    "PhD Scholar 3",
    "PhD Scholar 4",
    "PhD Scholar 5"
]

batch_labels = {
    "opt1": "S1, S3, S5, S7",
    "opt2": "S2, S5, S7",
    "opt3": "S2, S4, S6, S8",
    "opt4": "S4, S6, S8"
}

# -------------------- ROUTES --------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_teachers = request.form.getlist("teachers")
        selected_classrooms = request.form.getlist("classrooms")
        selected_batch = request.form.get("batch")

        # ✅ CORRECT LOGIC:
        # Required invigilators = number of classrooms selected
        required_classes = len(selected_classrooms)

        # -------------------- VALIDATION --------------------
        if required_classes == 0:
            return "Error: No classrooms selected"

        if len(selected_teachers) < required_classes:
            return "Error: Not enough teachers selected"

        # -------------------- RANDOM SELECTION --------------------

        # Randomly pick only required number of teachers
        assigned_teachers = random.sample(
            selected_teachers,
            required_classes
        )

        # Shuffle PhD scholars for fairness
        random.shuffle(phd_scholars)

        # -------------------- ALLOCATION --------------------
        allocation = []
        for i in range(required_classes):
            allocation.append({
                "classroom": selected_classrooms[i],
                "teacher": assigned_teachers[i],
                "phd": phd_scholars[i % len(phd_scholars)],
                "batches": batch_labels[selected_batch]
            })

        return render_template(
            "result.html",
            allocation=allocation
        )

    return render_template(
        "index.html",
        teachers=teachers
    )

# -------------------- RUN SERVER --------------------

if __name__ == "__main__":
    app.run(debug=True)
