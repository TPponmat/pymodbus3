'''
This service can be run with the following::

    twistd -ny modbus-udp.tac
'''
from twisted.application import service, internet
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

from pymodbus.constants import Defaults
from pymodbus.server.async import ModbusServerFactory
from pymodbus.transaction import ModbusSocketFramer

def BuildService():
    '''
    A helper method to build the service
    '''
    framer = ModbusSocketFramer
    factory = ModbusServerFactory(None, framer)
    application = internet.UDPServer(Defaults.Port, factory)
    return application

application = service.Application("Modbus UDP Server")
service = BuildService()
service.setServiceParent(application)