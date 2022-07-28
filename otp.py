
import cherrypy
cherrypy.config.update({'server.socket_port': 9999})

class test:                       
  @cherrypy.expose() 
  def otp(self,otp=None,status=0):
        import random
        from twilio.rest import Client
        x=[]
        client = Client("AC8524e480f521715997282f87d6879cf0", "302f4c8c7dca0fdd448f255ace993337")
        if status is 0:
            r=random.randrange(1000,9999)
            print(r)
            f=open("otp.txt",'w')
            f.write(str(r))
            f.close()
            msg="OTP:-"+str(r)
            print(msg)
            #phno="+91"+str(custid)
            phno="+919379067642"
            print(phno)
            client.messages.create(to=phno, 
                       from_="+12546553126", 
                       body=msg)            
        s=None
        l=0
        if status is '1':
            f=open("otp.txt",'r')
            s=f.readline()
            f.close()
            print(s,otp)
        
            if otp is s or int(otp)==int(s):
                print(True)
                l=1
            else:
                l=2  
        print(l)  
        x.append(l)      
        return """ 
<html>
<title>SuperMarket</title>

<head>
    <style>
        body {
            background-image: url(https://i.pinimg.com/originals/b4/f9/f9/b4f9f97ef17f943e969494a3f8e57cfb.jpg);
            background-repeat: no-repeat;
            background-size: 1000 500;
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
        
        .button {
            width: 115px;
            background-color: #4CAF50;
            color: white;
            position: absolute;
            z-index: 0;
            display: inline-block;
            padding: 14px 20px;
            margin: 80px -205px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        button:hover {
            background-color: #4574a0e0;
        }
        
        .imgcontainer {
            text-align: center;
            margin: 24px 0 12px 0;
            position: relative;
        }
        
        img.avatar {
            width: 200px;
            border-radius: 100;
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
            width: 500px;
            /* Full width */
            height: 600px;
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
            margin: 15px auto 25px auto;
          
            border: 1px solid #888;
            width: 350px;
            
            height: 500px;
        }
        
    </style>
    <body>
     <script>
            var v=%s
            system.log(v[0])
           if(v[0]==0){window.alert("OTP Sent to your mobile number")}
           else if(v[0]==1){  document.write("<form id='f1' action="admin" method='post'></form>")
               document.getElementById('f1').submit()}
           else(v[0]==2){window.alert("inccorect otp")}
        </script>
    <div class="container">
       
        <form class="modal-content animate" action="otp" method="post">
            <div class="imgcontainer">
                <img src="https://blog.cpanel.com/wp-content/uploads/2019/08/user-01.png" alt="Avatar" class="avatar">
            </div>

            <div class="container">
                <h1 style="font-size:20px;">
                    <center>OTP
                        <p>Two-Step authentication</p>
                    </center>
                </h1>
                <input type="text" placeholder="Enter user OTP" name="otp" required>
                <button class="button" type="submit" name="status" value="1">Submit</button>
            </div>
        </form>
    </div>
    <form id="f1" action='' method="post"></form>
    </body></html>
   """   % (str(x))  
     

#cherrypy.server.socket_host = '0.0.0.0'      
cherrypy.quickstart(test()) 
   

