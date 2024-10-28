# Retail Sales Data Pipeline with Azure

## Project Overview
This project develops a scalable and automated data pipeline for transforming and analyzing retail sales data using Azure services. It processes raw data from an on-premise SQL Server, performs multi-level data transformation, and visualizes insights in Power BI.

## Architecture
- **Data Ingestion**: Azure Data Factory pulls data from on-premise SQL Server to Azure Data Lake Gen2.
- **Data Transformation**: Implemented a Bronze-Silver-Gold transformation architecture in Azure Databricks.
- **Data Loading**: Transformed data is loaded into Azure Synapse Analytics.
- **Reporting**: Data from Synapse is visualized in Power BI dashboards.
- **CI/CD**: End-to-end deployment is automated with CI/CD pipeline in Azure DevOps.
  
![image](https://github.com/user-attachments/assets/11a8536b-ee0d-4b28-b6aa-be3c670b5ffa)


## Technologies Used
- **Azure Data Factory**
- **Azure Data Lake Gen2**
- **Azure Databricks**
- **Azure Synapse Analytics**
- **Power BI**
- **CI/CD**: Automated with Azure DevOps.
  
## Data Pipeline
- **Bronze Layer**: Raw data ingestion from SQL Server.
- **Silver Layer**: Cleansed and structured data in Databricks.
- **Gold Layer**: Aggregated data for analysis and reporting.

## CI/CD Pipeline
The CI/CD pipeline automates deployment using version-controlled configurations. This ensures that each change is tested and deployed seamlessly in the Azure environment.

![Report Image](https://github.com/user-attachments/assets/ba2523a3-c9fc-48c2-b899-da3e84c4b7f3)
