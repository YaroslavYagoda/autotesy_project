import os

from chromebrowser import ChromeBrowser
from selenium import webdriver
from selenium.webdriver.edge.service import Service as MsEdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class MsEdge(ChromeBrowser):
    """
    Браузер Microsoft Edge - дочерний класс "ChromeBrowser"
    """

    def __init__(self):
        options = webdriver.EdgeOptions()
        path_for_download = os.path.dirname(os.path.abspath(__file__)) + '\\downloads'
        prefs = {'download.default_directory': path_for_download}
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('detach', True)
        options.add_argument('--headless')
        self.driver = webdriver.Edge(options=options, service=MsEdgeService(EdgeChromiumDriverManager().install()))
        self.create_download_dir()