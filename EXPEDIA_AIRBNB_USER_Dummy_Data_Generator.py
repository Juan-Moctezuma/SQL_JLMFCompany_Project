"""
Created on Wed Sept Jan 08, 10:01:44 2020

Author: Juan Leonardo Moctezuma-Flores
"""

"""
    Modules need to be imported in order for some functions to operate.
    Faker will create dummy data for most of the table's columns.
    Random will generate some dummy data as well.
    The xlwt module will allow data from the script to get imported into an .xls file.
"""

from faker import Faker
from faker.providers import date_time
import pandas as pd
import random
from random import randint
import string
from xlwt import *

""" 
    To produce the same data set each time the code runs, a seed needs to be included.
    Any integer can be randomly selected for Faker.seed(). Variable 'fake' generates generic 
    dummy data.
"""

Faker.seed(787300)
fake = Faker()

"""
    The following variables represent the localized providers. Meaning that dummy data
    does not correspond to the United States only.
"""

fake_us = Faker('en_US')
fake_mx = Faker('es_MX')
fake_au = Faker('en_AU')
fake_ca = Faker('en_CA')

"""
   The variables below will get assigned to every record depending on localized providers. 
"""

us_citizenship = "UNITED STATES OF AMERICA"
au_citizenship = "AUSTRALIAN"
ca_citizenship = "CANADIAN"
mx_citizenship = "MEXICAN"

us_country = "UNITED STATES OF AMERICA"
au_country = "AUSTRALIA"
ca_country = "CANADA"
mx_country = "UNITED MEXICAN STATES"

"""
    The variables below contain all the possible characters that are used by passport numbers
    and user_ids.
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_num = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alpha_num_v2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
us_pass_no = "0123456789"
mx_pass_no = "MXPLE012345678"
ca_pass_no = "CANGQ01234567"
au_pass_no = "AUSP012345678"
de_pass_no = "DEU012345789"
fr_pass_no = "FRAC12345678"
nz_pass_no = "NEAZ00012345"
gb_pass_no = "ENGS23456789"

# These headers will get assigned to the first row of each file.
user_acc_h = ['USER_NAME','FIRST_NAME','LAST_NAME','FIRST_LAST_NAME','USER_ID','USER_ADDRESS',
              'USER_COUNTRY','USER_ZIP_CODE','EMAIL','USER_PHONE','USER_NATIONALITY','BIRTHDATE',
              'USER_PASSPORT_NO']

host_name_h = ['HOST_ID','HOST_FIRST_NAME','HOST_LAST_NAME','HOST_NAME','HOST_LOCATION_ID',
               'LISTING_TYPE']

review_h = ['REVIEWER','RATING']

airbnb_res_h = ['AIR_CONFIRMATION_ID','MOTIVE']

bookings_h = ['BOOKING_ID','BOOKING_CLASS']

expedia_data_h = ['PASSENGER_X_NAME','EXP_E_TICKET_ID_X','EXP_E_TICKET_ID_X_M','EXP_E_TICKET_ID_X_I',
                  'PASSENGER_X_NATIONALITY','PASSPORT_NO_US','PASSPORT_NO_CAN','PASSPORT_NO_AUS','PASSPORT_NO_NZ',
                  'PASSPORT_NO_GB','PASSPORT_NO_FR','PASSPORT_NO_DE','CONFIRMATION_KEY']

card_h = ['COMPANY','CARD_NO','EXPIRY','CVV']

user_records_h = ['TRANSACTION_DATE','TRANSACTION_ID']

"""
    The following domains will randomly get attached to the username. For the sake of simplicity, the username matches 
    the client's email address, since the goal is to use dummy data.
