# Image Recognition with OpenAI API

1. Make sure that you have set up your keys correctly with the exercise `01-OpenAI-Key.md` from Lesson 01

2. Make sure that your `venv` is activated

3. Run the following code on your terminal:

   ```bash
   pip install openai
   ```

   - This command will install the `openai` [API Package](https://github.com/openai/openai-python) on your environment

4. Create a new Python file

   - Create a new file on your favorite code editor or simply run `touch <filename>.py` on your terminal (Linux/MacOS) or `type nul > <filename>.py` on your terminal (Windows)

   - Remember to replace `<filename>` with the name of your file

5. Import the `openai` module on your file

   ```python
    from openai import OpenAI
   ```

   - This `client` can abstract all of the complexities of consuming the OpenAI API endpoints, like handling the authentication, the request and response formats, synchronous and asynchronous requests, and many other features

   - To use this library correctly, all you need to do is to understand well the [API parameters](https://platform.openai.com/docs) that you want to consume

6. Create a new `client` instance

   ```python
    client = OpenAI()
   ```

   - By default, this will try to use the `OPENAI_API_KEY` environment variable to create this client

   - You can customize the logic by doing an explicit definition like this:

   ```python
   import os
   from openai import OpenAI
   client = OpenAI(
       api_key=os.environ.get("OPENAI_API_KEY"),
   )
   ```

   - Here you can change `api_key` to any value that you want to use

   - Have caution if you prefer to hardcode your key in this file, since this could lead to you inadvertently sharing your key with others

7. Call the [Chat Completion](https://platform.openai.com/docs/guides/vision) endpoint in the `client` with the following parameters:

   ```python
   response = client.chat.completions.create(
       model="gpt-4-vision-preview",
       messages=[
           {
               "role": "user",
               "content": [
                   {"type": "text", "text": "What's in this image?"},
                   {
                       "type": "image_url",
                       "image_url": {
                           "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                       },
                   },
               ],
           }
       ],
       max_tokens=300,
   )
   ```

   - The `model` parameter is the name of the model that you want to use to analyze the image

     - The models available to use from OpenAI API are listed in the [Models](https://platform.openai.com/docs/models/overview) API documentation

   - The `messages` parameter is a list of messages that you want to send to the model

     - You can provide an image either by passing a link to the image in the `image_url` parameter or by encoding the image as a base64 string within the same parameter. Check the [Vision](https://platform.openai.com/docs/guides/vision) guide for more information

   - The `max_tokens` parameter is the maximum number of tokens to generate in the response

8. Print the response

   ```python
   print(response.choices[0].message.content)
   ```

9. Run the file

   ```bash
   # Linux/MacOS
   python <filename>.py
   ```

   ```bash
   # Windows
   py <filename>.py
   ```

10. Check the output

    - You should see the response from the model being printed on your terminal

    - Example of response

    ```text
    The image shows a beautiful nature scene with a wooden boardwalk stretching through a lush green meadow. The sky is partly cloudy with blue patches showing through, suggesting a pleasant day. The meadow appears to be tall grass or a wetland environment. The boardwalk serves as a walking path that allows visitors to enjoy the natural surroundings without disturbing the ecosystem. There are no people visible in the image, which adds to the peaceful and serene atmosphere. The greenery is vibrant and appears well-lit by the sunlight, indicating that the photo was taken during a time of day when the sun was shining brightly.
    ```

11. Experiment with the [Chat Completion API Parameters](https://platform.openai.com/docs/api-reference/chat) to test how the model behaves with different inputs and configurations

> View more information about the OpenAI API at <https://platform.openai.com/docs> and the OpenAI Python Package at <https://github.com/openai/openai-python>
