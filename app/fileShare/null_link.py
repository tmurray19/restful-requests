import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from app import app

import pyodbc


def null_project_li(proj_id):
    """Sends a null link to the database"""
    try:

        # Set the Connection Parameters
        params = urllib.parse.quote_plus(
            "DRIVER={SQL Server Native Client 11.0};"
            "SERVER="+app.config['DBCONNSERV']+";"
            "DATABASE="+app.config['DBASE']+";"
            "UID="+app.config['DBBUUID']+";"
            "PWD="+app.config['DBPW']+""
        )

        # Open DB Connection & Session
        engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))      
        Session = scoped_session(sessionmaker(bind=engine))
        s = Session()

        # Build the SQL Query
        query = 'UPDATE project SET FinalViedo_URL = Processing , Soc_FinalViedo_URL = Processing ' \
                +' WHERE [id]=' + str(proj_id)
        
        # Execute & Commit
        
        result = s.execute(query)
        result = s.execute('COMMIT')
    except Exception as e:
        result = str(e)
    return result