"""

e_domains = ['@gmail.com','@yahoo.com','@outlook.com','@aol.com','hotmail.com']

# Whitespace variable.
space = " "

# Airbnb Data - Motives for traveling.
motives = ['Leisure','Ecotourism','Business or work','Religious Tourism','Family Tourism','Health/Medical Tourism',
           'Sports Tourism','Education Tourism','Sports Tourism','Personal','Other']

# Airbnb Data - Host listing types.
listing_types = ['ENTIRE_PLACE','PRIVATE_ROOM','SHARED_ROOM']

# Booking Data - Booking types.
booking_class = ['CLASS_A','CLASS_B','CLASS_C']

# Expedia Data - Nationality.
exp_passenger_nationality = ["UNITED STATES OF AMERICA","AUSTRALIAN","CANADIAN",
                             "BRITISH CITIZEN","FRANÇAIS","NEW ZEALAND","DEUTSCH"]

# Credit/Debit Card Company.
credit_card_company = ['VISA','MASTERCARD','DISCOVER']
expiry_month = ['01','02','03','04','05','06','07','08','09','10','11','12']
expiry_year = ['21','22','23','24','25','26','27','28']

# Birthdays date range.
b_date1 = '1957-01-01'
b_date2 = '2000-01-01'
birth_date_dates = pd.date_range(b_date1,b_date2).tolist()

# Transaction date range.
date1 = '2016-04-01'
date2 = '2020-01-01'
transaction_dates = pd.date_range(date1, date2).tolist()

""" This function returns strings with random alpha numeric characters.
 Please note that ASCII stands for American Standard Code for Information Interchange. 
 Which is a character encoding standard for electronic communication."""

def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# Workbook is created.
wb_1 = Workbook()
wb_2 = Workbook()
wb_3 = Workbook()
wb_4 = Workbook()
wb_5 = Workbook()
wb_6 = Workbook()
wb_7 = Workbook()
wb_8 = Workbook()

# Add_sheet is used to create a sheet with a .xls extension. The file is named USER_ACCOUNT_DRAFT.
sheet1 = wb_1.add_sheet('USER_ACCOUNT')

# Add_sheet is used to create a sheet with a .xls extension. The file is named HOST_INFO_DRAFT.
sheet2 = wb_2.add_sheet('HOST_INFO')

# Add_sheet is used to create a sheet with a .xls extension. The file is named REVIEWS_DRAFT.
sheet3 = wb_3.add_sheet('REVIEWS')

# Add_sheet is used to create a sheet with a .xls extension. The file is named AIRBNB_RESERVATION_DETAILS_DRAFT.
sheet4 = wb_4.add_sheet('AIRBNB_RESERVATION_DETAILS')

# Add_sheet is used to create a sheet with a .xls extension. The file is named BOOKINGS_DRAFT.
sheet5 = wb_5.add_sheet('BOOKINGS')

# Add_sheet is used to create a sheet with a .xls extension. The file is named EXPEDIA_DATA_DRAFT.
sheet6 = wb_6.add_sheet('EXPEDIA_DATA')

# Add_sheet is used to create a sheet with a .xls extension. The file is named CARD_INFO_DRAFT.
sheet7 = wb_7.add_sheet('CARD_DATA')

# Add_sheet is used to create a sheet with a .xls extension. The file is named USER_RECORDS_DRAFT.
sheet8 = wb_8.add_sheet('USER_RECORDS')

"""
    The following for-loops will iterate the columns on the spreadsheets.
