# jira_lookup
Search for Apache Hive jiras with matching keywords

Clone the py file `search_jira_noauth.py` and run it as follows:
```
❯ python3 search_jira_noauth.py
Enter the string to search for in bug descriptions: MaxMessageSize
Found 2 bugs with matching string:
HIVE-27114: Provide a configurable filter for removing useless properties in Partition objects from listPartitions HMS Calls
HIVE-26633: Make thrift max message size configurable
