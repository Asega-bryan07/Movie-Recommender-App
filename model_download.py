import requests
import tempfile
import pickle

def download_and_save_model(url, output_path):
    with tempfile.NamedTemporaryFile(suffix='.pkl', delete=False) as temp_file:
        file_content = requests.get(url).content
        temp_file.write(file_content)

        # Reset the file pointer to the beginning before reading
        temp_file.seek(0)
        
        # Optional: Print the content to verify
        print(f"Content for {url}:", temp_file.read())

        # Reset the file pointer again before loading the model
        temp_file.seek(0)
        model = pickle.load(temp_file)

    # Save the model to the specified output path
    with open(output_path, 'wb') as output_file:
        output_file.write(file_content)

    return model


def main():
    similarity_url = 'https://drive.google.com/file/d/1uUb33kGuLlyJAIQlNPNRgR5zUDnFz3Cr/view?usp=drive_link'
    movies_url = 'https://drive.google.com/file/d/1X70vCuF4t5lHPysRi1XhJCfQHra5l4jI/view?usp=drive_link'

    similarity_model = download_and_save_model(similarity_url, './similarity.pkl')
    movies_model = download_and_save_model(movies_url, './movies.pkl')

if __name__ == "__main__":
    main()
