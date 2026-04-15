import streamlit as st

st.set_page_config(page_title="Viktoriya Li Portfolio", layout="wide")

st.title("Viktoriya Li")
st.subheader("Portfolio")
st.write(
    """
    My projects focus on creating structured systems, dashboards, and interactive tools that translate 
data into something visual and meaningful. I am especially interested in working at the intersection 
of technology, data, and user experience.
    """
)

st.markdown("---")

st.header("Projects")

project = st.selectbox(
    "Choose a project",
    [
        "Amsterdam Waste Management Dashboard",
        "Urban Tree Placement Simulation",
        "Virtual Dressing Room Concept",
        "Interactive Privacy Dashboard",
    ],
)

if project == "Amsterdam Waste Management Dashboard":
    st.subheader("Amsterdam Waste Management Dashboard")
    st.write(
        """
        This project focused on designing a more centralized system for the municipality to better manage urban waste data. 

The goal was not only to organize the data, but to make it easier to understand and act on. 
Since poorly managed waste and visible litter can negatively affect people’s well-being and perception of their environment, 
we wanted to create a system that helps identify problem areas and supports faster, more informed decisions.

The result is a Streamlit dashboard that visualizes key patterns across neighborhoods and makes complex operational data 
more accessible for decision-making.
        """
    )
    st.markdown("**My contribution**")
    st.write(
        """
        I worked on turning raw municipal-style data into a structured, visual dashboard
        with clear controls and user-friendly views.
        """
    )
    # st.markdown("**Why it is relevant**")
    # st.write(
    #     """
    #     This project shows dashboard design, Python-based data workflows,
    #     and building interfaces for non-technical users.
    #     """
    # )
    # st.markdown("**Tools used**")
    # st.write("Python, Streamlit, pandas, Plotly")
    # st.image("img/poo.png", caption="Tools used")
    st.image("img/Waste.jpg", caption="Waste dashboard screenshot")
    st.image("img/poo.png", caption="Tools used")

elif project == "Urban Tree Placement Simulation":
    st.subheader("Urban Tree Placement Simulation")
    st.write(
        """
       This project was carried out in collaboration with the Gemeente Amsterdam, with the goal of exploring how satellite data 
could be used to improve the city’s sustainability. We focused on simulating how tree placement and species selection 
could reduce PM2.5 and PM10 concentrations across Amsterdam.

We worked with environmental and spatial data to model how different types of trees and their locations could influence 
air quality. The project involved building a simulation and translating the results into visual outputs that could help 
identify where interventions would be most effective.

The aim was not only to analyze the data, but to make the results understandable and usable for decision-making. 
By combining simulation and visualization, we explored how data-driven insights could support more sustainable 
urban planning.
        """
    )
    st.markdown("**My contribution**")
    st.write(
        """
        I worked on visualization, and translating outputs
        into a dashboard concept for city planners. Proposed the main idea. 
        """
    )
    # st.markdown("**Why it is relevant**")
    # st.write(
    #     """
    #     This project shows systems thinking, simulation work,
    #     and making complex outputs easier to understand visually.
    #     """
    # )
    # st.markdown("**Tools used**")
    # st.write("Python, Plotly, simulation, data visualization")
    st.image("img/DSP.png", caption="Urban tree simulation project")

elif project == "Virtual Dressing Room Concept":
    st.subheader("Virtual Dressing Room Concept")
    st.write(
        """
        This project focused on designing a concept for an interactive system aimed at reducing clothing waste. 
The idea was to support users in making better clothing decisions through features such as body scanning, 
virtual try-on, and digital wardrobe management.

We explored how different technologies could be combined into one system, including computer vision for 
body measurements and recommendation systems for suggesting outfits or purchases. A large part of the 
project was focused on designing the overall system structure and user flow, ensuring that the experience 
would feel intuitive and useful rather than complex.

The goal was to reduce unnecessary purchases by helping users better understand what fits them, what they 
already own, and how new items would integrate into their wardrobe. This project reflects my interest in 
building systems that combine technical ideas with user-centered design and visual interaction.
        """
    )
    st.markdown("**My contribution**")
    st.write(
        """
        I worked on the system design, user flow, and the idea of making
        a technical concept intuitive and useful for users.
        """
    )
    # st.markdown("**Why it is relevant**")
    # st.write(
    #     """
    #     This project shows creative systems thinking, UX awareness,
    #     and interest in technology that supports visual interaction.
    #     """
    # )
    # st.markdown("**Tools used**")
    # st.write("System design, UX, user flow, concept development")
    st.image("img/IIS_Poster.png", caption="Virtual dressing room concept")

elif project == "Interactive Privacy Dashboard":
    st.subheader("Interactive Privacy Dashboard")
    st.link_button(
    "View Figma Prototype",
    "https://www.figma.com/proto/rHvFLZqXNiCl758o5sr7EC/Dashboard?node-id=30-300&t=kiqVqBVIsFJuvR3D-1&scaling=min-zoom&content-scaling=fixed&page-id=32%3A17&starting-point-node-id=30%3A300"
)
    st.write(
        """
        This project was developed as part of my master’s thesis and focused on how users understand cookies, 
tracking, and online privacy mechanisms. The goal was to explore how interactive dashboards can improve 
users’ awareness and understanding of how their data is collected and used online.

I designed a dashboard that presents information about cookies and tracking in a more transparent and 
accessible way, combining explanations with interactive elements and real examples. A key focus of the 
project was on usability — making complex and often hidden processes easier to understand for everyday users.

The results of the study were analyzed using Python, allowing me to evaluate how users interacted with 
the dashboard and how their understanding and confidence changed. This project reflects my interest in 
building tools that make complex systems more understandable and user-friendly.
        """
    )
    # st.markdown("**My contribution**")
    # st.write(
    #     """
    #     I focused on making complex information clearer through interactive content
    #     and more transparent interface design.
    #     """
    # )
    # st.markdown("**Why it is relevant**")
    # st.write(
    #     """
    #     This project shows interface thinking, usability focus,
    #     and interest in how people understand and navigate systems.
    #     """
    # )
    # st.markdown("**Tools used**")
    # st.write("UX, dashboard design, interaction design")
    st.image("img/dash1.png", caption="Privacy dashboard project")

st.markdown("---")
st.header("Contact")
st.write("Email: li.viiktoriiya@gmail.com")
