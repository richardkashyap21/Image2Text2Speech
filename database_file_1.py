import mysql.connector

def convert_to_binary_data(filename):

    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data


def insert_into_db(name, image_path, extracted_text,audio_file_path):

    global connection, my_cursor
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='image_db',
            user='root',
            password='1234'
        )
        my_cursor = connection.cursor()

        insert_image_query = """INSERT INTO images (name, image, extracted_text, audio_file)
                                    VALUES (%s, %s, %s, %s)"""

        image_data = convert_to_binary_data(image_path)
        audio_file_data = convert_to_binary_data(audio_file_path)

        my_cursor.execute(insert_image_query, (name, image_data, extracted_text, audio_file_data))
        connection.commit()
        print("Image, text, and audio file inserted successfully into images table")

    except mysql.connector.Error as error:
        print(f"Failed to insert image into MySQL table {error}")

    finally:
        if connection.is_connected():
            my_cursor.close()
            connection.close()
            print("MySQL connection is closed")


