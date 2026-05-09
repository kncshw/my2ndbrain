# SOC Weekly Summary Report

This document describes the design and usage of the SOC Weekly Summary Report tool, which provides statistics on AI-driven alert triage activity.

## Overview

The `bin/soc-report` tool aggregates activity data from FortiSOAR over a rolling 7-day window. It distinguishes between human actions and AI-driven actions by looking for the unique identification marker:
`[Triaged by BIS-AI Analyst — Gemma4-26B-A4B]`

## Key Metrics

The report is divided into two main sections:

### 1. AI Triage Activity (Last 7 Days)
This section captures alerts where the AI agent took a final action.
- **Resolved**: Alerts closed by the AI (either via whitelist auto-close or LLM investigation).
- **Escalated**: Alerts moved to "Investigating" status by the AI because they required human review.
- **Severity Breakdown**: Counts are provided for both **Critical** and **High** severities.

### 2. Current Backlog Snapshot
This section provides a real-time view of the entire alert queue, regardless of whether the AI or a human is handling them.
- **Under Investigation**: Total count of alerts currently in "Investigating" status. This represents the current workload for the human SOC team.
- **Pending Triage**: Total count of alerts currently in "Open" status. These are alerts awaiting either AI processing or manual pickup.

## Usage

Run the report from the repository root:

```bash
# Plain text output (default)
bin/soc-report

# HTML output with pie charts and tables
bin/soc-report --format html > report.html

# PDF output (requires playwright)
bin/soc-report --format pdf
```

## Features

- **Activity Mix**: A pie chart showing the ratio of Resolved vs. Escalated alerts.
- **Severity Breakdown**: Pie charts for Critical vs. High alerts within the Resolved and Escalated categories.
- **Escalated Alerts Table**: A detailed table of alerts escalated by the AI in the last 7 days, including direct FortiSOAR links.
- **Backlog Snapshot**: A real-time view of current alert volume and human workload.
- **PDF Export**: Generate a high-quality PDF version for sharing or archival.

## Technical Implementation

- **Data Source**: FortiSOAR REST API.
- **Filter Logic**: Uses `modifyDate[__gt]` with a Unix timestamp for the 7-day floor.
- **Marker Detection**: Scans the `closureNotes` field for the `BIS_AI_TRIAGE_MARKER`.
- **Concurrency**: Queries multiple severities and sources in parallel using `asyncio` to minimize report generation time.
