#!/usr/bin/env python

import dbus
import dbus.service
import dbus.mainloop.glib
import os

import logging

class Control(dbus.service.Object):
    def __init__(self, mongo_conn, rabbitmq_conn):
        self._mongo_conn = mongo_conn
        self._rabbitmq_conn = rabbitmq_conn

    def start(self):
        self._bus_name = dbus.service.BusName('br.org.cesar.knot.control', dbus.SystemBus())
        dbus.service.Object.__init__(self, self._bus_name, '/br/org/cesar/knot/control')
        self._mongo_conn.connect()
        self._rabbitmq_conn.connect()

    def _stop_process(self, process):
        logging.info('Stopping process: ' + process)
        stop = '/etc/knot/stop.sh '
        os.system(stop + process)

    def _stop_processes(self):
        processes = ['knot-fog', 'knot-connector']
        for proc in processes:
            self._stop_process(proc)

    @dbus.service.method('br.org.cesar.knot.control.FactoryReset')
    def factory_reset(self):
        # stop Daemons
        ### self._stop_processes()
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
