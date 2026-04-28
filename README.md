https://www.youtube.com/watch?v=uAhHcVu74n0

Quick Start (2 minutes)

1. Download the zip file from the green github button and open the index.html
2. It should open a new window in whatever browser you use
2. Wait until it says “Python ready”
3. Upload your CSV (Official 2024 csv file in the sample_data folder)
4. Click “Run Analysis”
5. Read the insights

That’s it.


## Where to look first

If you're not sure where to start, look here:

1. Top 5 Insights — quickest summary of what matters
2. Avg Engagement — overall event effectiveness
3. SPICES charts — balance of your programming
4. Top Events — what worked best


# How it works (high-level)

1. CSV data is loaded directly in the browser
2. Events are classified into SPICES categories using keyword matching
3. Engagement metrics are computed from RSVP and attendance data
4. A machine learning model is trained on your dataset to identify patterns
5. Results are visualized and translated into plain-English insights





# In Depth Walkthrough for data + Usage:

## SPICESsense:
A tool that reads your event attendance data and gives you plain-English insights — no coding required, no accounts, no internet needed after you *load* it. <br>
<br>
What is this?<br>
It's a single file — index.html — that you open in any web browser (Chrome, Firefox, Edge, Safari). It analyzes a CSV file from your Honors College event platform and tells you things like which events performed best, which SPICES categories are overrepresented, and what words in event titles tend to predict higher attendance.<br>
Everything runs inside your browser. Nothing is uploaded anywhere.<br>
<br>
### How to open it (from GitHub)<br>
You do not need to know how to code. You just need to download one file.<br>
<br>
Go to the GitHub page for this project and make sure your are on the  <> code tab of all the categories at the top.<br>
Click on the green code button, and download the zip file<br>
Open the zip file in your downloads and right click to hit extract.<br>
You should be able to see all of the github files now in that extracted folder.<br>
Click on the index.html file to open a new tab in whatever browser you are using.<br>
On the page that opens, look for a button that says "Download raw file" (it looks like a small download icon, top right of the file preview)<br>
Click it — your browser will save the file to your Downloads folder<br>
Find the file in your Downloads folder and double-click it <br>
It will open in your web browser like a normal webpage <br>
<br>
That's it. No installation. No setup. <br>
<br>
If the page looks blank or gives a security warning: Right-click the file → Open with → Choose your browser (Chrome/edge work best) <br>


## How to use it
Once it's open in your browser:<br>

Wait about at most 10–20 seconds — you'll see "Python ready" appear in the left panel. This is normal; it's loading a mini Python engine inside your browser.<br>
Upload your CSV file — click the dotted box that says "Drop your CSV here" and pick your file, or just drag and drop it in. You can also paste CSV text directly.<br>
Check the settings — on the left side you'll see three numbers:<br>
<br>
Cohort Size — how many students are in your Honors cohort (default: 460)<br>
Small ≤ — how many attendees makes an event "Small" (default: 15)<br>
Medium ≤ — the upper limit for "Medium" events (default: 34). Anything above this is "Large"<br>
<br>
<br>
Click Run Analysis — results appear on the right<br>
<br>
<br>
## What CSV file does it need?
Export your event data from your Honors platform (e.g. Presence, Campus Labs, or similar). The analyzer works best when your CSV has these columns:<br>
| Column Name           | What it is                         |
|----------------------|------------------------------------|
| Event Title          | The name of the event              |
| # Invited            | How many students were invited     |
| # RSVP Yes           | How many said they would come      |
| # RSVP No Response   | How many never replied             |
| # Marked Attended    | How many actually showed up        |
| Start Date           | Date of the event                  |
| Start Time           | Time the event started             |
| Description          | Event description text             |
| Status               | Whether the event was cancelled    |

The tool will still work if some columns are missing — it just won't be able to calculate certain things.<br>
<br>
## What do the results mean?
Event Statistics (the first section) <br>
The six summary numbers at the top:<br>

Total Events — how many events are in your CSV (cancelled ones are removed automatically)<br>
Large / Medium / Small — how many events fell into each size bucket based on your settings<br>
Avg Attended — on average, how many students came to each event<br>
Avg Engagement — a score (explained below) that captures how well events converted invitations into attendance<br>
<br>
The colored bar shows how your events are split across SPICES categories at a glance.<br>
<br>
## The Four Charts
Avg Attendance by SPICES — which category of event (Service, Professional Development, etc.) draws the most people on average<br>
Avg Engagement by SPICES — which category converts invitations into actual attendance most effectively (not the same as raw headcount)<br>
Event Count by SPICES — how many events you ran in each category. If one color dominates, your calendar may be unbalanced<br>
Size Distribution (donut chart) — what proportion of your events were Small, Medium, or Large<br>

