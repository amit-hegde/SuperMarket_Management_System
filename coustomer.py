from sqlite3 import connect
import cherrypy
cherrypy.config.update({'server.socket_port': 9999})

class test:                       
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
        
            <button type="submit" class="btn4" name="status" value="1" >Create User</button>
        <form action="bill" method="post">    
            <button type="submit" class="btn4" name="status" value="2">New Bill</button>
            <button type="submit" class="btn4" name="status" value="2">cancel</button>
        </form>
    </center>
    </div>
</center> 

</body>
</html>     """    
     

#cherrypy.server.socket_host = '0.0.0.0'      
cherrypy.quickstart(test()) 
   

