import json
from datetime import datetime, timedelta


def get_data(base, scenario):
    if scenario not in {"01", "02", "03"}: raise ValueError("Escenario no autorizado")
    source = "datos/agenda_" + scenario + ".json"
    data=json.loads((base/source).read_text(encoding="utf-8"))
    start=datetime.fromisoformat(data["window_start"]); limit=datetime.fromisoformat(data["window_end"])
    if start.tzinfo is None or limit.tzinfo is None: raise ValueError("Se requiere zona horaria")
    duration=timedelta(minutes=data["duration_minutes"])
    if duration.total_seconds() <= 0: raise ValueError("Duración inválida")
    slots=[]; candidate=start
    while candidate + duration <= limit:
        end=candidate+duration
        conflict=False
        for attendee in data["attendees"]:
            for busy_start,busy_end in attendee["busy"]:
                left=datetime.fromisoformat(busy_start); right=datetime.fromisoformat(busy_end)
                if candidate < right and end > left: conflict=True
        if not conflict: slots.append({"start":candidate.isoformat(),"end":end.isoformat()})
        candidate += timedelta(minutes=30)
    return {"scenario":scenario,"source":source,"agenda":data,"slots":slots[:3],"timezone":"UTC"}


def validate(output, observation):
    problems=[]
    if output["slots"] != observation["slots"]: problems.append("Horarios distintos a la herramienta")
    if output["scenario"] != observation["scenario"]: problems.append("Escenario incorrecto")
    if output["requires_human_approval"] is not True: problems.append("Falta aprobación humana")
    return problems
