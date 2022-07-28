
import pip
try:
    import cherrypy
except:
        pip.main(['install', 'cherrypy'])
try:
    from sqlite3 import connect
except:
        pip.main(['install', 'sqlite3'])
 
import cherrypy  
from sqlite3 import connect      
cherrypy.config.update({'server.socket_port': 8080})      
class PIMS:
   # webbrowser.open('http://127.0.0.1:8080')

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
         <div class="divh"><center><h1>Locator</h1></center> </div>
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


cherrypy.server.socket_host = '0.0.0.0'                 
cherrypy.quickstart(PIMS())     
x=input()      
