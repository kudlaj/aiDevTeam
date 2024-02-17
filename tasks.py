from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:


    def code_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Write a simple react app that has a button and each time you click it, it increments a counter.
        """
            ),
            agent=agent,
        )

    def write_to_file_task(self, agent):
        return Task(
            description=dedent("""
      YOU MUST USE the tool to write the code to a file 
      in the following path: ./workdir/index.js
                               
      Take the created code and save it to a file with a filename index.js
     
      You first write the file then your final answer 
      MUST be the content.

      RULES
      -----
      - Remove all the links, this should be single page landing page.
      - NEVER WRITE \\n (newlines as string) on the file, just the code.
      - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
      - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
      - Save the file as with `.js` extension.

      If you follow the rules I'll give you a $100 tip!!! 
      MY LIFE DEPEND ON YOU FOLLOWING IT!
  

    """),
            agent=agent,
        )
