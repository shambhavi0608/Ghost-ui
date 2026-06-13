from recommendations.rules import generate_rules


def generate_checklist(
    tracker_count,
    permission_count,
    entropy_score,
    identity_matches=0,
    image_risk="LOW"
):
    _, checklist = generate_rules(
        tracker_count,
        permission_count,
        entropy_score,
        identity_matches,
        image_risk
    )

    return {
        "checklist": checklist
    }