# Retail Sales Data Pipeline with Azure

## Project Overview
This project develops a scalable and automated data pipeline for transforming and analyzing retail sales data using Azure services. It processes raw data from an on-premise SQL Server, performs multi-level data transformation, and visualizes insights in Power BI.

## Architecture
- **Data Ingestion**: Azure Data Factory pulls data from on-premise SQL Server to Azure Data Lake Gen2.
- **Data Transformation**: Implemented a Bronze-Silver-Gold transformation architecture in Azure Databricks.
- **Data Loading**: Transformed data is loaded into Azure Synapse Analytics.
- **Reporting**: Data from Synapse is visualized in Power BI dashboards.
- **CI/CD**: End-to-end deployment is automated with CI/CD pipeline in Azure DevOps.

## Technologies Used
- **Azure Data Factory**
- **Azure Data Lake Gen2**
- **Azure Databricks**
- **Azure Synapse Analytics**
- **Power BI**
- **CI/CD**: Automated with Azure DevOps.

## Setup Instructions
1. Clone the repository.
2. Set up an Azure environment with the required services (Data Factory, Data Lake Gen2, Databricks, Synapse).
3. Configure Azure Data Factory pipeline (see `/data-pipeline` folder).
4. Deploy CI/CD pipeline configuration for automated deployment (see `/ci-cd` folder).

## Data Pipeline
- **Bronze Layer**: Raw data ingestion from SQL Server.
- **Silver Layer**: Cleansed and structured data in Databricks.
- **Gold Layer**: Aggregated data for analysis and reporting.

## CI/CD Pipeline
The CI/CD pipeline automates deployment using version-controlled configurations. This ensures that each change is tested and deployed seamlessly in the Azure environment.
