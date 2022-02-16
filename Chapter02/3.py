print("----- EXERCISE -----")

from my_modules import webget

webget.download("https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:skolegrunddistrikt&outputFormat=csv&SRSNAME=EPSG:4326","Chapter02/test.csv")

print("----- END -----")