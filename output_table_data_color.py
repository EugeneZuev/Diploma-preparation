#!/usr/bin/env python

import mysql.connector
import sys
mycolor=0

#Create the connection object
myconn = mysql.connector.connect(
      host="localhost",
      user="root",
      password="GE*5if2n",
      database="test"
)
cur = myconn.cursor()

try:
    #Reading the Employee data
    cur.execute("select * from the_beatles order by collectionName, releaseDate")

    #fetching the rows from the cursor object
    result = cur.fetchall()
    #printing the result

    print "Content-type: text/html\n\n"
    print "<html>\n<body>\n"
    print "<div style=\"width: 100%; font-size: 14px; font-weight: bold; text-align: center;\">\n"
    print( '<table border="1">');
    print( '<thead>');
    print( '<tr style="background-color:rgb(0, 204, 255);">');
    print( '<th>kind</th>');
    print( '<th>collectionName</th>');
    print( '<th>trackName</th>');
    print( '<th>collectionPrice</th>');
    print( '<th>trackPrice</th>');
    print( '<th>primaryGenreName</th>');
    print( '<th>trackCount</th>');
    print( '<th>trackNumber</th>');
    print( '<th>releaseDate</th>');
    print( '</tr>');
    print( '</thead>');
    print( '<tbody>');

    for x in result:
      if mycolor == 0:
        mycolor=1
        print('<tr style="background-color:rgb(255, 255, 204);"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td><td>'+st$
      else:
        mycolor=0
        print('<tr style="background-color:rgb(204, 255, 255);"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td><td>'+st$

    print('</tbody>');
    print('</table>');
    print "\n</div>\n"
    print "</body>\n</html>\n"
except:
    myconn.rollback()
myconn.close()