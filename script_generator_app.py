



# import streamlit as st
# import google.generativeai as genai
# import os

# # --- Configure Google Gemini API ---
# try:
#     genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# except KeyError:
#     st.error("Google API Key not found. Please add it to your Streamlit secrets.toml file as GOOGLE_API_KEY.")
#     st.stop()

# # --- Function to check available models ---
# @st.cache_resource
# def get_available_gemini_models():
#     available_models = []
#     try:
#         for m in genai.list_models():
#             if "generateContent" in m.supported_generation_methods:
#                 available_models.append(m.name)
#     except Exception as e:
#         st.error(f"Error fetching model list: {e}")
#     return available_models

# # --- Sidebar: Model Selection ---
# st.sidebar.title(" Settings")
# available_models_list = get_available_gemini_models()

# selected_model_name = ""

# if available_models_list:
#     default_index = 0
#     for i, model_name in enumerate(available_models_list):
#         if "flash" in model_name:
#             default_index = i
#             break
    
#     selected_model_name = st.sidebar.selectbox(
#         "Choose AI Model:",
#         available_models_list,
#         index=default_index,
#         help="If one model fails, try selecting a different one from this list."
#     )
# else:
#     st.sidebar.error("Could not retrieve available models. Using fallback.")
#     selected_model_name = "models/gemini-pro"

# try:
#     model = genai.GenerativeModel(selected_model_name)
# except Exception as e:
#     st.error(f"Failed to initialize model: {selected_model_name}. Error: {e}")

# # --- Script Generation Function ---
# def generate_script(topic):
#     prompt_template = (
#     f"You are an AI assistant tasked with generating comprehensive YouTube video scripts.\n"
#     f"Generate a complete YouTube script for the topic: '{topic}'.\n"
#     f"The script should be friendly, motivational, clear, and helpful.\n"
#     f"Structure the script exactly as follows, with clear headings for each section:\n\n"
#     f"**1. Hook (approx. 30 seconds):**\n"
#     f"   [Engaging opening that grabs viewer's attention and introduces the problem/question]\n\n"
#     f"**2. Introduction (Who you are and what viewers will learn):**\n"
#     f"   [Brief self-introduction, outline of what the video will cover and benefits]\n\n"
#     f"**3. Main Points (Use 3-4 clear, detailed sections):**\n"
#     f"   **Main Point 1: [Descriptive Title for Point 1]**\n"
#     f"   [Detailed explanation, examples, tips related to Point 1]\n\n"
#     f"   **Main Point 2: [Descriptive Title for Point 2]**\n"
#     f"   [Detailed explanation, examples, tips related to Point 2]\n\n"
#     f"   **Main Point 3: [Descriptive Title for Point 3]**\n"
#     f"   [Detailed explanation, examples, tips related to Point 3]\n\n"
#     f"   **(Optional) Main Point 4: [Descriptive Title for Point 4]**\n"
#     f"   [Detailed explanation, examples, tips related to Point 4]\n\n"
#     f"**4. Conclusion (Recap and Call to Action - CTA):**\n"
#     f"   [Brief summary of key takeaways, strong call to action for liking, subscribing, and commenting.]\n\n"
#     f"Ensure the script is long enough to cover the topic thoroughly, but concise."
#     )

#     try:
#         response = model.generate_content(prompt_template)
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # --- Streamlit App Interface ---
# st.set_page_config(
#     page_title=" YouTube Script Generator",
#     page_icon="🎬",
#     layout="centered",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS
# st.markdown(
#     """
#     <style>
#     .stButton>button {
#         background-color: #FF4B4B;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 24px;
#         font-weight: bold;
#     }
#     .stTextInput>div>div>input {
#         border: 2px solid #FF4B4B;
#         border-radius: 8px;
#     }
#     h1 { color: #FF4B4B; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("YouTube Script Generator")

# # --- SESSION STATE: Initialize variable to store script ---
# if 'generated_script' not in st.session_state:
#     st.session_state['generated_script'] = ""

