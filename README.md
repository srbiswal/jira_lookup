# jira_lookup
Search for Apache Hive jiras with matching keywords or class name from the error stack.

Clone the py file `search_jira_noauth.py` and run it as follows:
```
❯ python3 search_jira_noauth.py
Enter the string to search for in bug descriptions: org.apache.hive.com.esotericsoftware.kryo.uti1.DefaultClassResolver.readName
Found 1 bugs with matching string:
HIVE-25487: Caused by :org.apache.hive.com.esotericsoftware.kryo.KryoException:Unable  to find class :S_4
