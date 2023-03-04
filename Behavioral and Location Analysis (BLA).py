import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Define a function to perform BLA on a transaction
def perform_bla(transaction_data):
    # Preprocess the transaction data
    processed_data = preprocess_transaction_data(transaction_data)
    
    # Cluster the transaction data using K-means algorithm
    clustered_data = cluster_transaction_data(processed_data)
    
    # Return the cluster labels for the transaction
    return clustered_data

# Define a function to preprocess the transaction data
def preprocess_transaction_data(transaction_data):
    # Convert the transaction data to a Pandas DataFrame
    df = pd.DataFrame(transaction_data)
    
    # Remove any unnecessary columns
    df = df.drop(['transaction_id', 'user_id'], axis=1)
    
    # Scale the data to normalize the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    
    # Return the preprocessed data
    return scaled_data

# Define a function to cluster the transaction data using K-means algorithm
def cluster_transaction_data(processed_data):
    # Define the number of clusters
    n_clusters = 3
    
    # Create a K-means clustering model
    model = KMeans(n_clusters=n_clusters)
    
    # Fit the model to the processed data
    model.fit(processed_data)
    
    # Get the cluster labels for the transaction
    labels = model.predict(processed_data)
    
    # Return the cluster labels
    return labels