"""
"""
    The following code lines will serve the purpose of 
    generating some of the user's account information for USER_ACCOUNT_DRAFT.xls
    These files will get saved, into your venv (PyCharm's default Virtual Environment) folder.
"""

for x in range(len(user_acc_h)):
    sheet1.write(0, x, user_acc_h[x])

for x in range(1, 73):
    sheet1.write(x, 1, fake_us.first_name())
    sheet1.write(x, 2, fake_us.last_name())
    sheet1.write(x, 5, fake_us.address())
    sheet1.write(x, 7, Formula("RIGHT(F2:F73,5)"))
    sheet1.write(x, 6, us_country)
    sheet1.write(x, 10, us_citizenship)
    sheet1.write(x, 9, fake_us.phone_number())
    sheet1.write(x, 12, ran_gen(9,us_pass_no))

for x in range(73, 83):
    sheet1.write(x, 1, fake_mx.first_name())
    sheet1.write(x, 2, fake_mx.last_name())
    sheet1.write(x, 5, fake_mx.address())
    sheet1.write(x, 7, Formula("RIGHT(F74:F83,5)"))
    sheet1.write(x, 6, mx_country)
    sheet1.write(x, 10, mx_citizenship)
    sheet1.write(x, 9, fake_mx.phone_number())
    sheet1.write(x, 12, ran_gen(8,mx_pass_no))

for x in range(83, 93):
    sheet1.write(x, 1, fake_au.first_name())
    sheet1.write(x, 2, fake_au.last_name())
    sheet1.write(x, 5, fake_au.address())
    sheet1.write(x, 7, Formula("RIGHT(F84:F93,4)"))
    sheet1.write(x, 6, au_country)
    sheet1.write(x, 10, au_citizenship)
    sheet1.write(x, 9, fake_au.phone_number())
    sheet1.write(x, 12, ran_gen(9, au_pass_no))

for x in range(93, 100):
    sheet1.write(x, 1, fake_ca.first_name())
    sheet1.write(x, 2, fake_ca.last_name())
    sheet1.write(x, 5, fake_ca.address())
    sheet1.write(x, 7, Formula("TRIM(RIGHT(F94:F100,7))"))
    sheet1.write(x, 6, ca_country)
    sheet1.write(x, 10, ca_citizenship)
    sheet1.write(x, 9, fake_ca.phone_number())
    sheet1.write(x, 12, ran_gen(8, ca_pass_no))

for x in range(1,100):
    sheet1.write(x, 17, space)
    sheet1.write(x, 3, Formula("CONCATENATE(B2:B100,R2:R100,C2:C100)"))
    sheet1.write(x, 0, Formula("CONCATENATE(LEFT(B2:B100,1),C2:C100,LEFT(E2:E100,3))"))
    sheet1.write(x, 4, ran_gen(12, alpha_num))
    sheet1.write(x, 16, random.choice(e_domains))
    sheet1.write(x, 8, Formula("CONCATENATE(A2:A100,Q2:Q100)"))
    sheet1.write(x, 11, random.choice(birth_date_dates))

wb_1.save('USER_ACCOUNT_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating some of the Airbnb's host information for HOST_INFO_DRAFT.xls
"""

for x in range(len(host_name_h)):
    sheet2.write(0, x, host_name_h[x])

for x in range(1,23):
    sheet2.write(x, 17, space)
    sheet2.write(x, 0, "HST-" + ran_gen(7, alpha_num))
    sheet2.write(x, 1, fake.first_name())
    sheet2.write(x, 2, fake.last_name())
    sheet2.write(x, 3, Formula("CONCATENATE(B2:B100,R2:R100,C2:C100)"))
    sheet2.write(x, 4, "AIR-" + ran_gen(8, alpha_num))
    sheet2.write(x, 5, random.choice(listing_types))

wb_2.save('HOST_INFO_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating some of the Airbnb's ratings for REVIEW_DRAFT.xls
"""

for x in range(len(review_h)):
    sheet3.write(0, x, review_h[x])

for x in range(1,35):
    sheet3.write(x, 0, fake.first_name())
    sheet3.write(x, 1, randint(3,5))

wb_3.save('REVIEW_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating some of the Airbnb's data for AIRBNB_RESERVATION_DRAFT.xls
"""

for x in range(len(airbnb_res_h)):
    sheet4.write(0, x, airbnb_res_h[x])

for x in range(1,55):
    sheet4.write(x, 0, ran_gen(8, alpha_num_v2) + "-" + ran_gen(7, alpha_num_v2))
    sheet4.write(x, 1, random.choice(motives))

wb_4.save('AIRBNB_RESERVATION_DETAILS_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating booking data for BOOKING_DRAFT.xls
"""

for x in range(len(bookings_h)):
    sheet5.write(0, x, bookings_h[x])

for x in range(1,115):
    sheet5.write(x, 0, "AE-" + ran_gen(7, alpha_num_v2) + "-" + ran_gen(8, alpha_num_v2) + "-"
                 + ran_gen(7, alpha_num_v2))
    sheet5.write(x, 1, random.choice(booking_class))

wb_5.save('BOOKING_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating Expedia data for EXPEDIA_DATA_DRAFT.xls
"""

for x in range(len(expedia_data_h)):
    sheet6.write(0, x, expedia_data_h[x])

for x in range(1,120):
    sheet6.write(x, 0, fake.name())
    sheet6.write(x, 1, "EX-" + ran_gen(8, alpha_num_v2) + "-" + ran_gen(8,alpha))
    sheet6.write(x, 2, "EM-" + ran_gen(8, alpha_num_v2) + "-" + ran_gen(8, alpha))
    sheet6.write(x, 3, "EI-" + ran_gen(8, alpha_num_v2) + "-" + ran_gen(8, alpha))
    sheet6.write(x, 4, random.choice(exp_passenger_nationality))
    sheet6.write(x, 5, ran_gen(9, us_pass_no))
    sheet6.write(x, 6, ran_gen(8, ca_pass_no))
    sheet6.write(x, 7, ran_gen(9, au_pass_no))
    sheet6.write(x, 8, ran_gen(9, nz_pass_no))
    sheet6.write(x, 9, ran_gen(8, gb_pass_no))
    sheet6.write(x, 10, ran_gen(8, fr_pass_no))
    sheet6.write(x, 11, ran_gen(8, de_pass_no))
    sheet6.write(x, 12, ran_gen(3, alpha) + ran_gen(3, alpha_num))

wb_6.save('EXPEDIA_DATA_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating dummy credit/debit card data for CARD_INFO_DRAFT.xls
"""

for x in range(len(card_h)):
    sheet7.write(0, x, card_h[x])

for x in range(1,96):
    sheet7.write(x, 0, random.choice(credit_card_company))
    sheet7.write(x, 1, ran_gen(4,us_pass_no) + '-' + ran_gen(4,us_pass_no) + '-'
                 + ran_gen(4,us_pass_no) + '-' + ran_gen(4,us_pass_no))
    sheet7.write(x, 2, random.choice(expiry_month) + '/' + random.choice(expiry_year))
    sheet7.write(x, 3, ran_gen(3,us_pass_no))

wb_7.save('CARD_INFO_DRAFT.xls')

"""
    The following code lines will serve the purpose of 
    generating dummy transaction data for USER_RECORDS_DRAFT.xls
"""

for x in range(len(user_records_h)):
    sheet8.write(0, x, user_records_h[x])

for x in range(1,41):
    sheet8.write(x, 0, random.choice(transaction_dates))
    sheet8.write(x, 1, 'TXN-' + ran_gen(10,alpha_num_v2) + '-' + ran_gen(9,alpha_num_v2) + '-' + ran_gen(8,us_pass_no))

wb_8.save('USER_RECORDS_DRAFT.xls')

#END OF CODE




