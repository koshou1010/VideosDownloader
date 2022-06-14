import sys
import webview
import threading
import backend.server as server


if __name__ == '__main__':
    t = threading.Thread(target=server.start_server)
    t.daemon = True
    t.start()
    webview.create_window('Downloader', server.app, height=600, width=1000)
    webview.start()
    sys.exit()
    # server.start_server()