# # Input for the topic
# topic_input = st.text_input("Enter your video topic here:", "Mastering Home Brewing: The Ultimate Guide to Perfect Coffee")

# # Button: Only responsible for GENERATION
# if st.button("Generate Script"):
#     if topic_input:
#         # Spinner is ONLY active during the generation process
#         with st.spinner(f"🚀 Generating script using {selected_model_name}..."):
#             result = generate_script(topic_input)
#             # Save to session state so it persists
#             st.session_state['generated_script'] = result
#     else:
#         st.warning("Please enter a topic to generate a script.")

# # --- DISPLAY LOGIC: Handles showing the script (Outside the button/spinner block) ---
# # This checks if there is a script stored in the session and displays it
# if st.session_state['generated_script']:
#     script_content = st.session_state['generated_script']
    
#     # Handle potential errors
#     if script_content.startswith("Error:"):
#         st.error(script_content)
#         st.warning("Try selecting a different model from the sidebar.")
#     else:
#         st.subheader("✍️ Your Generated Script:")
#         st.markdown(script_content)
#         st.download_button(
#             label="Download Script",
#             data=script_content,
#             file_name=f"{topic_input.replace(' ', '_')}_script.md",
#             mime="text/markdown"
#         )

# st.markdown("---")
# st.markdown("Powered by Google Gemini and built with ❤️ using Streamlit.")





# import streamlit as st
# import google.generativeai as genai
# import os

# # --- Configure Google Gemini API ---
# try:
#     genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# except KeyError:
#     st.error("Google API Key not found. Please add it to your Streamlit secrets.toml file as GOOGLE_API_KEY.")
#     st.stop()

# # --- Function to check available models ---
# @st.cache_resource
# def get_available_gemini_models():
#     available_models = []
#     try:
#         for m in genai.list_models():
#             if "generateContent" in m.supported_generation_methods:
#                 available_models.append(m.name)
#     except Exception as e:
#         st.error(f"Error fetching model list: {e}")
#     return available_models

# # --- Sidebar: Model Selection ---
# st.sidebar.title(" Settings")
# available_models_list = get_available_gemini_models()

# selected_model_name = ""

# if available_models_list:
#     default_index = 0
#     for i, model_name in enumerate(available_models_list):
#         if "flash" in model_name:
#             default_index = i
#             break
    
#     selected_model_name = st.sidebar.selectbox(
#         "Choose AI Model:",
#         available_models_list,
#         index=default_index,
#         help="If one model fails, try selecting a different one from this list."
#     )
# else:
#     st.sidebar.error("Could not retrieve available models. Using fallback.")
#     selected_model_name = "models/gemini-pro"

# try:
#     model = genai.GenerativeModel(selected_model_name)
# except Exception as e:
#     st.error(f"Failed to initialize model: {selected_model_name}. Error: {e}")

# # --- Script Generation Function ---
# # 🔹 Updated to include tone + script_length_minutes
# def generate_script(topic, tone, script_length_minutes):
#     prompt_template = (
#         f"You are an AI assistant tasked with generating comprehensive YouTube video scripts.\n"
#         f"Generate a complete YouTube script for the topic: '{topic}'.\n\n"
#         f"Tone:\n"
#         f"- Adopt this tone consistently throughout the script: {tone}.\n"
#         f"- Match the energy, word choice, and pacing to this tone.\n\n"
#         f"Length & pacing:\n"
#         f"- Aim for a script suitable for approximately {script_length_minutes} minutes of spoken video.\n"
#         f"- Assume a natural speaking pace (about 130–160 words per minute).\n\n"
#         f"Structure the script exactly as follows, with clear headings for each section:\n\n"
#         f"**1. Hook (approx. 30 seconds):**\n"
#         f"   [Engaging opening that grabs viewer's attention and introduces the problem/question]\n\n"
#         f"**2. Introduction (Who you are and what viewers will learn):**\n"
#         f"   [Brief self-introduction, outline of what the video will cover and benefits]\n\n"
#         f"**3. Main Points (Use 3-4 clear, detailed sections):**\n"
#         f"   **Main Point 1: [Descriptive Title for Point 1]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 1]\n\n"
#         f"   **Main Point 2: [Descriptive Title for Point 2]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 2]\n\n"
#         f"   **Main Point 3: [Descriptive Title for Point 3]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 3]\n\n"
#         f"   **(Optional) Main Point 4: [Descriptive Title for Point 4]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 4]\n\n"
#         f"**4. Conclusion (Recap and Call to Action - CTA):**\n"
#         f"   [Brief summary of key takeaways, strong call to action for liking, subscribing, and commenting.]\n\n"
#         f"Ensure the script is long enough to cover the topic thoroughly, but concise, and always stay in the specified tone."
#     )

