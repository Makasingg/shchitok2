import os
import sys
import webview


def resource_path(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


if __name__ == "__main__":
    with open(resource_path("index.html"), encoding="utf-8") as f:
        html = f.read()
    webview.create_window("Щиток", html=html, width=1200, height=820, min_size=(900, 600))
    webview.start()
