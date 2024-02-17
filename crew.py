from crewai import Agent, Task, Crew, Process
import os
from textwrap import dedent

disk_writer = Agent(
  role='Disk Writer',
  goal='Write generated code to a file',
  backstory="You are a disk writer. You write generated code to a file.",
  allow_delegation=False,
  verbose=True
)


frontend_developer = Agent(
			role='Senior Frontend Developer',
			goal='Create react app as needed',
			backstory=dedent("""\
				You are a Senior Frontend Developer.
				Your expertise in programming in React and Nextjs and do your best to
				produce perfect code"""),
			allow_delegation=False,
			verbose=True
		)

backend_developer = Agent(
      role='Senior Backend Developer',
      goal='Create backend as needed',
      backstory=dedent("""\
        You are a Senior Backend Developer.
        Your expertise in programming in Golang and do your best to
        produce perfect code"""),
      allow_delegation=False,
      verbose=True
    )

qa_agent = Agent(
  role='Software Quality Control Engineer',
  		goal='create prefect code, by analizing the code that is given for errors',
  		backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  			You also check for security vulnerabilities, and logic errors"""),
			allow_delegation=False,
			verbose=True
		)