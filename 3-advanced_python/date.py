from datetime import datetime
from time import strftime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print('Bogota ', bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))