#     try:
#         response = model.generate_content(prompt_template)
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # --- Streamlit App Interface ---
# st.set_page_config(
#     page_title=" YouTube Script Generator",
#     page_icon="🎬",
#     layout="centered",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS
# st.markdown(
#     """
#     <style>
#     .stButton>button {
#         background-color: #FF4B4B;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 24px;
#         font-weight: bold;
#     }
#     .stTextInput>div>div>input {
#         border: 2px solid #FF4B4B;
#         border-radius: 8px;
#     }
#     h1 { color: #FF4B4B; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("YouTube Script Generator")

# # --- SESSION STATE: Initialize variable to store script ---
# if 'generated_script' not in st.session_state:
#     st.session_state['generated_script'] = ""

# # Topic input
# topic_input = st.text_input(
#     "Enter your video topic here:",
#     "Mastering Home Brewing: The Ultimate Guide to Perfect Coffee"
# )

# # 🔹 NEW: Tone dropdown
# tone_options = [
#     "Friendly & Conversational",
#     "Educational & Teacher-like",
#     "Motivational & Inspiring",
#     "Humorous & Fun",
#     "Dramatic & Storytelling",
#     "Calm & ASMR-style"
# ]
# selected_tone = st.selectbox(
#     "Choose the tone of your video:",
#     tone_options,
#     index=0
# )

# # 🔹 NEW: Script length slider (in minutes)
# script_length_minutes = st.slider(
#     "Approximate video length (in minutes):",
#     min_value=3,
#     max_value=30,
#     value=8,
#     help="This helps the AI decide how detailed and long the script should be."
# )

# # Button: Only responsible for GENERATION
# if st.button("Generate Script"):
#     if topic_input:
#         with st.spinner(f"🚀 Generating script using {selected_model_name}..."):
#             result = generate_script(topic_input, selected_tone, script_length_minutes)
#             st.session_state['generated_script'] = result
#     else:
#         st.warning("Please enter a topic to generate a script.")

# # --- DISPLAY LOGIC ---
# if st.session_state['generated_script']:
#     script_content = st.session_state['generated_script']
    
#     if script_content.startswith("Error:"):
#         st.error(script_content)
#         st.warning("Try selecting a different model from the sidebar.")
#     else:
#         st.subheader("✍️ Your Generated Script:")
#         st.markdown(script_content)
#         st.download_button(
#             label="Download Script",
#             data=script_content,
#             file_name=f"{topic_input.replace(' ', '_')}_script.md",
#             mime="text/markdown"
#         )

# st.markdown("---")
# st.markdown("Powered by Google Gemini and built with ❤️ using Streamlit.")

# import streamlit as st
# import google.generativeai as genai

# # =========================
# # PAGE CONFIG
# # =========================

# st.set_page_config(
#     page_title="YouTube Script Generator",
#     page_icon="🎬",
#     layout="centered",
#     initial_sidebar_state="expanded"
# )

# # =========================
# # SIMPLE LOGIN (NO DB)
# # =========================

# # Hard-coded demo users (username: password)
# USERS = {
#     "kanak": "1234",
#     "admin": "admin123",
#     "demo": "demo123"
# }

# if "user" not in st.session_state:
#     st.session_state["user"] = None

