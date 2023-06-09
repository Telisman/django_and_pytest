# import pytest
# from django.db import connection
#
#
# @pytest.mark.django_db
# def test_database_connection():
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT 1")
#         result = cursor.fetchone()
#     assert result[0] == 1
#     print("Database connection is successful!")
#
#
# # Run pytest with the -s option to enable output capture
# pytest.main(["-s"])
#
