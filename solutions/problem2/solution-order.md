# README

## Building Castle In The Cloud
## Objective

# Stock Price System Architecture

This document outlines the architecture of a **Stock Price Change Alert** system designed for a trading or financial platform. The system handles buy and sell orders, matches them, processes transactions, and stores data for analytics and accounting purposes.

---

## Components of the Architecture

### 1. **Client Update Service**
Handles client updates, particularly buy orders.

- **BUY Queues**: Queues for specific stock symbols (e.g., AMZN, CSCO, AAPL) where buy orders are placed.
  - Example Queues:
    - AMZN
    - CSCO
    - AAPL

---

### 2. **Send Order Status**
Manages the status of orders after processing.

- **No Match Buy Orders**: Orders that could not be matched with a sell order.
- **Result Topics**: Topics where order processing results (e.g., matched or unmatched) are published.
- **Match (Transaction)**: Orders that are successfully matched and result in a transaction.
- **No Match Other**: Orders that do not match for reasons other than the absence of a sell order.

---

### 3. **Transactions**
Core processing of transactions.

- **SMST**: Likely a system or service for managing stock market transactions.
- **SMS**: Could refer to a Simple Messaging Service or notification system for transaction updates.
- **Matching Engine**: Matches buy and sell orders.
- **EKS**: Amazon Elastic Kubernetes Service for container orchestration.
- **Router**: Routes transactions to the appropriate queues or services.
- **SELI Queues**: Queues for sell orders (e.g., AMZN, CSCO, AAPL).

---

### 4. **No Match Sell Orders**
Handles sell orders that do not find a match.

- **Lambda**: AWS Lambda functions for processing unmatched sell orders.
- **Update Order Status**: Updates the status of unmatched sell orders.
- **Kinesis Firehose**: Streams data to downstream services.
- **Financial Accounting**: Tracks financial transactions and updates accounting records.
- **Data Lake**: Stores raw data for future analysis.
- **Data Analytics**: Processes and analyzes data stored in the data lake.

---

### 5. **Save Orders**
Persists order data for future use.

- **DynamoDB**: NoSQL database for storing order details.
- **Kinesis Data Stream**: Real-time data streaming service for capturing and processing order data.

---

## Key Features

1. **Order Matching**: The system uses a matching engine to pair buy and sell orders, ensuring efficient transaction processing.
2. **Scalability**: Components like EKS, Lambda, and Kinesis ensure the system can scale to handle high volumes of orders.
3. **Real-Time Processing**: Kinesis Data Stream and Firehose enable real-time data processing and analytics.
4. **Durability and Storage**: DynamoDB and Data Lake provide durable storage for order data and financial records.
5. **Asynchronous Processing**: Queues (BUY and SELI) and Lambda functions allow for asynchronous processing of orders, improving system responsiveness.

---

## System Flow

1. **Client Update Service** receives buy orders and places them in the appropriate BUY Queues.
2. The **Matching Engine** processes buy and sell orders from the queues and attempts to match them.
3. Matched orders result in transactions, while unmatched orders are routed to the appropriate result topics or queues.
4. Unmatched sell orders are processed by Lambda functions and sent to Kinesis Firehose for further processing.
5. Order data is saved in DynamoDB and streamed via Kinesis Data Stream for real-time analytics.
6. Financial accounting and data analytics systems use the processed data for reporting and insights.

---

## Diagram (Mermaid)

```mermaid
graph TD
    A[Client Update Service] --> B[BUY Queues]
    B --> C[Matching Engine]
    C --> D[Match (Transaction)]
    C --> E[No Match Buy Orders]
    C --> F[No Match Sell Orders]
    D --> G[Transactions]
    E --> H[Result Topics]
    F --> I[Lambda]
    I --> J[Update Order Status]
    J --> K[Kinesis Firehose]
    K --> L[Financial Accounting]
    K --> M[Data Lake]
    M --> N[Data Analytics]
    G --> O[Save Orders]
    O --> P[DynamoDB]
    O --> Q[Kinesis Data Stream]