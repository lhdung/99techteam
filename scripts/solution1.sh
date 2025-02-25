#bin/bash

grep '"symbol": "TSLA", "side": "sell"' ../solutions/problem1/transaction-log.txt | jq -r '.order_id' | xargs -I {} curl -s "https://example.com/api/{}" >> output.txt
