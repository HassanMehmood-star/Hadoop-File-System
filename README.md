# Cloud Computing Project: Pokec Social Network Dataset on Hadoop

## **Overview**
This project utilizes the **Pokec Social Network Dataset** to predict the **completion_percentage** of user profiles and perform clustering analysis using **Hadoop MapReduce** on **Hadoop Distributed File System (HDFS)**.

The project is designed to process large-scale data, analyze user features, investigate correlations, and implement machine learning models using Hadoop's distributed framework.

## **Features**
- **MapReduce-based Classifier**: Predicts **completion_percentage** of user profiles.
- **Data Analysis**: Investigates correlations between **completion_percentage** and features like **age**, **gender**, and **region**.
- **Clustering**: Applies **K-means clustering** to segment users based on demographic features.
- **Feature Encoding**: Encodes categorical variables like **gender**, **region**, and **eye_color**.
- **Data Processing**: Handles sparsity, outliers, and multi-label columns.

## **Prerequisites**
Before running the project, ensure you have the following installed and configured:

### 1. **Hadoop Installation**
   - [Install Hadoop](http://hadoop.apache.org/docs/r3.2.1/hadoop-project-dist/hadoop-common/SingleCluster.html) on your local machine or set up a Hadoop cluster.
   - **Hadoop Version**: 3.x or above is recommended.
   - Ensure **HDFS** is properly configured and running.

### 2. **Java**
   - Install **Java** (JDK 1.8 or higher) since Hadoop requires Java.
   - Verify by running: 
     ```bash
     java -version
     ```

### 3. **Python** (if using Python scripts for data processing)
   - Install **Python 3.x** if needed for pre-processing or post-processing tasks.
   - Install necessary Python packages (use **requirements.txt** if applicable).

## **Configuration**

### 1. **HDFS Configuration**:
   - Set up **HDFS** on your local or cloud-based Hadoop environment.
   - Make sure **namenode** and **datanode** are configured properly.
   - Check the status of HDFS with:
     ```bash
     hdfs dfsadmin -report
     ```

### 2. **MapReduce Configuration**:
   - Ensure your MapReduce job is configured with the appropriate **input** and **output** directories in HDFS.

   Example:
   - Input path: `/user/hadoop/pokec_data`
   - Output path: `/user/hadoop/output_data`

### 3. **Java Class Configuration**:
   - Compile the MapReduce Java classes:
     ```bash
     javac -classpath `hadoop classpath` -d /path/to/output_mapper/ /path/to/mapper_analysis.java
     ```
   - Create the JAR file:
     ```bash
     jar -cvf mapper_analysis.jar -C /path/to/output_mapper/ .
     ```

## **Running the Project**

### 1. **Upload Data to HDFS**:
   Before running the MapReduce job, upload the **Pokec Social Network Dataset** to HDFS:
   ```bash
   hdfs dfs -put pokec_data.csv /user/hadoop/pokec_data
