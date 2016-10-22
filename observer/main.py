#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import humidity_sensor, website_notifier, mailing_service, water_mecanism

sensor = humidity_sensor.HumiditySensor()
sensor.register_observer(website_notifier.WebsiteNotifier())
sensor.register_observer(mailing_service.MailingService())

humidity = [20, 10, 21, 5, 14, 15, 16, 22, 30]

for h in humidity[0:5]:
    sensor.humidity = h
    sensor.notify_observer()

sensor.register_observer(water_mecanism.WaterMecanism())

for h in humidity[5:]:
    sensor.humidity = h
    sensor.notify_observer()
