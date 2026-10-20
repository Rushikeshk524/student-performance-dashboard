
from app import app, calculate_statistics


SAMPLE_STUDENTS = [
    {"name": "Asha", "maths": 78, "science": 85, "english": 90},
    {"name": "Rohan", "maths": 65, "science": 70, "english": 68},
    {"name": "Priya", "maths": 92, "science": 95, "english": 88},
    {"name": "Arjun", "maths": 35, "science": 42, "english": 38},
    {"name": "Neha", "maths": 80, "science": 75, "english": 82},
]


def test_total_students():
    stats, _, _ = calculate_statistics(SAMPLE_STUDENTS)
    assert stats["total_students"] == 5


def test_average_marks():
    stats, _, _ = calculate_statistics(SAMPLE_STUDENTS)
    assert stats["average_marks"] == 72.2


def test_highest_and_lowest_marks():
    stats, _, _ = calculate_statistics(SAMPLE_STUDENTS)
    assert stats["highest_mark"] == 95
    assert stats["lowest_mark"] == 35


def test_pass_percentage():
    stats, _, students = calculate_statistics(SAMPLE_STUDENTS)
    assert stats["pass_percentage"] == 80
    assert sum(s["average"] >= 40 for s in students) == 4


def test_subject_averages():
    _, averages, _ = calculate_statistics(SAMPLE_STUDENTS)
    results = {item["name"]: item["average"] for item in averages}

    assert results["Maths"] == 70
    assert results["Science"] == 73.4
    assert results["English"] == 73.2


def test_empty_student_list():
    stats, averages, students = calculate_statistics([])

    assert stats["total_students"] == 0
    assert stats["average_marks"] == 0
    assert stats["pass_percentage"] == 0
    assert stats["highest_mark"] == 0
    assert stats["lowest_mark"] == 0
    assert all(item["average"] == 0 for item in averages)
    assert students == []


def test_dashboard_loads():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Performance Dashboard" in response.data
    assert b"Asha" in response.data