## The Engagement Index — what it actually means
This is a number the tool calculates for every event. It combines three things:<br>
<br>
Reach Rate (50% of the score) — what fraction of invited students actually showed up. Walk-ins count here. This is weighted highest because showing up despite not RSVPing is a strong signal of interest.<br>
Attendance Rate (30%) — of the people who said they'd come, how many actually did<br>
Response Rate (20%) — the fewer people who ignored the invite entirely, the better<br>
<br>
An Engagement Index above 1.0 means more people showed up than RSVPed yes — good news (lots of 'walk-ins'). Below 1.0 means you're losing people between RSVP and the door.<br>
<br>
## The Pivot Tables
Two tables that cross SPICES category with event size:<br>
SPICES Event Count by Size — how many Small / Medium / Large events you had in each category. Useful for spotting if, say, all your Service events are small.<br>
SPICES Avg Engagement by Size — the average Engagement Index broken down by both category and size. Numbers above 1.0 are highlighted in green. These are your best-performing combinations.<br>
<br>
## Top Events Table
Your 25 highest-scoring events, sorted by Engagement Index. Columns:<br>
<br>
Event — the event title<br>
SPICES — which category it was classified into<br>
Size — Small, Medium, or Large<br>
Attended — actual headcount<br>
Size % — attended ÷ cohort size (e.g. 9.3% means 9.3% of all Honors students came)<br>
Att. Rate — attended ÷ RSVPed yes (did people who committed actually show?)<br>
Engagement — the Engagement Index score<br>
<br>
<br>
## ML Attendance Predictor (the second section)
This section uses machine learning — a statistical model trained on your own data — to figure out patterns. It learns from your events and tries to predict which ones will be well-attended.<br>
You do not need to understand how it works. Here's what the numbers mean:<br>
  Accuracy — what percentage of the time the model correctly guessed whether an event would be high or low attendance. 70%+ is solid for this kind of data.<br>
  High F1 / High Prec / High Recall — these measure how reliably the model identifies well-attended events specifically. Higher is better. If these are low, it means the model struggles to distinguish great     events from average ones — usually because the dataset is small.<br>
  Feature Importance (the bar chart) — this is the most useful part. It shows which words and factors are associated with higher or lower attendance in your data.<br>

  Green bars = things associated with more people coming<br>
  Red bars = things associated with fewer people coming<br>
<br>
These are patterns in your data, not universal rules. Treat them as "things worth investigating" not "guaranteed causes."<br>
<br>
## Ranked Insights
Up to 67 plain-English observations about your data, ranked by importance. Each one shows:<br>
<br>
Importance score — how significant this pattern appears to be (out of 100)<br>
Confidence badge — green (high), yellow (medium), or gray (low). Low-confidence insights are based on thin data and should be treated as hypotheses, not conclusions.<br>
Evidence % — how strongly the data supports this specific observation<br>
Tag — what type of insight it is (size, spices, ml, strategy, etc.)<br>
<br>
The top 5 are shown by default. Click "Show all insights" to see the full ranked list.<br>
<br>
All insights are statistical associations — patterns observed in your data. They are not proof of cause and effect. A low-confidence insight is still worth reading; it just means you'd want more data before acting on it.<br>
<br>

## Analysis Mode
In the left panel, you can choose:<br>
<br>
Both — runs everything (recommended)<br>
Stats — skips the ML section, faster<br>
ML — skips the stats section, just the prediction model<br>
<br>


# Common questions
The page just shows a white screen — Try opening in Chrome. Some browsers block local HTML files by default.<br>
It's stuck on "Loading Python runtime" — This can take up to 30 seconds on a slow connection. It only needs to load once per session.<br>
It says "Not enough events" — The ML model needs at least 10 events with attendance data. Stats will still work fine.<br>
My SPICES categories look wrong — The tool classifies events by scanning the title and description for keywords. If your events have unusual names, some may land in "Other." This is expected — the "Other" count in the insights will flag this.<br>
Can I share this with someone? — Yes. Just send them the HTML file. They open it the same way — no account needed.<br>
<br>
## Biases
These insights show patterns from data. **They Do Not Guarantee a Cause**<br>
A note on what this tool is and isn't: <br>
This tool is designed to help you ask better questions about your programming — not to give you definitive answers. The insights it generates are based on one semester of data, which is a small sample. Patterns that look strong here may not hold next semester.<br>
Use it to identify things worth investigating: which events to study more carefully, which categories to expand, which promotion strategies to test. The more semesters of data you add over time, the more reliable the patterns become.<br>
<br>

## CONTACT ME: 
william.olson@my.utsa.edu <br>
Or use the issues tab and create a new issue.<br>
<br>

## For Developers/Beyond the Website:
Disclaimer: I used claude code to help me make the website, as I am not very familiar with .html coding. All python was done by me and maybe cleaned up a little by AI. If you find discrepencies, I apologize.<br>
<br>
``````Bash
.
├── index.html              # Main tool (everything runs here)
├── index1.html             # Older / experimental version
├── dev/
│   ├── scripts/            # Core data + ML logic (Python)
│   │   ├── assign_spices.py
│   │   ├── honors_event_stats.py
│   │   ├── predict_attendance.py
│   │   └── sort_events.py
│   └── src/                # Unused / experimental app structure
├── sample_data/            # Example CSVs for testing
├── LICENSE.md
├── README.md
└── .venv/                  # Local Python environment (optional)
``````
<br>
How the Code Relates to the Website:<br>
<br>
The website (index.html) is a self-contained version of the project.<br>
<br>
The core logic comes from the Python scripts in dev/scripts/<br>
These were adapted into browser-compatible code (via in-browser Python / JS)<br>
The math, metrics, and transformations are the same<br>
<br>
Main scripts:<br>
<br>
assign_spices.py → SPICES classification<br>
honors_event_stats.py → engagement metrics + statistics<br>
predict_attendance.py → ML modeling (simplified for browser use)<br>
<br>
The website version removes complexity to keep it:<br>
- fast<br>
- portable<br>
- offline-capable (once dependencies are installed)<br>
<br>
Why Not Use Full scikit-learn in the Website?<br>
Running a full scikit-learn pipeline in the browser is possible, but:<br>
- slower startup<br>
- heavier memory usage<br>
- more fragile<br>
- worse user experience<br>
<br>
So the website uses a simplified, lightweight version of the model.<br>
<br>
If you want to extend it into a full ML app, the Python scripts are your starting point.<br>
<br>
Notes on src/ and .venv:<br>
src/ contains early-stage ideas for a larger application (not currently used)<br>
.venv/ is included for local development but not required for using the tool<br>
<br>
You can safely ignore both unless you plan to expand the project.<br>

<br>
<br>
<br>



## License

MIT License

Copyright (c) 2026 2xwlll

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


