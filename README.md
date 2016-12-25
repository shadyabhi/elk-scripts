# elk-scripts

## create_template.py

This script exists because as someone who manages ES clusters, you need to define specific mappings for an index pattern. The right way to define mapping for a group of indices is by writing a template. https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-templates.html. This script automates the part of downloading the current mapping for the index and then putting that as a starting point while writing our new template.

* Create a template based on current mapping
```
$ python create_template.py --index logstash-2016.12.23 --name=cedexis_logs --pattern logstash-\* > script.sh
```
* Now, the script to push the template based on the current mapping is present in `script.sh`.
* Make your changes in `script.sh`. 
* Push the new template (make sure that the ES endpoint is correct)
```
sh script.sh
```
