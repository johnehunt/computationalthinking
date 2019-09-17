import os, time

TUNE = ( (264, 250), (264, 250), (297, 100), (264, 1000), (352, 1000), (330, 2000),
         (264, 250), (264, 250), (297, 1000), (264, 1000), (396, 1000), (352, 2000),
         (264, 250), (264, 500), (440, 1000), (352, 1000), (330, 1000), (297, 1000), (440, 1000),
         (466, 250), (466, 250), (440, 1000), (352, 1000), (396, 1000), (352, 2000))

DELAY = 500 / 2000.0

for tuple in TUNE:
    os.system('beep -f ' + str(tuple[0]) + ' -l ' + str(tuple[1]))
    time.sleep(DELAY)