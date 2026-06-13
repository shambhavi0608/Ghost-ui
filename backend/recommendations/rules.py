def generate_rules(
    tracker_count,
    permission_count,
    entropy_score,
    identity_matches=0,
    image_risk="LOW"
):
    recommendations = []
    checklist = []

    # Tracker rules
    if tracker_count > 20:
        recommendations.append(
            "Consider using a tracker-blocking browser extension."
        )
        checklist.append(
            "Review websites that load excessive trackers."
        )

    # Permission rules
    if permission_count > 3:
        recommendations.append(
            "Review browser permissions and disable unnecessary access."
        )
        checklist.append(
            "Check camera, microphone, and location permissions."
        )

    # Fingerprint entropy rules
    if entropy_score > 75:
        recommendations.append(
            "Your browser fingerprint appears highly unique and easier to track."
        )
        checklist.append(
            "Enable anti-fingerprinting protections."
        )

    # Identity exposure rules
    if identity_matches > 0:
        recommendations.append(
            "Personal information appears to be publicly discoverable."
        )
        checklist.append(
            "Review publicly exposed profiles and remove unnecessary information."
        )

    # Image exposure rules
    if image_risk.upper() == "HIGH":
        recommendations.append(
            "Uploaded images may reveal identifiable personal information."
        )
        checklist.append(
            "Avoid sharing sensitive images publicly."
        )

    # Low-risk fallback
    if not recommendations:
        recommendations.append(
            "Your privacy exposure appears relatively low."
        )

        checklist.append(
            "Continue monitoring privacy settings regularly."
        )

    return recommendations, checklist