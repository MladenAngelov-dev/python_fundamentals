
limit = 200
name = "Goshe"
mp = 130
recharge = 30
charge = mp + recharge
if charge > limit:
    recharged = limit - mp
    mp = 200
    print(f"{name} recharged for {recharged} MP!")
    print(mp)
else:
    print(f"{name} recharged for {recharge} MP!")
    mp += recharge
    print(mp)