from sqlite3 import connect
import cherrypy
cherrypy.config.update({'server.socket_port': 9999})

class test:                       
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
            <button type="submit" formaction="Stock"  style="background-color: darkgrey">Manage Stocks</button>
            <button type="submit" formaction="Price">Price Management</button>
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
     

#cherrypy.server.socket_host = '0.0.0.0'      
cherrypy.quickstart(test()) 
   

