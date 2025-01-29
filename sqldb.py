import mysql.connector

class Sql:
  def __init__(self):
    self.all_list = []

  def license_db():
    mydb= mysql.connector.connect (host='localhost',user='root',passwd='1011', auth_plugin='mysql_native_password', database="license"
    )

    mycursor = mydb.cursor()

    mycursor.execute("select * from vehicle_registration v join driver_license d on v.license_plate=d.license_plate join violations vo on v.license_plate=vo.license_plate join emissions e on e.license_plate=v.license_plate join insurance i on i.license_plate=v.license_plate ")

    rows = mycursor.fetchall()

    for row in rows:
        all_list = [list(row) for row in rows]


# for i in range(len(all_list)):

#   print(all_list[i][19])



