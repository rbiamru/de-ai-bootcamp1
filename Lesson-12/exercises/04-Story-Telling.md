# Building a Storytelling Application

1. Open the _Story Telling App_ project created on **Lesson 08**

2. Edit the `route.ts` file

   - Replace the contents of the file following code

   ```typescript
   import OpenAI from "openai";
   import { OpenAIStream, StreamingTextResponse } from "ai";

   const openai = new OpenAI({
     baseURL: "http://127.0.0.1:5000/v1",
   });

   export const runtime = "edge";

   export async function POST(req: Request) {
     const { messages } = await req.json();

     const response = await openai.chat.completions.create({
       model: "gpt-3.5-turbo",
       stream: true,
       messages: [
         {
           role: "system",
           content: `You are a professional storyteller who has been hired to write a series of short stories for a new anthology. The stories should be captivating, imaginative, and thought-provoking. They should explore a variety of themes and genres, from science fiction and fantasy to mystery and romance. Each story should be unique and memorable, with compelling characters and unexpected plot twists.`,
         },
         ...messages,
       ],
     });

     const stream = OpenAIStream(response);
     return new StreamingTextResponse(stream);
   }
   ```

   - In the base URL parameter, replace 5000 with the port number that you have configured for your local API endpoint

   > Ensure that your local API is running for the application to work

3. Run the Text Generation WebUI and load a model

4. Test the app to evaluate how the AI responds to the user's requests

   - Run the app by executing the following command on the terminal:

   ```bash
   npm run dev
   ```
