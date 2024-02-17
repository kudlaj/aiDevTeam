from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.agent_toolkits import FileManagementToolkit

from write_code_to_file import CustomTools
from tools.file_tools import FileTools


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def agent_frontend_architect(self):
        return Agent(
            role='Senior Frontend Architect',
			      goal='Create the best architecture for the frontend',
            backstory=dedent("""\
                You are a Senior Frontend Architect.
                Your expertise in programming in React and Nextjs and do your best to
                produce perfect code. You think about the best architecture for the frontend"""),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
    
    def agent_frontend_developer(self):
        return Agent(
            role='Senior Frontend Developer',
			      goal='Create react app as needed',
            backstory=dedent("""\
                You are a Senior Frontend Developer.
                Your expertise in programming in React and Nextjs and do your best to
                produce perfect code"""),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def agent_file_creater(self):
        toolkit = FileManagementToolkit(
          root_dir='workdir',
          selected_tools=["read_file", "list_directory"]
        )

        return Agent(
            role='Disk Writer',
            goal='Write generated code to a file',
            backstory="You are a disk writer. You write generated code to a file.",
            tools=[FileTools.write_file]+ toolkit.get_tools(),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
