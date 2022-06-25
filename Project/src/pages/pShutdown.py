from app import*
import shutdownVariables

@app.get('/shutdown')
def pShutdown():
    with shutdownVariables.ShouldRunCV:
        shutdownVariables.ServerShouldRun = False
        shutdownVariables.ShouldRunCV.notify()
    return "Bye bye"