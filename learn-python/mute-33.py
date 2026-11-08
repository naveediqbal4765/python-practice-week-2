# 7. Fix the bug (example 8). This function is meant to start a fresh log for each order, 
# but the logs keep growing. Explain why, then fix it:

# def log_event(event, log=[]):
#     log.append(event)
#     return log

def log_event(event, log=None):
    if log is None:
        log = []
        log.append(event)
    return log

print(log_event("order created"))
print(log_event("payment received"))

#explained it many time earlier :(