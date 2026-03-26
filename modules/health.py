
def network_health(latency, interfaces, packetloss):
    score = 100
    if latency["Gateway"] > 10:
        score -= 10
    if latency["Internet"] > 80:
        score -= 20
    if "%" in str(packetloss):
        loss = int(packetloss.replace("%",""))
        score -= loss
    for iface in interfaces:
        if iface["Errors"] > 0:
            score -= 10
        if iface["Dropped"] > 0:
            score -= 10
    if score < 0:
        score = 0
    return score
