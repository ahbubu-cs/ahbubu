# -*- coding: utf-8 -*-
"""
SRE Roadmap Calendar Generator (Shiwei)
Start: Monday 27 Oct 2025 (SGT)
Schedule:
  Mon 20:00-22:00  Reading & Concepts
  Wed 20:00-22:00  Hands-On Lab
  Sun 14:00-18:00  Project Build
  Sun 19:00-20:00  Reflection
"""

from datetime import datetime, timedelta
from icalendar import Calendar, Event
from pytz import timezone

# --- CONFIG ---
START_DATE = datetime(2025, 10, 27, 20, 0)  # Monday 27 Oct 2025, 8PM
TZ = timezone("Asia/Singapore")
WEEKS = 12

cal = Calendar()
cal.add("prodid", "-//SRE Roadmap (Shiwei)//")
cal.add("version", "2.0")

def add_event(title, start_dt, end_dt, desc):
    e = Event()
    e.add("summary", title)
    e.add("dtstart", TZ.localize(start_dt))
    e.add("dtend", TZ.localize(end_dt))
    e.add("description", desc)
    cal.add_component(e)

topics = [
    "SRE Mindset & SLIs/SLOs",
    "Metrics & Observability Basics",
    "Prometheus and Grafana Stack",
    "Custom Metrics and Alerting",
    "AWS CloudWatch Observability",
    "AWS X-Ray and Reliability Pillar",
    "Terraform Reliable Infrastructure",
    "Python Auto-Healing with Boto3",
    "Incident Response and Runbooks",
    "Chaos Engineering (AWS FIS)",
    "Project Polish and Documentation",
    "Interview Preparation and Reflection",
]

for i, topic in enumerate(topics, start=1):
    base_week = START_DATE + timedelta(weeks=i - 1)

    # Monday 20:00–22:00  (Reading & Concepts)
    monday = base_week
    monday_desc = f"""Week {i} Reading & Concepts – {topic}
Duration: 2 hours

20:00–20:45  Read relevant Google SRE Book chapters.
20:45–21:30  Watch supporting video/webinar.
21:30–22:00  Write 3–5 key takeaways and 1 SLI idea.

Resources:
• Google SRE Book: https://sre.google/sre-book/table-of-contents/
• Example video: https://www.youtube.com/watch?v=uTEL8Ff1Zvk
Deliverable: notes_week{i}.md
"""
    add_event(
        f"Week {i} [Reading] {topic}",
        monday,
        monday + timedelta(hours=2),
        monday_desc,
    )

    # Wednesday 20:00–22:00 (Hands-On Lab)
    wednesday = base_week + timedelta(days=2)
    wed_desc = f"""Week {i} Hands-On Lab – {topic}
Duration: 2 hours

20:00–20:30  Setup environment & validate prerequisites.
20:30–21:15  Execute main lab steps.
21:15–22:00  Verify results, capture screenshots.

Deliverable: working config/scripts for week {i}.
"""
    add_event(
        f"Week {i} [Lab] {topic}",
        wednesday,
        wednesday + timedelta(hours=2),
        wed_desc,
    )

    # Sunday 14:00–18:00 (Project Build & Documentation)
    sunday = base_week + timedelta(days=6)
    sunday_desc = f"""Week {i} Project Build & Documentation – {topic}
Duration: 4 hours

14:00–15:00  Build core project components or automation scripts.
15:00–16:00  Add observability/monitoring.
16:00–17:00  Test features, validate metrics.
17:00–18:00  Write README, commit to repo.

Deliverable: completed project folder for week {i}.
"""
    add_event(
        f"Week {i} [Project] {topic}",
        sunday.replace(hour=14),
        sunday.replace(hour=18),
        sunday_desc,
    )

    # Sunday 19:00–20:00 (Reflection)
    reflection_desc = f"""Week {i} Reflection & Review – {topic}
Duration: 1 hour

Reflect on:
• What reliability insight stood out this week?
• Which tool/metric felt most valuable?
• What to automate next week?

Deliverable: update reflections.md with Week {i} notes.
"""
    add_event(
        f"Week {i} [Reflection] {topic}",
        sunday.replace(hour=19),
        sunday.replace(hour=20),
        reflection_desc,
    )

with open("Shiwei_SRE_Roadmap_2025.ics", "wb") as f:
    f.write(cal.to_ical())

print("✅ Created Shiwei_SRE_Roadmap_2025.ics — import into Google Calendar.")
