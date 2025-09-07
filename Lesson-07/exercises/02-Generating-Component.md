# Extending the Chef GPT App with an AI Generated Component

1. Open a terminal and navigate to the root of your project
2. Setup the V0 package in your project with the command `npx v0@latest init`
3. Log in to [Vercel V0](https://v0.dev/)

   > Vercel has recently released a chat mode for V0 with a different flow for generating components. Since it is still very experimental, we will keep using the normal mode to have more control over the process.

4. Create a starting UI from this prompt: `A simple leaderboard page with the most requested dishes in a restaurant`

   - Pick a color scheme in the dropdown below the prompt input

5. Make iterative changes until you have a page with a table listing some dishes and the number of requests for each
6. Change the appearance of the table and the elements using the `Pick and edit` tool

   - Click on the elements you want to change and write a specific prompt
     - Example: `Make the first column bold` or `make the first row with a golden background`

7. Make a prompt to add a new button to `Generate Recipe`
8. Make all the changes that you see fit until you have a complete page that you feel that you can use in your project
9. Click the "Code" button in the top right to open the code panel
10. copy the CLI command (should be something similar to `npx v0 add <id>`) and execute it in the terminal
11. Pick the default options
12. The new component should be created in the `components` folder in the root of your project
13. Now you can modify the `page.tsx` file to import the generated component to use it in that page
14. Test the new page in your project and make any adjustments needed
