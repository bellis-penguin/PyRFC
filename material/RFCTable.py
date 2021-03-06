from pyrfc import *
from pyrfc._exception import ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError
from decimal import Decimal

from configparser import ConfigParser

config = ConfigParser()
config.read('sapnwrfc.cfg')

conn = Connection(**config._sections['connection'])

h332 = {'LINE1': 'HALLO', 'LINE2': 'DU', 'LINE3': 'WAS', 'LINE4': 'GEHT'}

h1000 = {'LINE1': 'TEIL1',
  'LINE2': 'TEIL2',
  'LINE3': 'TEIL3',
  'LINE4': 'TEIL4',
  'LINE5': 'TEIL5'}

###
# For BAPI_EPM_PRODUCT_CREATE
# TODO: TEST
# TEST is ZJK_BCD2

header1 = {
    'PRODUCT_ID'     :'TEST1',
    'TYPE_CODE'      :'T1',
    'CATEGORY'       :'TEST-JK',
    'NAME'           :'TEST Object one',
    'DESCRIPTION'    :'A device for testing purposes',
    'SUPPLIER_ID'    :'SUPL1',
    'SUPPLIER_NAME'  :'A Supplier',
    'TAX_TARIF_CODE' :1,
    'MEASURE_UNIT'   :'m',
    'WEIGHT_MEASURE' :3.2,
    'WEIGHT_UNIT'    :'kg',
    'PRICE'          :100.23,
    'CURRENCY_CODE'  :'EUR',
    'WIDTH'          :10.2,
    'DEPTH'          :11.3,
    'HEIGHT'         :12.4,
    'DIM_UNIT'       :'m',
    'PRODUCT_PIC_URL':'http://flickr.com/a321dss'
}

header2 = {
    'PRODUCT_ID'     :'TEST2',
    'TYPE_CODE'      :'T2',
    'CATEGORY'       :'TEST-JK',
    'NAME'           :'TEST Object two',
    'DESCRIPTION'    :'Another device for testing purposes',
    'SUPPLIER_ID'    :'SUPL1',
    'SUPPLIER_NAME'  :'A Supplier',
    'TAX_TARIF_CODE' :1,
    'MEASURE_UNIT'   :'m',
    'WEIGHT_MEASURE' :23.2,
    'WEIGHT_UNIT'    :'kg',
    'PRICE'          :Decimal("200.23"),
    'CURRENCY_CODE'  :'EUR',
    'WIDTH'          :20.2,
    'DEPTH'          :21.3,
    'HEIGHT'         :22.4,
    'DIM_UNIT'       :'m',
    'PRODUCT_PIC_URL':'http://flickr.com/2a321dss'
}

# result = conn.call('RFC_TRANSFER_TABLE', APPEND=2, CHECKTAB='X', IMP0332=h332, IMP1000=h1000, TAB0332=[h332], TAB1000=[h1000])