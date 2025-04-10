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
   ```
2. Run MapReduce Job:
Execute the MapReduce job on Hadoop:

bash
Copy
hadoop jar mapper_analysis.jar /user/hadoop/pokec_data /user/hadoop/output_data
3. View Results:
After the job completes, retrieve the output from HDFS:

bash
Copy
hdfs dfs -cat /user/hadoop/output_data/part-*
Hadoop Cloud Tools
In the cloud, you can use several tools and services to enhance Hadoop's capabilities and streamline the process:

Amazon EMR (Elastic MapReduce): A cloud-native service to run big data frameworks such as Hadoop, Spark, and Hive.

Google Cloud Dataproc: A fully managed cloud service for running Hadoop and Spark clusters.

Azure HDInsight: A fully-managed cloud service for running Apache Hadoop and Spark clusters on Microsoft Azure.

Project Structure
The project directory is organized as follows:

graphql
Copy
Cloud-Computing-Pokec-Project/
│
├── map_scripts/                     # Folder containing MapReduce scripts
│   ├── color_completion_mapper.py    # Mapper script for color completion
│   ├── color_completion_reducer.py   # Reducer script for color completion
│   ├── days_since_registration.py   # Script for calculating days since registration
│   ├── encode_variables.py          # Script for encoding variables
│   ├── mapper_analysis.py           # Main analysis for Mapper logic
│   ├── mapper_correlation.py        # Script for correlation analysis
│   ├── multi_label.py               # Handle multi-label data
│   ├── normalize.py                 # Normalization script for features
│   ├── outlier_handler.py           # Script for handling outliers
│   ├── pokec_classifier.py          # Classifier logic for the Pokec dataset
│   └── reducer_analysis.py          # Main analysis for Reducer logic
│
├── Data/                             # Folder for dataset (subset if needed)
│   ├── pokec_profiles_sample.csv     # Sample of Pokec user profile data (optional)
│   └── README.txt                   # Description of dataset and how to access full data
│
├── Output/                           # Folder for storing output results
│   ├── results.txt                  # Output result file
│   └── predictions.csv              # Predicted values for completion_percentage
│
├── README.md                        # Project documentation (README file)
├── requirements.txt                 # List of dependencies (for Python scripts)
└── LICENSE                          # Optional: License file for open-source
Conclusion
This project demonstrates the application of MapReduce and Hadoop for large-scale data analysis. By processing and analyzing the Pokec Social Network Dataset, I was able to build predictive models and uncover insights into user behaviors and profile completion rates. The project successfully leveraged Hadoop's distributed computing capabilities to handle large datasets and perform complex data analysis tasks efficiently.

Feel free to reach out if you have any questions or feedback!

yaml
Copy

---

### **Updates**:
- **Project Structure** section added, detailing the organization of the files and folders.
- **Conclusion** summarizes the key outcomes of the project and its goals.