# def login_ui():
#     st.title("🔐 Login")

#     st.markdown(
#         """
#         <style>
#         .login-box {
#             max-width: 400px;
#             margin: 40px auto;
#             padding: 20px 25px;
#             border-radius: 12px;
#             border: 1px solid #eee;
#             box-shadow: 0 2px 8px rgba(0,0,0,0.05);
#             background: #ffffff;
#             text-align: center;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown('<div class="login-box">', unsafe_allow_html=True)
#     st.markdown("### Welcome to YouTube Script Generator")
#     st.write("Log in to generate scripts.")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if not username or not password:
#             st.warning("Please enter both username and password.")
#         elif username in USERS and USERS[username] == password:
#             st.session_state["user"] = {"username": username}
#             st.success(f"Welcome, {username}!")
#             st.experimental_rerun()
#         else:
#             st.error("Invalid username or password.")
#     st.markdown("</div>", unsafe_allow_html=True)

# # If not logged in → show only login and stop
# if st.session_state["user"] is None:
#     login_ui()
#     st.stop()

# # From here on, user is logged in
# user = st.session_state["user"]

# # =========================
# # GEMINI CONFIG
# # =========================

# try:
#     genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# except KeyError:
#     st.error("Google API Key not found. Please add it to your Streamlit secrets.toml file as GOOGLE_API_KEY.")
#     st.stop()

# @st.cache_resource
# def get_available_gemini_models():
#     available_models = []
#     try:
#         for m in genai.list_models():
#             if "generateContent" in m.supported_generation_methods:
#                 available_models.append(m.name)
#     except Exception as e:
#         st.error(f"Error fetching model list: {e}")
#     return available_models

# # =========================
# # SIDEBAR: MODEL + LOGOUT
# # =========================

# st.sidebar.title(" Settings")
# if user:
#     st.sidebar.write(f"Logged in as **{user.get('username', 'Guest')}**")
# else:
#     st.sidebar.write("Not logged in")


# if st.sidebar.button("Logout"):
#     st.session_state["user"] = None
#     st.experimental_rerun()

# available_models_list = get_available_gemini_models()
# selected_model_name = ""

# if available_models_list:
#     default_index = 0
#     for i, model_name in enumerate(available_models_list):
#         if "flash" in model_name:
#             default_index = i
#             break
    
#     selected_model_name = st.sidebar.selectbox(
#         "Choose AI Model:",
#         available_models_list,
#         index=default_index,
#         help="If one model fails, try selecting a different one from this list."
#     )
# else:
#     st.sidebar.error("Could not retrieve available models. Using fallback.")
#     selected_model_name = "models/gemini-pro"

# try:
#     model = genai.GenerativeModel(selected_model_name)
# except Exception as e:
#     st.error(f"Failed to initialize model: {selected_model_name}. Error: {e}")

# # =========================
# # SCRIPT GENERATION FUNCTION
# # =========================

# def generate_script(topic, tone, script_length_minutes):
#     prompt_template = (
#         f"You are an AI assistant tasked with generating comprehensive YouTube video scripts.\n"
#         f"Generate a complete YouTube script for the topic: '{topic}'.\n\n"
#         f"Tone:\n"
#         f"- Adopt this tone consistently throughout the script: {tone}.\n"
#         f"- Match the energy, word choice, and pacing to this tone.\n\n"
#         f"Length & pacing:\n"
#         f"- Aim for a script suitable for approximately {script_length_minutes} minutes of spoken video.\n"
#         f"- Assume a natural speaking pace (about 130–160 words per minute).\n\n"
#         f"Structure the script exactly as follows, with clear headings for each section:\n\n"
#         f"**1. Hook (approx. 30 seconds):**\n"
#         f"   [Engaging opening that grabs viewer's attention and introduces the problem/question]\n\n"
#         f"**2. Introduction (Who you are and what viewers will learn):**\n"
#         f"   [Brief self-introduction, outline of what the video will cover and benefits]\n\n"
#         f"**3. Main Points (Use 3-4 clear, detailed sections):**\n"
#         f"   **Main Point 1: [Descriptive Title for Point 1]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 1]\n\n"
#         f"   **Main Point 2: [Descriptive Title for Point 2]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 2]\n\n"
#         f"   **Main Point 3: [Descriptive Title for Point 3]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 3]\n\n"
#         f"   **(Optional) Main Point 4: [Descriptive Title for Point 4]**\n"
#         f"   [Detailed explanation, examples, tips related to Point 4]\n\n"
#         f"**4. Conclusion (Recap and Call to Action - CTA):**\n"
#         f"   [Brief summary of key takeaways, strong call to action for liking, subscribing, and commenting.]\n\n"
#         f"Ensure the script is long enough to cover the topic thoroughly, but concise, and always stay in the specified tone."
#     )

