#!/usr/bin/env python

import dbus
import dbus.service
import dbus.mainloop.glib
import os

#import gobject
#from gi.repository import Gtk

class Server(dbus.service.Object):
    def __init__(self, mongo_conn, rabbitmq_conn):
        self._mongo_conn = mongo_conn
        self._rabbitmq_conn = rabbitmq_conn

    def start(self):
        self._bus_name = dbus.service.BusName('br.org.cesar.knot.server', dbus.SystemBus())
        dbus.service.Object.__init__(self, self._bus_name, '/br/org/cesar/knot/server')
        self._mongo_conn.connect()
        self._rabbitmq_conn.connect()

    def _stop_processes(self):
        stop = '/etc/knot/stop.sh '
        processes = ['knot-fog', 'knot-connector']
        for proc in processes:
            os.system(stop + proc)

    #@dbus.service.method('br.org.cesar.knot.server.FactoryReset', in_signature='s', out_signature='s')
    @dbus.service.method('br.org.cesar.knot.server.FactoryReset')
    def factory_reset(self):
        # stop Daemons
        self._stop_processes()
        # - knot-cloud
        # - knot-fog
        # - knot-connector
        # - knot-web
        # - knotd
        # - inetbr
        # - nrfd-daemon
        # - wpantund

        # clean MongoDB
        self._mongo_conn.drop_all()
        # clean RabbitMQ
        self._rabbitmq_conn.remove_all()
        # reboot
        ### os.system('reboot')
        os.system('nautilus')
