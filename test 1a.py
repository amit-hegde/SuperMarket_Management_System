from sqlite3 import connect
import cherrypy
from datetime import date
cherrypy.config.update({'server.socket_port': 9999})
global day
day=date.today()
print(day)
class test:                       
  @cherrypy.expose() 
  def index(self,uname=None,psw=None,status=None):
        conn = connect('bill.db')
        cur = conn.cursor()
       
        print(uname,psw,status,type(status))
        
        global c
        
        if status == 'any':
            print(True)
            sql="SELECT * from login WHERE phno="+str(uname)+" and mode='enable' and pass="+str(psw)
            cur.execute(sql)
            c=cur.fetchall()
            conn.commit()
            status='bill'
        elif status != 'any' and uname is not None:
            sql="SELECT * from login WHERE phno="+str(uname)+" and pass="+str(psw)+" and desig='"+str(status)+"' and mode='enable'"
            cur.execute(sql)
            c=cur.fetchall()  
            conn.commit()  
        if status is not None:
           if len(c)>0:
               s=0
               a=status
           else:
               s=1
               a=1
        else:
            s=0
            a=1
        l=[s,a]       
        print(l)        
        conn.close()
        
        return """ 
<html>
<title>SuperMarket</title>

<head>
    <style>
        body {
            background-image: url(https://image.freepik.com/free-photo/empty-top-wooden-table-with-supermarket-blur-background_36051-467.jpg);
            background-repeat: no-repeat;
            background-size: 100% 100%;
        }
        
        .button {
            background-color: #4CAF50;
            position: absolute;
            left: 400px;
            top: 500px;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
        }
        
        .button2 {
            position: absolute;
            left: 600px;
            top: 500px;
        }
        
        .button3 {
            position: absolute;
            left: 800px;
            top: 500px;
        }
        
        button:hover {
            opacity: 0.8;
            border: ridge 3px darkslategray;
        }
        /* Full-width input fields */
        
        input[type=text],
        input[type=password] {
            width: 300px;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        /* Center the image and position the close button */
        
        .imgcontainer {
            text-align: center;
            margin: 24px 0 12px 0;
            position: relative;
        }
        
        img.avatar {
            width: 130px;
            border-radius: 6;
        }
        
        .container {
            padding: 16px;
        }
        
        span.psw {
            float: right;
            padding-top: 20px;
        }
        /* The Modal (background) */
        
        .modal {
            display: none;
            /* Hidden by default */
            position: fixed;
            /* Stay in place */
            z-index: 1;
            /* Sit on top */
            left: 0;
            top: 0;
            width: 1390px;
            /* Full width */
            height: auto;
            /* Full height */
            overflow: auto;
            /* Enable scroll if needed */
            background-color: rgb(0, 0, 0);
            /* Fallback color */
            background-color: rgba(0, 0, 0, 0.4);
            /* Black w/ opacity */
            padding-top: 60px;
        }
        /* Modal Content/Box */
        
        .modal-content {
            background-color: rgba(228, 196, 196, 0.582);
            margin: 50px auto 150px auto;
           
            border: 1px solid #888;
            width: 350px;
            /* Could be more or less, depending on screen size */
            height: auto;
        }
        /* The Close Button (x) */
        
        .close {
            position: absolute;
            right: 30px;
            top: 0;
            color: #000;
            font-size: 35px;
            font-weight: bold;
        }
        
        .close:hover,
        .close:focus {
            color: red;
            cursor: pointer;
        }
        
        .buttton {
            margin: 0px 120px;
            font-size: 20px;
            font-weight: bold;
        }
        
        .buttton:hover,
        .buttton:focus {
            color: red;
            cursor: pointer;
        }
        /* Add Zoom Animation */
        
        .animate {
            -webkit-animation: animatezoom 0.6s;
            animation: animatezoom 0.6s
        }
        
        @-webkit-keyframes animatezoom {
            from {
                -webkit-transform: scale(0)
            }
            to {
                -webkit-transform: scale(1)
            }
        }
        
        @keyframes animatezoom {
            from {
                transform: scale(0)
            }
            to {
                transform: scale(1)
            }
        }
        /* Change styles for span and cancel button on extra small screens */
        
        @media screen and (max-width: 300px) {
            span.psw {
                display: block;
                float: none;
            }
        }
    </style>
</head>

<body>
    <script>
        let val=%s
        if (val[0]==1){
            window.alert("Username and Password not maching or account dosent exist.")
        }
        else{
           if(val[1]!=1){
               document.write("<form id='f1' action='"+val[1]+"' method='post'></form>")
               document.getElementById('f1').submit()
           }
        }
    </script>
    <button class="button" onclick="document.getElementById('id01').style.display='block'">Admin Login</button>
    <button class="button button2" onclick="document.getElementById('id02').style.display='block'">Staff Login</button>
    <button class="button button3" onclick="document.getElementById('id03').style.display='block'">Biller Login</button>

    <div id="id01" class="modal">

        <form class="modal-content animate" action="index" method="post">
            <div class="imgcontainer">
                <span onclick="document.getElementById('id01').style.display='none'" class="close" title="Cancel">&times;</span>
                <img src="https://blog.cpanel.com/wp-content/uploads/2019/08/user-01.png" alt="Avatar" class="avatar">
            </div>

            <div class="container">
                <center><h1 style="font-size:20px;">Admin Login</h1></center>
                <label for="uname"><b>Username</b></label>
                <input type="text" placeholder="Enter Username" name="uname" required>

                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>
                <button class="buttton" type="submit" name="status" value="admin">Login</button>
                <span class="psw"> <a href="#">Forgot password?</a></span>

            </div>
        </form>
    </div>

    <div id="id02" class="modal">

        <form class="modal-content animate" action="index" method="post">
            <div class="imgcontainer">
                <span onclick="document.getElementById('id02').style.display='none'" class="close" title="Cancel">&times;</span>
                <img src="https://blog.cpanel.com/wp-content/uploads/2019/08/user-01.png" alt="Avatar" class="avatar">
            </div>

            <div class="container">
                <center><h1 style="font-size:20px;">Staff Login</h1></center>
                <label for="uname"><b>Username</b></label>
                <input type="text" placeholder="Enter Username" name="uname" required>

                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>

                <button class="buttton" type="submit" name="status" value="staff">Login</button>
            </div>
        </form>
    </div>

    <div id="id03" class="modal">

        <form class="modal-content animate" action="index" method="post">
            <div class="imgcontainer">
                <span onclick="document.getElementById('id03').style.display='none'" class="close" title="Cancel">&times;</span>
                <img src="https://blog.cpanel.com/wp-content/uploads/2019/08/user-01.png" alt="Avatar" class="avatar">
            </div>

            <div class="container">
                <center><h1 style="font-size:20px;">Biller Login</h1></center>
                <label for="uname"><b>Username</b></label>
                <input type="text" placeholder="Enter Username" name="uname" required>

                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>

                <button class="buttton" type="submit" name="status" value="any">Login</button>
            </div>
        </form>
    </div>
    <script>
        // Get the modal
        var modal = document.getElementById('id01');
        var modal2 = document.getElementById('id02');
        var modal3 = document.getElementById('id03');

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            } else if (event.target == modal2) {
                modal2.style.display = "none";
            } else if (event.target == modal3) {
                modal3.style.display = "none";
            }
        }
    </script>
    <form id="f1" action='bill' method="post"></form>
</body>

</html>
   """ % (str(l))   

  @cherrypy.expose() 
  def admin(self,status=None):

        return """ 
         <!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background-image: url(https://wallpapercave.com/wp/wp3152222.jpg);
            background-repeat: no-repeat;
            background-size: cover;
            font-family: "Lato", sans-serif;
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
            width:150px;
            height: 35px;
            font-weight: bold;
            /* Set a width if needed */
            display: block;
            border-top-right-radius:20px ;
            border-bottom-right-radius:20px
            /* Make the buttons appear below each other */
        }

        /* Add a background color on hover */
        
        .btn-group button:hover {
            background-color: rgba(127, 102, 216, 0.795);
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
            border-radius:5px;
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
        .div1{
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }
        .log>button{top: 35px;
            right: 30px;
            background-color: rgb(161, 152, 152);
            color: rgb(146, 62, 62);
            border: solid rgb(130, 131, 130) 3px;
        position:absolute;
    z-index: 10;}
    </style>
</head>

<body>
    <div class="div1"><center><h1>Admin Main</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
           <form action=" " method="POST" >
            <button type="submit" formaction="register">Manage Employee</button>
            <button type="submit" formaction="astock">Manage Stocks</button>
            <button type="submit" formaction="asreport">Stock Report</button>
            <button type="submit" formaction="billreport">Billing report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="change details">Other Details</button>
            <button type="submit" formaction="index">Logout</button>
            </form>
        </div>
    </div>
</body>

</html>
   """ 
                      
  @cherrypy.expose() 
  def register(self,aadhar=None,name=None,gender=None,mode=None,dob=None,phno=None,email=None,desig=None,status=0):
        conn = connect('bill.db')
        cur = conn.cursor()
        x=0
        if phno is not None:
             sql='INSERT or IGNORE into register VALUES('+str(phno)+',"'+str(name)+'","'+str(email)+'","'+str(aadhar)+'","'+str(gender)+'","'+str(dob)+'","'+str(desig)+'");'  
             print(sql)
             cur.execute(sql)
             conn.commit()
             sql='INSERT or IGNORE into login VALUES('+str(phno)+',"'+str(desig)+'","'+str(mode)+'",Null);'  
             print(sql)
             cur.execute(sql)
             cur = conn.cursor()
             conn.commit()
             x=1
        conn.close()
        l=[x]
        return """ 
<!DOCTYPE html>
<html>
<title>SuperMarket</title>
<style>
    body {
        background-image: url(https://i.pinimg.com/originals/b4/f9/f9/b4f9f97ef17f943e969494a3f8e57cfb.jpg);
        background-repeat: no-repeat;
        background-size: cover;
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
        width:150px;
        height: 35px;
        font-weight: bold;
        /* Set a width if needed */
        display: block;
        border-top-right-radius:20px ;
        border-bottom-right-radius:20px
        /* Make the buttons appear below each other */
    }

    /* Add a background color on hover */
    
    .btn-group button:hover {
        background-color: rgba(127, 102, 216, 0.795);
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
        border-radius:5px;
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
    .divh{
        height: 70px;
        border: solid;
        background-color: dimgrey;
    }
    .log>button{top: 35px;
        right: 30px;
        background-color: rgb(161, 152, 152);
        color: rgb(146, 62, 62);
        border: solid rgb(130, 131, 130) 3px;
    position:absolute;
z-index: 10;}
         
    input[type=text],
    select {
        width: 240px;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    
    input[type=date],
    select {
        width: 240px;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    
    input[type=number],
    select {
        width: 240px;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    
    .btn5 {
        width: 130px;
        background-color: #4caf4f36;
        color: rgb(109, 24, 24);
        border-color: #45a049;
        padding: 14px 20px;
        margin: 15px 100px;
    
        border-radius: 4px;
        cursor: pointer;
    }
    
    .btn5:hover {
        background-color: #45a049;
    }
    

    
    .div {
        background-color: rgba(204, 202, 202, 0.87);
        margin: 10px 220px;
        border-radius: 10px;
        width: 900px;
        height: 450px;
        padding: 20px;
    }
    
    .div1 {
        margin: -10px 0;
        width: 250px;
        height: 400px;
        padding: 30px;
        padding-top: 60px;
    }
    
    .div2 {
        margin: -460px 0;
        width: 250px;
        height: 400px;
        padding: 30px;
        float: right;
    }

    .div8{
        border-bottom:5px gray groove;
        position: relative;
        width: 400px;
        z-index: 8;
        height: 29px;
        margin-top: -5px;
        margin-left: 500px;
    }
    .btn4{
        border: solid darkslategrey 3px;
        border-bottom: none;
        margin-left: 60px;
        height: 45px;
        width: 100px;
        
        margin-top: -50px;
    }
    .btn4:hover{
        background-color: dimgray;
    }
</style>

<body>
    <script>
        var v=%s
        if(v[0]==1){
        window.alert("Staff created")}</script>
    <div class="divh"><center><h1>Admin Main</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
        <form method="post" action="">
            <button type="submit" formaction="register" style="background-color: darkgrey">Manage Employee</button>
            <button type="submit" formaction="astock">Manage Stocks</button>
            <button type="submit" formaction="asreport">Stock Report</button>
            <button type="submit" formaction="billreport">Billing report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="change details">Other Details</button>
            <button type="submit" formaction="index">Logout</button></form>
        </div>
    </div> 
    <div class="div">
        <form method="post" action="register">
            <div class="div1">
                <label for="adhno">Adhaar number</label>
                <input type="number" id="adhno" name="aadhar" placeholder="Your Adhaar card number">

                <label for="name">Name:</label>
                <input type="text" id="name" name="name" placeholder="Your name">

                <label for="gender">Sex</label>
                <select id="gender" name="gender">
      <option value="male">Male</option>
      <option value="female">Female</option>
      <option value="other">Others</option>
    </select>
    <label for="mode">Mode</label>
    <select id="mode" name="mode">
        <option value="enable">Enable</option>
        <option value="disable">Disable</option>
      </select>
            </div>
            <div class="div2">

                <label for="dob">Date of Birth</label>
                <input type="date" id="birthday" name="dob">

                <label for="phno">Phone number</label>
                <input type="number" id="phno" name="phno" placeholder="Your mobile number">

                <label for="email">Email</label>
                <input type="text" id="email" name="email" placeholder="example@xyz.com">

                <label for="state">Status</label>
                <input type="text" id="status" name="desig" readonly value="staff">
                </select>
                <button type="submit" class="btn5">ADD </button>
            </div>

            
        </form>
    </div>
   
    <div class="div8">
        <form action="bill" method="post">   
         <button type="submit" class="btn4" name="status" value="1" formaction="update">Update</button>
          <button type="submit" class="btn4" name="status" value="2" style="background-color: dimgrey;" formaction="register">ADD</button>
      </form>
  </div>
</body>

</html>
   """% (str(l))    
     

  @cherrypy.expose() 
  def staff(self,status=None):

        return """ 
         <!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background-image: url(https://wallpapercave.com/wp/wp3152222.jpg);
            background-repeat: no-repeat;
            background-size: cover;
            font-family: "Lato", sans-serif;
        }
        
        .btn-group button {
            background-color: rgba(243, 224, 224, 0.849);
            /* Green background */
            border: 2px solid rgba(11, 16, 27, 0.931);
            /* Green border */
            margin-left: -2px;  
            margin-top: 40px;
            
            color: rgba(0, 0, 0, 0.89);
            /* White text */
            padding: 3px 6px;
            /* Some padding */
            cursor: pointer;
            /* Pointer/hand icon */
            width:150px;
            height: 35px;
            font-weight: bold;
            /* Set a width if needed */
            display: block;
            border-top-right-radius:20px ;
            border-bottom-right-radius:20px
            /* Make the buttons appear below each other */
        }

        /* Add a background color on hover */
        
        .btn-group button:hover {
            background-color: rgba(127, 102, 216, 0.795);
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
            border-radius:5px;
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
        .div1{
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }
        .log>button{top: 35px;
            right: 30px;
            background-color: rgb(161, 152, 152);
            color: rgb(146, 62, 62);
            border: solid rgb(130, 131, 130) 3px;
        position:absolute;
    z-index: 10;}
    </style>
</head>

<body>
    <div class="div1"><center><h1>Staff Main</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
           <form action=" " method="POST" >
            <button type="submit" formaction="sstock">Manage Stocks</button>
            <button type="submit" formaction="ssreport">Stock Report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="index">Logout</button>
            </form>
        </div>
    </div>
</body>

</html>
   """ 


  @cherrypy.expose() 
  def bill(self,billid=None,custid=None,itmid=None,Qnty=1,status=0):
        conn = connect('bill.db')
        cur = conn.cursor()
        l1=[]
        cname=0
        print(status,type(status))
        status=int(status)
        print(status)

        if status is 2:
            cur.execute('select billid,Tprice from bill')
            c=cur.fetchall()     
            conn.commit()
            if c[len(c)-1][1] is None :
                billid=c[len(c)-1][0]
                sql='DELETE from bill WHERE billid='+str(billid)
                print(sql)
                cur.execute(sql)    
                sql='DELETE from billing WHERE billid='+str(billid)
                print(sql)
                cur.execute(sql)                 
                conn.commit()
                billid=None

        
                    
        if billid is  None:
            cur.execute('select billid,custid,Tprice from bill')
            c=cur.fetchall()     
            conn.commit()
            if len(c)==0:
                x=1
            elif c[len(c)-1][2] is None :
                x=c[len(c)-1][0]   
                custid= c[len(c)-1][1]
            else:   
                x=c[len(c)-1][0]
                print(x)
                x+=1 
            billid=x   
        
     
                   
        if custid is not None:
             sql='select custname from Customer where custid= '+str(custid)
             print(sql)
             cur.execute(sql)
             c=cur.fetchall()     
             conn.commit()
             if len(c)>0:
                cname=c[0][0]
             else:
                 cname="Unavailable"   
        else:
             custid=""
             cname='-'   
             
        if  billid is not None and  custid is not "" and cname is not "Unavailable":
            sql='INSERT or IGNORE into bill VALUES('+str(billid)+','+str(custid)+',"'+str(day)+'",Null,Null,Null,Null);'  
            print(sql)
            cur.execute(sql)
            conn.commit()   
        date=str(day)    
        l1=[billid,custid,cname,date]
   
        l=[]
        l.append(l1)
        iname=0
        iprice=0     
         
        if itmid is not None:
            sql="select i.itmid,i.iname,p.price from item i, price p WHERE p.itmid = i.itmid AND i.itmid="+str(itmid) 
            cur.execute(sql)  
            c=cur.fetchall()     
            conn.commit() 
            itmid=c[0][0]
            iname=c[0][1]
            iprice=c[0][2]
            
        if Qnty is "":
            Qnty=1
        print("Qny=",Qnty)    
        iprice=iprice*int(Qnty)    
        print(itmid,iname,Qnty,iprice)    
        
        if status is 3 and itmid is not None and iprice is not None:
            sql='SELECT Qnty,price from billing WHERE billid='+str(billid)+' AND itmid='+str(itmid)
            cur.execute(sql)
            c=cur.fetchall()
            conn.commit()  
            if len(c)>0:
                x=int(c[0][0])
                Qnty=x+int(Qnty)
                print(Qnty)
                price=Qnty*(int(c[0][1])/x)
                
                sql='UPDATE or IGNORE billing set Qnty='+str(Qnty)+', price='+str(price)+' WHERE billid='+str(billid)+' AND itmid='+str(itmid)
                print(sql)
                c=cur.execute(sql)
                conn.commit()
            else:                
                sql='INSERT or IGNORE into billing VALUES('+str(billid)+','+str(itmid)+','+str(Qnty)+','+str(iprice)+');'    
                print(sql)
                cur.execute(sql)
                conn.commit()         
        if status is 4 and  itmid is not None:
                sql='Delete from billing where billid='+str(billid)+' and itmid='+str(itmid)    
                print(sql)
                cur.execute(sql)
                conn.commit()
        sql='SELECT i.itmid,iname,Qnty,price from billing b,item i WHERE b.itmid=i.itmid and  b.billid='+str(billid)  
        print(sql)
        cur.execute(sql)   
        c=cur.fetchall()
        conn.commit()           
        
        subtotal=0
        SGST=0
        CGST=0
        items=0
        TQnty=0
        Total=0        
        
        for i in c:
            subtotal+=i[3]
            items=len(c)
            TQnty+=i[2]
           
        SGST=round(subtotal*0.025,2)
        CGST=round(subtotal*0.025,2)            
        Total=round(subtotal+SGST+CGST)
        l.append([subtotal,SGST,CGST,items,TQnty,Total])   
        
        for i in c:
          l.append([i[0],i[1],i[2],i[3]])  
        print(l)                 
        conn.close()
        
        return """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        body{
            background-image: url("https://media.istockphoto.com/photos/shopping-cart-view-in-supermarket-aisle-with-product-shelves-abstract-picture-id838816102?k=6&m=838816102&s=612x612&w=0&h=uPCuplmaLnfDesOl422jsccqTHwDvnAh5L0ydxa3HRA=");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            
        }
        .div1{
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }
        .div3{
            margin-top: 15px;
            padding: 5px;
            border: solid rgba(93, 93, 93, 0.986);;       
            display: flex;
            padding-left: 40px;
            border-radius: 10px;
            background-color: rgba(190, 190, 190, 0.801);
        }
        input{
            border-radius: 5px;
            margin: 20px;
            width: 250px;
            height: 20px;
        }
        .btn1{
            margin-left: -20px;
            border-radius: 500px;
            width: 42px;
            height:20px ;
            font-size: x-small;
          margin-right: 20px;
        }

        .div4{
            margin-top: 3px;
            padding: 5px;
            border: solid rgb(131, 130, 130);      
            display: flex;
            height: 385px;
            
            border-radius: 10px;
            background-color: rgba(200, 200, 200, 0.801);
        }
        .btn2{
            width: 65px;
            height: 30px;
            margin-top: -90px;


        }
        .div5{
            margin-top: 60px;
            margin-left:-660px ;
            height: 295px;
            width: 1000px;
            border: solid 1px;
           
        }
        .div6{
            height: 285px;
            width: 1000px;
            overflow: scroll;
        }
        table{
            width: 980px;
            text-align: center;
            border-collapse: collapse;
            border: 1px solid black;
            border-radius: 5px;
           
        }
        td, th {
          
            border: 1px solid black;
            padding: 3px;
          }
          .div7{
              margin-top: 150px;
              margin-left: 20px;
          }
          .div7>form>input{
              width: 70px;
              border-radius: 0;
              margin: 5px;
          }
        .btn3{
              margin: 10px;
              width: 80px;
              height: 25px;
              margin-left: 30px;
          }
          .div8{
              border-bottom:5px gray groove;
              position: relative;
              width: 700px;
              z-index: 8;
              height: 29px;
              margin-top: -1px;
              margin-left: 100px;
          }
          .btn4{
              border: solid darkslategrey 3px;
              border-bottom: none;
              margin-left: 60px;
              height: 45px;
              width: 100px;
              
              margin-top: -50px;
          }
          .btn4:hover{
              background-color: dimgray;
          }
          .div9{
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
            .btn5{margin-left: 20px;}
                   .log>button{top: 35px;
                right: 30px;
                background-color: rgb(161, 152, 152);
                color: rgb(146, 62, 62);
                border: solid rgb(130, 131, 130) 3px;
            position:absolute;
        z-index: 10;}
    </style>
</head>
<body>
   <div class="div1"><center><h1>BILLING</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
    
    <div class="div3">
        <form action="bill" method="post">
           <script>
            
               let val=%s
               let a=val[0]
               let p=val[1]
               let v=val.slice(2)
               
         document.write('<lable>Bill-ID:</lable><input type="text" name="billid" id="billid" value="'+a[0]+'" readonly>')
       
        document.write(' <lable>phno:</lable><input type="text" name="custid" id="custid" placeholder="Enter Customer phno" value="'+a[1]+'" required>') </script> 
         <button type="submit" class="btn1">search</button>
         
         
        </form> <script>
        document.write('<lable style="margin-top: 25px;">Name:</lable><input type="text" name="cutname" id="custname" value='+a[2]+' readonly>') 
        document.write('<h2 style="margin-left:30px;">'+a[3]+'</h2>')    
    </script> 
         
    </div>
    <div class="div4">
     <form action="bill" method="post">
        <input type="text" name="itmid" id="itmid" placeholder="Enter itemid" required>
        <input type="text" name="Qnty" id="Qnty"  placeholder="Enter Qnty else 1">
        <button type="submit" class="btn2" name="status" value="3">ADD</button>  </form>
       <br>
       <div class="div5">
       <table>
           <tr>
               <th>Item ID</th>
               <th>ITEM Name</th>
               <th>Qnty</th>
               <th>Price</th>
           </tr>
        </table>
           <div class="div6">
            <table> 
           <script>
                
                   for(i in v){
                    document.write("<tr>")
                     
                        document.write("<td style='width:241px;'>"+v[i][0]+"</td><td style='width:377px;'>"+v[i][1]+"</td><td style='width:163px;'>"+v[i][2]+"</td><td>"+v[i][3]+"</td>")
                       
                       document.write("</tr>")
                   } 
           </script>
        </table>
        </div>
       </div>
       <div class="div7">
        <form action="generate" method="POST">
           <script>
            document.write('<lable>Sub Total:</lable> <input type="text" name="subtotal" value='+p[0]+' readonly style="width:120px"><br>')
            document.write('<lable>SGST:</lable><input type="text" name="SGST" value='+p[1]+' readonly>')
            document.write('<lable>CGST:</lable> <input type="text" name="CGST" value='+p[2]+' readonly><br>')
            document.write('<lable>Items:</lable> <input type="text" name="Items" value='+p[3]+' readonly>')
            document.write('<lable>Qnty: </lable> <input type="text" name="Qnty" value='+p[4]+' readonly ><br><br>')
            document.write('<lable>Total:</lable> <input type="text" name="Total" value='+p[5]+' readonly style="width:120px"><br>')
           </script>
                  
           <button type="submit" class="btn3" name="status" value="5">Generate</button></form>
    
       </div>
    </div>
    <div class="div8">

        
          <form action="bill" method="post">   
           <button type="submit" class="btn4" name="status" value="1" formaction="newcust">Create User</button>
            <button type="button" class="btn4" onclick="del()">Delete Item</button>
            <button type="submit" class="btn4" name="status" value="2">New Bill</button>
            <button type="submit" class="btn4" name="status" value="2">cancel</button>
        </form>
    </div>
    <div class="div9" id="del1">
            <form action="bill" method="post">
        <input type="text" name="itmid" id="itmid" placeholder="Enter itemid">
       
        <button type="submit" class="btn5" name="status" value="4">Remove</button><button type="button" class="btn5" onclick="del2()">caccel</button>  </form>
        <script>function del(){
            document.getElementById("del1").style.display="block"
   }
   function del2(){
    document.getElementById("del1").style.display="None"
    }
   </script>
    </div>

</body>
</html>   """% (str(l))        
     

  @cherrypy.expose() 
  def newcust(self,custid=None,name=None,mail=None,status=0):
        conn = connect('bill.db')
        cur = conn.cursor()
        print(str(custid)+","+str(name)+","+str(mail))
        if custid is not None :
                  sql="Insert or ignore into customer values("+str(custid)+",'"+str(name)+"','"+str(mail)+"')"
                  print(sql)
                  cur.execute(sql)
                  conn.commit()
        conn.close()
        
        return """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        body{
            background-image: url("https://media.istockphoto.com/photos/shopping-cart-view-in-supermarket-aisle-with-product-shelves-abstract-picture-id838816102?k=6&m=838816102&s=612x612&w=0&h=uPCuplmaLnfDesOl422jsccqTHwDvnAh5L0ydxa3HRA=");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            
        }
        .div1{
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }
        .div3{
            margin-top: 15px;
            padding: 5px;
            border: solid rgba(93, 93, 93, 0.986);;       
           width: 600px;
           height: 400px;
            border-radius: 10px;
            background-color: rgba(190, 190, 190, 0.801);
        }
        input{
            border-radius: 5px;
            margin: 20px;
            width: 300px;
            height: 40px;
        }
        .btn1{
        
            border-radius: 500px;
            width: 100px;
            height:40px ;
            border-color: rgb(64, 114, 114);
            color: darkslategrey;
        }


          .div8{
              border-bottom:5px gray groove;
              position: relative;
              width: 600px;
              z-index: 8;
              height: 29px;
              margin-top: 70px;
             
          }
          .btn4{
              border: solid darkslategray 3px;
              border-bottom: none;
              margin-left: 30px;
              margin-right: 30px;
              height: 45px;
              width: 100px;
              
              margin-top: -50px;
          }
          .btn4:hover{
              background-color: lightslategray;
          }
          .btn4:first-child{
              background-color: dimgray;
          }
  
    </style>
</head>
<body>
    <div class="div1"><center><h1>Create Customer</h1></center> </div>
    <center>
    <div class="div3">
       
            <h2>Customer Detailes</h2>
        <form action="newcust" method="post" onsubmit=alert("Created") >   
        <label>Phone:</label><input type="text" name="custid" id="custid" placeholder="Enter Customer phno" required ><br>
        <label>Name:</label><input type="text" name="name" id="custname" placeholder="Enter Customer name" required ><br>
        <label>Email:</label><input type="text" name="mail" id="custmail" placeholder="Enter Customer Email" required ><br>
         <button type="submit" class="btn1">Create</button>
        </form>
    </div> 
    

    <div class="div8">
 <center>
        
           
        <form action="bill" method="post">    
            <button type="submit" class="btn4" name="status" value="1" formaction="newcust" >Create User</button>
            <button type="submit" class="btn4" name="status" value="2">New Bill</button>
            <button type="submit" class="btn4" name="status" value="2">cancel</button>
        </form>
    </center>
    </div>
</center> 

</body>
</html>     """   

  @cherrypy.expose() 
  def generate(self,subtotal=None,SGST=None,CGST=None,Items=None,Qnty=None,Total=None,status=0):
        conn = connect('bill.db')
        from twilio.rest import Client
        client = Client("AC8524e480f521715997282f87d6879cf0", "302f4c8c7dca0fdd448f255ace993337")
        cur = conn.cursor()
        l=[]
        print(True)
        print(subtotal,SGST,CGST,Items,Qnty,Total)
        cur.execute('select billid,custname from bill b,customer c where b.custid=c.custid and  b.Tprice is Null')
        c=cur.fetchall()     
        conn.commit() 
        try: 
            billid=c[0][0]   
            custname=c[0][1]   
            cur.execute('SELECT * from billing WHERE billid='+str(billid))
            c=cur.fetchall()     
            conn.commit() 
            for i in c:
                    sql="UPDATE or ignore stock set tsales=tsales+"+str(i[2])+" ,stock=stock-"+str(i[2])+" WHERE  stock>0 and itmid="+str(i[1])
                    cur.execute(sql)  
                    conn.commit()   
        except:
            cur.execute('select billid,custname from bill b,customer c where b.custid=c.custid')
            c=cur.fetchall()     
            conn.commit()
            billid=c[len(c)-1][0]
            custname=c[len(c)-1][1]    
        if Total is not None:
            sql='UPDATE or IGNORE bill set SGST='+str(SGST)+',CGST='+str(CGST)+',TQnty='+str(Qnty)+',TPrice='+str(Total)+' WHERE billid = '+str(billid)
            print(sql)
            cur.execute(sql)
            conn.commit()          
         
        sql='SELECT * from bill WHERE billid='+str(billid)
        print(sql)
        cur.execute(sql)   
        c=cur.fetchall()
        conn.commit()
        
        custid=c[0][1]
        date=c[0][2]
        SGST=c[0][3]
        CGST=c[0][4]
        Qnty=c[0][5]
        Total=c[0][6]  
        subtotal=int(Total)-int(CGST)-int(SGST)  
        print(subtotal,SGST,CGST,Items,Qnty,Total)
        sql='SELECT i.itmid,iname,Qnty,price from billing b,item i WHERE b.itmid=i.itmid and  b.billid='+str(billid)  
        print(sql)
        cur.execute(sql)   
        c=cur.fetchall()
        conn.commit()          
        
        Items=len(c)
        
        l.append([billid,custid,custname,date])    
        l.append([subtotal,SGST,CGST,Items,Qnty,Total])     
        
    
        for i in c:
              l.append([i[0],i[1],i[2],i[3]])  
        print(l) 
        print(status)
        if status is "1":
            msg="\nbillid:"+str(billid)+"\nCustid:"+str(custid)+"\ndate:"+str(date)+'\n'
            print(msg)
            l1=l[2:]
            for i in l1:
           
                for j in i:
                    msg+=str(j)
                    msg+='  '
                msg+='\n' 
            
            msg+="Subtotal="+str(subtotal)+"\nQnty="+str(Qnty)+"\nTotal="+str(Total)       
            print(msg)  
            #phno="+91"+str(custid)
            phno="+919379067642"
            print(phno)
            client.messages.create(to=phno, 
                       from_="+12546553126", 
                       body=msg)            
        
 
        conn.close()
        
        return """ 
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        body{
            background-image: url("https://media.istockphoto.com/photos/shopping-cart-view-in-supermarket-aisle-with-product-shelves-abstract-picture-id838816102?k=6&m=838816102&s=612x612&w=0&h=uPCuplmaLnfDesOl422jsccqTHwDvnAh5L0ydxa3HRA=");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            
        }
        .div1{
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }

          .div3{
              border-bottom:5px gray groove;
              position: fixed;
              width: 550px;
              z-index: 8;
              height: 45px;
              bottom: 5px;
             margin-left: 400px;
             background-color: rgba(197, 197, 197, 0.712);
          }
          .div4{
            height: 50px; 
          }
          .btn4{
              border: solid darkslategrey 3px;
              border-bottom: none;
              margin-left: 60px;
              height: 45px;
              width: 100px;
              
              
          }
          .btn4:hover{
              background-color: dimgray;
          }

          .div2{
              width: 400px;
              min-height: 400px;
              border: solid;
              margin-left: 450px;
              background-color: white;
          }
          td{text-align:center;}
    </style>
</head>
<body><center>
    <div class="div1"><h1>BILLING</h1></div> </center> 
   <div class="div2" id="div2">
     <script>
                     function sendm(){
                    window.alert("Bill Sent")
                }
       let val=%s
        let a=val[0]
        let p=val[1]
        let v=val.slice(2)
        document.write('---------------------------------------------------------------------------')
        document.write('<center>Invoice<center>')
        document.write('---------------------------------------------------------------------------')
        document.write('<table style="width:400px;"><tr><th>Bill-id :'+a[0]+'</th>,<th>Date:'+a[3]+'</th></tr>')
            
        document.write('<tr><th>Cust-Id :'+a[1]+'</th>,<th>Name:'+a[2]+'</th></tr></table>')
        document.write('---------------------------------------------------------------------------')
        document.write('<table style="width:400px;"><tr><th>Item ID</th><th>ITEM Name</th><th>Qnty</th><th>Price</th></tr>')
            for(i in v){
                document.write("<tr>")
                 
                    document.write("<td>"+v[i][0]+"</td><td>"+v[i][1]+"</td><td>"+v[i][2]+"</td><td>"+v[i][3]+"</td>")
                   
                   document.write("</tr>")
               } 
           
        document.write('</table>')
        document.write('---------------------------------------------------------------------------')
        document.write('<table style="width:400px;"><tr><th>Items :'+p[3]+'</th><th>Qnty:'+p[4]+'</th><th>Subtotal:'+p[0]+'</th></tr></table>')
        document.write('---------------------------------------------------------------------------')   
        document.write('<table style="width:400px;"><tr><th>CGST :'+p[2]+'</th><th>SGST:'+p[1]+'</th><th>Total:'+p[5]+'</th></tr></table>') 
            document.write()
        document.write()
        document.write()
     </script>
   </div>
   <div class="div4"></div>
    <div class="div3">
          <form action="generate" method="post">   
            <button type="button" class="btn4" onclick="billprint()">Print</button>
            <button type="submit" class="btn4" name="status" value="1" onclick="sendm()">Send</button>
            <button type="submit" class="btn4" name="status" value="2" formaction="bill">NewBill</button>
        </form>
   
    </div>
    <script>
        function billprint(){
            var divContents = document.getElementById("div2").innerHTML; 
            var a = window.open('', '', 'height=400, width=400'); 
            a.document.write('<html>'); 
            a.document.write('<body >'); 
            a.document.write(divContents); 
            a.document.write('</body></html>'); 
            a.document.close(); 
            a.print(); 
        }
    </script>

</body>
</html>
   """ % (str(l))  
  @cherrypy.expose() 
  def locator(self,item=None):
        conn = connect('bill.db')
        cur = conn.cursor()
        print(item)
        c=0       
        if item is not None:
            item="'"+item+"'"
            sql="SELECT i.iname,b.bname,block,columns,rack from locator l,item i ,Brand b WHERE i.itmid=l.itmid and b.bndid=i.bndid and i.iname="+item+"  UNION SELECT i.iname,b.bname,block,columns,rack from locator l,item i ,Brand b WHERE i.itmid=l.itmid and l.bndid=b.bndid and b.bname="+item
            print(sql)
            cur.execute(sql)
            c=cur.fetchall()
            print(c)    
            conn.commit()
            conn.close()
            for i in c:
                c[c.index(i)]=list(i)
            print(c)
        out='''

   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Item Locator</title>
    <style>
        body{
            background-color: gainsboro;
        }
        #item {
         border-radius: 5px;
         height: 25px; 
         min-width: 150px;
         width:350px ;  
         margin-top:100px ;
        }
        #submit{
            border-radius: 5px;
            height: 25px; 
            width:90px ;
            background-color: rgb(204, 250, 242);
            border: 2px solid rgba(18, 19, 17, 0.315) ;  
        }
        .div1{
         border-bottom: 2px solid darkgrey;
         padding-bottom:20px ;   
        }
        .div2{
            margin-top: 2px;
            border:2px solid darkgrey;
            color: black;
            padding-top: 3px;
            
            padding-bottom: 10px;
        }
        td{
            text-align:center;
        }
                  h1{
            text-decoration: underline;
            color:grey;
            
        }
       @media screen and (min-width: 100px and max-width:400px) {
            table{
                width:200px;
                font-size:25px;
            }
            }
        @media screen and (min-width: 1000px) {
            table{
                width:1000px;
                font-size:30px;
            }

            }
                    .divh{
            height: 70px;
            border: solid;
            background-color: dimgrey;
        }
        .log>button{top: 35px;
            right: 30px;
            background-color: rgb(161, 152, 152);
            color: rgb(146, 62, 62);
            border: solid rgb(130, 131, 130) 3px;
        position:absolute;
    z-index: 10;}
    </style>
</head>
<body>
         <div class="divh"><center><h1>Locator</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
         <div class="div1">
        <center>
        <form action="locator" method="POST">
           
          <input type="text" name="item" id="item" placeholder="Enter item name or Brand or category">
          <button type="submit" id="submit">Search</button>
        </form></center>
    </div>
    <div class="div2">
    <center>
    <h1>Product Location Details</h1></center>
 <script type="text/javascript">	
        let a=%s 
       
        document.write('<center>');
         document.write('<table border="solid 1px;" style="border-collapse: collapse; padding-top:20px;  color:black text-align: center;">');
        document.write('<tr><th>Item</th><th>Brand</th><th>Block</th><th>Column</th><th>Rack</th></tr>');
        for(i in a){
            document.write("<tr>");

            for(j in a[i]){
                document.write('<td>'+a[i][j]+'</td>');
            }
            document.write('</tr>');
        }
        document.write("</table>");
        document.write('</center>');
        
        </script>
</div>
</body>
</html> '''
        return out %(str(c)) 


    
  @cherrypy.expose() 
  def astock(self,itmid=None,date=None,stock=None,nstock=None,status=0):
        conn = connect('bill.db')
        cur = conn.cursor()
        print(itmid,status,stock)
        l=[]
        tsales=0
        iname=" "
        sname=" "
        if status is 0 or status is '0':
                 itmid=' '
                 stock=0
                 tsales=0                             
        if itmid is not None and  status is '1':
             sql='SELECT iname,mname from item i,supplier s WHERE i.mid=s.mid and itmid='+str(itmid) 
             print(sql)
             cur.execute(sql)
             c=cur.fetchall()
             conn.commit()
             print(c)
             if len(c)==0:
                 iname="Unavailable"
                 sname="Unavailable"
             else:
                 iname=c[0][0]
                 sname=c[0][1]
             if iname is not "Unavailable":    
                sql='SELECT stock,tsales from stock where itmid='+str(itmid) 
                print(sql)
                cur.execute(sql)
                c=cur.fetchall()
                conn.commit()
                if len(c)==0:
                    sql='INSERT or IGNORE INTO stock VALUES('+itmid+',0,0,0,NULL)' 
                    cur.execute(sql)
                    c=cur.fetchall()
                    conn.commit()
                    stock=0
                    tsales=0
                else:
                    stock=c[0][0]
                    tsales=c[0][1]                   
        
        if nstock is not None and nstock is not '':
            print(stock,nstock)
            stock=int(stock)+int(nstock)
            sql='UPDATE stock set qnty='+str(stock)+',stock='+str(stock)+',date="'+str(date)+'" WHERE itmid='+str(itmid)
            print(sql)
            cur.execute(sql)
            conn.commit()
            itmid=' '
            stock=0
            tsales=0             
            print(itmid,status,stock) 
        print(itmid,status,stock)                     
        l.append([itmid,iname,sname,stock,tsales]) 
        conn.close()
        print(l)
        return """ 
<!DOCTYPE html>
<html>
<title>Stock Management</title>
<style>
    body {
        background-image: url(https://i.pinimg.com/originals/b4/f9/f9/b4f9f97ef17f943e969494a3f8e57cfb.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }
    
    input[type=text], input[type=date], input[type=number],
    select {
        width: 240px;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    
    .button {
        width: 115px;
        background-color: #4CAF50;
        color: white;
        position: absolute;
        z-index: 0;
        display: inline-block;
        padding: 14px 20px;
        margin: 80px -240px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    
    button:hover {
        background-color: #4574a0e0;
    }
    
    .button1 {
        margin: 80px -100px;
        background-color: red;
    }
    
    .button2 {
        width: 65px;
        height: 20px;
        margin: 20px 40px;
        position: absolute;
        z-index: 10;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        background-color: #4c66afb2;
        padding-left: 10px;
    }
    

    
    .div {
        background-color: rgba(187, 182, 182, 0.938);
        margin: 30px 200px;
        width: 900px;
        height: 350px;
        padding: 50px;
    }
    
    .div1 {
        margin: 0px 0px;
        width: 250px;
        height: 400px;
        padding: 30px;
    }
    
    .div2 {
        margin: -460px 600px;
        position: absolute;
        z-index: 5;
        width: 250px;
        height: 400px;
        padding: 30px;
        float: right;
    }
    .log>button{top: 35px;
        right: 30px;
        background-color: rgb(161, 152, 152);
        color: rgb(146, 62, 62);
        border: solid rgb(130, 131, 130) 3px;
    position:absolute;
z-index: 10;}
.divh{
    height: 70px;
    border: solid;
    background-color: dimgrey;
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
    width:150px;
    height: 35px;
    font-weight: bold;
    /* Set a width if needed */
    display: block;
    border-top-right-radius:20px ;
    border-bottom-right-radius:20px
    /* Make the buttons appear below each other */
}

/* Add a background color on hover */

.btn-group button:hover {
    background-color: rgba(127, 102, 216, 0.795);
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
    border-radius:5px;
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
</style>

<body>
    <div class="divh"><center><h1>Stock Management</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
         <form action="" method="POST">
            <button type="submit" formaction="register">Manage Employee</button>
            <button type="submit" formaction="astock"  style="background-color: darkgrey">Manage Stocks</button>
            <button type="submit" formaction="asreport">Stock Report</button>
            <button type="submit" formaction="billreport">Billing report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="change details">Other Details</button>
            <button type="submit" formaction="index">Logout</button></form>
        </div>
    </div>
    <div class="div">
        <form method="post" action="astock">
            <div class="div1">
                <script>
                function fun(){
                    window.alert("Updated")
                }
                 var v=%s            
                document.write('<label for="itid">Item ID</label>')
                document.write('<input type="text" id="sid" name="itmid" value="'+v[0][0]+'" placeholder="Enter itemid" required>')
                document.write('<button type="submit" class="button2" name="status" value="1">Search</button>')
                document.write('<label for="fname">Item Name</label>')
                document.write('<input type="text" id="iname" value="'+v[0][1]+'">')

                document.write('<label for="Mname">Supplier Name</label>')
                document.write('<input type="text" id="mname" value="'+v[0][2]+'">')

                document.write('<label for="dos">Date</label>')
                document.write('<input type="date" id="date" name="date" >')

                document.write('</select>')
            </script>
            </div>
            <div class="div2">
                <script>
                    document.write('<label for="stock">Stock</label>')
                    document.write('<input type="text" id="stock" name="stock" value="'+v[0][3]+'" readonly>')

                    document.write('<label for="tsale">Total Sale</label>')
                    document.write('<input type="text" id="tsale" value="'+v[0][4]+'" readonly>')
                </script>
                <label for="nstock">New Stock</label>
                <input type="number" id="nstock" name="nstock" placeholder="Enter new stock">
                </select>
           
                <button type="submit" class="button" name="status" value="2" onclick="fun()">Submit</button>
                <button type="submit" class="button button1" name="status" value="0">Cancel</button>
            </div>
        </form>
    </div>


</body>

</html>
   """% (str(l)) 

  @cherrypy.expose() 
  def sstock(self,itmid=None,date=None,stock=None,nstock=None,status=0):
        conn = connect('bill.db')
        cur = conn.cursor()
        print(itmid,status,stock)
        l=[]
        tsales=0
        iname=" "
        sname=" "
        if status is 0 or status is '0':
                 itmid=' '
                 stock=0
                 tsales=0                             
        if itmid is not None and  status is '1':
             sql='SELECT iname,mname from item i,supplier s WHERE i.mid=s.mid and itmid='+str(itmid) 
             print(sql)
             cur.execute(sql)
             c=cur.fetchall()
             conn.commit()
             print(c)
             if len(c)==0:
                 iname="Unavailable"
                 sname="Unavailable"
             else:
                 iname=c[0][0]
                 sname=c[0][1]
             if iname is not "Unavailable":    
                sql='SELECT stock,tsales from stock where itmid='+str(itmid) 
                print(sql)
                cur.execute(sql)
                c=cur.fetchall()
                conn.commit()
                if len(c)==0:
                    sql='INSERT or IGNORE INTO stock VALUES('+itmid+',0,0,0,NULL)' 
                    cur.execute(sql)
                    c=cur.fetchall()
                    conn.commit()
                    stock=0
                    tsales=0
                else:
                    stock=c[0][0]
                    tsales=c[0][1]                   
        
        if nstock is not None and nstock is not '':
            print(stock,nstock)
            stock=int(stock)+int(nstock)
            sql='UPDATE stock set qnty='+str(stock)+',stock='+str(stock)+',date="'+str(date)+'" WHERE itmid='+str(itmid)
            print(sql)
            cur.execute(sql)
            conn.commit()
            itmid=' '
            stock=0
            tsales=0             
            print(itmid,status,stock) 
        print(itmid,status,stock)                     
        l.append([itmid,iname,sname,stock,tsales]) 
        conn.close()
        print(l)
        return """ 
<!DOCTYPE html>
<html>
<title>Stock Management</title>
<style>
    body {
        background-image: url(https://i.pinimg.com/originals/b4/f9/f9/b4f9f97ef17f943e969494a3f8e57cfb.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }
    
    input[type=text], input[type=date], input[type=number],
    select {
        width: 240px;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    
    .button {
        width: 115px;
        background-color: #4CAF50;
        color: white;
        position: absolute;
        z-index: 0;
        display: inline-block;
        padding: 14px 20px;
        margin: 80px -240px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    
    button:hover {
        background-color: #4574a0e0;
    }
    
    .button1 {
        margin: 80px -100px;
        background-color: red;
    }
    
    .button2 {
        width: 65px;
        height: 20px;
        margin: 20px 40px;
        position: absolute;
        z-index: 10;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        background-color: #4c66afb2;
        padding-left: 10px;
    }
    

    
    .div {
        background-color: rgba(187, 182, 182, 0.938);
        margin: 30px 200px;
        width: 900px;
        height: 350px;
        padding: 50px;
    }
    
    .div1 {
        margin: 0px 0px;
        width: 250px;
        height: 400px;
        padding: 30px;
    }
    
    .div2 {
        margin: -460px 600px;
        position: absolute;
        z-index: 5;
        width: 250px;
        height: 400px;
        padding: 30px;
        float: right;
    }
    .log>button{top: 35px;
        right: 30px;
        background-color: rgb(161, 152, 152);
        color: rgb(146, 62, 62);
        border: solid rgb(130, 131, 130) 3px;
    position:absolute;
z-index: 10;}
.divh{
    height: 70px;
    border: solid;
    background-color: dimgrey;
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
    width:150px;
    height: 35px;
    font-weight: bold;
    /* Set a width if needed */
    display: block;
    border-top-right-radius:20px ;
    border-bottom-right-radius:20px
    /* Make the buttons appear below each other */
}

/* Add a background color on hover */

.btn-group button:hover {
    background-color: rgba(127, 102, 216, 0.795);
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
    border-radius:5px;
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
</style>

<body>
    <div class="divh"><center><h1>Stock Management</h1></center><form action="index" method="POST" class="log"><button type="submit" >Logout</button></form> </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
              <form action=" " method="POST" >
            <button type="submit" formaction="sstock"  style="background-color: darkgrey">Manage Stocks</button>
            <button type="submit" formaction="ssreport">Stock Report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="index">Logout</button>
            </form>
        </div>
    </div>
    <div class="div">
        <form method="post" action="sstock">
            <div class="div1">
                <script>
                function fun(){
                    window.alert("Updated")
                }
                 var v=%s            
                document.write('<label for="itid">Item ID</label>')
                document.write('<input type="text" id="sid" name="itmid" value="'+v[0][0]+'" placeholder="Enter itemid" required>')
                document.write('<button type="submit" class="button2" name="status" value="1">Search</button>')
                document.write('<label for="fname">Item Name</label>')
                document.write('<input type="text" id="iname" value="'+v[0][1]+'">')

                document.write('<label for="Mname">Supplier Name</label>')
                document.write('<input type="text" id="mname" value="'+v[0][2]+'">')

                document.write('<label for="dos">Date</label>')
                document.write('<input type="date" id="date" name="date" >')

                document.write('</select>')
            </script>
            </div>
            <div class="div2">
                <script>
                    document.write('<label for="stock">Stock</label>')
                    document.write('<input type="text" id="stock" name="stock" value="'+v[0][3]+'" readonly>')

                    document.write('<label for="tsale">Total Sale</label>')
                    document.write('<input type="text" id="tsale" value="'+v[0][4]+'" readonly>')
                </script>
                <label for="nstock">New Stock</label>
                <input type="number" id="nstock" name="nstock" placeholder="Enter new stock">
                </select>
           
                <button type="submit" class="button" name="status" value="2" onclick="fun()">Submit</button>
                <button type="submit" class="button button1" name="status" value="0">Cancel</button>
            </div>
        </form>
    </div>


</body>

</html>
   """% (str(l)) 

        
  @cherrypy.expose() 
  def asreport(self,itmid=None,status='0'):
        conn = connect('bill.db')
        print(itmid,status)
        cur = conn.cursor()
        l=[]
        if status is '0':
            sql='SELECT s.itmid,i.iname,s.qnty,s.stock,s.tsales,s.date FROM stock s,item i WHERE s.itmid=i.itmid'
            cur.execute(sql)
            c=cur.fetchall()
            conn.commit()
            for i in c:
                l.append([i[0],i[1],i[2],i[3],i[4],i[5]])
        if status is '1':
                sql='SELECT s.itmid,i.iname,s.qnty,s.stock,s.tsales,s.date FROM stock s,item i WHERE s.itmid=i.itmid and i.itmid='+str(itmid)
                print(sql)
                cur.execute(sql)
                c=cur.fetchall()
                conn.commit()
                for i in c:
                    l.append([i[0],i[1],i[2],i[3],i[4],i[5]])    
        
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
            <h1>STOCK REPORT</h1>
        </center>
        <form action="index" method="POST" class="log"><button type="submit">Logout</button></form>
    </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
        <form action="" method="POST">
            <button type="submit" formaction="register">Manage Employee</button>
            <button type="submit" formaction="astock" >Manage Stocks</button>
            <button type="submit" formaction="asreport"  style="background-color: darkgrey">Stock Report</button>
            <button type="submit" formaction="billreport">Billing report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="">Other Details</button>
            <button type="submit" formaction="index">Logout</button></form>
        </div>
    </div>
    <form action="index" method="POST" class="log"><button type="submit">Logout</button></form>
    </div>

    <div class="div3">
        
        <form action="asreport" method="post"><label for="billid">ItmId:</label><input type="text" name="itmid" id="billid" placeholder="Enter Item Number">
        <button type="submit" class="button10" name="status" value="1">search</button>
        <button type="submit" class="button10" name="status" value="0">All</button>
    </form>

    </div>
    <div class="div4">
        <br>
        <div class="div5">
            <table>
                <tr>
                    <th>Item ID</th>
                    <th>ITEM Name</th>
                    <th>Qnty</th>
                    <th>Stock</th>
                    <th>Total_Sales</th>
                    <th>Date</th>
                </tr>
            </table>
            <div class="div6">
                <table>
                    <script>
                        var v=%s  
                        for (i in v) {
                            document.write("<tr>")

                            document.write("<td style='width:159px;'>" + v[i][0] + "</td><td style='width:247px;'>" + v[i][1] + "</td><td style='width:109px;'>" + v[i][2] + "</td><td style='width:118px;'>" + v[i][3] + "</td><td style='width:225px;'>" + v[i][4] + "</td><td>" + v[i][5] + "</td>")

                            document.write("</tr>")
                        }
                    </script>
                </table>
            </div>
        </div>