#     try:
#         response = model.generate_content(prompt_template)
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # =========================
# # CUSTOM CSS
# # =========================

# st.markdown(
#     """
#     <style>
#     .stButton>button {
#         background-color: #FF4B4B;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 24px;
#         font-weight: bold;
#     }
#     .stTextInput>div>div>input {
#         border: 2px solid #FF4B4B;
#         border-radius: 8px;
#     }
#     h1 { color: #FF4B4B; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # =========================
# # MAIN UI
# # =========================

# st.title("YouTube Script Generator")

# # --- SESSION STATE: Initialize variable to store script ---
# if "generated_script" not in st.session_state:
#     st.session_state["generated_script"] = ""

# # Topic input
# topic_input = st.text_input(
#     "Enter your video topic here:",
#     "Mastering Home Brewing: The Ultimate Guide to Perfect Coffee"
# )

# # Tone dropdown
# tone_options = [
#     "Friendly & Conversational",
#     "Educational & Teacher-like",
#     "Motivational & Inspiring",
#     "Humorous & Fun",
#     "Dramatic & Storytelling",
#     "Calm & ASMR-style"
# ]
# selected_tone = st.selectbox(
#     "Choose the tone of your video:",
#     tone_options,
#     index=0
# )

# # Script length slider (in minutes)
# script_length_minutes = st.slider(
#     "Approximate video length (in minutes):",
#     min_value=3,
#     max_value=30,
#     value=8,
#     help="This helps the AI decide how detailed and long the script should be."
# )

# # Generate button
# if st.button("Generate Script"):
#     if topic_input:
#         with st.spinner(f"🚀 Generating script using {selected_model_name}..."):
#             result = generate_script(topic_input, selected_tone, script_length_minutes)
#             st.session_state["generated_script"] = result
#     else:
#         st.warning("Please enter a topic to generate a script.")

# # Display script
# if st.session_state["generated_script"]:
#     script_content = st.session_state["generated_script"]
    
#     if script_content.startswith("Error:"):
#         st.error(script_content)
#         st.warning("Try selecting a different model from the sidebar.")
#     else:
#         st.subheader("✍️ Your Generated Script:")
#         st.markdown(script_content)
#         st.download_button(
#             label="Download Script",
#             data=script_content,
#             file_name=f"{topic_input.replace(' ', '_')}_script.md",
#             mime="text/markdown"
#         )

# st.markdown("---")
# st.markdown("Powered by Google Gemini and built with ❤️ using Streamlit.")


import streamlit as st
import google.generativeai as genai


st.set_page_config(
    page_title="YouTube Script Generator",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded"
)




if "users" not in st.session_state:
    # default demo users
    st.session_state["users"] = {
        "kanak": "1234",
        "admin": "admin123",
        "demo": "demo123"
    }

if "user" not in st.session_state:
    st.session_state["user"] = None

