# Python codebase snippets for MongoDB #

1.  Snippet to get connected to NoSQL DB - MongoDB
2.  Hope you have setted up the MongoDB account, cluster and access. To setup MongoDB ->> https://www.mongodb.com/
3.  Make sure you have setted up the access to readwrite database to allow you to make DB
4.  Make sure you have setted up the network endpoint to allow your IP to get connected to MongoDB

NOTE ->> Both the point 3 & 4 can be done in MongoDB UI - Database access and Network access options

**************** CODEBASE SETUP ****************
1.  app.py is the main file
        A.  Sets the Mongo Clinet
        B.  Triggers the sub workflow modules

2.  mongo_basic.py is the codebase holds small basic MongoDB snippets
        A.  Insert the document
        B.  Extract the data from DB

NOTE ->> In MongoDB database and collection is made only when it holds atleast 1 document

3.  Make sure to change the extract file path