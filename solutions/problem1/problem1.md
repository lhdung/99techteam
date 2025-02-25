# README

## Task Overview

This project involves processing a transaction log to extract Order IDs of TSLA sell transactions and sending HTTP GET requests to an API endpoint for each Order ID. The API responses are stored in an output file.

## Objective

- Extract Order IDs from `transaction-log.txt` where `symbol` is `TSLA` and `side` is `sell`.
- Send an HTTP GET request to `https://example.com/api/:order_id` for each extracted Order ID.
- Write the API response to `output.txt`.

## Prerequisites

Ensure you have the following installed:

- `jq`: A command-line JSON processor
- `curl`: A command-line tool for making HTTP requests
- `grep`: A tool for searching text
- `xargs`: A command-line utility to build and execute commands

## Usage

Run the following command in your terminal:

```bash
grep '"symbol": "TSLA", "side": "sell"' transaction-log.txt | jq -r '.order_id' | xargs -I {} curl -s "https://example.com/api/{}" >> output.txt
```

## Explanation

1. `grep` filters lines containing `"symbol": "TSLA"` and `"side": "sell"`.
2. `jq` extracts the `order_id` from the filtered JSON data.
3. `xargs` runs `curl` for each `order_id`, sending HTTP GET requests.
4. The API responses are appended to `output.txt`.

## Output

The output file `output.txt` will contain the API responses for all TSLA sell orders.

## Example Data

Sample transaction log entry:

```json
{"order_id": "12346", "symbol": "TSLA", "quantity": 50, "price": 890.15, "side": "sell", "timestamp": "2025-02-18T09:16:10Z"}
```

Corresponding API request:

```bash
curl -s "https://example.com/api/12346"
```

## Notes

- Ensure `transaction-log.txt` is available in the current directory.
- `output.txt` will store API responses. Use `cat output.txt` to view them.
- The command is optimized for efficiency in a single execution line.


