'''
At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.
'''

def manage_stage_changes(changes):
  scheduled = []
  canceled = []

  for change in changes:
    # if change contains "Schedule":
    #   push id from change
    # elif change is "Cancel":
    #   pop most recent schedule
    #   push in canceled stack
    # elif change is "Reschedule":
    #   pop from canceled:
    #   push in scheduled
    if "Schedule" in change:
      scheduled.append(change[-1])
    elif change == "Cancel":
      cancelled_event = scheduled.pop()
      canceled.append(cancelled_event)
    elif change == "Reschedule":
      rescheduled_event = canceled.pop()
      scheduled.append(rescheduled_event)

  return scheduled

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 