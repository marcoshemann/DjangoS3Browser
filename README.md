Django S3 File Browser
============


:Info: S3 File Browser For Django.


Django S3 File Browser is a simple web-based object browser for cloud-based blob datastores. Just add as an application
to a Django project, add some settings, and you'll be able to browse cloud containers and implied subdirectories, as
well as view / download objects.


Be sure to check out the following project resources:

* `GitHub page`_.

.. _`GitHub page`: https://github.com/mkaykisiz/DjangoS3Browser
.. toc


Quick Start
-----------
First, download library:

```bash
pip install git+https://github.com/initflow/DjangoS3Browser
```



Then, make the necessary configurations for the `Boto 3 <https://github.com/boto/boto3>`_ library:


    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False
    
    AWS_ENDPOINT_URL = None if use Amazon servers or http://<endpoint>:<port>


    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIRY = 60 * 60 * 24 * 7

    # Revert the following and use str after the above-mentioned bug is fixed in
    # either django-storage-redux or boto
    control = 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY)
    AWS_HEADERS = {
        'Cache-Control': bytes(control, encoding='latin-1')
    }



Next, add to TEMPLATES['OPTIONS'] in settings.py:


    'libraries': {
        's3-load': 'djangoS3Browser.templatetags.s3-tags',
    },


Then, add to urls.py before ^admin/:




    url(r'^admin/s3/', include('djangoS3Browser.s3_browser.urls')),
    url(r'^admin/', admin.site.urls),


Then, add this to the top of the page you want to add:

    {% load s3-tags %}


Finally, add this to the content of the page you want to add:


    {% load_s3 %}



![][image_browser]

[image_browser]: https://user-images.githubusercontent.com/5642113/30087574-225e38a8-92aa-11e7-8bf4-4da7a5048812.png
