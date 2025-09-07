# Generating text with LLMs

1. Install all of the required dependencies for this exercise

   - Run `pip install bitsandbytes optimum accelerate`

   > Note: bitsandbytes relies on CUDA, which is exclusively available for Nvidia GPUs. Please note that installation instructions for Windows and MacOS differ from the general instructions. For detailed guidelines on installing bitsandbytes on Windows and MacOS, refer to the official documentation [here](https://huggingface.co/docs/bitsandbytes/installation)

2. Create a new Python file
   - Create a new file on your favorite code editor or simply run `touch <filename>.py` on your terminal (Linux/MacOS) or `type nul > <filename>.py` on your terminal (Windows)
     - Remember to replace `<filename>` with the name of your file
3. Import the `pipeline` module from the `transformers` package

   ```python
   from transformers import pipeline
   ```

4. Import `torch` directly as well, since we're going to use some types from it later on

   ```python
   import torch
   ```

5. Create a new instance of the `pipeline` in a variable to handle the model loading and text generation

   - We're going to use the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` model due to the low memory requirements of the model to run properly

   ```python
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
   ```

6. Configure the pipeline for your hardware capabilities

   - If you have a GPU with at least 4GB of VRAM, you can use the `device_map="auto"` and `torch_dtype=torch.bfloat16` options to make the model run faster and use less memory

   ```python
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")
   ```

   - You might need to change some of these [configuration parameters](https://huggingface.co/docs/transformers/en/llm_optims#quantization) to better fit your hardware and the model you're using

7. Create an input text to be used as a prompt for the model

   ```python
   input_text = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds like an Italian chef",
    },
    {"role": "user", "content": "What is the best recipe for Pepperoni pizza?"},
   ]
   ```

8. Use the Tokenizer to apply the chat template to the input text

   ```python
   prompt = pipe.tokenizer.apply_chat_template(input_text, tokenize=False, add_generation_prompt=True)
   ```

9. Generate text using the model and the tokenized prompt text

   ```python
   outputs = pipe(prompt, max_new_tokens=256)
   ```

10. Print the generated text result inside the output object

    ```python
    print(outputs[0]["generated_text"])
    ```

11. Run the file

    ```bash
    # Linux/MacOS
    python <filename>.py
    ```

    ```bash
    # Windows
    py <filename>.py
    ```

12. Expect a considerable load time if you're running this command for the first time, as the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` model will be downloaded from the Hugging Face's model hub

    - The model is more than 2GB in size, so make sure you have enough disk space available on your device and a stable internet connection
    - The model will be downloaded to the `~/.cache/huggingface/transformers` directory on your device and will be available for future runs of the same script without downloading it again

13. If you get an "Out Of Memory" error, try to tweak the quantization parameters to make the computation fit on your device's memory

    - If all else fails, you can also try to run the script in a cloud-based environment with more resources available

14. If your script ran correctly, you should get an output like this:

    ```text
    What is the best recipe for Pepperoni pizza?

    A: Ingredients:

    2 1/4 tsp active dry yeast

    1/2 tsp sugar

    1 1/2 cup warm water (110 degrees F)

    3 cups bread flour

    2 tbsp olive oil

    1 tsp salt

    1. In a small bowl, dissolve the yeast and sugar in warm water. Let stand until creamy, about 10 minutes.

    2. In the bowl of an electric mixer fitted with a dough hook, combine the flour and salt. Add the yeast mixture and oil, and mix on low speed until the dough comes together, about 1 minute.

    3. Increase the speed to medium and knead for 6 to 8 minutes, until the dough is smooth and elastic.
    ```

> Find more information about generating text with LLMs at <https://huggingface.co/docs/transformers/main/en/llm_tutorial#generation-with-llms>