def auth_ui():
    st.title("🔐 Login")

    st.markdown(
        """
        <style>
        .login-box {
            max-width: 450px;
            margin: 40px auto;
            padding: 24px 28px;
            border-radius: 16px;
            border: 1px solid #2a2a2a;
            box-shadow: 0 2px 10px rgba(0,0,0,0.25);
            background: #111111;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

   
    st.markdown("### Welcome to YouTube Script Generator")
    st.write("Log in or sign up to generate scripts.")

    mode = st.radio("Mode", ["Login", "Sign Up"], horizontal=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if mode == "Sign Up":
        confirm_password = st.text_input("Confirm Password", type="password")

    users = st.session_state["users"]

    if mode == "Login":
        if st.button("Login"):
            if not username or not password:
                st.warning("Please enter both username and password.")
            elif username in users and users[username] == password:
                st.session_state["user"] = {"username": username}
                st.success(f"Welcome, {username}!")
                st.rerun()

            else:
                st.error("Invalid username or password.")

    else:  # Sign Up
        if st.button("Create Account"):
            if not username or not password or not confirm_password:
                st.warning("Please fill in all fields.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif username in users:
                st.error("That username is already taken.")
            else:
                # save in memory
                users[username] = password
                st.session_state["users"] = users
                st.success("Account created! You can now log in.")
    st.markdown("</div>", unsafe_allow_html=True)

# If not logged in → show only auth UI
if st.session_state["user"] is None:
    auth_ui()
    st.stop()

# From here on, user is logged in
user = st.session_state["user"]

# =========================
# GEMINI CONFIG
# =========================

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except KeyError:
    st.error("Google API Key not found. Please add it to your Streamlit secrets.toml file as GOOGLE_API_KEY.")
    st.stop()

@st.cache_resource
def get_available_gemini_models():
    available_models = []
    try:
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                available_models.append(m.name)
    except Exception as e:
        st.error(f"Error fetching model list: {e}")
    return available_models

# =========================
# SIDEBAR: MODEL + LOGOUT
# =========================

st.sidebar.title(" Settings")
user = st.session_state["user"]

# Sidebar safely shows login status
if user:
    st.sidebar.write(f"Logged in as **{user.get('username')}**")
else:
    st.sidebar.write("Not logged in")


if st.sidebar.button("Logout"):
    st.session_state["user"] = None
    st.rerun()

available_models_list = get_available_gemini_models()
selected_model_name = ""

if available_models_list:
    default_index = 0
    for i, model_name in enumerate(available_models_list):
        if "flash" in model_name:
            default_index = i
            break
    
    selected_model_name = st.sidebar.selectbox(
        "Choose AI Model:",
        available_models_list,
        index=default_index,
        help="If one model fails, try selecting a different one from this list."
    )
else:
    st.sidebar.error("Could not retrieve available models. Using fallback.")
    selected_model_name = "models/gemini-pro"

try:
    model = genai.GenerativeModel(selected_model_name)
except Exception as e:
    st.error(f"Failed to initialize model: {selected_model_name}. Error: {e}")

# =========================
# SCRIPT GENERATION FUNCTION
# =========================

def generate_script(topic, tone, script_length_minutes):
    prompt_template = (
        f"You are an AI assistant tasked with generating comprehensive YouTube video scripts.\n"
        f"Generate a complete YouTube script for the topic: '{topic}'.\n\n"
        f"Tone:\n"
        f"- Adopt this tone consistently throughout the script: {tone}.\n"
        f"- Match the energy, word choice, and pacing to this tone.\n\n"
        f"Length & pacing:\n"
        f"- Aim for a script suitable for approximately {script_length_minutes} minutes of spoken video.\n"
        f"- Assume a natural speaking pace (about 130–160 words per minute).\n\n"
        f"Structure the script exactly as follows, with clear headings for each section:\n\n"
        f"**1. Hook (approx. 30 seconds):**\n"
        f"   [Engaging opening that grabs viewer's attention and introduces the problem/question]\n\n"
        f"**2. Introduction (Who you are and what viewers will learn):**\n"
        f"   [Brief self-introduction, outline of what the video will cover and benefits]\n\n"
        f"**3. Main Points (Use 3-4 clear, detailed sections):**\n"
        f"   **Main Point 1: [Descriptive Title for Point 1]**\n"
        f"   [Detailed explanation, examples, tips related to Point 1]\n\n"
        f"   **Main Point 2: [Descriptive Title for Point 2]**\n"
        f"   [Detailed explanation, examples, tips related to Point 2]\n\n"
        f"   **Main Point 3: [Descriptive Title for Point 3]**\n"
        f"   [Detailed explanation, examples, tips related to Point 3]\n\n"
        f"   **(Optional) Main Point 4: [Descriptive Title for Point 4]**\n"
        f"   [Detailed explanation, examples, tips related to Point 4]\n\n"
        f"**4. Conclusion (Recap and Call to Action - CTA):**\n"
        f"   [Brief summary of key takeaways, strong call to action for liking, subscribing, and commenting.]\n\n"
        f"Ensure the script is long enough to cover the topic thoroughly, but concise, and always stay in the specified tone."
    )

    try:
        response = model.generate_content(prompt_template)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# =========================
# CUSTOM CSS
# =========================

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border: 2px solid #FF4B4B;
        border-radius: 8px;
    }
    h1 { color: #FF4B4B; }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# MAIN UI
# =========================

# =========================
# MAIN UI – TABS (Generate | History | Profile)
# =========================

st.title("YouTube Script Generator")

# --- SESSION STATE ---
if "generated_script" not in st.session_state:
    st.session_state["generated_script"] = ""

if "history" not in st.session_state:
    st.session_state["history"] = []   # list of dicts

tab_generate, tab_history = st.tabs(
    [" Generate Script", " History"]
)

# -----------------------------------------
# 1️⃣ TAB: GENERATE SCRIPT
# -----------------------------------------
with tab_generate:

    topic_input = st.text_input(
        "Enter your video topic here:",
        "Mastering Home Brewing: The Ultimate Guide to Perfect Coffee"
    )

    # Tone dropdown
    tone_options = [
        "Friendly & Conversational",
        "Educational & Teacher-like",
        "Motivational & Inspiring",
        "Humorous & Fun",
        "Dramatic & Storytelling",
        "Calm & ASMR-style"
    ]
    selected_tone = st.selectbox("Choose the tone of your video:", tone_options)

    # Video length slider
    script_length_minutes = st.slider(
        "Approximate video length (in minutes):",
        min_value=3, max_value=30, value=8
    )

    # Generate button
    if st.button("Generate Script"):
        if topic_input:
            with st.spinner(f"🚀 Generating script using {selected_model_name}..."):
                result = generate_script(topic_input, selected_tone, script_length_minutes)
                st.session_state["generated_script"] = result

                # SAVE TO HISTORY (if not error)
                if not result.startswith("Error"):
                    st.session_state["history"].append({
                        "topic": topic_input,
                        "tone": selected_tone,
                        "length": script_length_minutes,
                        "script": result
                    })
        else:
            st.warning("Please enter a topic to generate a script.")

    # Display generated script
    if st.session_state["generated_script"]:
        st.subheader("✍️ Your Generated Script")
        st.markdown(st.session_state["generated_script"])

        st.download_button(
            label="Download Script",
            data=st.session_state["generated_script"],
            file_name=f"{topic_input.replace(' ', '_')}.md",
            mime="text/markdown"
        )

# -----------------------------------------
# 2️⃣ TAB: HISTORY
# -----------------------------------------
with tab_history:
    st.subheader("📜 Your Script History")

    history = st.session_state["history"]

    if not history:
        st.info("No history yet. Generate a script first!")
    else:
        for idx, item in enumerate(history):
            with st.expander(f"{item['topic']}  |  {item['tone']} | {item['length']} min"):
                st.markdown(item["script"])
                
                st.download_button(
                    label="Download",
                    data=item["script"],
                    file_name=f"{item['topic'].replace(' ','_')}_history.md",
                    mime="text/markdown",
                    key=f"dl_{idx}"
                )
                
                if st.button("🗑 Delete", key=f"delete_{idx}"):
                    history.pop(idx)
                    st.rerun()

# -----------------------------------------


st.markdown("---")


