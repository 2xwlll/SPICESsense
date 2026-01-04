# SPICESsense  
### Understanding Event Attendance and SPICES Categories from a Spreadsheet

SPICESsense is a tool that works with a spreadsheet (CSV file) of event data and helps answer two questions:

1. **Which types of events tend to have higher or lower attendance?**
2. **Which SPICES categories apply to each event?**

It was created as part of an Honors College advisory board project and is designed to be **transparent, educational, and easy to reuse**.

No prior programming experience is required to understand what the project does.

---

## What is a CSV file?

A CSV file is a spreadsheet file (like Excel or Google Sheets) saved in a simple text format.  
If you can open and edit a spreadsheet, you already understand the input to this project.

---

## What This Project Does (in plain language)

Given a spreadsheet of events, SPICESsense:

- Looks at event titles, descriptions, and basic details
- Learns patterns associated with **higher or lower attendance**
- Shows which **words and event features** are linked to those patterns
- Automatically assigns **SPICES categories** to each event based on keywords

The results help explain *patterns*, not make decisions.

---

## SPICES Categories Used

Each event can be tagged with one or more of the following:

- **Service**
- **Professional Development**
- **Intellectual Achievement Beyond the Classroom**
- **Cultural Exploration**
- **Engaged Living**
- **Skill Development**

These categories are assigned using a clear, keyword-based system so the results are easy to understand and adjust.

---

## What This Project Does *Not* Do

- It does **not** decide whether an event is “good” or “bad”
- It does **not** guarantee accurate predictions for all situations
- It does **not** replace human judgment or institutional review
- It does **not** claim that identified features *cause* attendance changes

The project identifies **associations**, not causes.

---

## What Kind of Data Does It Use?

The input spreadsheet is expected to include columns similar to:

- Event Title  
- Description  
- Event Type  
- Visibility  
- Start Date  
- Start Time  
- Online Location  
- Number of people who attended  

If column names differ, they can be adjusted in the script.

---

## What You Get as Output

After running the project, you will see:

- A summary of how well the model distinguishes higher vs. lower attendance
- A list of words and event features linked to increased attendance
- A list of words and event features linked to decreased attendance
- A new spreadsheet where each event has SPICES categories assigned

These outputs are meant to support understanding and discussion.

---

## How to Use This Project (Step by Step)

You do **not** need to understand the code to use it.

1. Download the project
2. Place your CSV file in the `data/` folder
3. Run a single command that processes the spreadsheet
4. Review the printed summary and the updated CSV file

Detailed setup instructions are included for users who want to run the project locally.

---

## For Users With Technical Backgrounds (Optional)

- Model type: linear classification model
- Text handling: word-frequency–based representation
- Categorical data: converted to binary indicators
- Evaluation: accuracy, precision, recall, F1 score
- SPICES assignment: keyword-based multi-label tagging

The model is trained at runtime using a train/test split.

---

## Project Structure

SPICESsense/
│
├── scripts/
│ ├── predict_attendance.py
│ └── assign_spices.py
│
├── data/
│ └── sample_input.csv
│
├── requirements.txt
├── README.md
└── LICENSE


---

## Limitations

- Results depend on the quality and size of the data
- Patterns may change across years or contexts
- Feature importance reflects correlation, not causation

---

## Future Improvements

Possible future additions include:

- Using multiple years of data
- Saving trained models for reuse
- Predicting approximate attendance numbers
- Improving SPICES classification with labeled examples

---

## License

This project is released under the MIT License and is intended for educational and exploratory use.
