import os
from crewai import Agent, Task, Crew, Process


from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks




# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:


    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        frontend_developer = agents.agent_frontend_developer()
        file_creater = agents.agent_file_creater()

        # Custom tasks include agent name and variables as input
        coding = tasks.code_task(
            frontend_developer,
        )

        saving = tasks.write_to_file_task(
            file_creater,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[frontend_developer, file_creater],
            tasks=[coding, saving],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")


    custom_crew = CustomCrew()
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
