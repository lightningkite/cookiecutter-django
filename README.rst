Cookiecutter Django
=======================

.. image:: https://pyup.io/repos/github/pydanny/cookiecutter-django/shield.svg
     :target: https://pyup.io/repos/github/pydanny/cookiecutter-django/
     :alt: Updates

.. image:: https://travis-ci.org/pydanny/cookiecutter-django.svg?branch=master
     :target: https://travis-ci.org/pydanny/cookiecutter-django?branch=master
     :alt: Build Status

.. image:: https://badges.gitter.im/Join Chat.svg
   :target: https://gitter.im/pydanny/cookiecutter-django?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Powered by Cookiecutter_, Cookiecutter Django is a framework for jumpstarting production-ready Django projects quickly.

* Documentation: https://cookiecutter-django.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles
* If you have problems with Cookiecutter Django, please open issues_ before sending emails to the maintainers. You will get a much, MUCH faster response.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

.. _Troubleshooting: https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html

.. _528: https://github.com/pydanny/cookiecutter-django/issues/528#issuecomment-212650373
.. _issues: https://github.com/pydanny/cookiecutter-django/issues/new

Features
---------

* For latest version of Django (1.11)
* Works with Python 3.4.x or 3.5.x. Python 3.6 is experimental
* Renders Django projects with 100% starting test coverage
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Registration via django-allauth_
* Comes with custom user model ready to go
* Webpack bundling for client javascript and sass
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3
* Docker support using docker-compose_ for development and production
* Run tests with unittest or py.test
* Customizable PostgreSQL version


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3
* Configuration for DjangoQ_
* Integration with MailHog_ for local email testing
* Integration with Sentry_ for error logging

.. _django-environ: https://github.com/joke2k/django-environ
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _Mailgun: http://www.mailgun.com/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose


Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (9.2+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi except on AWS ELB).

Support this Project!
----------------------

This project is run by volunteers. Please support them in their efforts to maintain and improve Cookiecutter Django:

* https://www.patreon.com/danielroygreenfeld: Project lead. Expertise in AWS ELB and Django.

Projects that provide financial support to the maintainers:

Two Scoops of Django 1.11
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://cdn.shopify.com/s/files/1/0304/6901/files/tsd-111-alpha-470x235.jpg?2934688328290951771
   :name: Two Scoops of Django 1.11 Cover
   :align: center
   :alt: Two Scoops of Django
   :target: http://twoscoopspress.org/products/two-scoops-of-django-1-11

Two Scoops of Django is the best dairy-themed Django reference in the universe

pyup
~~~~~~~~~~~~~~~~~~

.. image:: https://pyup.io/static/images/logo.png
   :name: pyup
   :align: center
   :alt: pyup
   :target: https://pyup.io/

Pyup brings you automated security and dependency updates used by Google and other organizations. Free for open source projects!

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.4.0"

Now run it against this repo::

    $ cookiecutter https://github.com/lightningkite/cookiecutter-django

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

Answer the prompts with your own desired options_. For example::

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Project Name]: Reddit Clone
    project_slug [reddit_clone]: reddit
    author_name [Daniel Roy Greenfeld]: Daniel Greenfeld
    email [you@example.com]: pydanny@gmail.com
    description [A short description of the project.]: A reddit clone.
    domain_name [example.com]: myreddit.com
    version [0.1.0]: 0.0.1
    timezone [UTC]: America/Los_Angeles
    use_whitenoise [y]: n
    use_celery [n]: y
    use_mailhog [n]: n
    use_sentry_for_error_reporting [y]: y
    use_opbeat [n]: y
    use_pycharm [n]: y
    windows [n]: n
    use_docker [y]: n
    use_heroku [n]: y
    use_compressor [n]: y
    Select postgresql_version:
    1 - 9.5
    2 - 9.4
    3 - 9.3
    4 - 9.2
    Choose from 1, 2, 3, 4 [1]: 1
    Select js_task_runner:
    1 - Gulp
    2 - Grunt
    3 - None
    Choose from 1, 2, 3, 4 [1]: 1
    use_lets_encrypt [n]: n
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    use_elasticbeanstalk_experimental: n

Enter the project and take a look around::

    $ cd reddit/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:pydanny/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

* `Developing locally`_
* `Developing locally using docker`_

.. _options: http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html
.. _`Developing locally`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
.. _`Developing locally using docker`: http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

Community
-----------

* Have questions? **Before you ask questions anywhere else**, please post your question on `Stack Overflow`_ under the *cookiecutter-django* tag. We check there periodically for questions.
* If you think you found a bug or want to request a feature, please open an issue_.
* For anything else, you can chat with us on `Gitter`_.

.. _`Stack Overflow`: http://stackoverflow.com/questions/tagged/cookiecutter-django
.. _`issue`: https://github.com/pydanny/cookiecutter-django/issues
.. _`Gitter`: https://gitter.im/pydanny/cookiecutter-django?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

For Readers of Two Scoops of Django 1.8
--------------------------------------------

You may notice that some elements of this project do not exactly match what we describe in chapter 3. The reason for that is this project, amongst other things, serves as a test bed for trying out new ideas and concepts. Sometimes they work, sometimes they don't, but the end result is that it won't necessarily match precisely what is described in the book I co-authored.

For pyup.io Users
-----------------

If you are using `pyup.io`_ to keep your dependencies updated and secure, use the code *cookiecutter* during checkout to get 15% off every month.

.. _`pyup.io`: https://pyup.io

"Your Stuff"
-------------

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.
