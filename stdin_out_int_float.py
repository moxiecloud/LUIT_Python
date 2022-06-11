{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # read 2 integers from STDIN\
# perform integer and float division and print each\
# on separate line\
\
from __future__ import division\
import decimal\
from decimal import Decimal\
\
if __name__ == '__main__':\
  \
  a = int(input())\
  b = int(input())\
\
  print(a // b)\
  print(a/b)\
\
  # print(decimal.Decimal(a) / decimal.Decimal(b))}