</body>

</html>.
   """ % (str(l))

  @cherrypy.expose() 
  def ssreport(self,itmid=None,status='0'):
        conn = connect('bill.db')
        print(itmid,status)
        cur = conn.cursor()
        l=[]
        if status is '0':
            sql='SELECT s.itmid,i.iname,s.qnty,s.stock,s.tsales,s.date FROM stock s,item i WHERE s.itmid=i.itmid'
            cur.execute(sql)
            c=cur.fetchall()
            conn.commit()
            for i in c:
                l.append([i[0],i[1],i[2],i[3],i[4],i[5]])
        if status is '1':
                sql='SELECT s.itmid,i.iname,s.qnty,s.stock,s.tsales,s.date FROM stock s,item i WHERE s.itmid=i.itmid and i.itmid='+str(itmid)
                print(sql)
                cur.execute(sql)
                c=cur.fetchall()
                conn.commit()
                for i in c:
                    l.append([i[0],i[1],i[2],i[3],i[4],i[5]])    
        
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
            <h1>STOCK REPORT</h1>
        </center>
        <form action="index" method="POST" class="log"><button type="submit">Logout</button></form>
    </div>
    <div id="mySidenav" class="sidenav">
        <div class="btn-group">
        <form action="" method="POST">
            <button type="submit" formaction="sstock">Manage Stocks</button>
            <button type="submit" formaction="ssreport">Stock Report</button>
            <button type="submit" formaction="locator">Product Locator</button>
            <button type="submit" formaction="index">Logout</button></form>
        </div>
    </div>
    <form action="index" method="POST" class="log"><button type="submit">Logout</button></form>
    </div>

    <div class="div3">
        
        <form action="ssreport" method="post"><label for="billid">ItmId:</label><input type="text" name="itmid" id="billid" placeholder="Enter Item Number">
        <button type="submit" class="button10" name="status" value="1">search</button>
        <button type="submit" class="button10" name="status" value="0">All</button>
    </form>

    </div>
    <div class="div4">
        <br>
        <div class="div5">
            <table>
                <tr>
                    <th>Item ID</th>
                    <th>ITEM Name</th>
                    <th>Qnty</th>
                    <th>Stock</th>
                    <th>Total_Sales</th>
                    <th>Date</th>
                </tr>
            </table>
            <div class="div6">
                <table>
                    <script>
                        var v=%s  
                        for (i in v) {
                            document.write("<tr>")

                            document.write("<td style='width:159px;'>" + v[i][0] + "</td><td style='width:247px;'>" + v[i][1] + "</td><td style='width:109px;'>" + v[i][2] + "</td><td style='width:118px;'>" + v[i][3] + "</td><td style='width:225px;'>" + v[i][4] + "</td><td>" + v[i][5] + "</td>")

                            document.write("</tr>")
                        }
                    </script>
                </table>
            </div>
        </div>

</body>

</html>.
   """ % (str(l))  

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
                              
cherrypy.server.socket_host = '0.0.0.0'      
cherrypy.quickstart(test()) 
   

