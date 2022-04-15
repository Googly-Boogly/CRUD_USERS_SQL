# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )
    @classmethod
    def update( cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW()) WHERE users.id = %(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_one(self, cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        # make sure to call the connectToMySQL function with the schema you are targeting.

        resulst = connectToMySQL('users_schema').query_db( query, data )
        users = []
        for user in resulst:
            users.append( cls(user) )
        return users

    @classmethod
    def delete(self, cls, data):
        query = "DELETE * FROM users WHERE id = %(id)s"
        connectToMySQL('users_schema').query_db( query, data )
        return True