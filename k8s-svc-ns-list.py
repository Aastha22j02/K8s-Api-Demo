import streamlit as st
from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.CoreV1Api()


# Define a function to list all services in a namespace
def list_services(namespace):
    services = api_client.list_namespaced_service(namespace).items
    return services


# Create a Streamlit web app
def app():
    # Set the app title
    st.title("Kubernetes Services Explorer")

    # Add a dropdown to select the namespace
    all_namespaces = [ns.metadata.name for ns in api_client.list_namespace().items]
    namespace = st.selectbox("Select Namespace", ["All"] + all_namespaces)

    # Add a button to retrieve the services in the selected namespace
    if st.button("List Services"):
        if namespace == "All":
            # Get all services in all namespaces
            services = api_client.list_service_for_all_namespaces().items
        else:
            # Call the function to list the services in the selected namespace
            services = list_services(namespace)

        # Display the services in a table
        st.write("Services in Namespace:", namespace)
        for svc in services:
            st.write("- Name:", svc.metadata.name)
            st.write("  Type:", svc.spec.type)
            st.write("  Cluster IP:", svc.spec.cluster_ip)
            st.write("  Ports:")
            for port in svc.spec.ports:
                st.write("    - Name:", port.name)
                st.write("      Port:", port.port)
                st.write("      Protocol:", port.protocol)


# Run the app
if __name__ == '__main__':
    app()
