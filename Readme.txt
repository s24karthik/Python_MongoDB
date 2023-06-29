# Python codebase snippets for various MongoDB workflows #

1.  A snippet to get connected to popular NoSQL DB - MONGODB
2.  Hope you have setted up the MongoDB account, cluster and access

To setup MongoDB ->> https://www.mongodb.com/

3.  Make sure you have setted up the access to readwrite database to allow you to make DB
4.  Make sure you have setted up the network endpoint to allow your IP to get connected to MongoDB

NOTE ->> Both the point 3 & 4 can be done in MongoDB UI - Database access and Network access options

**************** CODEBASE SETUP ****************
1.  app.py is the main file
        A.  Sets the Mongo Clinet
        B.  Triggers the sub workflow modules

2.  basic.py is the codebase holds small basic MongoDB snippets
        A.  To load any document data use the " Doc_load.json " file 
        B.  Make sure to change the " document_load.json " to your specific location

NOTE ->> MongoDB to make A DB and collection is made only when it holds atleast 1 document

3.  For option 3. Insert Multi document - Make sure you have loaded 2 document in list format in the " Doc_multi_load.json " file
