from recommendations import generate_recommendations
from checklist import generate_checklist

sample_data = {
    "tracker_count": 25,
    "permission_count": 4,
    "entropy_score": 85,
    "identity_matches": 2,
    "image_risk": "HIGH"
}

recommendations = generate_recommendations(**sample_data)
checklist = generate_checklist(**sample_data)

print("\nRecommendations:")
print(recommendations)

print("\nChecklist:")
print(checklist)