from CoreLibrary import CoreLibrary
from flask import Flask, render_template
import importlib

class RouteLibrary:

    app = Flask('__main__')
    core = None

    def __init__(self):
        self.core = CoreLibrary()

    # def map(self, path, endpoint, controllerName, functionName):
    #     try:
    #         _class = getattr(importlib.import_module('Controllers.{0}'.format(controllerName)), controllerName)
    #         method_to_call = getattr( _class(), functionName)
    #         self.app.add_url_rule(path, endpoint, method_to_call)
    #     except Exception as _ex:
    #         self.core.consoleLog(_ex.message,'err')
    #         return (None, None)

    def map(self, controllerName, functionName, path, endpoint):
        try:
            _class = getattr(importlib.import_module('Controllers.{0}'.format(controllerName)), controllerName)
            method_to_call = getattr( _class(), functionName)
            self.app.add_url_rule(path, endpoint, method_to_call)
        except Exception as _ex:
            self.core.consoleLog(_ex.message,'err')
            return (None, None)

    def run(self, debugMode=False):
        self.app.register_error_handler(404, self.page_not_found)
        self.app.debug = debugMode
        self.app.run()
        self.app.run(debug = debugMode)

    def page_not_found(self, e):
        return "404"


    
        

            

