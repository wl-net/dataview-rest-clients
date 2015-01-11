Dataview REST API Python Requests client
========================================

Usage Instructions
----

```
rest = DataViewRestClient('http://DATAVIEW_HOST:8000/api/1/', 'authkey')

print(rest.list_models('user'))
print(rest.get_model('user', 'admin'))
````
