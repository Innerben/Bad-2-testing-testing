def GoToWork(actor):
    actor.enter(actor.career.location)

def LeaveWork(actor):
    if actor.location.parent is actor.career.location:
        actor.enter(actor.home)