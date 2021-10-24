# def a:
# planet_name = input('Please enter planet name ')
# days_in_one_year = int(input('How many days in the year? '))
# sec_in_day= 60*60*24
# seconds_in_year = sec_in_day*days_in_one_year
#
# print('There are', seconds_in_year,'seconds in one day','on planet', planet_name)

d = 365
planet_name= input('Please, enter planet name: ')
if planet_name.capitalize() !='Earth' :
   d = int(input('How many "Earth days" on this planet reach make one year '))

sec_in_hour = 60*60
sec_in_day = sec_in_hour *24
sec_in_year = sec_in_day * d
print('There are',sec_in_hour,'seconds in one hour')
print('There are', sec_in_day, 'seconds in one day')
print('There are', sec_in_year, 'seconds in one year on planet', planet_name.capitalize())

