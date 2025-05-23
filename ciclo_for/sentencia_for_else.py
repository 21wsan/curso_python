db_conection="192.168.0.1","7890","root","empleados"

for parametro in db_conection:
    print(parametro)
else:
    print("""el comando PostgresSQL es:
          $psql -h {server} -p {port} -U {user} -d  {db_name}""".format(
              server=db_conection[0], port=db_conection[1],
              user=db_conection[2],db_name=db_conection[3]
          ))