from sqlite3 import connect
import cherrypy
cherrypy.config.update({'server.socket_port': 9999})

class test:                       
  @cherrypy.expose() 
  def billreport(self,billid=None,custid=None,status='0'):
        conn = connect('bill.db')
         
        cur = conn.cursor()
        if billid is '':
            billid=0
        if custid is '':
            custid=0    
            
        l=[]
        if status is '0':
            sql='SELECT billid,custid,date,TQnty,Tprice from bill'
            cur.execute(sql)
            c=cur.fetchall()
            conn.commit()
            for i in c:
                l.append([i[0],i[1],i[2],i[3],i[4]])
        if status is '1':
                sql='SELECT billid,custid,date,TQnty,Tprice from bill WHERE billid='+str(billid)+' or custid='+str(custid)
                print(sql)
                cur.execute(sql)
                c=cur.fetchall()
                conn.commit()
                for i in c:
                    l.append([i[0],i[1],i[2],i[3],i[4]])    
        
        print(l)
        conn.close()
        
        return """ 
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Billing report</title>

    <style>
        body {
            background-image: url("https://media.istockphoto.com/photos/shopping-cart-view-in-supermarket-aisle-with-product-shelves-abstract-picture-id838816102?k=6&m=838816102&s=612x612&w=0&h=uPCuplmaLnfDesOl422jsccqTHwDvnAh5L0ydxa3HRA=");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
        }
        
        .button10 {
            background-color: #9dd184ee;
            margin-left: -20px;
            border-radius: 4px;
            width: 50px;
            height: 25px;
            font-size: x-small;
            margin-right: 20px;
            cursor: pointer;
        }
        
        button:hover {
            background-color: #4574a0e0;
        }
        
        .divh {
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }
        
        .log>button {
            top: 35px;
            right: 30px;
            background-color: rgb(161, 152, 152);
            color: rgb(146, 62, 62);
            border: solid rgb(130, 131, 130) 3px;
            position: absolute;
            z-index: 10;
        }
        
        .div3 {
            margin-top: 15px;
            width: 1160px;
            margin-left: 165px;
            padding: 5px;
            border: solid rgba(93, 93, 93, 0.986);
            ;
            display: flow-root;
            padding-left: 10px;
            border-radius: 10px;
            background-color: rgba(190, 190, 190, 0.801);
        }
        
        input {
            border-radius: 5px;
            margin: 20px;
            width: 250px;
            height: 20px;
        }
        
        .btn1 {
            margin-left: -20px;
            border-radius: 500px;
            width: 42px;
            height: 20px;
            font-size: x-small;
            margin-right: 20px;
        }
        
        input[type=date],
        select {
            width: 200px;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        .div4 {
            margin-top: 3px;
            width: 1160px;
            margin-left: 165px;
            padding: 5px;
            border: solid rgb(131, 130, 130);
            display: flex;
            height: 385px;
            border-radius: 10px;
            background-color: rgba(200, 200, 200, 0.801);
        }
        
        .btn2 {
            width: 65px;
            height: 30px;
            margin-top: -90px;
        }
        
        .sidenav {
            height: 400px;
            width: 165px;
            position: fixed;
            z-index: 1;
            top: 100px;
            left: 0;
            background-color: rgba(187, 187, 187, 0.924);
            border: solid darkslategrey 2px;
            border-radius: 5px;
            border-left: none;
            overflow-x: hidden;
            transition: 0.5s;
            padding-top: 10px;
        }
        
        .sidenav a:hover {
            color: #f1f1f1;
        }
        
        @media screen and (max-height: 450px) {
            .sidenav {
                padding-top: 15px;
            }
            .sidenav a {
                font-size: 18px;
            }
        }
        
        .btn-group button {
            background-color: rgba(243, 224, 224, 0.849);
            /* Green background */
            border: 2px solid rgba(11, 16, 27, 0.931);
            /* Green border */
            margin-left: -2px;
            margin-top: 20px;
            color: rgba(0, 0, 0, 0.89);
            /* White text */
            padding: 3px 6px;
            /* Some padding */
            cursor: pointer;
            /* Pointer/hand icon */
            width: 150px;
            height: 35px;
            font-weight: bold;
            /* Set a width if needed */
            display: block;
            border-top-right-radius: 20px;
            border-bottom-right-radius: 20px
            /* Make the buttons appear below each other */
        }
        /* Add a background color on hover */
        
        .btn-group button:hover {
            background-color: rgba(127, 102, 216, 0.795);
        }
        
        .div5 {
            margin-top: 20px;
            margin-left: 60px;
            height: 347px;
            width: 1020px;
            border: solid 1px;
        }
        
        .div6 {
            height: 317px;
            width: 1020px;
            overflow: scroll;
        }
        
        table {
            width: 1000px;
            text-align: center;
            border-collapse: collapse;
            border: 1px solid black;
            border-radius: 5px;
        }
        
        td,
        th {
            border: 1px solid black;
            padding: 3px;
        }
        
        .div7 {
            margin-top: 150px;
            margin-left: 20px;
        }
        
        .div7>form>input {
            width: 70px;
            border-radius: 0;
            margin: 5px;
        }
        
        .btn3 {
            margin: 10px;
            width: 80px;
            height: 25px;
            margin-left: 30px;
        }
        
        .div8 {
            border-bottom: 5px gray groove;
            position: relative;
            width: 700px;
            z-index: 8;
            height: 29px;
            margin-top: -1px;
            margin-left: 100px;
        }
        
        .btn4 {
            border: solid darkslategrey 3px;
            border-bottom: none;
            margin-left: 60px;
            height: 45px;
            width: 100px;
            margin-top: -50px;
        }
        
        .btn4:hover {
            background-color: dimgray;
        }
        
        .div9 {
            position: relative;
            z-index: 9;
            background-color: rgba(199, 199, 199, 0.931);
            border: solid 1px;
            width: 800px;
            height: 60px;
            margin-top: -60px;
            display: none;
            padding: 0;
        }
        
        .btn5 {
            margin-left: 20px;
        }
        
        .log>button {
            top: 35px;
            right: 30px;
            background-color: rgb(161, 152, 152);
            color: rgb(146, 62, 62);
            border: solid rgb(130, 131, 130) 3px;
            position: absolute;
            z-index: 10;
        }
    </style>
</head>

<body>
    <div class="divh">
        <center>
            <h1>Bill REPORT</h1>
        </center>
        <form action="index" method="POST" class="log"><button type="submit">Logout</button></form>
    </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
        <form action="" method="POST">
            <button type="submit" formaction="register">Manage Employee</button>
            <button type="submit" formaction="astock" >Manage Stocks</button>
            <button type="submit" formaction="asreport"  >Stock Report</button>
            <button type="submit" formaction="billreport" style="background-color: darkgrey">Billing report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="">Other Details</button>
            <button type="submit" formaction="index">Logout</button></form>
        </div>
    </div>
    <form action="index" method="POST" class="log"><button type="submit">Logout</button></form>
    </div>

    <div class="div3">
        
        <form action="billreport" method="post"><label for="billid">Bill Id:</label><input type="text" name="billid" id="billid" placeholder="Enter Bill Number">
        <label for="billid">Cust Id:</label><input type="text" name="custid" id="custid" placeholder="Enter cust Number">
        <button type="submit" class="button10" name="status" value="1">search</button>
        <button type="submit" class="button10" name="status" value="0">All</button>
    </form>

    </div>
    <div class="div4">
        <br>
        <div class="div5">
            <table>
                <tr>
                    <th>Bill-ID</th>
                    <th>Cust-Id</th>
                    <th>Date</th>
                    <th>Qnty</th>
                    <th>Price</th>
                </tr>
            </table>
            <div class="div6">
                <table>
                    <script>
                        var v=%s  
                        for (i in v) {
                            document.write("<tr>")

                            document.write("<td style='width:220px;'>" + v[i][0] + "</td><td style='width:247px;'>" + v[i][1] + "</td><td style='width:154px;'>" + v[i][2] + "</td><td style='width:170px;'>" + v[i][3] + "</td><td>" + v[i][4] + "</td>")

                            document.write("</tr>")
                        }
                    </script>
                </table>
            </div>
        </div>

</body>

</html>.
   """ % (str(l))
cherrypy.quickstart(test())   