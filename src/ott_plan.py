SERVICES={
    "Netflix":{
        "price":10,
        "unit":10
    },
    "Amazon Prime":{
        "price":2,
        "unit":5
    },
    "Hotstar":{
        "price":1,
        "unit":5
    }
}
def validate_hourse(service,hours):
    config=SERVICES[service]
    
    if hours<0:
        raise ValueError("Viewing hours cann't be negative")
    if hours%config["unit"]!=0:
        raise ValueError(f"{service} allows viewing hours in multiples of {config['unit']} only")
def calculate_total(plan):
    total=0
    for service,hours in plan.items():
        validate_hourse(service, hours)
        config=SERVICES[service]
        units=hours//config["unit"]
        cost=units*config["price"]
        total=total+cost
    return total
