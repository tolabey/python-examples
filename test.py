import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.tcmb.gov.tr/kurlar/today.xml'

uh = urllib.request.urlopen(url)
data = uh.read()

root = ET.fromstring(data)

for kurlars in root.findall('Currency'):
    Kod = kurlars.get('Kod')
    Unit = kurlars.find('Unit').text #    <Unit>1</Unit>
    isim = kurlars.find('Isim').text #    <Isim>ABD DOLARI</Isim>
    CurrencyName = kurlars.find('CurrencyName').text #    <CurrencyName>US DOLLAR</CurrencyName>
    ForexBuying = kurlars.find('ForexBuying').text #    <ForexBuying>2.9587</ForexBuying>
    ForexSelling = kurlars.find('ForexSelling').text #    <ForexSelling>2.964</ForexSelling>
    BanknoteBuying = kurlars.find('BanknoteBuying').text #    <BanknoteBuying>2.9566</BanknoteBuying>
    BanknoteSelling = kurlars.find('BanknoteSelling').text #    <BanknoteSelling>2.9684</BanknoteSelling>
    CrossRateUSD = kurlars.find('CrossRateUSD').text #    <CrossRateUSD>1</CrossRateUSD>
    print(Kod, Unit, isim, CurrencyName, BanknoteBuying)