<!DOCTYPE html>
<html {% if current_path == "login" %}class="full-bg"{% endif %} lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- CSS -->
        <link rel="stylesheet" href="{{ baseurl }}/static/css/netstyle.min.css" rel="stylesheet">
        <link href="{{ baseurl }}/static/css/alarmforwarder.css" rel="stylesheet">

        <!-- Favicon -->
        <link rel="shortcut icon" type="image/x-icon" href="{{ baseurl }}/static/img/favicon.ico" />

        <title>OpenNMS AlarmForwarder Admin</title>
    </head>

    <body {% if current_path == "login" %}class="full-bg"{% endif %} >
        {% if session.username %}
            {% include 'include/navbar.html.tpl' %}
            {% include 'include/messagebar.html.tpl' %}
        {% endif %}
        {% if current_path != "login" %}
            <main class="container">
        {% endif %}