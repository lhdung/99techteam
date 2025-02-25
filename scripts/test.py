from diagram_as_code import Diagram, Cluster, Node

def main():
    # Tạo diagram với tiêu đề và file output (ví dụ: trading_system.png)
    with Diagram("Highly Available Trading System", output="trading_system.png"):
        
        # Cluster: Client Access Layer
        with Cluster("Client Access Layer"):
            api_gateway = Node("API Gateway", icon="aws/network/apigateway")
            websocket_api = Node("WebSocket API", icon="aws/network/apigateway")
            alb = Node("Application Load Balancer", icon="aws/network/alb")
            # Kết nối từ API Gateway đến WebSocket API và ALB
            api_gateway.connect(websocket_api)
            api_gateway.connect(alb)
        
        # Cluster: Trading System Backend
        with Cluster("Trading System Backend"):
            # Cluster: Order Processing
            with Cluster("Order Processing"):
                order_engine = Node("Order Matching Engine", icon="aws/compute/ecs")
                event_bus = Node("Event Streaming (Kafka)", icon="custom/kafka")
                order_engine.connect(event_bus)
            
            # Cluster: Data Services
            with Cluster("Data Services"):
                primary_db = Node("Primary DB", icon="aws/database/aurora")
                replica_db = Node("Read Replica", icon="aws/database/aurora")
                cache = Node("Redis Cache", icon="aws/elasticache/redis")
                s3_storage = Node("S3 Storage", icon="aws/storage/s3")
                order_engine.connect(primary_db)
                order_engine.connect(cache)
                order_engine.connect(s3_storage)
                # Kết nối cơ sở dữ liệu chính với read replica (dotted line)
                primary_db.connect(replica_db, style="dotted")
            
            # Cluster: Notification & Messaging
            with Cluster("Notification & Messaging"):
                sqs_queue = Node("Trade Queue", icon="aws/integration/sqs")
                sns_service = Node("Notification Service", icon="aws/integration/sns")
                order_engine.connect(sqs_queue)
                order_engine.connect(sns_service)
            
            # Cluster: Security & Monitoring
            with Cluster("Security & Monitoring"):
                waf = Node("WAF", icon="aws/security/waf")
                shield = Node("Shield", icon="aws/security/shield")
                waf.connect(shield)
                shield.connect(alb)
        
        # Kết nối lớp client tới hệ thống backend (Order Matching Engine)
        api_gateway.connect(order_engine)

if __name__ == '__main__':
    main()
