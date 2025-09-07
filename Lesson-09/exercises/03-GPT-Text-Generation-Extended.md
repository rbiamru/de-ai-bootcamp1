# Generating text with GPTs

1. Start with the Text Generation example `TextGeneration.py` from the previous exercise

2. Use the following prompt

    ```python
    input_text = [
     {
         "role": "system",
         "content": "You are a friendly chatbot who always responds like an Italian chef",
     },
     {"role": "user", "content": "How to make a good sandwich?"},
    ]
    ```

3. Configure the generation parameters for the model

   ```python
   outputs = pipe(
   prompt,
   max_new_tokens=512,
   do_sample=True,
   temperature=0.5,
   top_k=50,
   top_p=0.9,
   no_repeat_ngram_size=3,
   )
   ```

   >Read more about the `generate` configs at <https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationConfig>

4. Add `do_sample=True` to start using the sampling method for generating text

    - Without this parameter, the model will use the greedy search method, which always picks the most likely next word, which is not always the best choice
    - Sampling is what gives the model the ability to generate different outputs each time it is called, based on the randomness of the sampling method and the model's training data
    - This parameter enables decoding strategies such as multinomial sampling, beam-search multinomial sampling, Top-K sampling and Top-p sampling, that are able select the next tokens from the probability distribution over the entire vocabulary with various strategy-specific adjustments

5. Add `temperature=0.5` to modulate the probabilities of sequential tokens

    - A temperature of 0.5 is a good starting point for the task we're trying to accomplish, but you can try different values to see how it affects the output

6. Add `top_k=75` to broaden the range of tokens that the model can pick from

    - This parameter will make the model consider the top 75 most likely tokens for the next word, which will make the output a bit more diverse

7. Add `top_p=0.9` to exclude less probable tokens from generation

    - This parameter will make the model consider the top 90% most likely tokens for the next word, which will probably make the output stay on topic and be more coherent

8. Add `no_repeat_ngram_size=3` to avoid repeating the same n-grams in the output

    - This parameter will make the model avoid repeating the same 3-grams in the output, which will prevent repetitive and boring outputs

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

    ```text
    1. Choose the right bread: Look for a soft, slightly sour bread like a ciabatta, a sourdough, or a whole grain bread.

    2. Choice of cheese: A good sandwhich requires a good cheese. Look for cheddar, Swiss, or provolone.
     
    3. Choosing the right condiments: A sandwich needs a good condiment to balance the flavors. Try a mustard, mayo, or ketchup.
      
    4. Chopping the vegetables: Choose fresh vegetables that complement the bread and cheese well.
       
    5. Add fillings: Add your fillings to the bread. Try tomato, avocado, lettuce, or ham.
        
    6. Make the sandwich: Take the bread, spread the cheese, add the vegetable or meat, and add the condiments.
           
    7. Roll the sandwhich: Roll the bread tightly, so it is easy to eat.
            
    8. Serve: Serve the sandbread with a knife and a fork.
             
    9. Enjoy your sandwich!
    ```

> Find more information about generating text with LLMs at <https://huggingface.co/docs/transformers/main/en/llm_tutorial#generation-with-llms>
