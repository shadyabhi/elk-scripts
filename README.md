# elk-scripts

## create_template.py
* Create a template based on current mapping
```
$ python create_template.py --index logstash-2016.12.23 --name=cedexis_logs --pattern logstash-\* > script.sh
```
* Now, the script to push the template based on the current mapping is present in `script.sh`.
* Make your changes in `script.sh`. 
* Push the new template (make sure that the ES endpoint is correct)
```
sh script.sh
```adsdasd
