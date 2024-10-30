import PIL.Image
import time
import pathlib
import google.generativeai as genai

# Author: Jeba Seelan
# Created Date: 30-10-2024
# Description: This script utilizes the Google Generative AI library to generate textual descriptions for images and videos.
# It includes functions for generating descriptions from single images, comparing multiple images, and analyzing video content.

# Define the media path relative to the current file's location
media = pathlib.Path(__file__).parents[1] / "third_party"

def single_image_text_gen_ai():
    """Generates a text description for a single image of an instrument."""
    model = genai.GenerativeModel("gemini-1.5-flash")  # Load the AI model
    organ = PIL.Image.open(media / "organ.jpg")  # Open the organ image
    
    # Generate a description based on the image
    response = model.generate_content(["Tell me about this instrument", organ])
    print(response.text)  # Output the generated text

def multi_image_text_gen_ai():
    """Generates text comparing two different images of instruments."""
    model = genai.GenerativeModel("gemini-1.5-flash")  # Load the AI model
    organ = PIL.Image.open(media / "organ.jpg")  # Open the organ image
    cajun_instrument = PIL.Image.open(media / "Cajun_instruments.jpg")  # Open the Cajun instrument image
    
    # Generate a comparative description based on both images
    response = model.generate_content(
        ["What is the difference between both of these instruments?", organ, cajun_instrument]
    )
    print(response.text)  # Output the generated text

def video_text_gen_ai():
    """Generates a description for a video after processing."""
    # Upload the video file for analysis
    myfile = genai.upload_file(media / "Big_Buck_Bunny.mp4")
    print(f"Uploaded file: {myfile.name}")  # Display the uploaded file name

    # Wait until the video processing is complete
    while myfile.state.name == "PROCESSING":
        print("Processing video...")
        time.sleep(5)  # Pause before checking the status again
        myfile = genai.get_file(myfile.name)  # Update the file status

    model = genai.GenerativeModel("gemini-1.5-flash")  # Load the AI model
    # Generate a description based on the video content
    response = model.generate_content([myfile, "Describe this video clip"])
    print(f"Response text: {response.text}")  # Output the generated text

if __name__ == "__main__":
    # Execute the text generation functions
    single_image_text_gen_ai()
    multi_image_text_gen_ai()
    video_text_gen_ai()
