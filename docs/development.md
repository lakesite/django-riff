# development #

This is a Django template, usage is straight forward:

```
        (pipenv-environment) $ django-admin startproject --template=https://github.com/lakesite/django-riff/archive/master.zip project_name
```

To test your own changes, simply refer to the template folder you've checked 
out locally and create an example project from that.

```
        (pipenv-environment) $ django-admin startproject --template=/path/to/django-riff/ project_name
```

Then ensure your changes and such are reflected in project_name