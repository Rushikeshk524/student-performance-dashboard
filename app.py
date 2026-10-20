
from flask import Flask, render_template

app = Flask(__name__)

SUBJECTS = ["maths", "science", "english"]

STUDENTS = [
    {"name": "Asha", "maths": 78, "science": 85, "english": 90},
    {"name": "Rohan", "maths": 65, "science": 70, "english": 68},
    {"name": "Priya", "maths": 92, "science": 95, "english": 88},
    {"name": "Arjun", "maths": 35, "science": 42, "english": 38},
    {"name": "Neha", "maths": 80, "science": 75, "english": 82},
]


def calculate_statistics(records):
    students = [student.copy() for student in records]

    for student in students:
        student["average"] = round(
            sum(student[subject] for subject in SUBJECTS)
            / len(SUBJECTS), 2
        )

    total_students = len(students)

    if total_students == 0:
        stats = {
            "total_students": 0,
            "average_marks": 0,
            "highest_mark": 0,
            "lowest_mark": 0,
            "pass_percentage": 0,
        }
        subject_averages = [
            {"name": subject.title(), "average": 0}
            for subject in SUBJECTS
        ]
        return stats, subject_averages, students

    all_marks = [
        student[subject]
        for student in students
        for subject in SUBJECTS
    ]

    average_marks = round(
        sum(student["average"] for student in students)
        / total_students, 2
    )

    passed_students = sum(
        student["average"] >= 40 for student in students
    )

    pass_percentage = round(
        passed_students / total_students * 100, 2
    )

    subject_averages = [
        {
            "name": subject.title(),
            "average": round(
                sum(student[subject] for student in students)
                / total_students, 2
            ),
        }
        for subject in SUBJECTS
    ]

    stats = {
        "total_students": total_students,
        "average_marks": average_marks,
        "highest_mark": max(all_marks),
        "lowest_mark": min(all_marks),
        "pass_percentage": pass_percentage,
    }

    return stats, subject_averages, students


@app.route("/")
def dashboard():
    stats, subject_averages, students = calculate_statistics(STUDENTS)

    return render_template(
        "index.html",
        students=students,
        stats=stats,
        subject_averages=subject_averages,
    )


if __name__ == "__main__":
    app.run(debug=True)
