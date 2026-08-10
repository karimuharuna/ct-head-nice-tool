# CT Head Decision Support Tool

A quick, interactive walkthrough of NICE's CT head guideline (NG232, 
2023) — built so the criteria are easy to check against on a busy shift, 
rather than having to hold the whole decision tree in your head.

🔗 **Live app:** [add your Streamlit Cloud URL here]

## Why I built this

NICE's head injury criteria genuinely save lives, but they're also a lot 
to remember precisely — different rules for adults and children, 
different time windows, a separate pathway for anticoagulants, and an 
easy-to-misremember count-based rule for kids. I wanted to turn the 
guideline into something interactive, both to teach myself the logic 
properly and to see what a faster reference tool for this might look 
like.

## What it does

- Branches by age (16+ or under 16) into the correct NICE pathway
- Walks through the criteria as simple checklists
- Gives a clear, colour-coded recommendation with the reasoning behind it

## Potential use

In a busy emergency department, tools like this — once properly 
validated — could help staff apply NICE criteria consistently and 
quickly, cutting down on missed scans or unnecessary delays during 
high-pressure decision-making.

## A genuine limitation

This applies NICE's published rules exactly as written — it doesn't 
learn from data, and it isn't a substitute for assessing the patient, 
discussing with radiology, or following local protocol.

## Tech stack

Python, Streamlit

## Source

[NICE guideline NG232 (2023)](https://www.nice.org.uk/guidance/ng232)

## Run it locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

**Disclaimer:** Educational/portfolio project only. Not a validated 
clinical device.
