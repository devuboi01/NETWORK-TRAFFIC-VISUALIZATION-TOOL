def detect_anomaly(usage):
    if usage > 400:
        return "🚨 HIGH TRAFFIC ALERT"
    elif usage > 250:
        return "⚠️ Suspicious Activity"
    else:
        return "Normal"