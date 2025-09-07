# Deploying and Agent to the Agentverse

The Agentverse is built on top of Fetch.ai blockchain technology, providing a secure way to develop Agents with the benefit of registering them on a decentralized platform and make them communicate and perform actions with one another.

## Steps

1. Create a new folder for this project:

   ```bash
   mkdir agentverse-agent
   cd agentverse-agent
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the [uagents](https://pypi.org/project/uagents/) dependency

   ```bash
   pip install uagents
   ```

4. Create a new file for the agent:

   ```bash
   touch agent.py
   ```

5. Create the code for the self hosted agent:

   ```python  
   from uagents import Agent, Context

   agent = Agent(name="alice", seed="secret_seed_phrase", port=8000, endpoint=["http://localhost:8000/submit"])

   @agent.on_event("startup")
   async def introduce_agent(ctx: Context):
       ctx.logger.info(f"Hello, I'm agent {agent.name} and my address is {agent.address}.")

   if __name__ == "__main__":
   agent.run()
   ```

6. Run the agent:

   ```bash
   python agent.py
   ```

   - You should see the agent running in the terminal

   ```bash
   INFO:     [alice]: Hello, I'm agent alice and my address is agent1qtu6wt5jphhmdjau0hdhc002ashzjnueqe89gvvuln8mawm3m0xrwmn9a76.
   ```

7. Create an account on the [Agentverse](https://agentverse.ai/)

8. Click on the `Create Agent` button

9. Select the `Your First Agent` template

10. Fill the name of the agent in the input field and click on the `Create` button

11. You should see the agent created in the Agentverse

12. Click on the `Start` button

13. You should see the agent deployed in the Agentverse and the logs in the terminal

14. Open the `</> Build` tab

15. There you can edit the `agent.py` file to customize the agent behavior
