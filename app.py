import streamlit as st
import time
from langchain.chat_models import ChatOllama
from langchain.agents import create_openai_tools_agent, AgentExecutor, load_tools
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
import streamlit.components.v1 as components

# ---- Set page config FIRST ----
st.markdown('<div class="title">AI Search Agent</div>', unsafe_allow_html=True)

# ---- Custom CSS ----
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-weight: 500;
            font-size: 30px;
            margin-bottom: 20px;
        }
        .right-align {
            text-align: right !important;
            background-color: #DCF8C6;
            padding: 10px 15px;
            border-radius: 16px;
            margin: 5px 0px;
            max-width: 70%;
            float: right;
            clear: both;
        }
        .left-align {
            text-align: left !important;
            background-color: #F1F0F0;
            padding: 10px 15px;
            border-radius: 16px;
            margin: 5px 0px;
            max-width: 70%;
            float: left;
            clear: both;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Typing animation message ----
components.html("""
    <div id="typing-text" style="
        font-size: 20px; 
        font-weight: 400; 
        text-align: center; 
        margin-top: 5px; 
        margin-bottom: 20px;
        font-family: 'Segoe UI', sans-serif;
        color: #333;">
    </div>

    <script>
    const text = "Hey! I'm your AI agent. Just ask a question, and I’ll search the web and Arxiv to help you out!";
    const typingDiv = document.getElementById("typing-text");
    let i = 0;

    function typeText() {
        if (i < text.length) {
            typingDiv.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeText, 40);
        }
    }

    window.onload = typeText;
    </script>
""", height=100)

# ---- LLM Setup ----
llm = ChatOllama(model="gemma:2b")
tools = load_tools(["wikipedia", "arxiv"])

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant 🤖"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_openai_tools_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

# ---- Session State ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "bot_output" not in st.session_state:
    st.session_state.bot_output = ""

# ---- Display Previous Chat History ----
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"<div class='right-align'>{message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='left-align'>{message}</div>", unsafe_allow_html=True)

# ---- User Input ----
user_input = st.chat_input("Ask anything...")

# ---- Handle New Input ----
if user_input:
    st.markdown(f"<div class='right-align'>{user_input}</div>", unsafe_allow_html=True)
    st.session_state.chat_history.append(("user", user_input))

    # Placeholder for bot reply
    bot_placeholder = st.empty()

    with st.spinner("generating"):
        response = agent_executor.invoke({"input": user_input})
        st.session_state.bot_output = response["output"]

    # Display Final Bot Output
    bot_placeholder.markdown(f"<div class='left-align'>{st.session_state.bot_output}</div>", unsafe_allow_html=True)
    st.session_state.chat_history.append(("bot", st.session_state.bot_output))
