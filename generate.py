from sqlite3 import connect
import cherrypy
cherrypy.config.update({'server.socket_port': 9999})

class test:                       
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
            <button type="submit" class="btn4" name="status" value="1">Send</button>
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
     

#cherrypy.server.socket_host = '0.0.0.0'      
cherrypy.quickstart(test()) 
   

