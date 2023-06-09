# import pytest
# from django.db import connection
#
#
# @pytest.mark.django_db
# def test_database_connection(capfd):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT 1")
#         result = cursor.fetchone()
#
#     assert result[0] == 1
#     print("Database connection is successful!")
#
#     # Retrieve the captured stdout and check if the print statement was output
#     captured = capfd.readouterr()
#     assert "Database connection is successful!" in captured.out
