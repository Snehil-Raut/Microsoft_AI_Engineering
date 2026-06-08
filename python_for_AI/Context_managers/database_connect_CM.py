# Stimulation of how to establish database connection using context managers
# why useful in database connection - because the connection is automatically closed and cleanup

# Create a context manager DatabaseConnection:
# It should:
# print "connection opened"
# simulate query execution
# print "connection closed automatically"

# Even if an error occurs inside the block

from contextlib import contextmanager    # using built-in library to eliminate the need of __enter__ and __exit__ function, this will convert generator function to context manager

@contextmanager
def Databaseconnection():
    conn = "Database: PostgreSQL" 
    print("Establishing connection with database")
    try:
        yield conn
    except Exception as e:
        raise e
    finally:
        print("Connection closed")

with Databaseconnection() as db:
    print("Using",db)


# this code establishes the connection with dataset
# after the connection is establish- close the connection automatically