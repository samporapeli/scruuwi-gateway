from ruuvitag_sensor.ruuvi import RuuviTagSensor
import api
import logger

logger.info('Listening to RuuviTags...')
for new_data in RuuviTagSensor._get_ruuvitag_data(bt_device=''):
    mac, data = new_data
    api.send(data)
