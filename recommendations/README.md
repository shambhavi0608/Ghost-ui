# Ghost Recommendation Engine

This module generates privacy recommendations and actionable checklists based on browser exposure analysis.

## Inputs

- tracker_count
- permission_count
- entropy_score
- identity_matches
- image_risk

## Outputs

### Recommendations

Personalized suggestions to reduce privacy exposure.

### Checklist

Actionable steps users can follow to improve privacy and security.

## Components

- rules.py → Core recommendation logic
- recommendations.py → Recommendation generator
- checklist.py → Checklist generator
- test_engine.py → Local testing utility