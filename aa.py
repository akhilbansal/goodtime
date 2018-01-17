import datetime
from datetime import date

one_date = datetime.timedelta(days=1)
bday = date(2018, 3, 31)
dates = ['2017-12-25', '2018-01-01', '2018-01-15', '2018-02-19', '2016-03-31']


def convert_to_date():
    lst = [];
    for x in dates:
        tempdt = datetime.datetime.strptime(x, '%Y-%m-%d').date()
        lst.append(tempdt)
    return lst


def sorted_list_greater_than_date(day):
    lst = convert_to_date()
    temp = sorted(x for x in lst if x >= day)
    return temp


def get_date_by_year(year):
    lst = convert_to_date()
    temp = sorted(x for x in lst if x.year == year)
    return temp

def dateToString(lst):
    return ' and '.join([x.strftime('%m/%d/%Y') for x in lst])


def sorted_list():
    lst = [];
    for x in dates:
        print("processing: ", x)
        tempdt = datetime.datetime.strptime(x, '%Y-%m-%d').date()
        lst.append(tempdt)
    print(lst)
    temp = sorted(lst)
    print(temp)


def col_play():
    for x in dates:
        print("processing: ", x)
        tempdt = datetime.datetime.strptime(x, '%Y-%m-%d').date()
        if (tempdt == bday):
            print("its your bday")

        if (tempdt.month == 3):
            print("its march")


def test():
    today = date.today()
    print(today)

    print(bday)
    print(bday - today)
    strdate = datetime.datetime.strptime('2018-03-31', '%Y-%m-%d').date()
    print(bday - strdate)


print(dateToString(sorted_list_greater_than_date(date.today())))
print(dateToString(get_date_by_year(2018)))

# sorted_list()
# col_play()
# test()
