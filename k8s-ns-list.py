# 1st version of code : define ns name yhen showing svc

# import streamlit as st
# from kubernetes import client, config
#
# # Load the Kubernetes configuration
# config.load_kube_config()
#
# # Create a Kubernetes API client
# api_client = client.CoreV1Api()
#
#
# # Define a function to list all services in a namespace
# def list_services(namespace):
#     services = api_client.list_namespaced_service(namespace)
#     return services
#
#
# # Create a Streamlit web app
# def app():
#     # Set the app title
#     st.title("Kubernetes Services Explorer")
#
#     # Add a dropdown to select the namespace
#     namespace = st.selectbox("Select Namespace", ["default", "kube-system", "my-namespace"])
#
#     # Add a button to retrieve the services in the selected namespace
#     if st.button("List Services"):
#         # Call the function to list the services
#         services = list_services(namespace)
#
#         # Display the services in a table
#         st.write("Services in Namespace:", namespace)
#         st.write(services)
#
#
# # Run the app
# if __name__ == '__main__':
#     app()

# 2nd version of ns seleted showing svc without button click
# import streamlit as st
# from kubernetes import client, config
#
# # Load Kubernetes config
# config.load_kube_config()
#
# # Create Kubernetes API client
# api_client = client.CoreV1Api()
#
# # Retrieve all namespaces
# namespaces = [ns.metadata.name for ns in api_client.list_namespace().items]
#
# # Create Streamlit app
# st.title("Kubernetes Services")
# selected_namespace = st.selectbox("Select a namespace", namespaces)
#
# # Retrieve all services in the selected namespace
# services = api_client.list_namespaced_service(selected_namespace).items
#
# # Display the services in a table
# st.write(f"Services in namespace '{selected_namespace}':")
# if not services:
#     st.write("No services found.")
# else:
#     for svc in services:
#         st.write(f"- {svc.metadata.name}")

import streamlit as st
from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.CoreV1Api()


# Define a function to list all services in a namespace
def list_services(namespace):
    services = api_client.list_namespaced_service(namespace)
    return services


# Create a Streamlit web app
def app():
    # Set the app title
    st.title("Kubernetes Services Explorer")

    # Get all namespaces in the config file
    all_namespaces = [ns.metadata.name for ns in api_client.list_namespace().items]

    # Add a dropdown to select the namespace
    namespace = st.selectbox("Select Namespace", ["All"] + all_namespaces)

    # Add a button to retrieve the services in the selected namespace
    if st.button("List Services"):
        if namespace == "All":
            # Get all services in all namespaces
            services = api_client.list_service_for_all_namespaces().items
        else:
            # Call the function to list the services in the selected namespace
            services = list_services(namespace).items

        # Display the services in a table
        st.write("Services in Namespace:", namespace)
        for svc in services:
            st.write("- Name:", svc.metadata.name)


# Run the app
if __name__ == '__main__':
    app()
