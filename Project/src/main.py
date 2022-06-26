from app import*
from db import*
import waitress

app = CreateApp()

server = waitress.create_server(app, host='localhost', port=80)
t = threading.Thread(target=server.run)
t.start()

with shutdownVariables.ShouldRunCV:
	while shutdownVariables.ServerShouldRun:
		shutdownVariables.ShouldRunCV.wait()

server.close()
t.join()
db.save(DB_FILE)