from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() # Path to the current file
css_file = current_dir / "styles" / "main.css" # Path to the CSS file
resume_file = current_dir / "assets" / "resume.pdf" # Path to the resume file
profile_pic = current_dir / "assets" / "me.jpg" # Path to the profile picture
