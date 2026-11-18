from datetime import date, timedelta

def solve(value):
    return (date.fromisoformat(value["date"]) + timedelta(days=value["days"])).isoformat()
