# Data Engineer Code Challenge - Levee

# Importing mysql connector library
import mysql.connector


class Database:
    # Method to open a connection to MySQL database
    def open(self, host="", port="", user="", password=""):
        try:
            self.conn = mysql.connector.connect(
                host=host, port=port, user=user, password=password
            )

            self.cursor = self.conn.cursor(dictionary=True)

            return self.conn, self.cursor

        # Generating error message if something goes wrong
        except Exception as error:
            return "Error: " + str(error)

    # Method to close a connection to MySQL database
    def close(self, conn=""):
        try:
            self.conn.close()

        # Generating error message if something goes wrong
        except Exception as error:
            return "Error: " + str(error)
